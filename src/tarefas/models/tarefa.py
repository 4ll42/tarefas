from datetime import datetime

from tarefas.models.database import Database

class Tarefa:
    """
    Prove metodos para armazenar, recuperar e processar os dados das 
    tarefas criadas a partir do formulario principal.
    """
    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Salvar a tarefa no banco de dados."""
        sql = 'INSERT INTO tarefa (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao) #proteje contra SQL injection

        #gerenciador de contexto (with)
        #Acessar os metodos __enter__e__exit__ da classe
        with Database() as db:
            db.executar(sql, params)


tarefa = Tarefa('Minha nova tarefa')
tarefa.salvarTarefa()

