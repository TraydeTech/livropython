word = "Garrafas"
for cerveja_num in range(99, 0, -1):
    print(cerveja_num, word, "Ha cerjeva na parede.")
    print(cerveja_num, word, "Ha cerveja.")
    print("pegue 1. ")
    print("passe ao redor. ")
    if cerveja_num == 1:
        print("não há mais garafa de cerveja na parede. ")
    else:
        new_num = cerveja_num - 1
        if new_num == 1:
            word = "Garrafa"
        print(new_num, word, "de cerveja na parede. ")
