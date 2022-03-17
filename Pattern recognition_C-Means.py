import random
from requests_html import HTMLSession
import re
import math
import matplotlib.pyplot as plt

class Small_model:
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species="None",Id=999):
        self.Id=Id
        self.SepalLengthCm=SepalLengthCm
        self.SepalWidthCm=SepalWidthCm
        self.PetalLengthCm=PetalLengthCm
        self.PetalWidthCm=PetalWidthCm
        self.Species=Species

def Calculate_the_distance(model1,model2):
    dist1=model1.SepalLengthCm-model2.SepalLengthCm
    dist2=model1.SepalWidthCm-model2.SepalWidthCm
    dist3=model1.PetalLengthCm-model2.PetalLengthCm
    dist4=model1.PetalWidthCm-model2.PetalWidthCm
    return math.sqrt(dist1**2+dist2**2+dist3**2+dist4**2)

def Judge_the_same(model1,model2):
    isprime=1
    if(model1.PetalLengthCm!=model2.PetalLengthCm or model1.SepalLengthCm!=model2.SepalLengthCm or model1.SepalWidthCm!=model2.SepalWidthCm or model1.PetalWidthCm!=model2.PetalWidthCm):
        isprime=0
    return isprime

def Calculate_the_center(Class):
    SepalLengthCm=0
    SepalWidthCm=0
    PetalLengthCm=0
    PetalWidthCm=0
    for i in range(0,len(Class)):
        SepalLengthCm=Class[i].SepalLengthCm+SepalLengthCm
        SepalWidthCm=Class[i].SepalWidthCm+SepalWidthCm
        PetalLengthCm=Class[i].PetalLengthCm+PetalLengthCm
        PetalWidthCm=Class[i].PetalWidthCm+PetalWidthCm
    SepalLengthCm=SepalLengthCm/len(Class)
    SepalWidthCm =SepalWidthCm/len(Class)
    PetalLengthCm=PetalLengthCm/len(Class)
    PetalWidthCm=PetalWidthCm/len(Class)
    AModel=Small_model(SepalLengthCm=SepalLengthCm,SepalWidthCm=SepalWidthCm,PetalLengthCm=PetalLengthCm,PetalWidthCm=PetalWidthCm)
    return AModel

def Calculate_The_Accurancy_Number(Class):
    Species1=0
    Species2=0
    Species3=0
    for i in range(0,len(Class)):
        if(Class[i].Species=="Iris-setosa"):
            Species1=Species1+1
        elif(Class[i].Species=="Iris-versicolor"):
            Species2=Species2+1
        else:
            Species3=Species3+1
    return(int(max(Species1,Species2,Species3)))

def Plot_the_figure(Class1,Class2,Class3):
    X1 = []
    X2 = []
    X3 = []
    Y1 = []
    Y2 = []
    Y3 = []
    for i in range(0, len(Class1)):
        X1.append(float(Class1[i].SepalLengthCm * Class1[i].SepalWidthCm))
        Y1.append(float(Class1[i].PetalLengthCm * Class1[i].PetalWidthCm))
    for i in range(0, len(Class2)):
        X2.append(float(Class2[i].SepalLengthCm * Class2[i].SepalWidthCm))
        Y2.append(float(Class2[i].PetalLengthCm * Class2[i].PetalWidthCm))
    for i in range(0, len(Class3)):
        X3.append(float(Class3[i].SepalLengthCm * Class3[i].SepalWidthCm))
        Y3.append(float(Class3[i].PetalLengthCm * Class3[i].PetalWidthCm))
    plt.plot(X1, Y1, 'ro')
    plt.plot(X2, Y2, 'bo')
    plt.plot(X3, Y3, 'go')
    plt.xlabel('SepalArea')
    plt.ylabel('PetalArea')

url="http://chwang.xmu.edu.cn/prml/docs/iris.txt"
session = HTMLSession()
r = session.get(url)
data_get=re.split(",| ",r.html.text)
data=[]
Id=[]
SepalLengthCm=[]
SepalWidthCm=[]
PetalLengthCm=[]
PetalWidthCm=[]
Species=[]

for i in range(0, len(data_get)):
    if(i%6==0):
        Id.append(data_get[i])
    elif i%6==1:
        SepalLengthCm.append(data_get[i])
    elif i%6==2:
        SepalWidthCm.append(data_get[i])
    elif i%6==3:
        PetalLengthCm.append(data_get[i])
    elif i%6==4:
        PetalWidthCm.append(data_get[i])
    elif i%6==5:
        Species.append(data_get[i])

data=[Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species]

## Here we assume that there are three different classes

Class1=[]
Class2=[]
Class3=[]
## input = 3

