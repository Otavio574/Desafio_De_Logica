def calcular_salario_bruto(salario_hora, horas_trabalhadas):
    return salario_hora * horas_trabalhadas


def calcular_salario_familia(salario_bruto, num_filhos):
    if salario_bruto <= 788.00:
        return num_filhos * 30.50
    elif salario_bruto <= 1100.00:
        return num_filhos * 18.50
    else:
        return num_filhos * 11.90


def calcular_salario_liquido(salario_bruto, salario_familia):
    return salario_bruto + salario_familia


def calcular_pagamento(salario_hora, horas_trabalhadas, num_filhos):
    salario_bruto = calcular_salario_bruto(salario_hora, horas_trabalhadas)
    salario_familia = calcular_salario_familia(salario_bruto, num_filhos)
    salario_liquido = calcular_salario_liquido(salario_bruto, salario_familia)
    return {
        "salario_bruto": round(salario_bruto, 2),
        "salario_familia": round(salario_familia, 2),
        "salario_liquido": round(salario_liquido, 2),
    }


def main():
    try:
        salario_hora = float(input("Informe o valor do salário hora: "))
        if salario_hora <= 0:
            raise ValueError("O salário por hora deve ser maior que zero.")

        horas_trabalhadas = float(input("Informe o total de horas trabalhadas em um mês: "))
        if horas_trabalhadas < 0:
            raise ValueError("O total de horas trabalhadas não pode ser negativo.")

        num_filhos = int(input("Informe a quantidade de filhos menores de 14 anos: "))
        if num_filhos < 0:
            raise ValueError("O número de filhos não pode ser negativo.")
        
        pagamento = calcular_pagamento(salario_hora, horas_trabalhadas, num_filhos)
        print(f"Salário Bruto: R$ {pagamento['salario_bruto']:.2f}")
        print(f"Salário Família: R$ {pagamento['salario_familia']:.2f}")
        print(f"Salário Líquido: R$ {pagamento['salario_liquido']:.2f}")
    
    except ValueError as e:
        print(f"Erro de entrada: {e}")
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()