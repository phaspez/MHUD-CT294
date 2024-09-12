import numpy as np
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

print("Number of classes: %d" % len(np.unique((iris_y))))
print("Number of data points: %d" % len(iris_y))

# split into 2/3 train 1/3 test
#X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.33, random_state=42)
# split into 80% train 20% test
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.2, random_state=42)


model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("GaussianNB")
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred, labels=[0, 1, 2])}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")

print(X_train)
