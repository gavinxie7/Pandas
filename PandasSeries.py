import pandas as pd

grades=pd.Series([87,100,94])

print(grades)

'''print(grades[0])
print(grades.count())'''

grades=pd.Series([87,100,94],index=['Wally','Eva','Sam'])
grades=pd.Series({'Wally':87,'Eva':100,'Sam':94})
print(grades['Eva'])
print(grades.Wally)
print(grades.dtype)
print(grades.values)

hardware=pd.Series(['Hammer','Saw','Wrench'])
print(hardware)

print(hardware.str.contains('a'))

print(hardware.str.upper())