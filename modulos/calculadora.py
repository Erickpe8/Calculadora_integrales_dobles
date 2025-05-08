import numpy as np
from scipy import integrate
import sympy as sp

def calcular_integral_doble(funcion_str, x_min, x_max, y_min, y_max):
    """
    Calcula la integral doble de una función en coordenadas rectangulares.
    
    Args:
        funcion_str (str): Expresión de la función a integrar en términos de x e y.
        x_min (float): Límite inferior para x.
        x_max (float): Límite superior para x.
        y_min (float): Límite inferior para y.
        y_max (float): Límite superior para y.
    
    Returns:
        float: Resultado de la integral doble.
    """
    try:
        # Primero intentamos con sympy para una solución simbólica
        x, y = sp.symbols('x y')
        funcion_sympy = sp.sympify(funcion_str)
        
        # Intentar integración simbólica
        try:
            resultado = sp.integrate(funcion_sympy, (y, y_min, y_max), (x, x_min, x_max))
            return float(resultado)
        except:
            # Si la integración simbólica falla, usamos integración numérica
            pass
        
        # Definir la función para integración numérica
        def funcion_numpy(y, x):
            # Reemplazar las variables en la expresión
            expr = funcion_str.replace('x', str(x)).replace('y', str(y))
            # Evaluar la expresión
            return eval(expr, {"__builtins__": {}}, 
                       {"sin": np.sin, "cos": np.cos, "tan": np.tan, 
                        "exp": np.exp, "log": np.log, "sqrt": np.sqrt,
                        "pi": np.pi, "e": np.e})
        
        # Calcular la integral usando scipy.integrate.dblquad
        resultado, error = integrate.dblquad(funcion_numpy, x_min, x_max, 
                                            lambda x: y_min, lambda x: y_max)
        
        return resultado
    
    except Exception as e:
        raise Exception(f"Error al calcular la integral: {str(e)}")

