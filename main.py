import sympy as sp
import metodos

def main():
    # Interface principal:
    print("+---------------------------+")
    print("| COMPARADOR ENTRE MÉTODOS: |")
    print("+---------------------------+")

    print("\nA função digitada será aplicada nos métodos da secante, misto, newton e bisessao, respectivamente.")
    print("No fim, haverá um comparativo entre o desempenho dos métodos.")
    print("A taxa de tolerância é de 1e-4 e o máximo de iterações é 100 para todos.\n")

    print("Digite as informações da função:")

    expr_str = input("Digite a função f(x): ")
    a = float(input("Digite o valor de a (início do intervalo): "))
    b = float(input("Digite o valor de b (fim do intervalo): "))

    x = sp.Symbol('x')
    f_expr = sp.sympify(expr_str)
    f = sp.lambdify(x, f_expr, "math")
    x0 = (a + b) / 2

    # calculo da derivada:
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, "math")

    # metodo da secante
    raiz_s, iteracoes_s, tempo_s, erro_s = metodos.metodo_secante(f, a, b)

    # metodo misto
    raiz_m, iteracoes_m, tempo_m, erro_m = metodos.metodo_misto(f, df, a, b, x0)

    # metodo de newton-raphson puro
    #raiz_nr, iteracoes_nr, tempo_nr, erro_nr = metodos.metodo_newton_raphson(f, a, b)
    print("fazer")

    # metodo da bisessao puro
    raiz_b, iteracoes_b, tempo_b, erro_b = metodos.metodo_bissecao(f, a, b)

    # tabela comparativa:
    print("+-----------------------------------------------------------------------------------------+")
    print("|                              TABELA COMPARATIVA DE MÉTODOS                              |")
    print("+-----------------------------------------------------------------------------------------+")
    print(f"| Secante          Raiz: {raiz_s:.6f} | Iterações: {iteracoes_s} | Tempo: {tempo_s:.6f}s | Precisão: {erro_s:.2e} |")
    print(f"| Misto            Raiz: {raiz_m:.6f} | Iterações: {iteracoes_m} | Tempo: {tempo_m:.6f}s | Precisão: {erro_m:.2e} |")
    # print(f"| Newton-Raphson  Raiz: {raiz_nr:.6f} | Iterações: {iteracoes_nr} | Tempo: {tempo_nr:.6f}s | Precisão: {erro_nr:.2e} |")
    print(f"| Bisessao         Raiz: {raiz_b:.6f} | Iterações: {iteracoes_b} | Tempo: {tempo_b:.6f}s | Precisão: {erro_b:.2e} |")
    print("+-----------------------------------------------------------------------------------------+")


if __name__ == "__main__":
    main()