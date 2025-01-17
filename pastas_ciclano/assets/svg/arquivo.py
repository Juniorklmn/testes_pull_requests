class aluno:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def leitura(self, horas_leitura):
        if horas_leitura > 4:
            print('passar leitura para o próximo(a)')
        else: print('ainda há tempo disponível')

aluno1 = aluno('João',17)
aluno1.leitura(3)