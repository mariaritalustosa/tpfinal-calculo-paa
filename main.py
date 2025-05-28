import sympy as sp

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
    x0 = (a + b) / 2


    # metodo da secante
    print("fazer")

    # metodo misto
    print("\nMétodo Misto: Newton-Raphson + Bisseção\n")

    print("fazer")

    # metodo de newton puro
    print("fazer")

    # metodo da bisessao puro
    print("fazer")

if __name__ == "__main__":
    main()