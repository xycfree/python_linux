#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/5/22 16:48
# @Descript:
import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier  # KNN
from sklearn.linear_model import LinearRegression  # 线性回归
import matplotlib.pyplot as plt

iris = datasets.load_iris()  # 花的数据集
iris_X = iris.data  # 类型
iris_y = iris.target  # 类别

print(iris_X[:2, :])  # 前2个数据的值
print(iris_y)

x_train, x_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3) # 把数据集分为学习和测试数据，测试占比30%

knn = KNeighborsClassifier()  # 定义knn
knn.fit(x_train, y_train)  # 训练数据集
print(knn.predict(x_test))  # 预测
print(y_test)

print('预测房价数据')
loaded_data = datasets.load_boston()  # 房价数据集
data_X = loaded_data.data
data_y = loaded_data.target
molder = LinearRegression()  # 定义线性回归对象
molder.fit(data_X, data_y)  # 训练数据集
print(molder.predict(data_X[:4, :]))  # 输出预测值
print(data_y[:4])  # 实际值

X,y = datasets.make_regression(n_samples=100, n_features=1,n_targets=1, noise=5)  # 自己创建线性数据集
plt.scatter(X, y)
# plt.show()

print('# -------------------------------------------------- #')
# 交叉验证
iris = datasets.load_iris()  # 花的数据集
X = iris.data  # 类型
y = iris.target  # 类别
from sklearn.cross_validation import cross_val_score  # 得分
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)  # 占比40%
knn = KNeighborsClassifier(n_neighbors=5)  # 考虑数据点附近的5个值，然后综合平均,n_neighbors选择值范围的考虑
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error')  # 误差
print(loss.mean)
scores = cross_val_score(knn, iris_X, iris_y, cv=10, scoring='accuracy')  # 把测试和学习的数据分成5组
print(scores)
print(scores.mean())  # 平均

print('# ------------------------------- #')
from sklearn.learning_curve import learning_curve  # 可视化
from sklearn.datasets import load_digits  # 数字 数据集
from sklearn.svm import SVC
# import matplotlib.pyplot as plt
# import numpy as np

digits = load_digits()
X = digits.data
y = digits.target

train_sizes, train_loss, test_loss = learning_curve(
    SVC(gamma=0.001), X, y, cv=10, scoring='mean_squared_error', train_sizes=[0.1, 0.25, 0.5, 0.75, 1]
)
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(train_sizes, train_loss_mean, 'o-', color='r', label='training')
plt.plot(train_sizes, test_loss_mean, 'o-', color='g', label='Cross-validation')

plt.xlabel('Training examples')
plt.ylabel('Loss')
plt.legend(loc='best')
plt.show()
