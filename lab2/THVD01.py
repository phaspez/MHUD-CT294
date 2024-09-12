import numpy as np
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

print("Number of classes: %d" % len(np.unique((iris_y))))
print("Number of data points: %d" % len(iris_y))

# split into 2/3 train 1/3 test
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.33, random_state=42)
# split into 80% train 20% test
#X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.2, random_state=42)

k_neighbors = [1, 2, 4, 6, 8, 10]
p_dis = [1, 2]

models_1 = {}
models_2 = {}
# Dictionary to store accuracies
accuracies = {p: [] for p in p_dis}

for k in k_neighbors:
    for p in p_dis:
        model = KNeighborsClassifier(n_neighbors=k, p=p)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        accuracies[p].append(accuracy)
        print(f"KNN with p={p}, k={k}")
        print(f"Accuracy: {accuracy}")
        print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred, labels=[0, 1, 2])}")
        print(f"Classification Report:\n{classification_report(y_test, y_pred)}")

# Plot the results
plt.figure(figsize=(10, 6))
for p in p_dis:
    plt.plot(k_neighbors, accuracies[p], marker='o', label=f'p={p}')

plt.title('Accuracy of KNN for different values of k and p')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()