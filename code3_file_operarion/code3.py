import pandas as pd

data = pd.read_csv("q2sample.csv")

max_salary = max(data['raisedAmt'])
min_salary = min(data['raisedAmt'])

print("Max Salary is {} and Min Salary is {}".format(max_salary, min_salary))