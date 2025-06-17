texto = "esse é o meu texto AfJjfkKl OnIcjOe e Eou OUe ViNee NãoOOOo ResPiRRoU Ee FeiSZ 32 AnOs AaAASDA@@@@"
print(texto.capitalize())

print(texto.title())

nome = 'vitor'
print(nome.center(40, '='))

asd = len(texto)
print(asd)

print(texto.lower())

print(texto.upper())

frase = 'asdoaisd'
print(frase.replace('asdoaisd', 'sajdkasjdka'))

arquivo = 'skins_vitor.csv'

#metodo.startswith(palavra), retorna se a palavra existe no inicio da variavel
print(arquivo.startswith('skins'))
#metodo.endswith(palavra), retorna se a palavra existe no inicio da variavel
print(arquivo.endswith('.py'))

nick = 'machearfa235447'
#metodo .isalnum() -> verifica se o texto possui letras e numeros APENAS
print(nick.isalnum())

#metodo .isalpha() -> verifica se o texto possui APENAS letras
print(nick.isalpha())

#metodo .isdigit() -> verifica se o texto possui APENAS numeros
print(nick.isdigit())

#metodo .strip() -> remove os espaços de um texto
senha = 'kikinho2014'
senhaTentativa = input('digite sua senha: ').strip()

#verifique se a senha é igual a senha tentativa
if senha == senhaTentativa:
    print("senha correta")
else:
    print('senha incorreta')


#crie uma variavel chamada frase_torta
#armazene nessa variavel uma frase que contenha letras minusculas, maiusculas, espaços nas extremidades
#crie uma outra variavel chamada frase_torta_formatada
#utilize o encadeamento de métodos para deixar a frase mais limpa

frase_torta = "frAse boNita"
frase_torta_formatada = frase_torta.lower().strip().replace('bonita', 'feia')
print(frase_torta_formatada)