### 1. De acuerdo al ejemplo 1 de la sección 3.3 de la página del curso, los vectores propios calculados con la función `princomp(records2, cor = TRUE)` difieren de los calculados directamente de la matriz de correlación con `eigen(cor.mat)` en algunos signos. ¿Por qué? ¿Cómo se justifica esto formalmente? ¿Afecta en algo a las componentes principales?

Primero hay que notar que `princomp` usa `eigen`, después de obtener la matriz de correlación o de covarianza del dataset que se le pasa, por lo que se podría esperar obtener los mismos resultados salvo que realice algún otro postproceso que facilite la interpretación (análisis, lectura) de las carga de los componentes principales; pero, numéricamente, se llegan a los mismos resultados (en autovalores y autovectores), por lo tanto, este cambio de signo se vuelve como un tipo de convenio o de estandarización sobre los outputs de PCA para facilitar la interpretación de los resultados. El cambio de signo, en algún autovector, no impone ningún problema para el propio PCA (varianza explicada, selección de número de componentes), únicamente se debe que cambiar la narrativa que se le da a la interpretación de los valores/cargas en cada componente principal, el cómo interactúan dentro del mismo o cómo se "leen" respecto a otros componentes principales.

*REFERENCIA:*
* [1] D. Harvey & B. Hanson, A Comparison of Functions for PCA. R Project: https://cran.r-project.org/web/packages/LearnPCA/vignettes/Vig_07_Functions_PCA.pdf

-------

### 2. En general, ¿Cuál es la forma de elegir con cuántas componentes principales trabajar? Justifica tu respuesta. Deberás consultar algún libro o artículo. Cítalo(s) e incluye la(s) referencia(s) completa(s).

Una forma de elegir el número de componentes principales es usar un scree plot en el que se hace el plot de los eigenvalores ordenados (del más grande al más pequeño) con el fin de encontrar el codo o punto de inflexión, que ocurre cuando los restantes o siguientes eigenvalores son de magnitudes relativamente pequeñas (esto comparado con los valores más grandes o anteriores) y similares; lo anterior se puede ver como encontrar el punto donde todos los siguientes eigenvalores son de magnitudes similares y pequeños. Y supongo que esto funciona debido a que si solo se conservan los eigenvalores de magnitudes o valores más grandes entonces la mayor parte de la varianza de los datos se podría explicar con éstos (justamente cómo conservar los eigenvalores que explican un cierto umbral de varianza pero de forma más sistemática).

*REFERENCIA:*
* [1] R. Johnson & D. Wichern, Applied Multivariate Statistical Analysis. Harlow, England: Pearson Educated Limited, 2014. 

-------
