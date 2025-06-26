frase = '                              viNiMNpN é NuUbi NUO RubÇolG'

#metodo .strip(), exclui os espaços iniciais e os finais
print(frase.strip().replace('viNiMNpN', 'vinicius').replace('NuUbi', 'noob').replace('NUO', 'no').replace('RubÇolG', 'roblox'))

frase2 = 'bem vindo ao PYTHON'

print(frase2.lower().replace('PYTHON', 'mundo'))

frase3 = '    bem vindo ao PYTHON'
frase3_formatada = frase3.strip().capitalize().replace('python', 'oniche')
print(frase3_formatada)