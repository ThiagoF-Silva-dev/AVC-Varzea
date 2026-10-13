def main():
    largura = 80
    print("="*largura)
    print()
    print("CAMPANHA TIME DE VÁRZEA".center(largura))
    print()
    print("="*largura)
    print()


    total_jogos = int(input("Digite a quantidade de jogos da campanha de 1 a 30 jogos: \n"))

    while total_jogos < 1 or total_jogos > 30:
        print(f"Quantidade de jogos invalido! \n")
        total_jogos = int(input("Digite a quantidade de jogos da campanha de 1 a 30 jogos:\n"))


if __name__=="__main__":
    main()