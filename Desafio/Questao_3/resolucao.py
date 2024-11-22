def gerar_fibonacci(n):
    # Gerar os N primeiros números de Fibonacci
    fibonacci = [1, 1]  # Os dois primeiros números da sequência são 1
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]

def verificar_fibonacci(n):
    # Verificar se o número n está na sequência de Fibonacci
    fibonacci = [1, 1]  # Os dois primeiros números da sequência são 1
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return n in fibonacci

def main():
    try:
        # Solicita ao usuário o valor de N
        n = int(input("Informe o valor de N: "))
        
        if n <= 0:
            raise ValueError("N deve ser um número positivo.")
        
        # Gerar e imprimir os N primeiros números de Fibonacci
        fibonacci = gerar_fibonacci(n)
        print(f"Os {n} primeiros números da sequência de Fibonacci são: {fibonacci}")
        
        # Verificar se o número N faz parte da sequência
        if verificar_fibonacci(n):
            print(f"{n} faz parte da sequência de Fibonacci.")
        else:
            print(f"{n} não faz parte da sequência de Fibonacci.")
    
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
