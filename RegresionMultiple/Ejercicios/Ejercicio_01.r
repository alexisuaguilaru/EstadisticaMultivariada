## Ejercicio 01
## Un analista hace un estudio químico y espera que el rendimiento de 
## cierta sustancia se vea afectado por dos factores. Se realizan 17
## experimentos cuyos datos se registran en el cuadro siguiente. Por 
## experimentos similares, se sabe que los factores $x_1$ y $x_2$ no
## están relacionados; por ello, el analista decide utilizar un modelo
## de regresión lineal múltiple. Calcule el modelo de regresión y 
## grafíquelo sobre las observaciones.


## Carga de datos y División de los datos para modelos
Experimentos <- read.csv('RegresionMultiple/Ejercicios/est_quimico.csv')
# Experimentos


## Extracción de los valores para las matrices X , y
size_n <- nrow(Experimentos)

DataX <- Experimentos[c('x1','x2')]
# DataX
MatrizX <- as.matrix(cbind(x0=1,DataX))
# MatrizX
ValuesY <- as.matrix(Experimentos['y'])
# ValuesY


## Modelo de Regresión Multiple Manual
EstimatorBeta <- solve(t(MatrizX)%*%MatrizX)%*%t(MatrizX)%*%ValuesY
# EstimatorBeta
EstimateY_Manual <- MatrizX%*%EstimatorBeta
# EstimatorY_Manual

## Modelo de Regresión Multiple
Modelo <- lm(y ~ x1 + x2,Experimentos)
SummaryModel <- summary(Modelo)
SummaryModel


## Métricas del modelo R^2, SSE y estimación de $\sigma^2$
SummaryModel$r.squared
# SummaryModel$adj.r.squared
SSE <- sum(residuals(Modelo)^2)
SSE

EstimateSquareSigma <- SSE/(size_n - nrow(EstimatorBeta))
EstimateSquareSigma


## Plotting de valores observados contra estimados
par(pin = c(5, 5))
plot(
    x=ValuesY,
    y=fitted(Modelo),
    xlab = 'Valores Observados',
    ylab = 'Valores Estimados',
)
abline(
    a=0,
    b=1, 
    col='gray',
    lwd=1,
)
