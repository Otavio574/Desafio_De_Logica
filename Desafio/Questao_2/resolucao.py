def main():
    quantidade = int(input("Informe a quantidade de números a ser digitada: "))
    numeros = []
    
    for i in range(quantidade):
        numero = float(input(f"Informe o {i + 1}º número: "))
        numeros.append(numero)
    
    print("\nSequência digitada:", numeros)
    print(f"\nO menor número é: {min(numeros)}")
    print(f"O maior número é: {max(numeros)}")

if __name__ == "__main__":
    main()
