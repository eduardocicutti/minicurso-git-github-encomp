from pathlib import Path
from pypdf import PdfReader
p=Path('output/pdf/fundamentacao-pratica.pdf')
r=PdfReader(str(p))
text='\n'.join((page.extract_text() or '') for page in r.pages)
required=['Comandos básicos do Bash','Criar o commit','Branches','Merge','Clonar um repositório','Push','Pull','Pull request','Conventional Commits','Issues','Termos comuns do GitHub','Referências']
print('arquivo=',p.resolve())
print('paginas=',len(r.pages))
print('tamanho_bytes=',p.stat().st_size)
print('metadados_titulo=',r.metadata.title)
for item in required:
    print(item, '=', item in text)
print('paginas_sem_texto=',[i+1 for i,x in enumerate(r.pages) if not (x.extract_text() or '').strip()])
