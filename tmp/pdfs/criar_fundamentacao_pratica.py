from pathlib import Path
import re, html
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, Preformatted, HRFlowable
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(r'C:\Users\eduar\Downloads\00 A classificar\minicurso-git-github-encomp')
SRC = ROOT / 'fundamentacao-pratica.md'
OUT = ROOT / 'output' / 'pdf' / 'fundamentacao-pratica.pdf'

# Fonts with complete Portuguese coverage.
font_dir = Path(r'C:\Windows\Fonts')
regular = font_dir / 'segoeui.ttf'
bold = font_dir / 'segoeuib.ttf'
mono = font_dir / 'consola.ttf'
mono_bold = font_dir / 'consolab.ttf'
for name, path in [('UI', regular), ('UI-Bold', bold), ('Code', mono), ('Code-Bold', mono_bold)]:
    if not path.exists():
        raise FileNotFoundError(path)
    pdfmetrics.registerFont(TTFont(name, str(path)))

NAVY = colors.HexColor('#172554')
BLUE = colors.HexColor('#2563EB')
SKY = colors.HexColor('#EAF2FF')
INK = colors.HexColor('#182230')
MUTED = colors.HexColor('#526071')
LINE = colors.HexColor('#D7DFE9')
CODE_BG = colors.HexColor('#111827')
CODE_FG = colors.HexColor('#F3F4F6')
GREEN = colors.HexColor('#16A34A')
WHITE = colors.white

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyUI', fontName='UI', fontSize=10.3, leading=15.1, textColor=INK, spaceAfter=7))
styles.add(ParagraphStyle(name='Lead', fontName='UI', fontSize=12.2, leading=18, textColor=MUTED, alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name='H1UI', fontName='UI-Bold', fontSize=19, leading=23, textColor=NAVY, spaceBefore=10, spaceAfter=9, keepWithNext=True))
styles.add(ParagraphStyle(name='H2UI', fontName='UI-Bold', fontSize=13.2, leading=17, textColor=BLUE, spaceBefore=8, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle(name='BulletUI', fontName='UI', fontSize=10.1, leading=14.5, textColor=INK, leftIndent=14, firstLineIndent=-8, bulletIndent=3, spaceAfter=4))
styles.add(ParagraphStyle(name='NumberUI', fontName='UI', fontSize=10.1, leading=14.5, textColor=INK, leftIndent=17, firstLineIndent=-12, bulletIndent=1, spaceAfter=4))
styles.add(ParagraphStyle(name='CodeUI', fontName='Code', fontSize=8.7, leading=12.3, textColor=CODE_FG, leftIndent=0, rightIndent=0, spaceAfter=8))
styles.add(ParagraphStyle(name='TableHead', fontName='UI-Bold', fontSize=8.6, leading=11.2, textColor=WHITE))
styles.add(ParagraphStyle(name='TableCell', fontName='UI', fontSize=8.5, leading=11.4, textColor=INK))
styles.add(ParagraphStyle(name='TOCHeading', fontName='UI-Bold', fontSize=21, leading=25, textColor=NAVY, spaceAfter=14))
styles.add(ParagraphStyle(name='TOC1', fontName='UI', fontSize=10.3, leading=15, leftIndent=0, textColor=INK))
styles.add(ParagraphStyle(name='Ref', fontName='UI', fontSize=9, leading=13, textColor=MUTED, leftIndent=12, firstLineIndent=-7, spaceAfter=5))
styles.add(ParagraphStyle(name='Small', fontName='UI', fontSize=8.7, leading=12, textColor=MUTED))


def inline(text):
    text = html.escape(text.strip())
    text = re.sub(r'`([^`]+)`', r'<font name="Code" color="#1D4ED8">\1</font>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<link href="\2" color="#2563EB"><u>\1</u></link>', text)
    return text

class CourseDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(filename, pagesize=A4, rightMargin=18*mm, leftMargin=18*mm,
                         topMargin=20*mm, bottomMargin=18*mm,
                         title='Fundamentação prática de Git, GitHub e Bash',
                         author='Eduardo Cicutti')
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='body')
        self.addPageTemplates([PageTemplate(id='main', frames=frame, onPage=self.draw_page)])
    def draw_page(self, canvas, doc):
        page = canvas.getPageNumber()
        if page == 1:
            return
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.6)
        canvas.line(18*mm, A4[1]-13*mm, A4[0]-18*mm, A4[1]-13*mm)
        canvas.setFont('UI', 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(18*mm, A4[1]-10*mm, 'Fundamentação prática de Git, GitHub e Bash')
        canvas.drawRightString(A4[0]-18*mm, 10*mm, str(page))
        canvas.restoreState()
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name == 'H1UI':
            text = flowable.getPlainText()
            key = 'h%d' % abs(hash((text, self.page)))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=0, closed=False)
            self.notify('TOCEntry', (0, text, self.page, key))


