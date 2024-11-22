import pytest
from resolucao import gerar_fibonacci, verificar_fibonacci

@pytest.mark.parametrize("n, esperado", [
    (1, [1]),              
    (2, [1, 1]),           
    (5, [1, 1, 2, 3, 5]),  
    (7, [1, 1, 2, 3, 5, 8, 13]),
])
def test_gerar_fibonacci(n, esperado):
    resultado = gerar_fibonacci(n)
    assert resultado == esperado

@pytest.mark.parametrize("n, esperado", [
    (1, True),           
    (2, True),           
    (3, True),           
    (4, False),          
    (5, True),           
    (10, False),         
    (13, True),          
    (21, True),          
])

def test_verificar_fibonacci(n, esperado):
    resultado = verificar_fibonacci(n)
    assert resultado == esperado
