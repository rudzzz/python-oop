from veiculo import Veiculo
from carro import Carro

veiculo_branco = Veiculo('branco', 'fiat', 4, 20)

print('Cor:', veiculo_branco.cor)
print('Marca:',veiculo_branco.marca)
print('Rodas:',veiculo_branco.rodas)
print('Tanque:',veiculo_branco.tanque)

veiculo_verde = Veiculo('verde', 'Wolks', 4, 15)
print()

print('Cor:', veiculo_verde.cor)
print('Marca:',veiculo_verde.marca)
print('Rodas:',veiculo_verde.rodas)
print('Tanque:',veiculo_verde.tanque)

veiculo_verde.abastecer(20)
print()
print()
print('Carro preto')

print('Depois de abastecer o carro preto:')

carro1 = Carro('preto', 'fiat', 30)

print('Cor:', carro1.cor)
print('Marca:',carro1.marca)
print('Rodas:',carro1.rodas)
print('Tanque:',carro1.tanque)

