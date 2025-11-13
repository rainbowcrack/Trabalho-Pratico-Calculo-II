# Feito pela Any

def calculo_caso3():
    print("="*70)
    print("CÁLCULO DA DECOMPOSIÇÃO EM FRAÇÕES PARCIAIS")
    print("="*70)

    print("Forma da integral: ∫ (A*x + B) / ((x² + x1)*(x² + x2)) dx")

    try:
        A = float(input("\nA = "))
        B = float(input("B = "))
        X1 = float(input("x1 = "))
        X2 = float(input("x2 = "))

        # ==================== Validações ====================
        if X1 == X2:
            print("\n❌ Erro: x1 e x2 não podem ser iguais (divisão por zero).")
            return
        if (-X2 + X1) == 0:
            print("\n❌ Erro: divisão por zero detectada (verifique os valores de x1 e x2).")
            return

        # ==================== Cálculos ====================
        E = A / (-X2 + X1)
        C = -A / (-X2 + X1)
        F = B / (-X2 + X1)
        D = -B / (-X2 + X1)

        # ==================== Resultados ====================
        print("\nCoeficientes encontrados:")
        print(f"    C = -A / (-x2 + x1)   = {C:.6f}")
        print(f"    D = -B / (-x2 + x1)   = {D:.6f}")
        print(f"    E =  A / (-x2 + x1)   = {E:.6f}")
        print(f"    F =  B / (-x2 + x1)   = {F:.6f}")

        print("\nDecomposição:")
        print("---------------------------------------------------------------------")
        print(f"(A*x + B)/((x² + x1)*(x² + x2)) = "
              f"({C:.4f}x + {D:.4f})/(x² + {X1}) + ({E:.4f}x + {F:.4f})/(x² + {X2})")
        print("---------------------------------------------------------------------")

        # ==================== Integração ====================
        print("\n" + "="*70)
        print("INTEGRAÇÃO")
        print("="*70)

        print("\nCalculando as integrais separadamente, obtemos:\n")

        print(f"∫ ({C:.4f}x + {D:.4f}) / (x² + {X1}) dx  +  ∫ ({E:.4f}x + {F:.4f}) / (x² + {X2}) dx")

        print("\nIntegral final:")
        print("---------------------------------------------------------------------")
        print(f"({C:.4f}/2) * ln|x² + {X1}|  +  ({D:.4f}) * arctan(x/√{X1})")
        print(f"+ ({E:.4f}/2) * ln|x² + {X2}|  +  ({F:.4f}) * arctan(x/√{X2})  +  C")
        print("---------------------------------------------------------------------")

        print("\nFim do cálculo ✅")

    except ValueError:
        print("\n❌ Erro: você deve digitar apenas números.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")


# ============================================================
#  Execução direta
# ============================================================
if __name__ == "__main__":
    calculo_caso3()
