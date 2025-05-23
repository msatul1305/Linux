import pandas as pd


def azureml_main(dataframe1=None, dataframe2=None):
    scored_results = dataframe1[['PatientID', 'Scored Labels', 'Scored Probabilities']]
    scored_results.rename(columns={'Scored Labels': 'DiabetesPrediction',
                                   'Scored Probabilities': 'Probability'},
                          inplace=True)
    return scored_results
