import random


class Agente:
    def __init__(self, sexo, periodo, curso, religiao, origem, x=0, y=0):
        self.sexo = sexo
        self.periodo = periodo
        self.curso = curso
        self.religiao = religiao
        self.origem = origem
        self.x = x
        self.y = y

    def __str__(self):
        return f"Pos: ({self.x},{self.y}) | Sexo: {self.sexo}, Período: {self.periodo}, Curso: {self.curso}, Religião: {self.religiao}, Origem: {self.origem}"

def gerar_grid_agentes(height: int, width: int) -> list[Agente]:
    agents = []
    for y in range(height):
        for x in range(width):
            agent = Agente(
                sexo=random.randint(1, 3),
                periodo=random.randint(1, 8),
                curso=random.randint(1, 20),
                religiao=random.randint(1, 7),
                origem=random.randint(1, 5),
                x=x,
                y=y
            )
            agents.append(agent)
    return agents