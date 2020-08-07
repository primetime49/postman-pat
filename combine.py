import csv

userDict = {}
userHeader = []
with open('users.csv', 'r' , newline='') as myfile:
    user = csv.reader(myfile, delimiter=',')
    for row in user:
        if row[0] == 'user_id':
            userHeader += [row[1], row[2], row[3], row[4], row[5]]
            continue
        userDict[row[0]] = [row[1], row[2], row[3], row[4], row[5]]

header = []
res = []
with open('test.csv', 'r' , newline='') as myfile:
    train = csv.reader(myfile, delimiter=',')
    for row in train:
        if row[0] == 'country_code':
            header += [row[0], row[1], row[2], row[3], row[4], row[5], 
            row[6], row[7], row[8], row[9], row[10], row[11], 
            row[12], row[13], row[14], row[15], row[16]]
            header += userHeader
            continue
        temp = [row[0], row[1], row[2], row[3], row[4], row[5], 
        row[6], row[7], row[8], row[9], row[10], row[11], 
        row[12], row[13], row[14], row[15], row[16]]
        temp += userDict[row[2]]
        res.append(temp)

with open('mixed.csv', 'w' , newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(header)
with open('mixed.csv', 'a' , newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(res)