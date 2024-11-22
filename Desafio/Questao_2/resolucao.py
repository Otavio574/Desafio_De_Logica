def main():
    # Recebe a quantidade de números a serem digitados
    quantidade = int(input("Informe a quantidade de números a ser digitada: "))
    
    # Cria uma lista para armazenar os números
    numeros = []
    
    # Recebe a sequência de números
    for i in range(quantidade):
        numero = float(input(f"Informe o {i + 1}º número: "))
        numeros.append(numero)
    
    # Exibe a sequência
    print("\nSequência digitada:", numeros)
    
    # Exibe o menor e o maior número da sequência
    print(f"\nO menor número é: {min(numeros)}")
    print(f"O maior número é: {max(numeros)}")

# Chama a função main para rodar o programa
if __name__ == "__main__":
    main()
