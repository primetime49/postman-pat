import csv
import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv("combine.csv")
test = pd.read_csv("mixed.csv")

columns = list(train.columns)
# features = columns[:-2]
features = columns[:]
## Contain non numeric values
features.remove('grass_date')
features.remove('email')
## Contain nil values
features.remove('attr_1')
features.remove('age')
## Contain unnecessary information
features.remove('open_flag')
features.remove('row_id')

x_train = train[features]
x_train = x_train.convert_objects(convert_numeric=True).fillna(0)
y_train = train['open_flag']

x_test = test[features]
x_test = x_test.convert_objects(convert_numeric=True).fillna(0)

# lr = LogisticRegression()
lr = LogisticRegression(max_iter=1000)
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