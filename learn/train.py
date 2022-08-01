'''train.py loads a clean csv and trains a model on it.
'''

#standard imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.svm import SVC

def train(X_train, Y_train):
	'''Takes in X_train and Y_train should output a model
	'''
	logit = LogisticRegression()
	logit.fit(X_train, Y_train)
	return logit

def evaluate(model, X_test, Y_test):
	'''Takes in X_test and Y_test should output a classification report
	'''
	Y_pred = model.predict(X_test)
	return classification_report(Y_pred, Y_test)

def featurize(df):
	'''
	   X - Should take a dataframe of feature columns and
	   output a 2D NxK numpy of N data points and K dimensional
	   features. 
	'''
	df['CRASH_TYPE'] = 1.0 * (cdf['CRASH_TYPE'] == 'INJURY AND / OR TOW DUE TO CRASH')
	return df.to_numpy()

#The main() function  of this program
if __name__ == "__main__":
	cdf = pd.read_csv('clean.csv')

  #Q2.TODO 
	label = 'DAMAGE'
	features =  ['POSTED_SPEED_LIMIT', 'CRASH_TYPE', 'NUM_UNITS', 'INJURIES_TOTAL', 'CRASH_HOUR']#

	X = featurize(cdf[features])
	Y = cdf[label].to_numpy()

	X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

    #Q3.TODO
	model = train(X_train,Y_train)

	#Q4.TODO
	print(evaluate(model, X_test, Y_test))