def cover():
    items = [Spacer(1, 33*mm)]
    badge = Table([[Paragraph('MATERIAL DE APOIO PRÁTICO', ParagraphStyle(
        'badge', fontName='UI-Bold', fontSize=9, textColor=WHITE, alignment=TA_CENTER))]], colWidths=[70*mm])
    badge.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),BLUE),('BOX',(0,0),(-1,-1),0,BLUE),
                               ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    items += [badge, Spacer(1, 13*mm),
              Paragraph('Fundamentação prática<br/>de Git, GitHub e Bash', ParagraphStyle(
                  'CoverTitle', fontName='UI-Bold', fontSize=30, leading=35, textColor=NAVY, alignment=TA_CENTER)),
              Spacer(1, 8*mm),
              Paragraph('Comandos básicos, fluxo de trabalho e conceitos do GitHub para acompanhar a aula.', styles['Lead']),
              Spacer(1, 12*mm)]
    topics = Table([
        [Paragraph('<b>Bash</b><br/><font color="#526071">Navegação e arquivos</font>', styles['BodyUI']),
         Paragraph('<b>Git</b><br/><font color="#526071">Commits, branches e merge</font>', styles['BodyUI']),
         Paragraph('<b>GitHub</b><br/><font color="#526071">Clone, push, pull e colaboração</font>', styles['BodyUI'])]
    ], colWidths=[52*mm,52*mm,52*mm])
    topics.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),SKY),('BOX',(0,0),(-1,-1),0.6,LINE),
                                ('INNERGRID',(0,0),(-1,-1),0.6,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),
                                ('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),
                                ('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
    items += [topics, Spacer(1, 31*mm), HRFlowable(width='100%', thickness=1, color=LINE), Spacer(1, 5*mm),
              Paragraph('ENCOMP 2026  •  Fedora e Linux Mint  •  Terminal Bash', ParagraphStyle(
                  'CoverFoot', fontName='UI', fontSize=9, textColor=MUTED, alignment=TA_CENTER)), PageBreak()]
    return items


def code_box(code):
    pre = Preformatted(code.rstrip(), styles['CodeUI'], maxLineLength=100)
    t = Table([[pre]], colWidths=[doc.width])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),CODE_BG),('BOX',(0,0),(-1,-1),0.7,CODE_BG),
                           ('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),11),
                           ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
    return t


def md_table(lines):
    rows=[]
    for ln in lines:
        cells=[c.strip() for c in ln.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-{3,}:?', c) for c in cells):
            continue
        rows.append(cells)
    data=[]
    for ri,row in enumerate(rows):
        sty=styles['TableHead'] if ri==0 else styles['TableCell']
        data.append([Paragraph(inline(c), sty) for c in row])
    n=max(len(r) for r in data)
    widths=[doc.width/n]*n
    if n==2: widths=[38*mm, doc.width-38*mm]
    tbl=Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
    tbl.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),NAVY),('TEXTCOLOR',(0,0),(-1,0),WHITE),
        ('BACKGROUND',(0,1),(-1,-1),colors.white),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor('#F7F9FC')]),
        ('GRID',(0,0),(-1,-1),0.55,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
    ]))
    return tbl


def parse_markdown(text):
    lines=text.splitlines()
    flow=[]
    i=0
    paragraph=[]
    def flush():
        nonlocal paragraph
        if paragraph:
            flow.append(Paragraph(inline(' '.join(x.strip() for x in paragraph)), styles['BodyUI']))
            paragraph=[]
    while i < len(lines):
        ln=lines[i]
        if ln.startswith('```'):
            flush(); lang=ln[3:].strip(); i+=1; buf=[]
            while i<len(lines) and not lines[i].startswith('```'):
                buf.append(lines[i]); i+=1
            flow.append(code_box('\n'.join(buf))); flow.append(Spacer(1,2)); i+=1; continue
        if ln.startswith('# '):
            flush(); i+=1; continue  # title is on cover
        if ln.startswith('## '):
            flush(); flow.append(Paragraph(inline(ln[3:]), styles['H1UI']));
            rule = HRFlowable(width='100%', thickness=0.7, color=LINE, spaceAfter=5)
            rule.keepWithNext = True
            flow.append(rule); i+=1; continue
        if ln.startswith('### '):
            flush(); flow.append(Paragraph(inline(ln[4:]), styles['H2UI'])); i+=1; continue
        if ln.startswith('|') and i+1<len(lines) and lines[i+1].startswith('|'):
            flush(); buf=[]
            while i<len(lines) and lines[i].startswith('|'):
                buf.append(lines[i]); i+=1
            flow.append(md_table(buf)); flow.append(Spacer(1,7)); continue
        m=re.match(r'^- (.+)$',ln)
        if m:
            flush(); flow.append(Paragraph('• '+inline(m.group(1)), styles['BulletUI'])); i+=1; continue
        m=re.match(r'^(\d+)\. (.+)$',ln)
        if m:
            flush(); flow.append(Paragraph(m.group(1)+'. '+inline(m.group(2)), styles['NumberUI'])); i+=1; continue
        if not ln.strip():
            flush(); i+=1; continue
        paragraph.append(ln); i+=1
    flush(); return flow

text=SRC.read_text(encoding='utf-8')
doc=CourseDoc(str(OUT))
story=cover()
toc=TableOfContents()
toc.levelStyles=[styles['TOC1']]
story += [Paragraph('Sumário', styles['TOCHeading']), toc, PageBreak()]
story += parse_markdown(text)
doc.multiBuild(story)
print(OUT)
