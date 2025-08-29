## Ejercicio de Tarea 04
Explica lo siguiente. 

### **a**. ¿Qué supuestos del modelo de regresión lineal múltiple deben verificarse?
* El modelo sea lineal en sus parámetros (coeficientes de regresión)
* Correcta especificación del modelo
* Independencia entre las variables y el error
* Esperanza del error es $0$
* Homocedasticidad
* No autocorrelación en los errores
* Normalidad en los errores
* Más muestras/observaciones que parámetros en el modelo ($n>p+1$)
* Variación en la variable de respuesta
* No colinealidad entre las variables regresoras

### **b**. ¿Cómo se interpretan los intervalos de confianza? Si construimos un intervalo de confianza del 95% para un coeficiente $\beta_j$, ¿Cuál sería la lectura correcta o interpretación correcta sobre este intervalo?
Según la longitud (o tamaño) del intervalo generado se tiene una mayor o menor confianza sobre la estimación del coeficiente (o parámetro, en general); mientras más grande sea el intervalo de confianza, menor confianza (o seguridad) se tiene sobre la estimación.

Si se usa un nivel de confianza se vuelve a la probabilidad de que el valor real del parámetro pertenezca al intervalo, es decir, el 95% de los intervalos que se construyan (independientemente de su tamaño) contendrán al valor real del parámetro que se está estimando.

### **c**. Describe los métodos de selección de variables y sus ventajas y desventajas:

#### i Selección hacia adelante (forward) 
A partir de un modelo lineal simple que usa la mejor la variable para describir la variable de respuesta, se van añadiendo variables, según algún estadístico o criterio, hasta que se hayan terminado de considerar todas las variables o no haya una mejora según el criterio seleccionado. Como es un proceso greedy, no se garantiza que se alcance el mejor modelo global, sino que (en la mayoría de los casos) se llegue a un modelo subóptimo, esto se debe a que no se está considerando el quitar variables ya añadidas; en cambio, puede añadir variables que, en conjunto con las ya añadidas, sean significativas para el modelo.

#### ii Selección hacia atrás (backward)
A partir de un modelo lineal conformado por todas las variables, se van eliminando variables, según algún estadístico o criterio, hasta que se hayan considerado todas las variables o no se pueda eliminar más variables. Como considera todas las variables posibles le permite puede evaluar sí una variable es importante para el modelo o no al momento de que es removida, esto permite considerar, en la mayoría de los casos, únicamente la variables importantes; no considera las variables que son importantes en combinación y se vuelve sensible a la multicolinealidad, haciendo que se alcancen modelos subóptimos. 


#### iii selección por pasos (stepwise) y/o mejor subconjunto (best subset) 
Hace uso de forward y backward selection para obtener las mejores variables, donde primero intenta añade una variable con paso forward y luego intenta elimina una con paso backward, esto en base a la criteria o estadístico empleado. Esta doble verificación hace que el algoritmo sea computacional complejo, es decir, tiene que pasar más veces por varios posibles modelos; pero esto le permite escoger el mejor subconjunto variables de forma robusta, es decir, evita los modelos subóptimos.


#### Explica cómo se utilizan para elegir el modelo final.
Se puede generar un modelo por cada uno de los métodos y posterior escoger el mejor modelo según una criterio o métrica. De forma alternativa se puede escoger la selección stepwise para asegurar con cierta robustez obtener el mejor modelo.