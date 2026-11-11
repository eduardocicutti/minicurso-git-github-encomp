from pathlib import Path
import re, html, json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted, KeepTogether
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image, ImageDraw

ROOT = Path(r'C:\Users\eduar\Downloads\00 A classificar\minicurso-git-github-encomp')
SOURCE = ROOT / 'fundamentacao-teorica-revisada.md'
OUT = ROOT / 'output' / 'pdf' / 'fundamentacao-teorica-revisada.pdf'
QA = ROOT / 'tmp' / 'pdfs' / 'render-fundamentacao'
OUT.parent.mkdir(parents=True, exist_ok=True)
QA.mkdir(parents=True, exist_ok=True)

source = SOURCE.read_text(encoding='utf-8')
font_dir = Path('C:/Windows/Fonts')
for name, filename in [('Arial','arial.ttf'),('ArialBold','arialbd.ttf'),('ArialItalic','ariali.ttf'),('ArialBI','arialbi.ttf'),('Mono','consola.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='ArialBold', italic='ArialItalic', boldItalic='ArialBI')

blue = colors.HexColor('#2057B7')
dark = colors.HexColor('#14213D')
muted = colors.HexColor('#5C677D')
light = colors.HexColor('#EEF4FF')
line = colors.HexColor('#C9D8F0')

styles = {
    'body': ParagraphStyle('body', fontName='Arial', fontSize=10.6, leading=15.4, spaceAfter=7.5, textColor=dark),
    'h1': ParagraphStyle('h1', fontName='ArialBold', fontSize=19, leading=23, textColor=blue, spaceBefore=15, spaceAfter=10, keepWithNext=True),
    'h2': ParagraphStyle('h2', fontName='ArialBold', fontSize=14.5, leading=18, textColor=blue, spaceBefore=13, spaceAfter=8, keepWithNext=True),
    'h3': ParagraphStyle('h3', fontName='ArialBold', fontSize=11.6, leading=15, textColor=dark, spaceBefore=10, spaceAfter=6, keepWithNext=True),
    'slide': ParagraphStyle('slide', fontName='ArialBold', fontSize=10.5, leading=14, textColor=blue, leftIndent=10, rightIndent=10, spaceBefore=9, spaceAfter=9),
    'cell': ParagraphStyle('cell', fontName='Arial', fontSize=8.8, leading=11.5, textColor=dark),
    'headcell': ParagraphStyle('headcell', fontName='ArialBold', fontSize=8.8, leading=11.5, textColor=colors.white),
    'code': ParagraphStyle('code', fontName='Mono', fontSize=8.2, leading=11, textColor=dark),
    'title': ParagraphStyle('title', fontName='ArialBold', fontSize=28, leading=34, textColor=blue, spaceAfter=18),
    'subtitle': ParagraphStyle('subtitle', fontName='Arial', fontSize=14, leading=20, textColor=dark, spaceAfter=18),
    'caption': ParagraphStyle('caption', fontName='Arial', fontSize=9, leading=13, textColor=muted, spaceAfter=10),
}

def inline(text):
    pattern = r'(`[^`]+`|\*\*.+?\*\*|\*[^*]+?\*|\[[^\]]+\]\([^\)]+\))'
    out = []
    for part in re.split(pattern, text):
        if part.startswith('`'):
            out.append('<font name="Mono" size="8.6">' + html.escape(part[1:-1]) + '</font>')
        elif part.startswith('**'):
            out.append('<b>' + inline(part[2:-2]) + '</b>')
        elif part.startswith('*') and part.endswith('*'):
            out.append('<i>' + inline(part[1:-1]) + '</i>')
        elif part.startswith('[') and '](' in part:
            m = re.match(r'\[([^\]]+)\]\(([^\)]+)\)', part)
            label, url = m.groups()
            if url.startswith('http'):
                out.append('<link href="' + html.escape(url, quote=True) + '" color="#2057B7">' + html.escape(label) + '</link>')
            else:
                out.append(html.escape(label))
        else:
            out.append(html.escape(part))
    return ''.join(out)

class Document(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'toclevel'):
            self.canv.bookmarkPage(flowable.key)
            self.canv.addOutlineEntry(flowable.getPlainText(), flowable.key, flowable.toclevel, False)
            self.notify('TOCEntry', (flowable.toclevel, flowable.getPlainText(), self.page, flowable.key))

def header_footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setFont('Arial', 8)
    canvas.setFillColor(muted)
    canvas.drawString(44, height - 28, 'MINICURSO GIT E GITHUB  |  ENCOMP 2026')
    canvas.setStrokeColor(line)
    canvas.line(44, 36, width - 44, 36)
    canvas.drawString(44, 23, 'Fundamentação teórica alinhada aos slides')
    canvas.drawRightString(width - 44, 23, str(doc.page))
    canvas.restoreState()

story = [
    Spacer(1, 72),
    Paragraph('Git e GitHub', styles['title']),
    Paragraph('Fundamentação teórica alinhada aos slides', styles['subtitle']),
    Spacer(1, 18),
    Paragraph('Material de apoio ao instrutor para consulta no tablet durante o minicurso.', styles['body']),
    Spacer(1, 22),
    Paragraph('<b>ENCOMP 2026</b><br/>11 de novembro de 2026<br/>Fedora ou Linux Mint, terminal Bash', styles['body']),
    Spacer(1, 35),
    Paragraph('Esta edição acompanha as nove páginas reais da apresentação e o percurso prático atual do minicurso.', styles['caption']),
    PageBreak(),
    Paragraph('Índice', styles['h1'])
]
toc = TableOfContents()
toc.levelStyles = [
    ParagraphStyle('toc0', fontName='ArialBold', fontSize=10, leading=14, spaceBefore=4, textColor=dark),
    ParagraphStyle('toc1', fontName='Arial', fontSize=9.2, leading=12.5, leftIndent=14, spaceBefore=2, textColor=dark)
]
story += [toc, PageBreak()]

lines = source.splitlines()
i = 0
heading_id = 0
while i < len(lines):
    raw = lines[i]
    i += 1
    text = raw.strip()
    if not text:
        continue
    if text.startswith('# '):
        continue
    if text.startswith('```'):
        code = []
        while i < len(lines) and not lines[i].strip().startswith('```'):
            code.append(lines[i])
            i += 1
        i += 1
        box = Table([[Preformatted('\n'.join(code), styles['code'])]], colWidths=[A4[0] - 108])
        box.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), light), ('BOX', (0,0), (-1,-1), 0.5, line),
            ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
            ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8)
        ]))
        story.extend([box, Spacer(1, 8)])
        continue
    if text.startswith('|'):
        rows = [text]
        while i < len(lines) and lines[i].strip().startswith('|'):
            rows.append(lines[i].strip())
            i += 1
        rows = [r for r in rows if not re.fullmatch(r'[|\s:\-]+', r)]
        data = []
        for row_index, row in enumerate(rows):
            cells = [c.strip() for c in row.strip('|').split('|')]
            style = styles['headcell'] if row_index == 0 else styles['cell']
            data.append([Paragraph(inline(c), style) for c in cells])
        usable = A4[0] - 88
        widths = [usable * .13, usable * .34, usable * .53] if len(data[0]) == 3 else [usable / len(data[0])] * len(data[0])
        table = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), blue), ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light]),
            ('VALIGN', (0,0), (-1,-1), 'TOP'), ('GRID', (0,0), (-1,-1), .25, line),
            ('LEFTPADDING', (0,0), (-1,-1), 6), ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6)
        ]))
        story.extend([table, Spacer(1, 10)])
        continue
    match = re.match(r'^(#{2,4})\s+(.+)$', text)
    if match:
        level = len(match.group(1))
        title = match.group(2)
        if title.startswith('Apoio ao slide') or title.startswith('Apoio aos slides') or title.startswith('Apoio direto'):
            callout = Table([[Paragraph(inline(title), styles['slide'])]], colWidths=[A4[0] - 88])
            callout.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),light),('BOX',(0,0),(-1,-1),.6,blue)]))
            story.append(callout)
            continue
        heading_id += 1
        style = styles['h1'] if level == 2 else styles['h2'] if level == 3 else styles['h3']
        p = Paragraph(inline(title), style)
        if level == 2:
            p.key = f'h{heading_id}'
            p.toclevel = 0
        story.append(p)
        continue
    if text.startswith('- '):
        story.append(Paragraph(inline(text[2:]), styles['body'], bulletText='•'))
        continue
    story.append(Paragraph(inline(text), styles['body']))

