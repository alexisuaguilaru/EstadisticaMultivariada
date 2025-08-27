import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

import pandas as pd

def PlotScatterReg(
        Dataset: pd.DataFrame,
        FeaturesModel: list[str],
        TargetLabel: str,
        TargetName: str,
    ):
    """
    Función para generar el plot 
    de dispersión entre los atributos 
    y la variable de respuesta.
    """

    pair_plot = sns.PairGrid(Dataset[[*FeaturesModel,TargetLabel]])
    pair_plot.map_diag(
        sns.histplot
    )
    pair_plot.map_offdiag(
        sns.regplot,
        ci=None,
        line_kws = {
            'color' : 'gray',
            'ls' : ':',
        },
    )

    pair_plot.figure.suptitle(
        f'Relación de Atributos con \n{TargetName}', 
        fontsize = 18,
        y = 1.05,
    )

    for ax in pair_plot.axes.flat:
        ax.set_xlabel(
            ax.get_xlabel(),
            fontsize=14,
        )
        ax.set_ylabel(
            ax.get_ylabel(),
            fontsize=14,
        )

        ax.tick_params(
            axis = 'both',
            which = 'major',
            labelsize = 12,
        )

    return pair_plot

def PlotQQResiduals(
        LinearModel    
    ):
    """
    Función para plotear los cuartiles de 
    los valores predichos (observados/esperados 
    contra los obtenidos).
    """

    QuantilesTheoObs , RegressionLineParams = stats.probplot(
        LinearModel.resid,
        dist = 'norm',
    )

    fig , axes = plt.subplots()
    sns.scatterplot(
        x = QuantilesTheoObs[0],
        y = QuantilesTheoObs[1],
        ax = axes,
    )

    axes.axline(
        (0,0),
        slope=RegressionLineParams[0],
        color = 'gray',
        linestyle = ':',
    )
    axes.set_xlabel('Cuantiles Teóricos')
    axes.set_ylabel('Cuantiles de Residuales')
    axes.set_title('Probabilidad Normal de los Residuales',size=13)

    return fig

def PlotExpectedEstimate(
        LinearModel,
        ExpectedValuesY: pd.Series,
    ):
    """
    Función para plotear los valores 
    esperados y estimados del modelo 
    lineal.
    """

    fig , axes = plt.subplots()

    sns.scatterplot(
        x = ExpectedValuesY,
        y = LinearModel.fittedvalues,
        ax = axes,
    )
    axes.axline(
        (0,0),
        slope = 1,
        color = 'gray',
        linestyle = ':',
    )
    axes.set_title('Ajuste del Modelo')
    axes.set_xlabel('Valores Observados')
    axes.set_ylabel('Valores Estimados')

    return fig

def PlotPredictResiduals(
        LinearModel,
        TargetName: str,
    ):
    """
    Función para plotear los residuales 
    en función de las valores predichos.
    """

    fig , axes = plt.subplots()
    
    sns.scatterplot(
        x = LinearModel.fittedvalues,
        y = LinearModel.resid,
        ax = axes,
    )
    axes.set_xlabel(TargetName)
    axes.set_ylabel('Residual')
    axes.set_title('Residuales en Función de la Respuesta Predicha',size=13)

    return fig

def PlotVariableResiduals(
        LinearModel,
        Dataset: pd.DataFrame,
        FeaturesModel: list[str],
    ):
    """
    Función para plotear los residuales 
    en función de las variables del modelo.
    """

    fig , axes = plt.subplots(
        len(FeaturesModel),
        figsize = (7,3*len(FeaturesModel)+1),
        layout = 'tight',
    )

    for feature , ax in zip(FeaturesModel,axes.ravel()):
        sns.scatterplot(
            x = Dataset[feature],
            y = LinearModel.resid,
            ax = ax,
        )
        ax.set_ylabel('Residuales')

    fig.suptitle('Residuales en Función de las Variables Regresoras',size=13,y=1.0)

    return fig