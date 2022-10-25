import pandas as pd
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler as rs
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
# from sklearn.preprocessing import LabelEncoder, MinMaxScaler
# from sklearn.metrics import accuracy_score, log_loss, precision_score, recall_score
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
# from sklearn import metrics
# from xgboost import XGBClassifier
# from sklearn.tree import DecisionTreeClassifier

def load_data(data_list):
  data = pd.DataFrame([data_list], columns=['GENDER','AGE_GROUP','BMI','HIGHCHOL','HIGHBP','PHYSACTIVITY','ALCOHOL','FRUITS','VEGGIES','SMOKING','YELLOW_FINGERS','COUGHING','SHORT_BREATH'])
  return data

def get_prediction(model_url,df):
  loaded_model = joblib.load(model_url)
  # new_array = rs.fit_transform(new)
  # newdata = pd.DataFrame(new_array, columns=data.columns)
  result = loaded_model.predict(df)
  return result[0]


# nl = [0,1,22,1,0,1,0,1,1,0,0,0,0]
# print(get_prediction("models/model_stroke.sav",load_data(nl)))