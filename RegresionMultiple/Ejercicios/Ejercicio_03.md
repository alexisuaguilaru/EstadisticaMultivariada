# Ejercicio 03
Subir a Github los dos ejercicios previos tanto con solución en R como en Python. Comparar las funciones. Ventajas y desventajas de ambas.

## Actividad
Ambos métodos, para los dos ejercicios realizados, llegan a los mismos resultados por lo cual podría no haber una distinción significativa salvo el cómo se realiza; una implementación robusta y ya probada siempre será mejor que una realizada a mano, haciendo que, independientemente del lenguaje usado, sea conveniente usar los modelos de regresión múltiple ya implementados.

Debido al enfoque y soluciones generadas (análisis estadísticos) con R, se tiene que sus implementaciones y funciones permiten obtener los valores y gráficos para evaluar el modelo ajustado al conjunto de datos; esto facilita obtener las métricas suficiente para descartar un modelo (debido a underfit o overfit) o mejorarlo con otros parámetros. 

En cambio, en Python, se tiene que realizar lo anterior de manera 'manual' (si se hace uso de Scikit Learn se tiene que llamar las funciones respectivas para generar las métricas) para evaluar un modelo, esto hace que se consuma más tiempo para generar resultados similares; pero a la vez genera una mayor robustez al momento de generar o crear modelos más complejos, haciendo que tengamos un control más fino sobre las predicciones o estimaciones obtenidas.