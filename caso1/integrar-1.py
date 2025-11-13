# Feito pelo Rafael
import math

def integral_racional_raizes_reais():
    print("Forma da integral: ∫ (A*x + B) / ((x - x1)*(x - x2)) dx")
    A = float(input("A = "))
    B = float(input("B = "))
    x1 = float(input("x1 = "))
    x2 = float(input("x2 = "))

    if x1 == x2:
        print("\nErro: As raízes devem ser distintas (x1 ≠ x2).")
        return

    print("\n" + "="*70)
    print("CÁLCULO DA DECOMPOSIÇÃO EM FRAÇÕES PARCIAIS")
    print("="*70)

    # Cálculo dos coeficientes
    C = (A * x1 + B) / (x1 - x2)
    D = (A * x2 + B) / (x2 - x1)

    print(f"\nNumerador:      ({A})x + ({B})")
    print(f"Denominador:    (x - {x1})*(x - {x2})")

    print(f"\nCoeficientes encontrados:")
    print(f"    C = (A*x1 + B) / (x1 - x2) = {C:.6f}")
    print(f"    D = (A*x2 + B) / (x2 - x1) = {D:.6f}")

    print("\nDecomposição:")
    print(f"    (A*x + B)/((x - x1)*(x - x2)) = {C:.4f}/(x - {x1}) + {D:.4f}/(x - {x2})")

    print("\n" + "="*70)
    print("INTEGRAÇÃO")
    print("="*70)

    print("\nTipo do denominador: Δ > 0 → Duas raízes reais distintas (resultado logarítmico)")

    print("\nIntegral final:")
    print("-"*70)
    print("∫ (A*x + B)/((x - x1)*(x - x2)) dx =")
    print(f"    {C:.4f} * ln|x - {x1}|")
    print(f"  + {D:.4f} * ln|x - {x2}| + C")
    print("-"*70)

    print("\nFim do cálculo!!")

if __name__ == "__main__":
    integral_racional_raizes_reais()
