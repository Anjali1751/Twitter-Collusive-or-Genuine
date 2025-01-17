from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sn
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from sklearn import preprocessing 
import statsmodels.api as sm 
import scipy.optimize as opt 
import numpy as np 
import pylab as pl 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import jaccard_score 

#dataset
chd_data = pd.read_csv('massachusetts.csv')
chd_data.drop(['education'], inplace=True, axis=1)

#Removing NaN
chd_data.dropna(axis=0, inplace=True)
print(chd_data.head(), chd_data.shape)
print(chd_data.TenYearCHD.value_counts())



