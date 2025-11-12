import math
from fractions import Fraction

class IntegradorCaso3:
    """
    Implementa a decomposição e integração do Caso 3:
    Integral de (Ax+B) / (x^2 + x1)(x^2 + x2) dx
    Decomposição: (Cx+D)/(x^2+x1) + (Ex+F)/(x^2+x2)
    """
    
    def __init__(self, A_num, B_num, x1_const, x2_const):
        """
        Inicializa com os coeficientes do numerador (Ax+B) e as constantes
        dos fatores quadráticos irredutíveis (x^2 + x1) e (x^2 + x2).
        
        Args:
            A_num: Coeficiente A do numerador
            B_num: Coeficiente B do numerador
            x1_const: Constante do primeiro fator quadrático
            x2_const: Constante do segundo fator quadrático
        """
        # Coeficientes do numerador (Ax + B)
        self.A = Fraction(A_num)
        self.B = Fraction(B_num)
        
        # Constantes dos fatores quadráticos irredutíveis
        self.x1_const = x1_const
        self.x2_const = x2_const
        
    def _integrar_quadratico(self, C, D, a_const):
        """
        Calcula a integral de (Cx + D) / (x^2 + a_const) dx.
        
        Fórmula: (C/2) * ln|x^2 + a_const| + (D/sqrt(a_const)) * arctan(x/sqrt(a_const))
        
        Args:
            C: Coeficiente linear do numerador
            D: Termo constante do numerador
            a_const: Constante do fator quadrático
            
        Returns:
            str: String representando a integral calculada
        """
        # Calcula a primeira parte: (C/2) * ln|x^2 + a_const|
        C_div_2 = C.divide(Fraction(2))
        integral_x = f"({C_div_2}) * ln|x^2 + {a_const}|"

        # Calcula a raiz quadrada da constante
        a = math.sqrt(a_const)
        
        # Calcula a segunda parte: (D/sqrt(a_const)) * arctan(x/sqrt(a_const))
        D_sobre_a = D.doubleValue() / a 
        integral_const = f"{D_sobre_a:.5f} * arctan(x/{a:.5f})"
        
        # Retorna a soma das duas partes
        return f"{integral_x} + {integral_const}"
        
    def decompor_e_integrar(self):
        """
        Realiza a decomposição em frações parciais e calcula a integral final.
        
        Utiliza as fórmulas deduzidas:
        - E = A / (x1 - x2)  e  C = -E
        - F = B / (x1 - x2)  e  D = -F
        
        Returns:
            str: String com o resultado da integral ou mensagem de erro
        """
        x1, x2 = self.x1_const, self.x2_const
        
        # Valida se os fatores quadráticos são distintos
        if x1 == x2:
            return "Erro: Fatores quadráticos repetidos. Esta implementação requer fatores distintos."
            
        try:
            # Calcula o denominador (x1 - x2)
            denominador = Fraction(x1 - x2)
            
            # Calcula os coeficientes de decomposição
            E_coef = self.A / denominador
            C_coef = -E_coef
            F_coef = self.B / denominador
            D_coef = -F_coef
            
            # --- 1. Apresentação da Decomposição ---
            print("--- Decomposição em Frações Parciais (Caso 3) ---")
            print(f"Coeficientes encontrados (baseados em {self.A}x + {self.B}):")
            print(f"  C = {C_coef}, D = {D_coef}")
            print(f"  E = {E_coef}, F = {F_coef}")
            
            # Exibe a decomposição final
            decomposicao = f"({C_coef}x + {D_coef})/(x^2 + {x1}) + ({E_coef}x + {F_coef})/(x^2 + {x2})"
            print(f"\nDecomposição: {decomposicao}")

            # --- 2. Integração dos Termos ---
            # Integra cada termo da decomposição
            integral_1 = self._integrar_quadratico(C_coef, D_coef, x1)
            integral_2 = self._integrar_quadratico(E_coef, F_coef, x2)
            
            # Formata o resultado final
            resultado_final = f"\nResultado Integral:\n{integral_1} + {integral_2} + C_int"
            
            return resultado_final
        
        except ZeroDivisionError:
            return "Erro: x1 e x2 são iguais. Divisão por zero."
        
        except Exception as e:
            return f"Ocorreu um erro: {e}"
