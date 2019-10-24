import os

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from sklearn.pipeline import Pipeline, FeatureUnion
from transformers import ItemSelector, DummyTransformer

# get data
data = pd.read_csv("data/churn.csv")

# preprocess
data_explore = data.dropna()
data_explore['TotalCharges'] = data_explore['TotalCharges'].astype('float')

drop_columns = ['gender', 'Partner', 'Dependents', 'IDs']

cat_cols = ['PhoneService', 'MultipleLines',
            'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
            'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
            'PaymentMethod']

numerical_columns = list(set(data_explore.columns.tolist())
                         - set(cat_cols) - set(drop_columns) - {"Churn"})
print(numerical_columns)

# Pipeline
dummy_pipeline = Pipeline(steps=[
    ("select", ItemSelector(cat_cols)),
    ("dummy", DummyTransformer(cat_cols)),
])

pipeline = \
    FeatureUnion([
        ("numerical", ItemSelector(numerical_columns)),
        ("dummy", dummy_pipeline),
    ])

X_prep = pipeline.fit_transform(data_explore)
# y = LabelEncoder().fit_transform(data_explore["Churn"])
y = data_explore["Churn"].replace({"Yes": 1, "No": 0})

# save pipeline
directory = "tmp/saved_models"
if not os.path.exists(directory):
    os.makedirs(directory)
joblib.dump(pipeline, os.path.join(directory, "pipeline.pkl"))

# save data
# print(X_prep[0])
# print(X_prep.shape)
np.savetxt("data/X_prep.csv", X_prep, delimiter=",")
np.savetxt("data/y_prep.csv", y, delimiter=",")
print("Success")
