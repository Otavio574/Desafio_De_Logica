import pytest
from resolucao import gerar_fibonacci, verificar_fibonacci  # Importe as funções do arquivo principal

# Teste para a função gerar_fibonacci
@pytest.mark.parametrize("n, esperado", [
    (1, [1]),              # O primeiro número da sequência
    (2, [1, 1]),           # Os dois primeiros números da sequência
    (5, [1, 1, 2, 3, 5]),  # Os primeiros 5 números
    (7, [1, 1, 2, 3, 5, 8, 13]),  # Os primeiros 7 números
])
def test_gerar_fibonacci(n, esperado):
    resultado = gerar_fibonacci(n)
    assert resultado == esperado

# Teste para a função verificar_fibonacci
@pytest.mark.parametrize("n, esperado", [
    (1, True),           # O número 1 faz parte da sequência
    (2, True),           # O número 2 faz parte da sequência
    (3, True),           # O número 3 faz parte da sequência
    (4, False),          # O número 4 não faz parte da sequência
    (5, True),           # O número 5 faz parte da sequência
    (10, False),         # O número 10 não faz parte da sequência
    (13, True),          # O número 13 faz parte da sequência
    (21, True),          # O número 21 faz parte da sequência
])
def test_verificar_fibonacci(n, esperado):
    resultado = verificar_fibonacci(n)
    assert resultado == esperado
