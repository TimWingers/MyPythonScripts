#Тitanic machine learning
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
#loading dataframes
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
train_data.shape
#looking what's behind the table
train_data.head(10)
#looking how many empty cells
train_data.isnull().sum()
#creating diagram how many people survived
sb.countplot('Survived',data=train_data)
plt.show()
#analyzing how many survived by sex
train_data.groupby(['Sex', 'Survived',])['Survived'].count()
#analyzing more detail
train_data[['Sex', 'Survived']].groupby(['Sex']).mean().plot.bar()
sb.countplot('Sex', hue='Survived', data=train_data)
plt.show()
#analyzing how Survivability is correlate with Ticket Class
sb.countplot('Pclass', hue='Survived', data=train_data)
plt.title('Pclass: Survived vs Dead')
plt.show()
#analyzing more in detail that hypotesis
pd.crosstab([train_data.Sex, train_data.Survived], train_data.Pclass, margins=True).style.background_gradient(cmap='summer_r')
#creating chart on that data
sb.factorplot('Pclass', 'Survived', hue='Sex', data=train_data)
plt.show()
#let's analyze at what age survived people
print ('Oldest person Survived was of:',train_data['Age'].max())
print ('Youngest person Survived was of:',train_data['Age'].min())
print ('Average person Survived was of:',train_data['Age'].mean())
#let's create beautiful chart of what that we're discovered
f,ax=plt.subplots(1,2,figsize=(18,8))
sb.violinplot('Pclass','Age', hue='Survived',data=train_data,split=True,ax=ax[0])
ax[0].set_title('PClass and Age vs Survived')
ax[0].set_yticks(range(0,110,10))
sb.violinplot('Sex', 'Age', hue='Survived', data=train_data,split=True,ax=ax[1])
ax[1].set_title('Sex and Age vs Survived')
ax[1].set_yticks(range(0,110,10))
plt.show
#extracting Name initials 
train_data['Initial']=0
for i in train_data:
  train_data['Initial']=train_data.Name.str.extract('([A-Za-z]+)\.')
pd.crosstab(train_data.Initial,train_data.Sex).T.style.background_gradient(cmap='summer_r') 
#creating a diagram of distribution of Survived people
f,ax=plt.subplots(1,2,figsize=(20,20))
train_data[train_data['Survived']==0].Age.plot.hist(ax=ax[0],bins=20,edgecolor='black',color='red')
ax[0].set_title('Survived = 0')
x1=list(range(0,85, 5))
ax[0].set_xticks(x1)
train_data[train_data['Survived']==1].Age.plot.hist(ax=ax[1],bins=20, edgecolor='black', color='green')
x2=list(range(0,85, 5))
ax[1].set_xticks(x2)
ax[1].set_title('Survived = 1')
plt.show()
#creating another chart to find how many women and children Survived at different Age
sb.factorplot('Pclass','Survived',col='Initial',data=train_data)
plt.show()
#calcutating how many Survived or Died people we're alone
pd.crosstab([train_data.SibSp],train_data.Survived).style.background_gradient('summer_r')
f,ax=plt.subplots(1,2,figsize=(20,8))
sb.barplot('SibSp','Survived', data=train_data, ax=ax[0])
ax[0].set_title('SibSp vs Survived in BarPlot')
sb.factorplot('SibSp','Survived', data=train_data, ax=ax[1])
ax[1].set_title('SibSp vs Survived in FactorPlot')
plt.close(2)
plt.show()
#Final table
pd.crosstab(train_data.SibSp,train_data.Pclass).style.background_gradient('summer_r')
