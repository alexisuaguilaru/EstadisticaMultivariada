## Ejercicio 02
## Repetir el ejemplo con los datos `datasets::trees` de 
## R que proporciona mediciones del diámetro, altura y 
## volumen de madera en 31 cerezos negros talados. Repetir 
## el ejemplo con los datos `datasets::trees` de R que 
## proporciona mediciones del diámetro, altura y volumen 
## de madera en 31 cerezos negros talados.


## Descargar el dataset para usarlo en Python
# data(trees)
# write.csv(trees,file='trees_dataset.csv',row.names=FALSE)


## Carga de datos y División de los datos para modelos
Arboles <- read.csv('RegresionMultiple/Ejercicios/trees_dataset.csv')
# Arboles
pairs(Arboles)


## Extracción de los valores para las matrices X , y
size_n <- nrow(Arboles)

DataX <- Arboles[c('Girth','Height')]
# DataX
MatrizX <- as.matrix(cbind(x0=1,Arboles))
# MatrizX
ValuesY <- as.matrix(Arboles['Volume'])
# ValuesY


## Modelo de Regresión Multiple Manual
EstimatorBeta <- solve(t(MatrizX)%*%MatrizX)%*%t(MatrizX)%*%ValuesY
# EstimatorBeta
EstimateY_Manual <- MatrizX%*%EstimatorBeta
# EstimatorY_Manual

## Modelo de Regresión Multiple
Modelo <- lm(Volume ~ Girth + Height,Arboles)
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
