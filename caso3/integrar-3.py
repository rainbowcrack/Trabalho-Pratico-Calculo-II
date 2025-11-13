def calculo_caso3():
    print("Caso 3 selecionado.")
    print("Forma da integral: ∫ (A*x + B) / (x² + x1)(x² + x2) dx")

    try:
        A = float(input("Digite o valor de A: "))
        B = float(input("Digite o valor de B: "))
        X1 = float(input("Digite o valor de X1: "))
        X2 = float(input("Digite o valor de X2: "))

        # Validações
        if X1 == X2:
            print("❌ Erro: X1 e X2 não podem ser iguais, pois causariam divisão por zero.")
            return
        if (-X2 + X1) == 0:
            print("❌ Erro: divisão por zero detectada (verifique os valores de X1 e X2).")
            return

        # Cálculos
        E = A / (-X2 + X1)
        C = -A / (-X2 + X1)
        F = B / (-X2 + X1)
        D = -B / (-X2 + X1)

        print("\nExpandindo a integral:")
        print(f"∫ ({C}x + {D}) / (x² + {X1}) dx  +  ∫ ({E}x + {F}) / (x² + {X2}) dx")

        print("\nCalculando as integrais separadamente, conseguimos o seguinte resultado:")
        print(f"({C}/2) * ln|x² + {X1}| + arctg(x) + ({D}/2) * ln|x² + {X2}| + arctg(x) + C")
        print("\nOnde ln é o logaritmo natural e arctg é a função arco-tangente.")
        print("\nFim do cálculo ✅")

    except ValueError:
        print("❌ Erro: você deve digitar apenas números.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")
