import time

def f(x):
    return x**3 - x - 2

def metodo_newton(x0, tolerancia=1e-4, max_iteracoes=100):
    inicio = time.time()
    iteracoes = 0

def metodo_bissecao(f, a, b, tolerancia = 1e-4, max_iteracoes=100):
    inicio = time.time()
    iteracoes = 0

    if f(a) * f(b) >= 0:
        print("O método da bisseção requer que a e b tenham sinais opostos")
        return None, 0, 0, None
    
    while iteracoes < max_iteracoes:
        c = (a + b) / 2.0
        fc = f(c)

        if abs(fc) < tolerancia or (b - a) / 2 < tolerancia:
            tempo = time.time() - inicio
            erro = abs(fc)
            return c, iteracoes + 1, tempo, erro
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c    

        iteracoes += 1

    tempo = time.time() - inicio
    c = (a + b) / 2.0
    erro = abs(f(c))
    return c, iteracoes, tempo, erro        
      

def metodo_misto(a, b, tolerancia= 1e-4, max_iteracoes=100):
    print("fazer")


def secante(f, x0, x1, tolerancia= 1e-4, max_iteracoes = 100):
    inicio = time.time()
    iteracoes = 0

    for i in range(max_iteracoes):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            print("Divisão por zero evitada")
            break
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        iteracoes += 1

        if abs(x2 - x1) < tolerancia:
            tempo = time.time() - inicio
            erro = abs(f(x2))
            return x2, iteracoes, tempo, erro     
        x0, x1 = x1, x2

    tempo = time.time() - inicio
    erro = abs(f(x1))
    return x1, iteracoes, tempo, erro
    

# a fazer: adicionar essa parte na interface principal
# print("DESEMPENHO DOS MÉTODOS")
# print(f"Secante         Raiz: {raiz_s:.6f} | Iterações: {iteracoes_s} | Tempo: {tempo_s:.6f}s | Precisão: {erro_s:.2e}")
# print(f"Newton-Raphson  Raiz: {raiz_n:.6f} | Iterações: {iteracoes_n} | Tempo: {tempo_n:.6f}s | Precisão: {erro_n:.2e}")
# print(f"Misto           Raiz: {raiz_m:.6f} | Iterações: {iteracoes_m} | Tempo: {tempo_m:.6f}s | Precisão: {erro_m:.2e}")
