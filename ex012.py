preco = float(input('Qual o valor do produto? '))
desconto = float(input('Qual o desconto desejado? '))
precoFinal = preco-(preco*desconto/100)
print('Valor do produto com desconto: R${:.2f}'.format(precoFinal))