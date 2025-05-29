import time
import sympy as sp

def metodo_secante(f, x0, x1, tolerancia= 1e-4, max_iteracoes = 100):
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


def metodo_misto(a, b, tolerancia= 1e-4, max_iteracoes=100):
    print("a fazer")


def metodo_newton_raphson(x0, tolerancia=1e-4, max_iteracoes=100):
    print("a fazer")
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
