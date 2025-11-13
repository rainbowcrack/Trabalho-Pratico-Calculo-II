# Feito pela Izabel
import math

def integral_racional_misto():
    print("Forma da integral: ∫ (A*x² + B*x + C) / ((x - a)*(x² + b)) dx")
    A = float(input("A = "))
    B = float(input("B = "))
    C = float(input("C = "))
    a = float(input("a = "))
    b = float(input("b = "))

    if b <= 0:
        print("\nErro: O termo (x² + b) deve ser positivo (b > 0) para representar fator quadrático irreducível.")
        return

    print("\n" + "="*70)
    print("CÁLCULO DA DECOMPOSIÇÃO EM FRAÇÕES PARCIAIS")
    print("="*70)

    # Coeficientes
    Q = (A*b - B*a - C) / (a**2 + b)
    P = A - Q
    R = B + Q*a

    print(f"\nNumerador:      ({A})x² + ({B})x + ({C})")
    print(f"Denominador:    (x - {a})*(x² + {b})")

    print(f"\nCoeficientes encontrados:")
    print(f"    Q = (A*b - B*a - C)/(a² + b) = {Q:.6f}")
    print(f"    P = A - Q                    = {P:.6f}")
    print(f"    R = B + Q*a                  = {R:.6f}")

    print("\nDecomposição:")
    print(f"    (A*x² + B*x + C)/((x - a)*(x² + b)) = {P:.4f}/(x - {a}) + ({Q:.4f}x + {R:.4f})/(x² + {b})")

    print("\n" + "="*70)
    print("INTEGRAÇÃO")
    print("="*70)

    print("\nTipo do denominador: fator linear e quadrático irreducível (resultado com ln e arctan)")

    parte_ln1 = f"{P:.4f} * ln|x - {a}|"
    parte_ln2 = f"({Q:.4f}/2) * ln|x² + {b}|"
    parte_arctan = f"({R:.4f}/√{b}) * arctan(x/√{b})"

    print("\nIntegral final:")
    print("-"*70)
    print("∫ (A*x² + B*x + C)/((x - a)*(x² + b)) dx =")
    print(f"    {parte_ln1}")
    print(f"  + {parte_ln2}")
    print(f"  + {parte_arctan} + C")
    print("-"*70)

    print("\nFim do cálculo!!")

if __name__ == "__main__":
    integral_racional_misto()
