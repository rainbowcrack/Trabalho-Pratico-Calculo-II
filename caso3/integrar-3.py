import math

def integral_racional_quadraticos():
    print("Forma da integral: ∫ (A*x + B) / ((x² + x1)*(x² + x2)) dx")
    A = float(input("A = "))
    B = float(input("B = "))
    x1 = float(input("x1 = "))
    x2 = float(input("x2 = "))

    if x1 == x2:
        print("\nErro: Os termos quadráticos devem ser distintos (x1 ≠ x2).")
        return

    print("\n" + "="*70)
    print("CÁLCULO DA DECOMPOSIÇÃO EM FRAÇÕES PARCIAIS")
    print("="*70)

    # Coeficientes
    C = A / (x2 - x1)
    D = B / (x2 - x1)
    E = -C
    F = -D

    print(f"\nNumerador:      ({A})x + ({B})")
    print(f"Denominador:    (x² + {x1})*(x² + {x2})")

    print(f"\nCoeficientes encontrados:")
    print(f"    C =  A / (x2 - x1) = {C:.6f}")
    print(f"    D =  B / (x2 - x1) = {D:.6f}")
    print(f"    E = -C             = {E:.6f}")
    print(f"    F = -D             = {F:.6f}")

    print("\nDecomposição:")
    print(f"    (A*x + B)/((x² + x1)*(x² + x2)) = ({C:.4f}x + {D:.4f})/(x² + {x1}) + ({E:.4f}x + {F:.4f})/(x² + {x2})")

    print("\n" + "="*70)
    print("INTEGRAÇÃO")
    print("="*70)

    print("\nTipo do denominador: produto de dois quadráticos distintos (resultado com ln e arctan)")

    parte_ln = f"({A}/(2*({x2} - {x1}))) * ln|(x² + {x1})/(x² + {x2})|"
    parte_arctan = f"({B}/({x2} - {x1})) * [ (1/√{x1}) * arctan(x/√{x1}) - (1/√{x2}) * arctan(x/√{x2}) ]"

    print("\nIntegral final:")
    print("-"*70)
    print("∫ (A*x + B)/((x² + x1)*(x² + x2)) dx =")
    print(f"    {parte_ln}")
    print(f"  + {parte_arctan} + C")
    print("-"*70)

    print("\nFim do cálculo!!")

if __name__ == "__main__":
    integral_racional_quadraticos()
