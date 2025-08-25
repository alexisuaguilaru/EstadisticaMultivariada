from scipy import stats
import numpy as np

import pandas as pd

def TestIndividualCoefficients(
        LinearModel,
        Dataset: pd.DataFrame,
        FeaturesModel: list[str],
        LevelSignificance: float = 0.05,
    ):
    """
    Función para calcular el estadístico t_0 
    para la prueba sobre los coeficientes 
    individuales de regresión en un Modelo 
    Lineal; también se muestra el valor de 
    t_1 (para la prueba alternativa) con 
    un cierto nivel de significancia.
    """

    CovarianceEstimateBetas = CalculatedCovarianceEstimateBetas(LinearModel,Dataset,FeaturesModel)

    t_Value_1 = stats.t.ppf(1-LevelSignificance/2,LinearModel.df_resid)
    print(f't_1 :: {t_Value_1}')
    print(f'\nt_0 Values')
    for index_feature , (feature,beta_value) in enumerate(LinearModel.params[1:].items(),1):
        tValue_0 = beta_value / np.sqrt(CovarianceEstimateBetas[index_feature,index_feature])
        print(f'{feature} :: {tValue_0}')

def ConfidenceIntervalsCoefficient(
        LinearModel,
        Dataset: pd.DataFrame,
        FeaturesModel: list[str],
        IndexFeatures: list[int],
        LevelSignificance: float = 0.05,
    ) -> None:
    """
    Función para determinar los intervalos de 
    confianza para los coeficientes de 
    regresión de un modelo.
    """

    CovarianceEstimateBetas = CalculatedCovarianceEstimateBetas(LinearModel,Dataset,FeaturesModel)
    
    tValue_1 = stats.t.ppf(1 - LevelSignificance/2,LinearModel.df_resid)
    for index_feature in IndexFeatures:
        beta_value = LinearModel.params.iloc[index_feature]
        interval_borders = tValue_1*np.sqrt(CovarianceEstimateBetas[index_feature+1,index_feature+1])
        left_interval = beta_value - interval_borders
        right_interval = beta_value + interval_borders
        print(f'{FeaturesModel[index_feature]} , {beta_value} :: [{left_interval} , {right_interval}] , Longitud {right_interval-left_interval}')

def ConfidenceIntervalsMeanResponse(
        LinearModel,
        Dataset: pd.DataFrame,
        FeaturesModel: list[str],
        Observations: pd.DataFrame,
        LevelSignificance: float = 0.05,
    ) -> None:
    """
    Función para determinar los intervalos de 
    confianza para la respuesta/predicción 
    media del modelo.
    """

    CovarianceEstimateBetas = CalculatedCovarianceEstimateBetas(LinearModel,Dataset,FeaturesModel)
    
    tValue_1 = stats.t.ppf(1 - LevelSignificance/2,LinearModel.df_resid)
    for index_observation , observation in enumerate(Observations.iloc):
        actual_values = observation[FeaturesModel]
        values_x = np.concat([[1],actual_values])[:,None]
        prediction = LinearModel.predict(observation).iloc[0]

        var_prediction = (values_x.T@CovarianceEstimateBetas@values_x)[0,0]
        interval_borders = tValue_1*np.sqrt(var_prediction)

        left_interval = prediction - interval_borders
        right_interval = prediction + interval_borders
        print(f'[{index_observation}] :: {left_interval} <= {prediction} <= {right_interval} , Longitud {right_interval-left_interval}')

def CalculatedCovarianceEstimateBetas(
        LinearModel,
        Dataset: pd.DataFrame,
        FeaturesModel: list[str],
    ) -> np.ndarray:
    """
    Función para calcular la matriz 
    de covarianza de los parámetros 
    o coeficientes de regresión en 
    base a las observaciones y modelo 
    lineal.
    """

    SizeN = Dataset.shape[0]
    DataMatrix = np.concat(
        [
            np.ones((SizeN,1)),
            Dataset[FeaturesModel].to_numpy()
        ],
        axis=1,
    )

    EstimateSquareSigma = LinearModel.mse_resid # == ANOVA.loc['Residuales','Cuadrados Medios']
    return EstimateSquareSigma*np.linalg.inv(DataMatrix.T@DataMatrix)