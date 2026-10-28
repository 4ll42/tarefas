# gerenciar de tarefas
Este projeto servirá para aprimorarmos nossa logica de 
programação  ao mesmo tempo em que exploramos conceitos
e tecnicas de programação back-end e fullstack. Vamos
utilizar a desenvolver o conceito MVC (model-View-
Controller), algumas particularidades da programação
orientada a Objetos, Programação Funcional,
persistencia de dados (MySQL), microframework Flask 
e gerenciador de pacotes do Python (Astral uv)

alguns passos iniciais para preparar o projeto:
1. caso não esteja instalado, prepare o uv no seu OS:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Faça a iniciação do projeto com o comando:
```bash
uv init 
```

ate então utilizavamos layout de pacotes (Package Layout) denominado
*flat-layout. O uv adota uma estruturação mais moderna chamada *src-layout*,
que previne erros de importação comuns chamados `import shadowing` (importação mascarada). 

3. crie um ambiente virtual do python:
```bash
uv venv
```

ative o ambiente virtual:
```powershell
.\.venv\Scripts\activate.ps1 # no Powershell do windows 
source .venv/scripts/activate # no Git Bash do Windows
source .venv/bin/activate # no Bash do linux
```

4. instale o Flask
```bash
uv add flask
```

Será criado o arquivo uv.lock contendo as depedencias (requerimentos)
e versões dos pacotes do seu projeto.

5. Crie um arquivo app.py contendo codigo inicial do projeto
```python 
from flask import Flask

app = Frask(__name__)

@app.route('/test')
def test():
    return 'Servidor online!'
```

6. teste a aplicação iniciando o servidor do Flask
```bash
uv run flask run
```