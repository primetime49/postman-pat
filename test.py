import csv
import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

columns = list(train.columns)
features = columns[:-2]
features.remove('grass_date')

x_train = train[features]
x_train = x_train.convert_objects(convert_numeric=True).fillna(0)
y_train = train['open_flag']

x_test = test[features]
x_test = x_test.convert_objects(convert_numeric=True).fillna(0)

lr = LogisticRegression()
lr.fit(x_train, y_train)

hasil = lr.predict(x_test)
res = []
idx = 0
for h in hasil:
    res.append([idx,h])
    idx += 1

with open('res.csv', 'w' , newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['row_id','open_flag'])
with open('res.csv', 'a' , newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(res)