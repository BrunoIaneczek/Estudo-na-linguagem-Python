
def notas(*nota,sit = 0):
    """
    Função que analisa notas de uma turma
    :param nota: notas dos alunos
    :param sit: situação geral da turma
    :return: A media da turma, a maior nota da turma, a menor nota da turma
    """
    somadasnotas = sum(nota)
    media = somadasnotas/len(nota)
    Turma = {'Total':len(nota),'Maior':max(nota),'Menor':min(nota),'Média':media}
    if sit:
        if media >6:
            sit = 'Bom'
        elif media <=6 and media >=5:
            sit = 'razoavel'
        else:
            sit = 'ruim'
        Turma['Situação']=sit
    return  Turma

Turma = (notas(5,4,3,2,3,5,2,1,5,6,sit=False))
print(Turma)
help(notas)