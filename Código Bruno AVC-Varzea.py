def main ():
    # =========================================================================
    # PESSOA 4: Bruno - Relatório Final, Cálculos de Aproveitamento e Situação do Time
    # =========================================================================
    print("\n" + "=" * largura)
    print("RESUMO DA CAMPANHA".center(largura))
    print("=" * largura)

    # Cálculos finais fora dos laços (aproveitamento, média de gols, saldo)
    saldo_gols = gols_pro_total - gols_contra_total
    media_gols = gols_pro_total / total_jogos
    aproveitamento = (pontos_totais / (total_jogos * 3)) * 100

    # Situação do time
    if aproveitamento >= 70:
        situacao = "Briga pelo titulo"
    elif aproveitamento >= 50:
        situacao = "Zona de classificacao"
    elif aproveitamento >= 30:
        situacao = "Meio de tabela"
    else:
        situacao = "Risco de rebaixamento"

    # Parte final que imprime totais, estatísticas, situação e lista completa
    print("\n Lista de Jogos Registrados:")
    for j in registros:
        print(
            f" - Jogo {j['numero']}: {j['g_time']} x {j['g_adversario']} ({j['resultado']}) | Goleada: {j['goleada']}")

    print(f"\n Estatísticas Finais:")
    print(f" • Total de Jogos: {total_jogos}")
    print(f" • Pontos Conquistados: {pontos_totais}")
    print(f" • Vitórias: {vitorias} | Empates: {empates} | Derrotas: {derrotas}")
    print(f" • Goleadas: {goleadas}")
    print(f" • Gols Pró: {gols_pro_total} | Gols Contra: {gols_contra_total} | Saldo: {saldo_gols}")
    print(f" • Média de gols marcados por jogo: {media_gols:.2f}")
    print(f" • Maior número de gols marcados em um jogo: {maior_gols}")
    print(f" • Aproveitamento: {aproveitamento:.2f}%")
    print(f" • Situação: {situacao}")
    print("=" * largura)

if __name__=="__main__":
    main()