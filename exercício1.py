a = 10.9878
b = 10.5696
c = 10.7833
d = 10.4558
media_aritmetica = (a + b + c + d) / 4
print(f'A média aritmética é:{media_aritmetica:.2f}') 

valor_a = int(input('Insira um valor: '))
valor_b = int(input('Insira um valor: '))
valor_c = int(input('Insira um valor: '))
valor_d = int(input('Insira um valor: '))
media = (valor_a + valor_b + valor_c + valor_d) / 4
print(f'A média é: {media:.2}')

f = int(input('Insira um valor em reais R$'))
print(f'O saldo da conta R$ {f:,.2f}')

# receber 4 notas digitadas pelo usuario e faça a media
# se a media < 6 ela reprovou, se > 6 ela passou
# tem que exibir a mensagem


informacoes = input('Insira seu nome: ')
informacoes_2 = input('Insira sua idade: ')
informacoes_3 = input('Insira sua série: ')

nota1 = float(input("1º Bimestre: "))
nota2 = float(input('2º Bimestre: '))
nota3 = float(input('3º Bimestre: '))
nota4 = float(input('4º Bimestre: '))
media_anual = float (nota1 + nota2 + nota3 + nota4) / 4

print(f'{informacoes}\n{informacoes_2:}\n{informacoes_3}\n')
      
if media_anual >=6:
    print('Parabéns!')
    print(f'Sua média anual foi: {media_anual:.2f}')
else :
    print('Estude mais!')
    print(f'Sua média anual foi: {media_anual:.2f}')

