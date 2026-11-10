<div align="center">

<img width="100%" alt="Banner do Minicurso Git e GitHub: ENCOMP" src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:1F6FEB,100:8250DF&height=230&section=header&text=Git%20%26%20GitHub&fontSize=58&fontColor=ffffff&fontAlignY=38&desc=Minicurso%20ENCOMP%20%7C%20Do%20primeiro%20commit%20ao%20GitHub&descAlignY=59&descSize=18&animation=fadeIn" />

# 🚀 Minicurso de Git e GitHub

**Aprenda a versionar projetos, trabalhar com branches e publicar seu código no GitHub.**

[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.kernel.org/)
[![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)](https://www.markdownguide.org/)

[**📚 Conteúdo**](#-conteúdo-do-minicurso) · [**💻 Prática**](#-comece-a-praticar) · [**⌨️ Comandos**](#-comandos-essenciais) · [**🔗 Materiais**](#-materiais-e-referências)

</div>

---

## 💡 Sobre o minicurso

Este repositório reúne materiais e exercícios de apoio ao **minicurso de Git e GitHub da ENCOMP**. A proposta é apresentar os conceitos essenciais de controle de versão e guiar quem está começando desde a criação de um repositório local até a publicação de alterações no GitHub.

> **Não precisa dominar Git antes de começar!** Aqui, o foco é entender os conceitos e praticar os comandos passo a passo.

### 🎯 O que você vai aprender?

- Entender a diferença entre **Git** e **GitHub**.
- Reconhecer **repositórios, commits, branches** e os estados de arquivos no Git.
- Criar e configurar um repositório local.
- Preparar alterações, registrar commits e consultar o histórico.
- Conectar um projeto a um repositório remoto e enviar arquivos.
- Entender o fluxo básico de **branch**, **merge**, **clone**, **pull** e **pull request**.

## 🧭 Conteúdo do minicurso

| Etapa | Conteúdo | Objetivo |
| :-- | :-- | :-- |
| **01 · Fundamentos** | Git, GitHub, versionamento e repositórios | Entender por que e como versionar |
| **02 · Demonstração** | `init`, `add`, `commit`, `status`, `log`, branches e merge | Acompanhar o fluxo de trabalho |
| **03 · Kahoot** | Perguntas de revisão | Fixar o conteúdo de forma interativa |
| **04 · Prática guiada** | README, repositório remoto, `push` e GitHub | Publicar um projeto |
| **05 · Encerramento** | Revisão e próximos passos | Continuar praticando |

<details>
<summary><strong>📂 Explorar a estrutura do repositório</strong></summary>

```text
minicurso-git-github-encomp/
├── README.md
├── Git e Github.excalidraw
├── Merge e Branches.excalidraw
├── pratica/
│   ├── passo-a-passo.md
│   └── erros-comuns.md
├── perfil/
│   ├── README.md
│   └── como-personalizar.md
├── desafios/
│   └── depois-do-minicurso.md
├── projetos/
│   └── ideias-para-praticar.md
└── referencias/
    └── materiais-de-estudo.md
```

*Alguns arquivos de apoio ainda estão em preparação.*

</details>

## 💻 Comece a praticar

Os exemplos abaixo funcionam no **terminal Bash do Fedora** e em outras distribuições Linux com Git instalado.

### 1. Verifique se o Git está instalado

```bash
git --version
```

Caso não esteja instalado no Fedora:

```bash
sudo dnf install git -y
```

### 2. Configure sua identidade no Git

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"
```

> Use preferencialmente um e-mail associado à sua conta GitHub ou seu endereço `noreply` disponibilizado pelo GitHub.

### 3. Crie seu primeiro repositório local

```bash
mkdir meu-primeiro-repositorio
cd meu-primeiro-repositorio
git init -b main
printf '# Meu primeiro repositório\n' > README.md
git status
git add README.md
git commit -m "docs: adiciona README inicial"
```

### 4. Publique no GitHub

Crie no GitHub um **repositório remoto vazio** (sem adicionar README, licença ou `.gitignore` nessa etapa). Depois, substitua `<SEU_USUARIO>` e `<NOME_DO_REPO>`:

```bash
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git
git push -u origin main
```

**Atenção:** estar logado no site do GitHub não autentica automaticamente o terminal. Configure a autenticação por um método compatível (por exemplo, um gerenciador de credenciais ou GitHub CLI) antes do `push`.

## ⌨️ Comandos essenciais

| Comando | Para que serve |
| :-- | :-- |
| `git init` | Inicia um repositório Git local |
| `git status` | Mostra o estado dos arquivos |
| `git add .` | Adiciona alterações à área de preparação (*staging*) |
| `git commit -m "mensagem"` | Registra um commit |
| `git log --oneline` | Exibe um histórico resumido |
| `git branch` | Lista as branches locais |
| `git switch -c nova-branch` | Cria e acessa uma nova branch |
| `git switch main` | Volta para a branch principal |
| `git merge nova-branch` | Integra a branch indicada à branch atual |
| `git remote -v` | Mostra os remotos configurados |
| `git push -u origin main` | Envia a branch `main` e configura o upstream |
| `git clone URL` | Clona um repositório remoto |
| `git pull` | Obtém e integra alterações do remoto |
| `git fetch` | Obtém informações do remoto sem integrá-las automaticamente |

### 🌿 Fluxo básico de versionamento

```text
Editar arquivos → git status → git add → git commit → git push
```

> `git add` prepara as alterações; `git commit` registra a versão **localmente**; `git push` envia os commits ao repositório **remoto**.

## 🧩 Materiais e atividades

| Recurso | Acesso |
| :-- | :-- |
| 📝 Passo a passo da prática | [pratica/passo-a-passo.md](pratica/passo-a-passo.md) |
| 🛠️ Erros comuns | [pratica/erros-comuns.md](pratica/erros-comuns.md) |
| 👤 README de perfil | [perfil/README.md](perfil/README.md) |
| 🎨 Personalização de perfil | [perfil/como-personalizar.md](perfil/como-personalizar.md) |
| 🎯 Desafios pós-minicurso | [desafios/depois-do-minicurso.md](desafios/depois-do-minicurso.md) |
| 💭 Ideias para praticar | [projetos/ideias-para-praticar.md](projetos/ideias-para-praticar.md) |
| 📖 Materiais de estudo | [referencias/materiais-de-estudo.md](referencias/materiais-de-estudo.md) |
| 🖍️ Diagrama: Git e GitHub | [Git e Github.excalidraw](Git%20e%20Github.excalidraw) |
| 🌿 Diagrama: Merge e Branches | [Merge e Branches.excalidraw](Merge%20e%20Branches.excalidraw) |

## 🔗 Materiais e referências

- [Documentação oficial do Git](https://git-scm.com/doc)
- [Livro Pro Git (gratuito)](https://git-scm.com/book/pt-br/v2)
- [Documentação do GitHub](https://docs.github.com/pt)
- [Guia de Markdown](https://www.markdownguide.org/basic-syntax/)
- [Ferramentas para README](https://github.com/HenryLok0/awesome-github-readme-tools)

## 👨‍🏫 Organização

**Minicurso:** Git e GitHub · ENCOMP  
**Responsável pelo repositório:** [Eduardo Cicutti](https://github.com/eduardocicutti)

Se este material te ajudou, considere deixar uma ⭐ no repositório!

<div align="center">

<img width="100%" alt="Rodapé em formato de onda" src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:1F6FEB,100:8250DF&height=110&section=footer" />

<sub>Feito para aprender, praticar e compartilhar conhecimento. 💙</sub>

</div>
