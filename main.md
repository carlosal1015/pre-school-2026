---
bibliography: references.bib
nocite: |
  @*
---

# Pre-pre-curso: Fundamentos de computación científica con Python

**Evento:** [Sac3 Summer School on Applied Analysis, Scientific Computing and Data Science](https://numerics.ovgu.de/sac3/?show=events_summerschooltrujillo2026)  
**Fechas del Pre-pre-curso:** Del 5 de enero al 20 de febrero.  
**Frecuencia:** Dos veces por semana (90 minutos por sesión).  
**Ubicación:** Online.

---

## Descripción del Curso

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

## Facilitadores

Este pre-curso será facilitado por un equipo de tres entusiastas de
las matemáticas y la programación:
- **Carlos**: Matemático organizador.
- **Matihus**: Estudiante de matemática, quien recientemente presentó un póster sobre su investigación.
- **Karen**: Estudiante de matemática con un gran interés en la aplicación de la tecnología al análisis numérico.

La idea de este curso nació de conversaciones informales y el deseo compartido de hacer la computación científica más accesible para nuestros compañeros. ¡Esperamos aprender juntos!

## Horario preliminar

| Fecha             | Módulo                                                  | Actividad de Programación                                                                                                  |
| :---------------- | :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------- |
| **5 de enero**    | **Módulo 1:** De Python a NumPy                         | **Práctica 1:** Cargar un dataset (CSV) con NumPy, calcular estadísticas y visualizarlo con Matplotlib.                    |
| **9 de enero**    | **Módulo 2:** Descenso de Gradiente desde Cero          | **Práctica 2:** Implementar GD para encontrar el mínimo de una función multivariable (ej. Rosenbrock).                     |
| **12 de enero**   | **Módulo 3:** Acelerando la Convergencia                | **Práctica 3:** Añadir Momento y una tasa de aprendizaje adaptativa (ej. AdaGrad) a la implementación de GD.               |
| **16 de enero**   | **Módulo 4:** Optimización Práctica con SciPy           | **Práctica 4:** Resolver un problema de optimización no lineal usando `scipy.optimize.minimize` con diferentes algoritmos. |
| **19 de enero**   | **Módulo 5:** Métodos de 2º Orden (Optim. sin Restric.) | **Práctica 5:** Implementar el Método de Newton y comparar su convergencia con los métodos de 1er orden.                   |
| **23 de enero**   | **Módulo 6:** Optimización con Restricciones (KKT)      | **Práctica 6:** Resolver un problema de asignación de recursos (ej. cartera de inversión) usando KKT.                      |
| **26 de enero**   | *Semana de Repaso y Consultas 1*                        | (Opcional) Taller de revisión de código y profundización en la teoría de la dualidad lagrangiana.                          |
| **30 de enero**   | *Semana de Repaso y Consultas 2*                        | (Opcional) Taller de depuración de código (`pdb`) y preparación para el bloque de Deep Learning.                           |
| **6 de febrero**  | **Módulo 7:** Introducción al Deep Learning con PyTorch | **Práctica 7:** Construir un Perceptrón Multicapa (MLP) en PyTorch y entrenarlo en el dataset MNIST.                       |
| **9 de febrero**  | **Módulo 8:** Modelos de Regresión con PyTorch          | **Práctica 8:** Implementar y entrenar un modelo de regresión logística para un problema de clasificación.                 |
| **13 de febrero** | **Proyecto Final:** Ideación y Propuesta                | **Entregable:** Propuesta de proyecto de 1 página (objetivos, dataset y métricas de éxito).                                |
| **16 de febrero** | **Proyecto Final:** Desarrollo y Mentoría               | **Hito:** Prototipo funcional del modelo. Sesiones de mentoría para resolver dudas.                                        |
| **20 de febrero** | **Proyecto Final:** Demo Day                            | **Presentación:** Demo de 5 minutos del proyecto, resultados y lecciones aprendidas.                                       |

## Referencias

Aznarán, C. (n.d.-a). Introducción a la programación en lenguaje python. Retrieved January 13, 2026, from https://numerical-analysis-2024.github.io/tutorial/intro_python/python.html  
Aznarán, C. (n.d.-b). Introduction to scientific computing with python 🎪. Retrieved January 13, 2026, from https://scientificpython.readthedocs.io  
Beck, A. (2023). Introduction to nonlinear optimization: Theory, algorithms, and applications with python and MATLAB, second edition (2nd ed.). Society for Industrial; Applied Mathematics. https://doi.org/10.1137/1.9781611977622  
CS50. (n.d.-a). CS50’s adaptation of ChatGPT for students and teachers. Retrieved January 13, 2026, from https://cs50.ai  
CS50. (n.d.-b). CS50’s adaptation of codespaces for students and teachers. Retrieved January 13, 2026, from https://cs50.dev  
Johansson, R. (2024). Numerical python: Scientific computing and data science applications with numpy, SciPy and matplotlib. Apress. https://doi.org/10.1007/979-8-8688-0413-7  
Liu, R., Zenke, C., Liu, C., Holmes, A., Thornton, P., & Malan, D. J. (2024). Teaching CS50 with AI: Leveraging generative artificial intelligence in computer science education. Proceedings of the 55th ACM Technical Symposium on Computer Science Education v. 1, 750–756. https://doi.org/10.1145/3626252.3630938  
Lynch, S. (2018). Dynamical systems with applications using python. Springer International Publishing. https://doi.org/10.1007/978-3-319-78145-7  
Malan, D. J. (2025). Teaching CS50 with AI. https://www.youtube.com/watch?v=6rAWxGAG6EI.  
Nagar, S. (2018). Introduction to python for engineers and scientists: Open source solutions for numerical computation. Apress. https://doi.org/10.1007/978-1-4842-3204-0  
project, P. (n.d.). Material. Retrieved January 13, 2026, from https://numerics.ovgu.de/pec3/document/index.php  
Sundnes, J. (2020). Introduction to scientific programming with python. Springer International Publishing. https://doi.org/10.1007/978-3-030-50356-7