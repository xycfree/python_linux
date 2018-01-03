#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/5/22 15:05
# @Descript:

import os
import numpy as np
import mahotas as mh
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report

x = []
y = []

for path, subdirs, files in os.walk('data'):
    print(path, subdirs, files)
    for filename in files:
        f = os.path.join(path, filename)
        target = filename[3:filename.index('-')]
        img = mh.imread(f, as_grey=True)
        if img.shape[0] <= 30 or img.shape[1] <= 30:
            continue
        img_resized = mh.imresize(img, (30, 30))  # 设置图片大小为30,30
        x.append(img_resized.reshape((900, 1)))
        y.append(target)

x = np.array(x)
x = x.reshape(x.shape[:2])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.1)
pipeline = Pipeline([
    ('clf', SVC(kernel='rbf', gamma=0.01, C=100))
])

paramters = {
    'clf__gamma': (0.01, 0.03, 0.1, 0.3, 1),
    'clf__c': (0.1, 0.3, 1, 3, 10, 30),
}

grid_search = GridSearchCV(pipeline, paramters, n_jobs=3, verbose=1, scoring='accuracy')
grid_search.fit(x_train, y_train)
print('最佳效果：%0.3f' % grid_search.best_score_)
print('最优参数集: ')
best_parameters = grid_search.best_estimator_.get_params()
for param_name in sorted(paramters.keys()):
    print('\t%s: %r' % (param_name, best_parameters[param_name]))
predictions = grid_search.predict(x_test)
print(classification_report(y_test, predictions))






