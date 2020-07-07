import datetime
import pandas as pd
import pickle
from xgboost.sklearn import XGBRegressor 
from sklearn.model_selection import GridSearchCV
import sys


def nex_7_days():
    """"
    return list of next 7 days times
    """
    holder=[]
    base = datetime.datetime.today()
    for x in range(0, 7):
        holder.append(base + datetime.timedelta(days=x))
    return holder



def create_features(df, label=None):
    """
    Creates time series features from time feature
    """
    df['dayofweek'] = df['time'].dt.dayofweek
    df['quarter'] = df['time'].dt.quarter
    df['month'] = df['time'].dt.month
    df['year'] = df['time'].dt.year
    df['dayofyear'] = df['time'].dt.dayofyear
    df['dayofmonth'] = df['time'].dt.day
    df['weekofyear'] = df['time'].dt.weekofyear
    
    X = df[['dayofweek','quarter','month','year',
           'dayofyear','dayofmonth','weekofyear']]
    if label:
        y = df[label]
        return X, y
    return X


if __name__ == '__main__':
    try:
        df = pd.DataFrame({'time':nex_7_days()})
        df1 = create_features(df)
        # Load model from file
        with open('Model/pickle_model.pkl', 'rb') as file:
            pickle_model = pickle.load(file)
        # Make forcasting
        next_7days_prediction = pd.DataFrame({'time':nex_7_days(), 'predection' : pickle_model.predict(df1),})
        # Save Dataframe as csv file
        next_7days_prediction.to_csv('prediction/forcastNext7Days.csv',
         index = False,
         line_terminator = '|')
    except:
        print('Please retry operation with valid requirements')
        sys.exit(0)