estoque = (
    ('mouse LG Tech', 10),
    ('mic Hiper x', 5),
    ('acer Nitro 5', 3),
    ('webcam HD', 0)
)

for i in estoque:
    if i[1] <= 5:
        print('os numeros menores que 5 são:')
        print(f'-{i[0]}')
media = sum(i) / len(i)
print(media)