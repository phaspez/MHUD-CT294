import numpy as np
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv("./winequality-red.csv", sep=";")
df.info()
df.describe()
df.isna().sum()
df["quality"].unique()
X = df[["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
               "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH",
               "sulphates", "alcohol"]]
y = df[["quality"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)
# split into 2/3 test 1/3 train
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.33)

print("Number of data points x: %d" % len(X))
print("Number of classes: %d" % len(np.unique((y))))
print("Number of data points: %d" % len(y))

model = KNeighborsClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")

pred_7 = model.predict(X_test[0:8])
accuracy = accuracy_score(y_test[0:8], pred_7)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test[0:8], pred_7)}")
print(f"Classification Report:\n{classification_report(y_test[0:8], pred_7)}")

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")