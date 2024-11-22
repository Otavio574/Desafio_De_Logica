import pytest
from io import StringIO
from unittest.mock import patch  # Importando patch para simular a entrada
from contextlib import redirect_stdout  # Importando redirect_stdout
from resolucao import main  # Certifique-se de que a função main() esteja no arquivo correto

# Função para capturar o output da função main()
def run_main(inputs):
    # Redireciona a saída para capturar o print
    f = StringIO()
    with patch('builtins.input', side_effect=inputs):  # Usando o patch para simular entradas
        with redirect_stdout(f):  # Usando redirect_stdout para capturar a saída
            main()
    return f.getvalue().strip()  # Remove a nova linha extra

# Testes
@pytest.mark.parametrize("entrada, esperado", [
    # Caso com 5 números
    (['5', '10', '25', '5', '15', '30'], "Sequência digitada: [10.0, 25.0, 5.0, 15.0, 30.0]\n\nO menor número é: 5.0\nO maior número é: 30.0"),

    # Caso com 3 números
    (['3', '100', '50', '75'], "Sequência digitada: [100.0, 50.0, 75.0]\n\nO menor número é: 50.0\nO maior número é: 100.0"),

    # Caso com 1 número
    (['1', '42'], "Sequência digitada: [42.0]\n\nO menor número é: 42.0\nO maior número é: 42.0"),

    # Caso com números negativos
    (['4', '-10', '-5', '-20', '-15'], "Sequência digitada: [-10.0, -5.0, -20.0, -15.0]\n\nO menor número é: -20.0\nO maior número é: -5.0"),
])
def test_sequencia(entrada, esperado):
    resultado = run_main(entrada)
    assert resultado == esperado
