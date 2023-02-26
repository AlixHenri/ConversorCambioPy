import requests

cambioEntrada = str(input('Digite a abreviação da moeda que você deseja converter: ')).upper()

cambioSaida = str(input(f'Digite a abreviação da moeda que você deseja que {cambioEntrada} seja convertida: ')).upper()

qtdMoeda = float(input('Digite a quantidade de dinheiro que deseja ser convertido: '))

try:
    conversao = requests.get(f'https://api.frankfurter.app/latest?amount={qtdMoeda}&from={cambioEntrada}&to={cambioSaida}')
except:
    print('Um erro inesperado aconteceu, verifique se uma das abreviações de cambio estão certas e tente novamente')
    quit()

print(conversao.status_code)