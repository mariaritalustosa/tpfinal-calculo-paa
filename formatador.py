def formatar_raiz(raiz):
    if abs(raiz) == 0:
        raiz = 0

    if raiz >= 0:
        return f" {raiz:.6f}"
    
    return f"{raiz:.6f}"

def formatar_iteracoes(iteracoes):
    if iteracoes < 10:
        return f"  {iteracoes}"
    elif iteracoes < 100:
        return f" {iteracoes}"
    
    return f"{iteracoes}"