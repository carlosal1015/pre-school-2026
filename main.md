---
bibliography: references.bib
nocite: |
  @*
---

# Pre-pre-curso: Fundamentos de computación científica con Python

**Evento:** [Summer School and Workshop on Optimization and Operator Learning](https://numerics.ovgu.de/sac3/?show=events_summerschooltrujillo2026)  
**Fechas del Pre-pre-curso:** Del 6/01/2026 al 17 de febrero de 2026.  
**Frecuencia:** Martes y Viernes (15:00-17:00 hrs).  
**Ubicación:** [Zoom Video Communications](https://us05web.zoom.us/j/83960651426?pwd=zQDqM3kfC7uPOP7dWf5UzxwJgLCm1H.1#success).

---

## Descripción del curso

Este curso intensivo de 10 días está diseñado para preparar a los
asistentes para la pre-escuela de verano principal (Summer School).
El objetivo es proporcionar una base sólida en los conceptos
fundamentales y las herramientas de programación en Python que son
esenciales para la computación científica y el análisis de datos.
Las sesiones serán prácticas, enfocadas en el uso de librerías
estándar de la industria y la implementación de algoritmos básicos.

Cubriremos los fundamentos de la programación en Python, el manejo de
arreglos numéricos de alto rendimiento con NumPy, la visualización de
datos con Matplotlib y una introducción práctica a los conceptos de
aprendizaje automático como el _descenso de gradiente_ y la
_regresión lineal_.

## Audiencia

Este pre-pre-curso está dirigido a estudiantes de pregrado,
investigadores jóvenes y profesionales en las áreas de ciencia,
tecnología, ingeniería y matemáticas (STEM) que planean asistir a la
pre-escuela de verano y desean fortalecer sus habilidades de
programación para el análisis numérico.

## Prerrequisitos

No se requiere experiencia previa en programación.
Sin embargo, se asume una familiaridad con conceptos matemáticos
básicos a nivel universitario, como cálculo y álgebra lineal.
La motivación para aprender a programar es el requisito más
importante.

## Objetivos de Aprendizaje

Al finalizar este pre-pre-curso, los participantes serán capaces de:

- Escribir y ejecutar scripts básicos en Python.
- Utilizar Jupyter Notebooks para la computación interactiva.
- Manejar y manipular arreglos multidimensionales con NumPy y PyTorch.
- Crear visualizaciones y gráficos de datos 2D con Matplotlib.
- Comprender el concepto de descenso de gradiente.
- Implementar un modelo simple de regresión lineal desde cero.
- Preparar su entorno de computación para los temas avanzados de la
pre-escuela de verano.

## Software y Materiales

- **Laptop personal:** Obligatoria para todas las sesiones.
- **Software:** Se solicitará a los participantes que instalen el
administrador de paquetes [uv](https://docs.astral.sh/uv/getting-started/installation)
antes del inicio del curso.
Esto proporcionará todas las herramientas necesarias, incluyendo
Python, JupyterLab, NumPy, SciPy, PyTorch y Matplotlib.
- **Materiales del curso:** Se proporcionarán notebooks de Jupyter y
otros materiales a través de un repositorio público.
- **Carpeta compartida**: [Enlace a Dropbox](https://www.dropbox.com/scl/fo/x67ac9r8enaa4zewgwzbm/AB9oGu5a1UAm0IXajbaue60?rlkey=kt6d4ygbr4ys1f0n9880bec6h&st=3lculzjs&dl=0).
- **Grabación de las sesiones**: [Lista de reproducción](https://youtube.com/playlist?list=PLWb96MFebtXjpVhTF9N7-CAo1fOtPoB6q&si=ZIyWQPGGfyT8dAgz).
- **Disponibilidad de ejemplos**: [Programas ejemplos del libro](https://github.com/carlosal1015/pre-school-2026/tree/main/src/gaddis).
- **Repositorios de ejemplos complementarios**: [Python-Programming](https://github.com/carlosal1015/Python-Programming) / [Cpp-Programming](https://github.com/carlosal1015/Cpp-Programming).
- **Lectura sobre ecuaciones diferenciales**: https://numerics.ovgu.de/teaching/numnn/skript.pdf
<!-- https://www.octotree.io -->


## Facilitadores

Este pre-pre-curso será facilitado por un equipo de tres entusiastas
de las matemáticas y la programación:
- **Carlos**: Matemático organizador.
- **Matihus**: Estudiante de matemática, quien recientemente presentó un póster sobre su investigación.
- **Karen**: Estudiante de matemática con un gran interés en la aplicación de la tecnología al análisis numérico.

La idea de este curso nació de conversaciones informales y el deseo
compartido de hacer la computación científica más accesible para
nuestros compañeros. ¡Esperamos aprender juntos!

$$\mathbf{a}_{n+1}=\mathbf{a}_n-\eta\nabla f(\mathbf{a}_n)$$

## Programa preliminar

| Fecha             | Sesiones                                        | Actividad de Programación                                                                                                                                                                                                                 | Referencias                                  |
| :---------------- | :---------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------- |
| *Antes del 6/01*  | **Sesión 0:** Instalación y Ambiente            | [Instalar `uv`](https://www.youtube.com/watch?v=jF-1tfnqxtA) y familiarizarse con JupyterLab. Crear un notebook que importe NumPy, SciPy y PyTorch para verificar sus versiones.                                                          | @Aznaran2022 @Aznaran2022a @Aznaran2025      |
| 6/01/2026         | **Fundamentos:** de Python a NumPy              | Cargar un dataset (CSV), calcular estadísticas (media, std), y visualizarlo con Matplotlib. Implementar multiplicación de matrices y resolver un sistema lineal con NumPy. [Ejercicios](https://cpp-review-dune.github.io/python/ex1.pdf) | @Gaddis2023 @Wei2022 @Sundnes2020 @Nagar2018 |
| 9/01/2026         | **Optimización I:** Descenso de Gradiente (GD)  | Implementar GD desde cero para minimizar una función (ej. Rosenbrock) y comparar variantes (batch, mini-batch).                                                                                                                           | @Beck2023 @Grippo2023 @Pec32026              |
| *Fin de semana*   | *Proyecto 1: Regresión Lineal*                  | Implementar regresión lineal usando solo NumPy y luego comparar con una implementación básica en PyTorch (sin `nn.Linear`).                                                                                                               | @Johansson2024                               |
| 13/01/2026        | **Optimización II:** Acelerando la Convergencia | Añadir Momento y una tasa de aprendizaje adaptativa (ej. AdaGrad/RMSProp) a la implementación de GD.                                                                                                                                      |                                              |
| **16 de enero**   | **Optimización III:** SciPy y ODEs              | Resolver un problema de optimización no lineal con `scipy.optimize.minimize`. Adicionalmente, resolver una Ecuación Diferencial Ordinaria (ODE) simple con `scipy.integrate.solve_ivp`.                                                   |                                              |
| **20 de enero**   | **Optimización IV:** Métodos de 2º Orden        | Implementar el Método de Newton y comparar su convergencia con los métodos de 1er orden.                                                                                                                                                  |                                              |
| **23 de enero**   | **Optimización V:** con Restricciones (KKT)     | Resolver un problema de asignación de recursos (ej. cartera de inversión) usando las condiciones KKT.                                                                                                                                     |                                              |
| *Fin de semana*   | *Proyecto 2: Optimizador Avanzado*              | Implementar un optimizador como Adam desde cero, encapsulándolo en una clase.                                                                                                                                                             |                                              |
| **27 de enero**   | *Semana de Repaso y Consultas 1*                | (Opcional) Taller de revisión de código y profundización en la teoría de la dualidad lagrangiana.                                                                                                                                         |                                              |
| **30 de enero**   | *Semana de Repaso y Consultas 2*                | (Opcional) Taller de depuración de código (`pdb`) y preparación para el bloque de Deep Learning.                                                                                                                                          |                                              |
| **3 de febrero**  | **Deep Learning I:** Intro a PyTorch            | Comprender tensores y `autograd`. Construir un Perceptrón Multicapa (MLP) en PyTorch y entrenarlo en el dataset MNIST.                                                                                                                    |                                              |
| **6 de febrero**  | **Deep Learning II:** Modelos de Regresión      | Implementar y entrenar un modelo de regresión logística con PyTorch para un problema de clasificación.                                                                                                                                    |                                              |
| **10 de febrero** | **Proyecto Final:** Ideación y Propuesta        | **Entregable:** Propuesta de proyecto de 1 página (objetivos, dataset y métricas de éxito).                                                                                                                                               |                                              |
| **13 de febrero** | **Proyecto Final:** Desarrollo y Mentoría       | **Hito:** Prototipo funcional del modelo. Sesiones de mentoría para resolver dudas.                                                                                                                                                       |                                              |
| **17 de febrero** | **Proyecto Final:** Demo Day                    | **Presentación:** Demo de 5 minutos del proyecto, resultados y lecciones aprendidas.                                                                                                                                                      |