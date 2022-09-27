from bson import ObjectId

from db.aula import AulaDB
from db.database import Database


class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome


class Professor(Pessoa):
    def __init__(self, especialidade, nome):
        Pessoa.__init__(self, nome)
        self.especialidade = especialidade

    def to_string(self):
        return 'O professor %s da especialidade %s' % (self.nome, self.especialidade)


class Aluno(Pessoa):
    def __init__(self, matricula: int, curso: str, periodo: int, nome: str):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo

    def to_string(self):
        return 'O aluno %s do curso %s do periodo %s' % (self.nome, self.curso, self.periodo)

    def getAluno(self):
        return ({"matricula": self.matricula, "curso": self.curso, "periodo": self.periodo, "nome":  self.nome})


class Aula:
    def __init__(self, assunto):
        self.assunto = assunto
        self.professor: Professor = None
        self.alunos: list[Aluno] = []

    def getLista(self) -> str:
        lista = []

        for aluno in self.alunos:
            lista.append(aluno.getAluno())
        return lista

    def getListaPresenca(self) -> str:
        lista = f'''
        Aula de {self.assunto}
            Professor: {self.professor.to_string()}
        '''

        for aluno in self.alunos:
            lista += f'\n    {aluno.to_string()}'
        return lista

    def creatAula(self) -> str:
        submitAula = {
            "assunto": self.assunto,
            "professor": {"especialidade": self.professor.especialidade, "nome": self.professor.nome},
            "alunos": self.getLista()
        }
        return submitAula


aluno1 = Aluno(25, 'GES', 7, 'Ana')
aluno2 = Aluno(10, 'GET', 2, 'Maria')
aluno3 = {25, 'GES', 7, 'Ana'}
professor = Professor('Banco de dados', 'Renzo')
Aula1 = Aula('Mongo')
Aula1.professor = professor
Aula1.alunos.append(aluno1)
Aula1.alunos.append(aluno2)

aulaDB = AulaDB()

submitAula = {
    "assunto": "Mongo",
    "professor": {"especialidade": "Banco de dados", "nome": "Renzoedit"},
    "alunos": [
        {"matricula": 25, "curso": "GES", "periodo": 7, "nome": "Ana"},
        {"matricula": 45, "curso": "GEt", "periodo": 1, "nome": "Joao"}
    ]
}

createAula = aulaDB.createAula(Aula1.creatAula())

updateAula = aulaDB.updateAula("633268aecc981a62a6872152", submitAula)

aulaDB.deleteAula("633267adf0979085b17e26be")

getAulas = aulaDB.getAllAulas()

print(getAulas)
