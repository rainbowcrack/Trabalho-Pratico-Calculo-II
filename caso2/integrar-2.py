import math

def integral_racional_terminal():
    print("Forma da integral: ∫ (A*x + B) / (a*x² + b*x + c) dx")
    A = float(input("A = "))
    B = float(input("B = "))
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print("\n" + "="*70)
    print("CÁLCULO DA DECOMPOSIÇÃO EM FRAÇÕES PARCIAIS")
    print("="*70)

    # Coeficientes da decomposição
    P = A / (2 * a)
    Q = B - (A * b) / (2 * a)

    print(f"\nNumerador:      ({A})x + ({B})")
    print(f"Denominador:    ({a})x² + ({b})x + ({c})")
    print(f"\nCoeficientes encontrados:")
    print(f"    P = A / (2a)           = {P:.6f}")
    print(f"    Q = B - (A*b)/(2a)     = {Q:.6f}")

    print("\nDecomposição:")
    print(f"    (A*x + B)/(a*x² + b*x + c) = {P:.4f}*(2{a}x + {b})/({a}x² + {b}x + {c}) + {Q:.4f}/({a}x² + {b}x + {c})")

    print("\n" + "="*70)
    print("INTEGRAÇÃO")
    print("="*70)

    delta = b**2 - 4*a*c
    print(f"\nDiscriminante Δ = b² - 4ac = {delta:.6f}")

    # Primeira parte da integral (sempre logarítmica)
    parte1 = f"({A}/(2*{a})) * ln|{a}x² + {b}x + {c}|"

    # Segunda parte depende do discriminante
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        parte2 = (f"1/({a:.4f} * ({x1:.4f} - {x2:.4f})) * ln| (x - {x1:.4f}) / (x - {x2:.4f}) |")
        tipo = "Δ > 0 → Duas raízes reais (resultado logarítmico)"
    elif delta == 0:
        parte2 = f"-1 / ({a:.4f} * (x + {b/(2*a):.4f}))"
        tipo = "Δ = 0 → Raiz dupla (resultado racional simples)"
    else:
        sqrt_neg_delta = math.sqrt(-delta)
        denom = math.sqrt(4*a*c - b**2)
        parte2 = (f"(2 / {denom:.4f}) * arctan( (2*{a}x + {b}) / {denom:.4f} )")
        tipo = "Δ < 0 → Sem raízes reais (resultado com arctan)"

    print(f"\nTipo do denominador: {tipo}")

    print("\nIntegral final:")
    print("-"*70)
    print(f"∫ (A*x + B)/(a*x² + b*x + c) dx =")
    print(f"    {P:.4f} * ln|{a}x² + {b}x + {c}|")
    print(f"  + {Q:.4f} * [{parte2}] + C")
    print("-"*70)

    print("\nFim do cálculo!!")

if __name__ == "__main__":
    integral_racional_terminal()
