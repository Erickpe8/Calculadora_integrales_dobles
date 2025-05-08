# Calculadora de Integrales Dobles 🔢📊

La Calculadora de Integrales Dobles es una herramienta interactiva que permite calcular integrales de funciones matemáticas con dos variables, 
𝑥 y 𝑦. La aplicación cuenta con una interfaz fácil de usar, donde el usuario puede ingresar la función matemática y los límites de integración para cada variable. Además de calcular el valor de la integral, la herramienta también genera una representación gráfica en 3D de la función, mostrando tanto la superficie de la función como el área y el volumen bajo la curva. 

Esta visualización gráfica facilita la comprensión del resultado y la interpretación geométrica del concepto de la integral doble. Con esta herramienta, los usuarios pueden obtener resultados precisos de manera rápida y sencilla.

## Características 📐

- **Cálculo de integrales dobles:** Ingresa una función y los límites de integración para obtener el resultado de la integral. ✍️
- **Visualización 3D:** Muestra la función \( f(x, y) \) y el volumen bajo la superficie. 🧮
- **Interfaz fácil de usar:** Permite ingresar las funciones y los límites de integración de manera clara. 🧠
- **Funciones adicionales:** Botones para calcular, graficar y limpiar los campos de entrada.

## Funcionamiento 🧮

El sistema sigue tres etapas principales:

1. **Ingreso de Datos:** El usuario ingresa la función \( f(x, y) \) y los límites de integración para \( x \) e \( y \). ✍️
2. **Cálculo de la Integral Doble:** Al hacer clic en "Calcular Integral", el sistema utiliza la librería **SymPy** para interpretar y calcular simbólicamente la integral.▶️
3. **Visualización de la Función:** Al hacer clic en "Mostrar Gráfica", el sistema genera una gráfica 3D usando **Matplotlib**, representando la superficie de la función y la región de integración. ▶️

## Uso de la Aplicación

1. Ingresa la función \( f(x, y) \) en el campo correspondiente.
2. Define los límites de integración para \( x \) y \( y \).
3. Haz clic en "Calcular Integral" para obtener el resultado de la integral. ▶️
4. Haz clic en "Mostrar Gráfica" para visualizar la función en 3D. 📊

## Ejecución del Programa 🛠️

Puedes ejecutar el programa de dos maneras:

1. Abre el archivo `main.py` y presiona "F5".
2. O en el menú, selecciona **Run > Ejecutar Archivo de Python**.

## Instalación ✍️🛠️

### Requisitos

Para usar esta herramienta, necesitas tener instalados los siguientes programas:

- **Visual Studio Code**: Un entorno de desarrollo recomendado para trabajar con Python.
- **Python**: El lenguaje de programación utilizado para desarrollar el sistema.

#### Instalación de Visual Studio Code

1. Puedes descargar Visual Studio Code desde su página oficial:  
   [Descargar Visual Studio Code](https://code.visualstudio.com/).

2. Alternativamente, si estás en Windows, puedes instalarlo desde la **Microsoft Store**:  
   [Descargar desde Microsoft Store](https://apps.microsoft.com/store/detail/XP9KHM4BK9FZ7Q).

#### Instalación de Python

1. Para instalar Python, visita la página oficial y descarga la última versión:  
   [Descargar Python](https://www.python.org/downloads/).

   También puedes instalar Python directamente desde Visual Studio Code.

### Instalación de Librerías 📚

El proyecto utiliza las siguientes librerías:

- **🧠 SymPy**: Para matemáticas simbólicas y cálculo de integrales.
- **📐 NumPy**: Para cálculos numéricos y manipulación de arreglos.
- **📊 Matplotlib**: Para la visualización gráfica en 3D.
- **🖼️ Tkinter**: Para la creación de la interfaz gráfica de usuario.

Para instalar estas librerías, abre el terminal de Visual Studio Code y ejecuta los siguientes comandos:

```bash
pip install sympy
pip install numpy
pip install matplotlib
pip install tkinter
