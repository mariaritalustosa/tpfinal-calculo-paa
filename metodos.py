import time
import sympy as sp

def metodo_secante(f, x0, x1, tolerancia= 1e-4, max_iteracoes = 100):
    inicio = time.time()
    iteracoes = 0

    for i in range(max_iteracoes):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-4:
            print("Divisão por zero evitada")
            break
         #calcula o próximo ponto da iteração pelo método da secante
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        iteracoes += 1

         #critério de parada: se o valor absoluto da função em x2 é menor que a tolerância desejada
        if abs(f(x2)) < tolerancia:
            tempo = time.time() - inicio
            erro = abs(f(x2))
            return x2, iteracoes, tempo, erro     
        x0, x1 = x1, x2

    #caso não tenha convergido, retorna a última aproximação, e o tempo, número de iterações e erro
    tempo = time.time() - inicio
    erro = abs(f(x1))
    return x1, iteracoes, tempo, erro


def metodo_misto(f, df, a, b, x0, tol=1e-4, max_iter=100):
    inicio = time.time()

    if f(a) * f(b) >= 0:
        print("Erro no metodo misto: f(a) e f(b) devem ter sinais opostos.")
        return 0, 0, 0, 0

    erro = None

    for i in range(max_iter):
        
        fx = f(x0)
        dfx = df(x0)
        # Tenta Newton-Raphson
        if dfx != 0:
            x_new = x0 - fx / dfx
        else:
            # Se a derivada for 0, força bisseção
            x_new = (a + b) / 2

        # Se Newton-Raphson sair do intervalo, força bisseção
        if not (a < x_new < b):
            x_new = (a + b) / 2

        f_new = f(x_new)
        erro = abs(x_new - x0)
        
        # descomente para seguir o método passo a passo:
        # print(f"Iteração {i+1}: x = {x_new:.6f}, f(x) = {f_new:.6e}, erro = {erro:.2e}")

        # caso chegue em uma tolerância aceitável
        if erro < tol:
            tempo = time.time() - inicio
            return x_new, i, tempo, erro

        # Atualiza intervalo
        if f(a) * f_new < 0:
            b = x_new
        else:
            a = x_new

        x0 = x_new

    # Não convergiu após o número máximo de iterações
    tempo = time.time() - inicio
    return x0, 100, tempo, erro


def metodo_newton_raphson(f, df, x0, tol=1e-4, max_iter=100):
    inicio = time.time()

    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            print("Erro no metodo de newton-raphson: Derivada igual a zero. Método falhou.")
            return 0, 0, 0, 0

        # Fórmula do método de Newton-Raphson
        x1 = x0 - fx / dfx
        erro = abs(x1 - x0)

        # descomente para seguir o método passo a passo:
        # print(f"Iteração {i+1}: x = {x1:.6f}, f(x) = {fx:.6f}, erro = {erro:.6e}")

        if erro < tol:
            tempo = time.time() - inicio
            return x1, i + 1, tempo, erro

        x0 = x1

    # Número máximo de iterações atingido sem convergência
    tempo = time.time() - inicio
    return x1, i + 1, tempo, erro


def metodo_bissecao(f, a, b, tolerancia = 1e-4, max_iteracoes=100):
    #inicia a contagem de tempo para medir a duração do método
    inicio = time.time()
    iteracoes = 0

    #verifica se f(a) e f(b) tem sinais opostos
    if f(a) * f(b) >= 0:
        print("Erro no método da bisseção: requer que a e b tenham sinais opostos")
        return 0, 0, 0, 0
    
    while iteracoes < max_iteracoes:
        c = (a + b) / 2.0
        #avalia a função do ponto médio
        fc = f(c)
        #calcula o erro aproximado como metade do tamanho do intervalo
        erro = abs(b - a) / 2.0

        if abs(fc) < tolerancia or erro < tolerancia:
            tempo = time.time() - inicio
            #retorna a raiz aproximada, número de iterações, tempo gasto e erro
            return c, iteracoes + 1, tempo, erro
          
        #atualiza o intervalo [a, b] dependendo do sinal do produto f(a)*f(c)
        if f(a) * fc < 0:
            b = c
        else:
            a = c

        iteracoes += 1

    tempo = time.time() - inicio
    c = (a + b) / 2.0
    erro = abs(b - a) / 2.0
    return c, iteracoes, tempo, erro
