def inicializar_cache(tamanho_cache):
    cache = {}
    for cont in range(tamanho_cache):
        cache[cont] = -1
    return cache


def imprimir_cache(cache):
    tamanho = len(cache)
    print("Tamanho da cache: ", tamanho)
    print(" Cache | Memória")
    for cache, memoria in cache.items():
        print(f"{cache:6} | {memoria:5}")


def mapeamento_direto(tamanho_cache, pos_memoria):
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache)

    hits = 0
    miss = 0

    for posicao_memoria in pos_memoria:
        posicao_cache = posicao_memoria % tamanho_cache

        if cache[posicao_cache] == posicao_memoria:
            hits += 1
            print(
                f"Hit! Posição {posicao_memoria} foi encontrada na posição {posicao_cache} da cache"
            )
        else:
            miss += 1
            print(
                f"Miss! Posição {posicao_memoria} não foi encontrada na cache. Inserindo na posição {posicao_cache}"
            )
            cache[posicao_cache] = posicao_memoria
        imprimir_cache(cache)

    numero_acessos = hits + miss
    if numero_acessos > 0:
        taxa_hit = hits / numero_acessos
        taxa_hit_porcentagem = taxa_hit * 100
    else:
        taxa_hit = 0

    print(f"Total de posições acessadas: {numero_acessos}")
    print(f"Total de hits: {hits}")
    print(f"Total de misses: {miss}")
    print(f"Taxa de hits: {taxa_hit_porcentagem:.2f}%")

    return cache


posicoes_memoria_acessar = [1, 6, 1, 11, 1, 16, 1, 21, 1, 26]
tamanho_cache = 5


mapeamento_direto(tamanho_cache, posicoes_memoria_acessar)
