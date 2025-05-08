import tkinter as tk
from tkinter import ttk, messagebox
from modulos.calculadora import calcular_integral_doble
from modulos.graficador import generar_grafica_3d

class AplicacionIntegralesDobles:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Integrales Dobles")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        self.configurar_estilo()
        self.crear_widgets()
    
    def configurar_estilo(self):
        estilo = ttk.Style()
        estilo.configure("TLabel", font=("Arial", 11))
        estilo.configure("TButton", font=("Arial", 11), padding=5)
        estilo.configure("TEntry", font=("Arial", 11), padding=5)
        estilo.configure("Titulo.TLabel", font=("Arial", 14, "bold"))
        estilo.configure("Resultado.TLabel", font=("Arial", 12), background="#e6f2ff", padding=10)
    
    def crear_widgets(self):
        frame_principal = ttk.Frame(self.root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame_principal, text="Calculadora de Integrales Dobles", style="Titulo.TLabel").grid(
            row=0, column=0, columnspan=2, pady=(0, 20), sticky="w")
        
        ttk.Label(frame_principal, text="Función f(x,y):").grid(
            row=1, column=0, sticky="w", pady=(10, 5))
        self.funcion_entry = ttk.Entry(frame_principal, width=40)
        self.funcion_entry.grid(row=1, column=1, sticky="ew", pady=(10, 5))
        ttk.Label(frame_principal, text="Ejemplo: x**2 + y**2, sin(x)*cos(y), etc.").grid(
            row=2, column=1, sticky="w", pady=(0, 10))
        
        ttk.Label(frame_principal, text="Límites para x:").grid(
            row=3, column=0, sticky="w", pady=5)
        frame_limites_x = ttk.Frame(frame_principal)
        frame_limites_x.grid(row=3, column=1, sticky="ew", pady=5)
        ttk.Label(frame_limites_x, text="Desde:").pack(side=tk.LEFT, padx=(0, 5))
        self.x_min_entry = ttk.Entry(frame_limites_x, width=10)
        self.x_min_entry.pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(frame_limites_x, text="Hasta:").pack(side=tk.LEFT, padx=(0, 5))
        self.x_max_entry = ttk.Entry(frame_limites_x, width=10)
        self.x_max_entry.pack(side=tk.LEFT)
        
        ttk.Label(frame_principal, text="Límites para y:").grid(
            row=4, column=0, sticky="w", pady=5)
        frame_limites_y = ttk.Frame(frame_principal)
        frame_limites_y.grid(row=4, column=1, sticky="ew", pady=5)
        ttk.Label(frame_limites_y, text="Desde:").pack(side=tk.LEFT, padx=(0, 5))
        self.y_min_entry = ttk.Entry(frame_limites_y, width=10)
        self.y_min_entry.pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(frame_limites_y, text="Hasta:").pack(side=tk.LEFT, padx=(0, 5))
        self.y_max_entry = ttk.Entry(frame_limites_y, width=10)
        self.y_max_entry.pack(side=tk.LEFT)
        
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.grid(row=5, column=0, columnspan=2, pady=20)
        
        self.calcular_btn = ttk.Button(frame_botones, text="Calcular Integral", 
                                       command=self.calcular_integral)
        self.calcular_btn.pack(side=tk.LEFT, padx=10)
        
        self.graficar_btn = ttk.Button(frame_botones, text="Mostrar Gráfica", 
                                       command=self.mostrar_grafica)
        self.graficar_btn.pack(side=tk.LEFT, padx=10)

        # Botón para limpiar los campos
        self.limpiar_btn = ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos)
        self.limpiar_btn.pack(side=tk.LEFT, padx=10)
        
        frame_resultados = ttk.LabelFrame(frame_principal, text="Resultado")
        frame_resultados.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)
        self.resultado_label = ttk.Label(frame_resultados, text="", style="Resultado.TLabel")
        self.resultado_label.pack(fill=tk.X, expand=True, padx=10, pady=10)
        
        frame_principal.columnconfigure(1, weight=1)
    
    def calcular_integral(self):
        try:
            funcion = self.funcion_entry.get().strip()
            x_min = self.x_min_entry.get().strip()
            x_max = self.x_max_entry.get().strip()
            y_min = self.y_min_entry.get().strip()
            y_max = self.y_max_entry.get().strip()
            
            if not funcion or not x_min or not x_max or not y_min or not y_max:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
                return
            
            try:
                x_min = float(eval(x_min))
                x_max = float(eval(x_max))
                y_min = float(eval(y_min))
                y_max = float(eval(y_max))
            except:
                messagebox.showerror("Error", "Los límites deben ser expresiones numéricas válidas.")
                return
            
            resultado = calcular_integral_doble(funcion, x_min, x_max, y_min, y_max)
            self.resultado_label.config(text=f"El resultado de la integral doble es: {resultado:.6f}")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
    
    def mostrar_grafica(self):
        try:
            funcion = self.funcion_entry.get().strip()
            x_min = self.x_min_entry.get().strip()
            x_max = self.x_max_entry.get().strip()
            y_min = self.y_min_entry.get().strip()
            y_max = self.y_max_entry.get().strip()
            
            if not funcion or not x_min or not x_max or not y_min or not y_max:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
                return
            
            try:
                x_min = float(eval(x_min))
                x_max = float(eval(x_max))
                y_min = float(eval(y_min))
                y_max = float(eval(y_max))
            except:
                messagebox.showerror("Error", "Los límites deben ser expresiones numéricas válidas.")
                return
            
            generar_grafica_3d(funcion, x_min, x_max, y_min, y_max)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al generar la gráfica: {str(e)}")

    def limpiar_campos(self):
        self.funcion_entry.delete(0, tk.END)
        self.x_min_entry.delete(0, tk.END)
        self.x_max_entry.delete(0, tk.END)
        self.y_min_entry.delete(0, tk.END)
        self.y_max_entry.delete(0, tk.END)
        self.resultado_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionIntegralesDobles(root)
    root.mainloop()
