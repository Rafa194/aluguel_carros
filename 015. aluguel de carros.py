dias = int(input('Digite quantos dias ficou com o carro: '))
km_percorridos = float(input('Digite a quantidade de km percorridos: '))
taxa_total = (dias * 60) + (km_percorridos * 0.15)
print('O total a pagar é de R${:.2f}'.format(taxa_total))