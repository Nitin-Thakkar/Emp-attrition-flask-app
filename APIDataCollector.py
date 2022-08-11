import numpy

from database import Database
import pandas as pd
import pymysql
import numpy as np

# data = Database("kaggle datasets download -d pavansubhasht/ibm-hr-analytics-attrition-dataset")
#
# pd_data=pd.DataFrame(data.dataset[0])
# pd_data.to_csv('C:/Users/User/Documents/Big Data Analyst/SEM 1/Data Programming/Final Project/Dataset/Attrition.csv',sep=",",index=False)


load_data = pd.read_csv(
    "C:/Users/User/Documents/Big Data Analyst/SEM 1/Data Programming/Final Project/Dataset/Attrition.csv")
# print(load_data.columns)


x = numpy.int64(50)


# print("============",type(x))

def db_connect():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pythondb',
        cursorclass=pymysql.cursors.DictCursor,
        port=3306
    )


print(len(load_data))

for k in range(0,len(load_data)):
    print(k)
    ls1 = []
    print(k)
    for i in load_data.iloc[k]:
        # print(type(i))

        if type(i) == type(x):
            # print("true")
            ls1.append(np.str(i))
        else:
            ls1.append(i)
    # print(ls1)
    print(ls1)

    for i in [6,10,13,14,16,24,25,27,30]:
        if i==6:
            if ls1[i]=='1':
                ls1[i]='Below College'
            if ls1[i]=='2':
                ls1[i]='College'
            if ls1[i]=='3':
                ls1[i]='Bachelor'
            if ls1[i]=='4':
                ls1[i]='Master'
            if ls1[i]=='5':
                ls1[i]='Doctor'
        if i==10 or i==13 or i==16 or i==25:
            if ls1[i]=='1':
                ls1[i]='Low'
            if ls1[i]=='2':
                ls1[i]='Medium'
            if ls1[i]=='3':
                ls1[i]='High'
            if ls1[i]=='4':
                ls1[i]='Very High'
        if i==14 or i==27:
            if ls1[i]=='0':
                ls1[i]='Level 0'
            if ls1[i]=='1':
                ls1[i]='Level 1'
            if ls1[i]=='2':
                ls1[i]='Level 2'
            if ls1[i]=='3':
                ls1[i]='Level 3'
            if ls1[i]=='4':
                ls1[i]='Level 4'
            if ls1[i]=='5':
                ls1[i]='Level 5'
        if i==24:
            if ls1[i]=='1':
                ls1[i]='Low'
            if ls1[i]=='2':
                ls1[i]='Good'
            if ls1[i]=='3':
                ls1[i]='Excellent'

            if ls1[i]=='4':
                ls1[i]='Outstanding'
        if i == 30:
            if ls1[i] == '1':
                ls1[i] = 'Bad'
            if ls1[i] == '2':
                ls1[i] = 'Good'
            if ls1[i] == '3':
                ls1[i] = 'Better'
            if ls1[i] == '4':
                ls1[i] = 'Best'


    connection = db_connect()
    cursor1 = connection.cursor()
    cursor1.execute(
        "INSERT INTO finalproject(Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,"
        "Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,"
        "Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,"
        "TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,"
        "YearsWithCurrManager) VALUES ('" + ls1[0] + "','" + ls1[1] + "','" + ls1[2] + "','" + ls1[3] + "','" + ls1[
            4] + "', '" + ls1[5] + "','" + ls1[6] + "','" + ls1[7] + "','" + ls1[8] + "','" + ls1[9] + "','" + ls1[
            10] + "','" + ls1[11] + "','" + ls1[12] + "','" + ls1[13] + "','" + ls1[14] + "','" + ls1[15] + "','" + ls1[
            16] + "','" + ls1[17] + "','" + ls1[18] + "','" + ls1[19] + "','" + ls1[20] + "','" + ls1[21] + "','" + ls1[
            22] + "','" + ls1[23] + "','" + ls1[24] + "','" + ls1[25] + "','" + ls1[26] + "','" + ls1[27] + "','" + ls1[
            28] + "','" + ls1[29] + "','" + ls1[30] + "','" + ls1[31] + "','" + ls1[32] + "','" + ls1[33] + "','" + ls1[
            34] + "')")
    connection.commit()
    print("Insert Successfully")
    cursor1.close()
    connection.close()

# print(ls1)


'''

CREATE TABLE `pythondb`.`finalproject`( `id` INT(255) NOT NULL AUTO_INCREMENT, `Age` INT(100), `Attrition` VARCHAR(100), `BusinessTravel` VARCHAR(100), `DailyRate` INT(100), `Department` VARCHAR(100), `DistanceFromHome` INT(100), `Education` INT(100), `EducationField` VARCHAR(100), `EmployeeCount` INT(100), `EmployeeNumber` INT(100), `EnvironmentSatisfaction` INT(100), `Gender` VARCHAR(100), `HourlyRate` INT(100), `JobInvolvement` INT(100), `JobLevel` INT(100), `JobRole` VARCHAR(100), `JobSatisfaction` INT(100), `MaritalStatus` VARCHAR(100), `MonthlyIncome` INT(100), `MonthlyRate` INT(100), `NumCompaniesWorked` INT(100), `Over18` VARCHAR(100), `OverTime` VARCHAR(100), `PercentSalaryHike` INT(100), `PerformanceRating` INT(100), `RelationshipSatisfaction` INT(100), `StandardHours` INT(100), `StockOptionLevel` INT(100), `TotalWorkingYears` INT(100), `TrainingTimesLastYear` INT(100), `WorkLifeBalance` INT(100), `YearsAtCompany` INT(100), `YearsInCurrentRole` INT(100), `YearsSinceLastPromotion` INT(100), `YearsWithCurrManager` INT(100), PRIMARY KEY (`id`) ); 

'''