n=3
Model_Store=[]
for i in range(1,len(data[0])):
    OneModel=Small_model(Id=int(Id[i]),SepalLengthCm=float(SepalLengthCm[i]),SepalWidthCm=float(SepalWidthCm[i]),PetalLengthCm=float(PetalLengthCm[i]),PetalWidthCm=float(PetalWidthCm[i]),Species=Species[i])
    Model_Store.append(OneModel)
# Class1.append(Model_Store[0])
# Class2.append(Model_Store[1])
# Class3.append(Model_Store[2])
res=random.sample(range(0, len(Model_Store)), n)    ##random seed
print(res)
res=[134,67,102]
#print(res)
##Initialization considerations select the first three as the center of the three classes(no random selection)

The_First_Class_Before_Center=Small_model(SepalLengthCm=Model_Store[res[0]].SepalLengthCm,SepalWidthCm=Model_Store[res[0]].SepalWidthCm,PetalLengthCm=Model_Store[res[0]].PetalLengthCm,PetalWidthCm=Model_Store[res[0]].PetalWidthCm)
The_Second_Class_Before_Center=Small_model(SepalLengthCm=Model_Store[res[1]].SepalLengthCm,SepalWidthCm=Model_Store[res[1]].SepalWidthCm,PetalLengthCm=Model_Store[res[1]].PetalLengthCm,PetalWidthCm=Model_Store[res[1]].PetalWidthCm)
The_Third_Class_Before_Center=Small_model(SepalLengthCm=Model_Store[res[2]].SepalLengthCm,SepalWidthCm=Model_Store[res[2]].SepalWidthCm,PetalLengthCm=Model_Store[res[2]].PetalLengthCm,PetalWidthCm=Model_Store[res[2]].PetalWidthCm)
find=0
while(find==0):
    Class1=[]
    Class2=[]
    Class3=[]

    for i in range(0,len(Model_Store)):
        dist1=Calculate_the_distance(Model_Store[i],The_First_Class_Before_Center)
        dist2=Calculate_the_distance(Model_Store[i],The_Second_Class_Before_Center)
        dist3=Calculate_the_distance(Model_Store[i],The_Third_Class_Before_Center)
        if(dist1<dist2 and dist1 < dist3):
            Class1.append(Model_Store[i])
        elif(dist2 < dist1 and dist2 < dist3):
            Class2.append(Model_Store[i])
        elif(dist3 < dist1 and dist3 < dist2):
            Class3.append(Model_Store[i])

    The_First_Class_New_Center = Calculate_the_center(Class1)
    The_Second_Class_New_Center = Calculate_the_center(Class2)
    The_Third_Class_New_Center = Calculate_the_center(Class3)

    if(Judge_the_same(The_First_Class_New_Center,The_First_Class_Before_Center) and Judge_the_same(The_Second_Class_New_Center,The_Second_Class_Before_Center)and Judge_the_same(The_Third_Class_New_Center,The_Third_Class_Before_Center)):
        find=1
    else:
        The_First_Class_Before_Center=The_First_Class_New_Center
        The_Second_Class_Before_Center=The_Second_Class_New_Center
        The_Third_Class_Before_Center=The_Third_Class_New_Center
print("The first kind:")
for i in range(0,len(Class1)):
    print(str(Class1[i].Id)+str(Class1[i].Species))
print()
print("The second kind:")
for i in range(0,len(Class2)):
    print(str(Class2[i].Id)+str(Class2[i].Species))
print()
print("The third kind:")
for i in range(0,len(Class3)):
    print(str(Class3[i].Id)+str(Class3[i].Species))

total=Calculate_The_Accurancy_Number(Class1)+Calculate_The_Accurancy_Number(Class2)+Calculate_The_Accurancy_Number(Class3)
print("The Accurancy is:"+str(total/len(Model_Store)*100)+"%")

##Plot the figure with SepalArea and PetalArea -- for SepalArea=SepalLengthCm*SepalWidth and PetalArea=PetalLength*PetalWidth
##Put two figures in one window to compare
fig = plt.figure(1)
plt.subplot(2,1,1)
Plot_the_figure(Class1,Class2,Class3)
plt.title('The first figure is through C-Means get ')
Class4=[]
Class5=[]
Class6=[]
for i in range(0,len(Model_Store)):
    if(Model_Store[i].Species=="Iris-setosa"):
        Class4.append(Model_Store[i])
    elif Model_Store[i].Species=="Iris-versicolor":
        Class5.append(Model_Store[i])
    else:
        Class6.append(Model_Store[i])
plt.subplot(2,1,2)
Plot_the_figure(Class4,Class5,Class6)
plt.title("the second figure is the standard data")
plt.show()

