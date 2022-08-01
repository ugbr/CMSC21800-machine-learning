'''scratch.py

You will write down any "scratch" code that you use to explore the dataset in
this file. This code does not produce any outputs (it does not modify any files)
but allows you to explore the data. We're separating this code from the rest because 
it allows us to understand your thought process during data exploration.

*Remember to replace the return statements with your code*
'''

#standard imports
from scipy.stats import pearsonr 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.svm import SVC

#TODO 1.
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


#TODO 2.
def plot(df):
  '''plot(df) takes as input a clean dataframe and generates a plot. The 
  style of the plot and variables are up to you.
  '''
  
  plt.scatter(df['A'],df['B'])
  return None

def train(X_train, Y_train):
	logit = LogisticRegression()
	logit.fit(X_train,Y_train)
	return logit

def evaluate(model, X_test, Y_test):
  Y_pred = model.predict(X_test)
  return classification_report(Y_pred, Y_test)

def featurize(df):
  df['CRASH_TYPE'] = 1.0 * (df['CRASH_TYPE'] == 'INJURY AND / OR TOW DUE TO CRASH') 
  return df.to_numpy()

#The main() function  of this program

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    df = load('data_2.csv')
    cdf = clean(df)

    # cdf['CRASH_TYPE'] = 1.0 * (cdf['CRASH_TYPE'] == 'INJURY AND / OR TOW DUE TO CRASH')
    # cdf['DAMAGE'] = cdf['DAMAGE'].replace('$500 OR LESS', 0)
    # cdf['DAMAGE'] = cdf['DAMAGE'].replace('$501 - $1,500', 1)
    # cdf['DAMAGE'] = cdf['DAMAGE'].replace('OVER $1,500', 2)

    # print('Correlation between DAMAGE and POSTED_SPEED_LIMIT', pearsonr(cdf['DAMAGE'], cdf['POSTED_SPEED_LIMIT']))
    # print('Correlation between DAMAGE and CRASH_TYPE', pearsonr(cdf['DAMAGE'], cdf['CRASH_TYPE']))
    # print('Correlation between DAMAGE and NUM_UNITS', pearsonr(cdf['DAMAGE'], cdf['NUM_UNITS']))
    # cdf = cdf[~cdf['INJURIES_TOTAL'].isna()]
    # print('Correlation between DAMAGE and INJURIES_TOTAL', pearsonr(cdf['DAMAGE'], cdf['INJURIES_TOTAL']))
    # print('Correlation between DAMAGE and CRASH_HOUR', pearsonr(cdf['DAMAGE'], cdf['CRASH_HOUR']))

    # print('Missing Values for DAMAGE -',cdf['DAMAGE'].isna().sum())
    # print('Missing Values for POSTED_SPEED_LIMIT -',cdf['POSTED_SPEED_LIMIT'].isna().sum())
    # print(cdf['ALIGNMENT'].value_counts())
    # print(cdf['TRAFFICWAY_TYPE'].value_counts())
    # print(cdf.groupby(['DAMAGE','FIRST_CRASH_TYPE'])[['FIRST_CRASH_TYPE']].count())
    # print(cdf.groupby(['DAMAGE','TRAFFICWAY_TYPE'])[['TRAFFICWAY_TYPE']].count())

    #print(cdf.head())

    label = 'DAMAGE'
    features =  ['POSTED_SPEED_LIMIT', 'CRASH_TYPE', 'NUM_UNITS', 'INJURIES_TOTAL', 'CRASH_HOUR']#

    X = featurize(cdf[features])
    Y = cdf[label].to_numpy()


    X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

    #Q3.TODO
    model = train(X_train, Y_train)

    #Q4.TODO
    print(evaluate(model, X_test, Y_test))