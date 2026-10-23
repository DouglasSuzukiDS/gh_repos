# 🚚 Migração de repositórios GitHub

Este script automatiza a cópia de vários repositórios GitHub de uma conta de
origem para uma conta de destino, preservando o histórico de branches e tags e
atualizando os dados de autor e committer de todos os commits.

> ⚠️ **Atenção:** o processo reescreve o histórico Git e usa `push --force`.
> Utilize-o somente quando tiver certeza de que essa é a operação desejada.

## ✨ O que o script faz

Para cada repositório informado na lista `repos`, o script:

1. 📥 Faz um clone bare do repositório de origem.
2. 🧾 Altera o nome e o e-mail do autor e do committer em todos os commits.
3. 🧹 Remove referências temporárias criadas pelo `filter-branch`.
4. 🗑️ Expira os reflogs e executa a limpeza agressiva do repositório.
5. 🔗 Altera o endereço remoto `origin` para a conta de destino.
6. 🚀 Envia todas as branches e tags para o repositório de destino.

## ✅ Pré-requisitos

- 🐍 Python 3 instalado.
- 🔧 Git instalado e disponível no `PATH`.
- 🪟 No Windows, recomenda-se executar pelo **Git Bash**, pois o script usa
  comandos de shell no filtro de histórico.
- 🌐 Os repositórios da conta de origem precisam estar **públicos**.
- 🏗️ Na conta GitHub de destino, é necessário criar antes um repositório
  **vazio com o mesmo nome** do repositório de origem.

### Sobre o nome dos repositórios

O repositório de destino precisa inicialmente ter o mesmo nome para que o
script consiga apontar o remoto e enviar os dados corretamente. Depois que a
migração terminar, você pode renomear o repositório no GitHub, se desejar.

> 💡 Crie o repositório de destino sem iniciar com README, `.gitignore` ou
> licença, evitando conflitos com o histórico que será enviado.

## ⚙️ Configuração

Abra [`clone_repos.py`](./clone_repos.py) e ajuste os valores abaixo:

```python
repos = [
    "repo1",
    "repo2",
    "repo3",
]

gh_user_origin = "USUARIO_GITHUB_ORIGEM"
correct_name = "SEU_NOME"
correct_email = "seu-email@exemplo.com"
```

| Campo | Descrição |
| --- | --- |
| `repos` | Lista dos repositórios públicos que serão migrados. |
| `gh_user_origin` | Usuário ou organização do GitHub de origem. |
| `correct_name` | Nome que será gravado como autor e committer dos commits. |
| `correct_email` | E-mail que será gravado como autor e committer dos commits. |

O usuário de destino é definido pelo valor de `correct_name` no script. Por
isso, esse valor deve corresponder ao usuário da conta GitHub de destino, caso
os repositórios estejam nesse perfil. Se o nome exibido e o nome de usuário
forem diferentes, ajuste o script antes de executar.

## ▶️ Como executar

1. Clone ou baixe este projeto.
2. Crie na conta de destino um repositório vazio para cada item de `repos`,
   usando exatamente o mesmo nome.
3. Configure a origem, o nome, o e-mail e a lista de repositórios em
   [`script.py`](./script.py).
4. Abra o Git Bash na pasta do projeto.
5. Execute:

```bash
python script.py
```

Durante o processo, o Git poderá solicitar autenticação para enviar os dados
à conta de destino. Use um método de autenticação aceito pelo GitHub, como
Git Credential Manager ou um Personal Access Token (PAT). Nunca coloque tokens
ou senhas diretamente no código.

## 🛡️ Cuidados importantes

- 💥 O `push --force` substitui o conteúdo do destino. Não execute contra um
  repositório que contenha trabalho que você queira preservar.
- 🧬 A reescrita altera os hashes dos commits. O histórico migrado não terá os
  mesmos identificadores do histórico original.
- 👥 Colaboradores que possuem clones locais precisarão sincronizar novamente
  ou reclonar os repositórios após a migração.
- 💾 Faça um backup antes de iniciar.
- 🧪 Teste primeiro com um repositório não crítico.
- 🔒 Confira cuidadosamente o e-mail informado antes de reescrever o histórico.
- ⏱️ Repositórios grandes podem levar bastante tempo para serem processados.

## 🧯 Solução rápida de problemas

### O clone falha

Confirme se o repositório de origem existe, está público e se
`gh_user_origin` e o nome listado em `repos` estão corretos.

### O push falha

Verifique se o repositório de destino já foi criado com o mesmo nome, se a
conta tem permissão de escrita e se a autenticação do GitHub está configurada.

### O script para em um repositório

O script usa `check=True`, então qualquer erro interrompe a execução. Corrija o
problema indicado pelo Git antes de executar novamente. Como os diretórios
bare são criados localmente com o formato `<nome>.git`, remova ou mova o
diretório do repositório que falhou antes de tentar uma nova migração.