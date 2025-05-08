import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def generar_grafica_3d(funcion_str, x_min, x_max, y_min, y_max):
    """
    Genera una gráfica 3D de la función y la región de integración.
    
    Args:
        funcion_str (str): Expresión de la función a graficar en términos de x e y.
        x_min (float): Límite inferior para x.
        x_max (float): Límite superior para x.
        y_min (float): Límite inferior para y.
        y_max (float): Límite superior para y.
    """
    try:
        # Crear una malla de puntos
        x = np.linspace(x_min, x_max, 50)
        y = np.linspace(y_min, y_max, 50)
        X, Y = np.meshgrid(x, y)
        
        # Evaluar la función en la malla
        Z = np.zeros_like(X)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                # Reemplazar las variables en la expresión
                expr = funcion_str.replace('x', str(X[i, j])).replace('y', str(Y[i, j]))
                # Evaluar la expresión
                try:
                    Z[i, j] = eval(expr, {"__builtins__": {}}, 
                                  {"sin": np.sin, "cos": np.cos, "tan": np.tan, 
                                   "exp": np.exp, "log": np.log, "sqrt": np.sqrt,
                                   "pi": np.pi, "e": np.e})
                except:
                    Z[i, j] = np.nan
        
        # Crear la figura
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Graficar la superficie
        surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.8,
                              linewidth=0, antialiased=True)
        
        # Graficar la región de integración (base)
        xx, yy = np.meshgrid([x_min, x_max], [y_min, y_max])
        zz = np.zeros_like(xx)
        ax.plot_surface(xx, yy, zz, color='red', alpha=0.3)
        
        # Graficar los límites de la región
        for x_val in [x_min, x_max]:
            ax.plot([x_val, x_val], [y_min, y_max], [0, 0], 'r-', linewidth=2)
        for y_val in [y_min, y_max]:
            ax.plot([x_min, x_max], [y_val, y_val], [0, 0], 'r-', linewidth=2)
        
        # Configurar etiquetas y título
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z = f(X,Y)')
        ax.set_title(f'Gráfica de f(x,y) = {funcion_str}\nRegión: [{x_min}, {x_max}] × [{y_min}, {y_max}]')
        
        # Añadir una barra de color
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
        
        # Mostrar la gráfica
        plt.tight_layout()
        plt.show()
    
    except Exception as e:
        raise Exception(f"Error al generar la gráfica: {str(e)}")

