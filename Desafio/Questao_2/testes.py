import pytest
from io import StringIO
from unittest.mock import patch  
from contextlib import redirect_stdout  
from resolucao import main  

def run_main(inputs):
    f = StringIO()
    with patch('builtins.input', side_effect=inputs):  
        with redirect_stdout(f):  
            main()
    return f.getvalue().strip() 

# Testes
@pytest.mark.parametrize("entrada, esperado", [
    (['5', '10', '25', '5', '15', '30'], "Sequência digitada: [10.0, 25.0, 5.0, 15.0, 30.0]\n\nO menor número é: 5.0\nO maior número é: 30.0"),
    (['3', '100', '50', '75'], "Sequência digitada: [100.0, 50.0, 75.0]\n\nO menor número é: 50.0\nO maior número é: 100.0"),\
    (['1', '42'], "Sequência digitada: [42.0]\n\nO menor número é: 42.0\nO maior número é: 42.0"),
    (['4', '-10', '-5', '-20', '-15'], "Sequência digitada: [-10.0, -5.0, -20.0, -15.0]\n\nO menor número é: -20.0\nO maior número é: -5.0"),
])
def test_sequencia(entrada, esperado):
    resultado = run_main(entrada)
    assert resultado == esperado
