from flask import Flask, redirect, render_template, request, url_for
 
from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa
 
app = Flask(__name__)
 
with app.app_context():
    init_db()
   
@app.route('/test')
def test():
    return 'Servidor online!'
 
@app.route('/', methods=['GET', 'POST'])
def home():
 
    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa'] # casa com o nome do input no form
        data_conclusao_form = request.form['dataConclusao'] #casa com o nome do input no form
 
        data_corrigida = data_conclusao_form or None
        # 'or' nesse caso é um operador de
 
        # Instnaciamos uma nova tarefa com os dados recebidos do form
        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)
       
        # Salvamos a tarefa no banco
        tarefa.salvarTarefa()
 
        return redirect(url_for('home'))
 
    tarefas = Tarefa.listarTarefas()
 
    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas
    )

    """
    TAREFA - UPDATE: crie uma funcionalidade para editar/atualizar cada
    uma das tarefas, individualmente. A tarefa devera ser editada/alterada no
    proprio formulario da pagina `base.html`. Note que vc devera criar:

    - um metodo no modelo (tarefa) para carregar uma tarefa salva no banco
    na memoria (heap) do computador, instanciando um novo objeto;
    - um metodo no modelo (Tarefa) para alterar a tarefa com os novos objetos;
    - um link no View/Template (base.html) para chamar a rota do Controller 
    - o botao `adicionar` deve se tornar um botao `atualizar`
    - uma rota no Controller (app.py) para intermediar a operacao que aceite
    os metodos GET (carregar a tarefa no formulario) e POST (enviar os dados
    alterados e volta opara o controller)
    - n use JavaScript

    """
 
# Crie uma nova funcionalidade para apagar casa uma das tarefas cadastradas
@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    Tarefa.apagarTarefa(id)
    return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']
        data_corrigida = data_conclusao_form or None
 
        tarefa = Tarefa(titulo=titulo_form, id=id, data_conclusao=data_corrigida)
        tarefa.atualizarTarefa()
 
        return redirect(url_for('home'))
 
    tarefas = Tarefa.listarTarefas()
    tarefa_selecionada = Tarefa.carregarTarefa(id)
 
    return render_template(
        'base.html',
        titulo_da_pagina='Editar tarefa',
        tarefas_da_pagina=tarefas,
        tarefa_edicao=tarefa_selecionada
    )
 
if __name__ == '__main__':
    app.run()