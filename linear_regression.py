import pandas

ds=pandas.read_csv('salaryDataSet.csv')

x=ds['YearsExperience'].values.reshape(30,1)
y=ds['Salary']

from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(x,y)

print('\x1b[1;32;40m' + "Press exit to terminate....." + '\x1b[0m')

while True:
    user_data=input('\x1b[1;36;40m' + "Enter your years of experience " + '\x1b[0m')
    if(user_data=="exit"):
        break
    exp=float(user_data)
    if(exp==0):
        print('\x1b[1;31;40m' + "Better earn some experience first!!!" + '\x1b[0m')
    else:
        predicted_value=model.predict([[exp]])
        print('\x1b[1;36;40m' + "Predicted Salary of person with {} yrs of experience is".format(exp) + '\x1b[1;31;40m' + " {}".format(predicted_value[0]) + " INR" + '\x1b[0m')

print('\x1b[1;32;40m' + "Program Quited!!!" + '\x1b[0m')
