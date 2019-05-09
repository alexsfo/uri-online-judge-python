nome = (input())
salário_fixo = float(input())
total_vendas = float(input())

bonus = total_vendas * 15 / 100
total_salario = salário_fixo + bonus
print("TOTAL = R$ %.2f" % total_salario)
