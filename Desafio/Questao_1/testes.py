import pytest
from resolucao import calcular_pagamento

@pytest.mark.parametrize("salario_hora, horas_trabalhadas, num_filhos, esperado", [
    # Caso salário bruto <= R$ 788,00
    (10, 70, 2, {"salario_bruto": 700.00, "salario_familia": 61.00, "salario_liquido": 761.00}),
    
    # Caso R$ 788,01 <= salário bruto <= R$ 1.100,00
    (15, 55, 1, {"salario_bruto": 825.00, "salario_familia": 18.50, "salario_liquido": 843.50}),
    
    # Caso salário bruto > R$ 1.100,00
    (20, 60, 3, {"salario_bruto": 1200.00, "salario_familia": 35.70, "salario_liquido": 1235.70}),
    
    # Teste sem filhos
    (20, 40, 0, {"salario_bruto": 800.00, "salario_familia": 0.00, "salario_liquido": 800.00}),
    
    # Teste limite inferior de salário família (arredondamento correto em duas casas)
    (15, 52.53, 1, {"salario_bruto": 787.95, "salario_familia": 30.50, "salario_liquido": 818.45}),
    
    # Teste limite superior de salário família (salário bruto exatamente R$ 1.100,00)
    (20, 55, 2, {"salario_bruto": 1100.00, "salario_familia": 37.00, "salario_liquido": 1137.00}),
])
def test_calcular_pagamento(salario_hora, horas_trabalhadas, num_filhos, esperado):
    resultado = calcular_pagamento(salario_hora, horas_trabalhadas, num_filhos)
    assert resultado == esperado
