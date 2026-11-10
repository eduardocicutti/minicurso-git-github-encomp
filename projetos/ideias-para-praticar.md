# Projetos simples para praticar Git e GitHub

Você não precisa começar com um projeto grande. Um programa pequeno já permite praticar repositório, commits, branches, README e `push`.

Escolha uma ideia, faça primeiro a versão mais básica e registre cada parte pronta em um commit separado.

## 1. Calculadora no terminal

**Linguagem:** C ou Python.

Crie um programa que receba dois números e permita escolher entre soma, subtração, multiplicação e divisão.

Exemplo:

```text
Primeiro número: 10
Operação: +
Segundo número: 5
Resultado: 15
```

Uma sequência possível de commits:

```text
Adiciona leitura dos números
Adiciona operações básicas
Trata divisão por zero
Adiciona instruções ao README
```

Referências:

- Python: [introdução à linguagem](https://docs.python.org/pt-br/3/tutorial/introduction.html) e [controle de fluxo](https://docs.python.org/pt-br/3/tutorial/controlflow.html).
- C: consulte `man 3 printf` e `man 3 scanf` no terminal.

## 2. Jogo de adivinhação

**Linguagem:** C ou Python.

O programa escolhe um número aleatório e o jogador tenta descobrir qual é. Depois de cada tentativa, informe se o número correto é maior ou menor.

Exemplo:

```text
Escolha um número entre 1 e 100: 40
O número correto é maior.
Nova tentativa: 73
Você acertou em 2 tentativas.
```

Comece com um intervalo fixo. Depois, crie uma branch chamada `limite-de-tentativas` e adicione uma quantidade máxima de jogadas.

Referências:

- Python: módulo [`random`](https://docs.python.org/pt-br/3/library/random.html).
- C: consulte `man 3 rand` e `man 3 srand` no terminal.

## 3. Quiz de perguntas e respostas

**Linguagem:** C ou Python.

Monte cinco perguntas de múltipla escolha. O programa deve conferir as respostas e mostrar a pontuação final.

Exemplo:

```text
Qual comando mostra o estado do repositório?
1. git log
2. git status
3. git push

Resposta: 2
Correto!
```

Você pode começar com as perguntas no próprio código e depois separá-las em outro arquivo.

Referências:

- Python: [listas](https://docs.python.org/pt-br/3/tutorial/datastructures.html) e [instruções `if`](https://docs.python.org/pt-br/3/tutorial/controlflow.html#if-statements).
- C: consulte `man 3 puts`, `man 3 fgets` e `man 3 strcmp` no terminal.

## 4. Lista de tarefas

**Linguagem:** Python.

Crie um programa com opções para adicionar, listar e concluir tarefas. Na primeira versão, as tarefas podem existir apenas enquanto o programa estiver aberto.

Exemplo:

```text
1. Adicionar tarefa
2. Listar tarefas
3. Concluir tarefa
4. Sair
```

Depois que a versão básica estiver funcionando, salve as tarefas em um arquivo JSON. Essa melhoria pode ser feita em uma branch separada.

Referências:

- [Estruturas de dados do Python](https://docs.python.org/pt-br/3/tutorial/datastructures.html).
- [Leitura e escrita de arquivos](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files).
- Módulo [`json`](https://docs.python.org/pt-br/3/library/json.html).

## 5. Cadastro de alunos

**Linguagem:** C ou Python.

Cadastre nome, matrícula e duas notas. O programa deve calcular a média e informar se o aluno foi aprovado ou reprovado.

Exemplo:

```text
Nome: Ana
Matrícula: 2026001
Notas: 8.0 e 7.5
Média: 7.75
Situação: Aprovada
```

Na versão seguinte, permita cadastrar mais de um aluno e listar todos no final.

Referências:

- Python: [listas e dicionários](https://docs.python.org/pt-br/3/tutorial/datastructures.html).
- C: consulte `man 3 printf`, `man 3 scanf` e pesquise sobre `struct` no material da disciplina.

## 6. Controle simples de gastos

**Linguagem:** Python.

Registre uma descrição, uma categoria e o valor de cada gasto. Ao final, mostre o total e quanto foi gasto em cada categoria.

Exemplo:

```text
Descrição: Almoço
Categoria: alimentação
Valor: 25.00

Total registrado: R$ 25,00
```

Uma evolução simples é salvar os dados em JSON e permitir que o programa carregue os registros quando for aberto novamente.

Referências:

- Módulo [`json`](https://docs.python.org/pt-br/3/library/json.html).
- [Formatação de strings](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#formatted-string-literals).

## O que colocar no repositório

Mesmo em um projeto pequeno, tente manter uma estrutura parecida com esta:

```text
nome-do-projeto/
├── README.md
└── programa.c
```

ou:

```text
nome-do-projeto/
├── README.md
└── programa.py
```

No `README.md`, explique:

- o que o programa faz;
- qual linguagem foi usada;
- como executar;
- quais funcionalidades já estão prontas;
- o que você ainda pretende adicionar.

Para praticar Git, evite fazer o projeto inteiro em um único commit. Termine uma parte, confira com `git status`, crie o commit e continue.

```bash
git status
git add .
git commit -m "Adiciona operação de soma"
git push
```
