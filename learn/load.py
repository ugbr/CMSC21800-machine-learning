'''load.py Load loads the dataset, cleans it, and generates a new clean
csv file.
'''

#standard imports
import pandas as pd


def load(filename):
  '''load(filename) takes as input a filename and loads a dataframe.
  '''
  return pd.read_csv(filename) #demo


def clean(df):
  '''clean(df) takes as input a dataframe and fixes any data errors  
     *that might affect your results*. it returns a copy of the dataframe 
     without errors.
  '''

  df['INJURIES_TOTAL'] = df['INJURIES_TOTAL'].fillna(0)
  df['INJURIES_FATAL'] = df['INJURIES_FATAL'].fillna(0)
  df['INJURIES_INCAPACITATING'] = df['INJURIES_INCAPACITATING'].fillna(0)  
  df['INJURIES_NON_INCAPACITATING'] = df['INJURIES_NON_INCAPACITATING'].fillna(0)
  df['INJURIES_REPORTED_NOT_EVIDENT'] = df['INJURIES_REPORTED_NOT_EVIDENT'].fillna(0)
  df['INJURIES_NO_INDICATION'] = df['INJURIES_NO_INDICATION'].fillna(0)  
  df.loc[df.NUM_UNITS > df.INJURIES_TOTAL + df.INJURIES_NO_INDICATION, 'INJURIES_NO_INDICATION'] = df['NUM_UNITS'] - df['INJURIES_TOTAL']
  
  df = df[df['LATITUDE'].notna()]
  df = df[df['LONGITUDE'].notna()]
  df = df[(df['WEATHER_CONDITION'] != 'UNKNOWN') & (df['LIGHTING_CONDITION'] != 'UNKNOWN') & (df['ROADWAY_SURFACE_COND'] != 'UNKNOWN')]

  return df #demo


#The main() function  of this program

if __name__ == "__main__":
    df = load('data_2.csv')
    cdf = clean(df)
    cdf.to_csv('clean.csv')