doc = Document(str(OUT), pagesize=A4, rightMargin=44, leftMargin=44, topMargin=48, bottomMargin=48,
               title='Fundamentação teórica do minicurso de Git e GitHub', author='Eduardo Cicutti')
doc.multiBuild(story, onFirstPage=header_footer, onLaterPages=header_footer)

reader = PdfReader(str(OUT))
extracted = '\n'.join(page.extract_text() or '' for page in reader.pages)
required = ['Apoio ao slide 3', 'git push -u origin main', 'Prática guiada: README', 'Fedora e Linux Mint']
missing = [item for item in required if item not in extracted]
if missing:
    raise RuntimeError(f'Conteúdo ausente no PDF: {missing}')

pdf = pdfium.PdfDocument(str(OUT))
thumbs = []
for index, page in enumerate(pdf):
    image = page.render(scale=1.35).to_pil().convert('RGB')
    image.save(QA / f'pagina-{index + 1:02}.png')
    thumb = image.copy()
    thumb.thumbnail((244, 346))
    tile = Image.new('RGB', (260, 376), 'white')
    tile.paste(thumb, ((260 - thumb.width) // 2, 6))
    ImageDraw.Draw(tile).text((12, 355), f'Página {index + 1}', fill='black')
    thumbs.append(tile)
for start in range(0, len(thumbs), 12):
    batch = thumbs[start:start+12]
    sheet = Image.new('RGB', (260 * 4, 376 * 3), '#d9d9d9')
    for j, tile in enumerate(batch):
        sheet.paste(tile, ((j % 4) * 260, (j // 4) * 376))
    sheet.save(QA / f'contato-{start // 12 + 1}.png')

(QA / 'verificacao.json').write_text(json.dumps({
    'paginas': len(reader.pages), 'bytes': OUT.stat().st_size,
    'caracteres_extraidos': len(extracted), 'conteudos_obrigatorios_ausentes': missing
}, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'pdf': str(OUT), 'paginas': len(reader.pages), 'bytes': OUT.stat().st_size, 'folhas_contato': (len(thumbs)+11)//12}, ensure_ascii=False))
