loja_games = {
    'Minecraft' :  {'preço' : 59.90, 'estoque' : 5},
    'fifa23' :     {'preço' : 199.90, 'estoque' : 3},
    'God of war' : {'preço' : 149.90, 'estoque' : 4}
}

for jogo, info in loja_games.items():
    print(f' {jogo} - {info['preço']} - estoque: {info["estoque"]}')

print("-" * 50)

escolha_cliente = input("qual jogo voce deseja? : ").capitalize().strip()

if escolha_cliente in loja_games:
    print("o jogo esta disponivel")
    quantidade_solicidada = int(input("quantas unidades vc quer? : "))
    if quantidade_solicidada >= loja_games[escolha_cliente]["estoque"]:
        print("não tem estoque suficiente")
else:
    print("o jogo não esta disponivel")