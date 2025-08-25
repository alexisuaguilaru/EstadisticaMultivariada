import numpy as np

import pandas as pd

def ANOVATable(
        LinearModel,
    ) -> pd.DataFrame:
    """
    Función para construir la tabla de ANOVA 
    en base a un modelo de Regresión Lineal, 
    se extraen los valores de interés y son 
    reacomodados en un formato tabular.
    """
    
    ColumnsANOVA = [
        'Fuente Variación',
        'Suma de Cuadrados',
        'Grados de Libertad',
        'Cuadrados Medios',
        'F_0',
    ]
    Table = pd.DataFrame(columns=ColumnsANOVA)
    Table['Fuente Variación'] = ['Regresión','Residuales','Total']

    MeanSquares_Reg = LinearModel.mse_model
    MeanSquares_Res = LinearModel.mse_resid
    MeanSquares_Tot = LinearModel.mse_total
    Table['Cuadrados Medios'] = [MeanSquares_Reg,MeanSquares_Res,MeanSquares_Tot]

    DegreeFreedom_Reg = LinearModel.df_model
    DegreeFreedom_Res = LinearModel.df_resid
    DegreeFreedom_Tot = DegreeFreedom_Reg + DegreeFreedom_Res
    Table['Grados de Libertad'] = [DegreeFreedom_Reg,DegreeFreedom_Res,DegreeFreedom_Tot]

    Table['Suma de Cuadrados'] = Table['Cuadrados Medios']*Table['Grados de Libertad']

    Table['F_0'] = [LinearModel.fvalue,np.nan,np.nan]

    return Table.set_index('Fuente Variación')

def ANOVATable_Manual(
        DataMatrixX: np.ndarray,
        RealValuesY: np.ndarray,
        EstimateBetas: np.ndarray,
    ) -> pd.DataFrame:
    """
    Función para construir la tabla de ANOVA 
    en base a las observaciones (`DataMatrixX` y 
    `RealValuesY`) y los coeficientes de regresión 
    (`EstimateBetas`), se hacen uso de las formulas 
    matriciales para determinar los diferentes 
    valores de la tabla.
    """

    ColumnsANOVA = [
        'Fuente Variación',
        'Suma de Cuadrados',
        'Grados de Libertad',
        'Cuadrados Medios',
        'F_0',
    ]
    Table = pd.DataFrame(columns=ColumnsANOVA)
    Table['Fuente Variación'] = ['Regresión','Residuales','Total']

    SizeN = DataMatrixX.shape[0]
    SumSquares_Tot = (RealValuesY.T@RealValuesY - np.sum(RealValuesY)**2/SizeN)[0,0]
    SumSquares_Reg = (EstimateBetas.T@DataMatrixX.T@RealValuesY - np.sum(RealValuesY)**2/SizeN)[0,0]
    SumSquares_Res = SumSquares_Tot - SumSquares_Reg
    Table['Suma de Cuadrados'] = [SumSquares_Reg,SumSquares_Res,SumSquares_Tot]

    DegreeFreedom_Reg = len(EstimateBetas) - 1
    DegreeFreedom_Res = SizeN - len(EstimateBetas)
    DegreeFreedom_Tot = DegreeFreedom_Reg + DegreeFreedom_Res
    Table['Grados de Libertad'] = [DegreeFreedom_Reg,DegreeFreedom_Res,DegreeFreedom_Tot]

    Table['Cuadrados Medios'] = Table['Suma de Cuadrados']/Table['Grados de Libertad']

    Table['F_0'] = [Table['Cuadrados Medios'].iloc[0]/Table['Cuadrados Medios'].iloc[1],np.nan,np.nan]

    return Table.set_index('Fuente Variación')