# -*- coding: utf-8 -*-
"""Materi-9-Decision-Tree-Contoh-Syafrudin Fahrul Anas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aLOJTGADY2Uv-N-OxqJVopN1hrTwtLut
"""

from sklearn import tree

# Database Gerbang Logika AND
# X = Data, y = Target

x = [[0,0], [0,1], [1,0], [1,1]]

y = [0,0,0,1]

# Training and clasify

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# Prediction
print("Logika AND Metode Decision Tree")
print("Logika = Prediksi")
print(clf.predict([[0,0]]))
print(clf.predict([[0,1]]))
print(clf.predict([[1,0]]))
print(clf.predict([[1,1]]))

from google.colab import drive
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Mount Google Drive
drive.mount('/content/drive')

#path ke file di google drive
FileDB = '/content/drive/My Drive/modul9/Sinus.txt' # Sesuaikan path file
Database = pd.read_csv(FileDB, sep=",", header=0)

#Lihat Data
print("--------------------")
print(Database)

# x data, y data
x = Database[["Feature"]]# Replace with your actual column names
y = Database.Target

reg = DecisionTreeRegressor(random_state=1)
reg = reg.fit(x,y)

# Display predicted data
xx = np.arange(1, 21, 1)
n = len(xx)
print("xx(i) Decission Tree")
for i in range(n):
  y_dct = reg.predict([[xx[i]]])
  print('{:.2f}'.format(xx[i]),y_dct)

# plot the predicted data
y_dct2 = reg.predict(x)
plt.figure()
plt.plot(x, y_dct2, color='red')
plt.scatter(x, y, color='blue')
plt.title('Prediksi Data Decision Tree Sinus')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Decision Tree', 'data'], loc=2)
plt.show()