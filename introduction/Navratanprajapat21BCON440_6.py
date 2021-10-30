import pandas as pd
import matplotlib.pyplot as plt
Name=['Lokesh','Mehul','Ishanshu','Vishal','Kapil','Shashank',
      'Tarun','Aayush','Mayur','Harshit']
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
a={'Name':Name,'math_marks':math_marks,'science_marks':science_marks}
Test_Data=pd.DataFrame(a)
print(Test_Data.to_string(index=False))
plt.plot(Name,math_marks,color='yellow',label='Math Marks',marker='s')
plt.plot(Name,science_marks,color='cyan',label='Science Marks',marker='h')
plt.xlabel('Students Name',fontsize=18)
plt.xticks(Name,rotation=30,fontsize=10)
plt.ylabel('Marks Obtained',fontsize=18)
plt.title('Record Of Students',fontsize=22)
plt.legend()
plt.ylim(0,120)
plt.show()
