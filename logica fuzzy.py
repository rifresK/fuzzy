import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variáveis de entrada
campo_eletrico = ctrl.Antecedent(np.arange(0, 2501, 1), 'campo_eletrico')
precipitacao = ctrl.Antecedent(np.arange(0, 101, 1), 'precipitacao')

# Variável de saída
alerta = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'alerta')

# Definindo as funções de pertinência para cada variável
campo_eletrico['baixo'] = fuzz.trimf(campo_eletrico.universe, [0, 0, 1000])
campo_eletrico['medio'] = fuzz.trimf(campo_eletrico.universe, [800, 1500, 2200])
campo_eletrico['alto'] = fuzz.trimf(campo_eletrico.universe, [2000, 2500, 2500])

precipitacao['fraca'] = fuzz.trimf(precipitacao.universe, [0, 0, 50])
precipitacao['media'] = fuzz.trimf(precipitacao.universe, [30, 50, 80])
precipitacao['forte'] = fuzz.trimf(precipitacao.universe, [70, 100, 100])

alerta['baixo'] = fuzz.trimf(alerta.universe, [0, 0, 0.5])
alerta['medio'] = fuzz.trimf(alerta.universe, [0, 0.5, 1])
alerta['alto'] = fuzz.trimf(alerta.universe, [0.5, 1, 1])

# Visualizando as funções
campo_eletrico.view()
precipitacao.view()
alerta.view()

# Mostrar todos os gráficos
plt.show()

# Regras de inferência 
regra1 = ctrl.Rule(campo_eletrico['alto'] & precipitacao['forte'], alerta['alto'])
regra2 = ctrl.Rule(campo_eletrico['medio'] & precipitacao['media'], alerta['medio'])
regra3 = ctrl.Rule(campo_eletrico['baixo'] & precipitacao['fraca'], alerta['baixo'])

# Sistema de controle Fuzzy
sistema_fuzzy = ctrl.ControlSystem([regra1, regra2, regra3])
sistema_alerta = ctrl.ControlSystemSimulation(sistema_fuzzy)

# Entrada de dados
sistema_alerta.input['campo_eletrico'] = 800
sistema_alerta.input['precipitacao'] = 0

# Computando o resultado
sistema_alerta.compute()

# Mostrando o valor de saída
print(f"Valor de alerta: {sistema_alerta.output['alerta']}")

# Visualizando o resultado da defuzificação
alerta.view(sim=sistema_alerta)


input("Pressione Enter para fechar os gráficos...")
