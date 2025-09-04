loja_games = {
    'Minecraft' :  {'preço' : 59.90, 'estoque' : 5},
    'Fifa23' :     {'preço' : 199.90, 'estoque' : 3},
    'God of war' : {'preço' : 149.90, 'estoque' : 4}
}

carrinho = {}


for jogo, info in loja_games.items():
    print(f' {jogo} - {info['preço']} - estoque: {info["estoque"]}')

while True:

    print("-" * 50)

    escolha_cliente = input("qual jogo voce deseja? : ").capitalize().strip()

    if escolha_cliente == 'Sair':
        print('resumo da compra'.center(40, '-'))
        total = 0
        for jogo, qtd in carrinho.items():
            preco = loja_games[jogo]['preço']
            total += preco * qtd
            print(f'-{jogo} x {qtd}')
            print(f'-'*40)
        print('preço:' ,total)
        break


    if escolha_cliente in loja_games:

        print("o jogo esta disponivel")
        quantidade_solicidada = int(input("quantas unidades vc quer? : "))
        if quantidade_solicidada > loja_games[escolha_cliente]["estoque"]:
            print("não tem estoque suficiente")
        else:
            print('compra realizada com sucesso')
            loja_games[escolha_cliente]['estoque'] -= quantidade_solicidada
            carrinho[escolha_cliente] = quantidade_solicidada

    else:
        print('não tem jogo')

    print(f'tem { loja_games[ escolha_cliente]['estoque'] } unidades restantes')