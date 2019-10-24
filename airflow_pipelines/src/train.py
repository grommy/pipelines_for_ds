import os

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier
import joblib

# get data
# X_prep = pd.read_csv("data/churn_preprocessed.csv")
print("Start")
X_prep = np.genfromtxt("data/X_prep.csv", delimiter=",")
y_prep = np.genfromtxt("data/y_prep.csv", delimiter=",")

# # Split data into train and test sets.
# X = data.drop(['Churn'], axis=1)
# y = data['Churn']
trainX, testX, trainY, testY = train_test_split(X_prep, y_prep, test_size=0.2, random_state=42)

params = {'base_score': 0.5,
          'booster': 'gbtree',
          'colsample_bylevel': 1,
          'colsample_bytree': 1,
          'gamma': 0,
          'learning_rate': 0.1,
          'max_delta_step': 0,
          'max_depth': 4,
          'min_child_weight': 1,
          'missing': None,
          'n_estimators': 50,
          'nthread': 1,
          'objective': 'binary:logistic',
          'reg_alpha': 0,
          'reg_lambda': 1,
          'scale_pos_weight': 1,
          'seed': 0,
          'silent': 1,
          'subsample': 0.7,
          'early_stopping_rounds': 10}

model = XGBClassifier(**params)
model.fit(trainX, trainY)

# evaluate
predY = model.predict(testX)
score = roc_auc_score(testY, predY)

print(score)

directory = "tmp/saved_models"
if not os.path.exists(directory):
    os.makedirs(directory)

joblib.dump(model, os.path.join(directory, "model.pkl"))
# model.save_model(os.path.join(directory, "model.pkl"))

print("Success")
