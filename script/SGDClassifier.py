from sklearn.linear_model import SGDClassifier
from sklearn.datasets import fetch_openml

import numpy as np
import joblib

mnist = fetch_openml('mnist_784', version=1)
mnist.keys()

X, y = mnist["data"], mnist["target"]
X.shape
y.shape

y = y.astype(np.uint8)


X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

y_train_5 = (y_train == 5)
y_test = (y_test == 5)

sgd_clf = SGDClassifier(max_iter=1000, tol=1e-3, random_state=42)
sgd_clf.fit(X_train, y_train_5)


some_digit = X[0]

print(sgd_clf.predict([some_digit]))

filename = 'finalized_model.sav'
joblib.dump(model, filename)
