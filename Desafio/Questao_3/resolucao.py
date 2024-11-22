def gerar_fibonacci(n):
    fibonacci = [1, 1] 
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]


def verificar_fibonacci(n):
    fibonacci = [1, 1] 
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return n in fibonacci


def main():
    try:
        n = int(input("Informe o valor de N: "))
        
        if n <= 0:
            raise ValueError("N deve ser um número positivo.")
        
        fibonacci = gerar_fibonacci(n)
        print(f"Os {n} primeiros números da sequência de Fibonacci são: {fibonacci}")
    
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
