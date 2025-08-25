import numpy as np

import pandas as pd

def ManualLinearModel(
        Dataset: pd.DataFrame,
        FeaturesModel: list[str],
        TargetLabel: str,
    ) -> np.ndarray:
    """
    Función para calcular los valores de  
    los parámetro betas para un modelo lineal.
    """

    SizeN = Dataset.shape[0]

    DataMatrixX = np.concat(
            [
                np.ones((SizeN,1)),
                Dataset[FeaturesModel].to_numpy()
            ],
            axis=1,
        )
    RealValuesY = Dataset[[TargetLabel]].to_numpy()

    return np.linalg.inv(DataMatrixX.T@DataMatrixX) @ DataMatrixX.T @ RealValuesY , DataMatrixX , RealValuesY