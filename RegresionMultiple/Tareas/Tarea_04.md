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


#### ii Selección hacia atrás (backward)


#### iii selección por pasos (stepwise) y/o mejor subconjunto (best subset) 


#### Explica cómo se utilizan para elegir el modelo final.
