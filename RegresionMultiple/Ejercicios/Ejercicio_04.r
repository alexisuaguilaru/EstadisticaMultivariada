## Ejercicio 4
## Usaremos el conjunto de datos data("marketing") que contiene 200 observaciones 
## de un experimento publicitario que evalúa el impacto de tres medios de anuncio en 
## las ventas. Para cada observación se registran los presupuestos de publicidad (en miles 
## de dólares) y las ventas obtenidas.

# install.packages("datarium")
library(datarium)
data("marketing")
# write.csv(marketing,file='marketing_dataset.csv',row.names=FALSE)