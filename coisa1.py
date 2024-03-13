class Funcionario:
    def _init_(self, nome, id, salario):
        self.nome = nome
        self.id = id
        self.salario = salario
    
    def aumentar_salario(self, percentual):
        self.salario *= (1 + percentual / 100)

class Gerente(Funcionario):
    def _init_(self, nome, id, salario, departamento):
        super()._init_(nome, id, salario)
        self.departamento = departamento
    
    def promover_funcionario(self, funcionario):
        funcionario.aumentar_salario(10)

class FuncionarioRegular(Funcionario):
    pass

def calcular_folha_pagamento(lista_funcionarios):
    total_folha = 0
    for funcionario in lista_funcionarios:
        total_folha += funcionario.salario
    return total_folha

# Teste das classes e função
lista_funcionarios = [
    Gerente("João", 1, 5000, "TI"),
    FuncionarioRegular("Maria", 2, 3000),
    FuncionarioRegular("Pedro", 3, 2500)
]

total_folha_pagamento = calcular_folha_pagamento(lista_funcionarios)
print("Total da folha de pagamento:", total_folha_pagamento)