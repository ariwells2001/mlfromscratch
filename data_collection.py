import requests

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(data.text)
with open('iris.csv','w') as f:
    f.write(data.text)