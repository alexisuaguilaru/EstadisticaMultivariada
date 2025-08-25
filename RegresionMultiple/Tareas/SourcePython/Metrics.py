import pandas as pd

def ManualRSquared(
        ANOVA: pd.DataFrame,
    ) -> float:
    """
    Función para calcular el puntaje r^2  
    de forma manual.
    """

    return float.__truediv__(*ANOVA['Suma de Cuadrados'][['Regresión','Total']])

def ManualAdjRSquared(
        ANOVA: pd.DataFrame,
    ) -> float:
    """
    Función para calcular el puntaje r^2  
    ajustado de forma manual.
    """

    r_squared = ManualRSquared(ANOVA)
    return 1-((1-r_squared)*ANOVA.loc['Total','Grados de Libertad'])/(ANOVA.loc['Residuales','Grados de Libertad'])