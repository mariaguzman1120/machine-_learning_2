import pandas as pd


def data_clean(text):
    list_text = text.replace('\n', ' ').split('. ')
    df = pd.DataFrame({'sentences': list_text})
    return df


