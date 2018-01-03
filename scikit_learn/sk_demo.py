#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/5/22 9:39
# @Descript:

"""
print(__doc__)


# Code source: Jaques Grobler
# License: BSD 3 clause


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

##############################################################################
# Binarize image data

im = np.array(Image.open('code.jpg'))
# print(im)
h, w, san = im.shape
# X = [(h - x, y) for x in range(h) for y in range(w) if im[x][y]]
X = [(h - x, y) for x in range(h) for y in range(w) if im[x][y][2] < 200]
X = np.array(X)
n_clusters = 4

##############################################################################
# Compute clustering with KMeans

k_means = KMeans(init='k-means++', n_clusters=n_clusters)
k_means.fit(X)
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_
k_means_labels_unique = np.unique(k_means_labels)

##############################################################################
# Plot result

colors = ['#4EACC5', '#FF9C34', '#4E9A06', '#FF3300']
plt.figure()
plt.hold(True)
for k, col in zip(range(n_clusters), colors):
    my_members = k_means_labels == k
    cluster_center = k_means_cluster_centers[k]
    plt.plot(X[my_members, 1], X[my_members, 0], 'w',
             markerfacecolor=col, marker='.')
    plt.plot(cluster_center[1], cluster_center[0], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)
plt.title('KMeans')
plt.grid(True)
plt.show()
