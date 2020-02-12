import pandas as pd

grades_dict={'Wally':[87,96,70],'Eva':[100,87,90],'Sam':[94,77,90],'Katie':[100,81,82],'Bob':[83,65,85]}
grades=pd.DataFrame(grades_dict)
#print(grades)

grades.index=['Test1','Test2','Test3']
#print()
print(grades)
#print()
#print(grades['Eva'])
#print()
#print(grades.Sam)

#print()
#print(grades.loc['Test1'])
#print()
#print(grades.iloc[1])
#print()
#print(grades.loc['Test1':'Test3']) #the upper limit is included
#print()
#print(grades[0:2]) #the upper limit is not included
#print()
#print(grades.loc[['Test1','Test3']]) #only test1 and test3
#print()
#print(grades.loc['Test1':'Test2',['Eva','Katie']])
#print()
#print(grades.iloc[[0,2],:3])
#so basically, both loc and iloc ask for rows first and than column (but iloc asks for indexes)
#print(grades[(90>grades) & (grades>=80)]) #showing grades between 80~89
#print()
#print(grades[(90<=grades) | (grades<80)]) #showing grades <80 or >=90
#print()
#print(grades.at['Test2','Eva']) #look for certain test grade for a student
#print()
#print(grades.iat[0,2])
#grades.at['Test2','Eva']=100
#print()
#print(grades.at['Test2','Eva'])
#print(grades) #as seen, it's a change permenantly
#pd.set_option('precision',2)
#print()
#print(grades.describe())
#print()
#print(grades.mean())
#grades.T
#print()
#print(grades.T)
#print()
#print(grades.sort_index(ascending=False)) #descending by rows
#print()
#print(grades.sort_index(axis=1)) #ascending by columns
#print()
#print(grades.sort_values(by='Test1',axis=1,ascending=False)) #sort by Test1 score
#print()
#print(grades.T.sort_values(by='Test1',ascending=False))
print()
print(grades.loc['Test1'].sort_values(ascending=False)) #a combine to make use of the tool we just learned