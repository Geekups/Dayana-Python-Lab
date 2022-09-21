# Importing packages 
import matplotlib.pyplot as plt 
# Define x and y values 
x = [7, 14, 21, 28, 35, 42, 49] 
y = [8, 13, 21, 30, 31, 44, 50] 
# Plot a simple line chart without any feature 
plt.plot(x, y)
plt.show()

###

# Importing packages 
import numpy as np
# Define x value 
x = np.random.randint(low=1, high=10, size=25) 
plt.plot(x, linewidth=3) 
plt.show()

###

# Define x and y values 
x = [7, 14, 21, 28, 35, 42, 49] 
y = [8, 13, 21, 30, 31, 44, 50] 
# Plot points on the line chart 
plt.plot(x, y, 'o--', linewidth=2) 
plt.show()

###

# Define x and y values 
x = np.array([7, 11, 24, 28, 35, 34, 41])
y = np.array([8, 20, 13, 30, 31, 48, 50])
# Drawn a simple scatter plot for the data given 
plt.scatter(x, y, marker='*', color='k')

# Generating the parameters of the best fit line 
m, c = np.polyfit(x, y, 1) 
# Plotting the straight line by using the generated parameters 
plt.plot(x, m*x+c) 
plt.show()

###

import pandas as pd 
# Let's create a Dataframe using lists 
Name = ['Sara', 'Mahsa', 'Zahra', 'Maryam', 'Ayda'] 
Score = ['19.02', '19.74', '18.34', '17.26', '19.87']
# Now, create a pandas dataframe using above lists 
df_ = pd.DataFrame( 
 {'Name' : Name, 'Score' : Score}) 
# Plotting the data from the dataframe created using matplotlib 
plt.figure(figsize=(9, 5))
plt.plot(df_['Name'], df_['Score'], '-b', linewidth=2) 
plt.xticks(rotation=60) 
plt.xlabel('Name') 
plt.ylabel('Score') 
plt.show()

###

#importing the required libraries 
import matplotlib.pyplot as plt 
import seaborn as sns 
#Creating the dataset 
df = sns.load_dataset("iris") 
df=df.groupby('sepal_length')['sepal_width'].sum().to_frame().reset_index() 
#Creating the line chart 
plt.plot(df['sepal_length'], df['sepal_width']) 
#Adding the aesthetics 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title') 
#Show the plot 
plt.show()

###

import numpy as np
from mpl_toolkits import mplot3d 
# Setting 3 axes for the graph 
plt.axes(projection='3d') 
# Define the z, y, x data 
z = np.linspace(0, 1, 100) 
x = 4.5 * z 
y = 0.8 * x + 2
# Plotting the line 
plt.plot(x, y, z, 'r', linewidth=2) 
plt.title('Plot a line in 3D') 
plt.show()

###

#importing the required libraries 
import seaborn as sns 
# Define the x and y data 
x = [1, 2, 3, 4, 5] 
y = [1, 5, 4, 7, 4] 
sns.lineplot(x, y)
plt.show()

###

# Define the x and y data 
x = ['day 1', 'day 2', 'day 3']
y = [1, 5, 4] 
sns.lineplot(x, y)
plt.show()

###

import numpy as np
import matplotlib.pyplot as plt 
# Dataset generation 
objects = ('Python', 'C++', 'Julia', 'Go', 'Rust', 'c') 
y_pos = np.arange(len(objects)) 
performance = [10,8,6,4,2,1] 
# Bar plot 
plt.barh(y_pos, performance, align='center', alpha=0.5) 
plt.yticks(y_pos, objects) 
plt.xlabel('Usage') 
plt.title('Programming language usage') 
plt.show()

###

import matplotlib.pyplot as plt 
import seaborn as sns 
x = ['A', 'B', 'C'] 
y = [1, 5, 3] 
sns.barplot(y, x)
plt.show()

###

import numpy as np
import matplotlib.pyplot as plt 
# Dataset generation 
data_dict = {'CSE':33, 'ECE':28, 'EEE':30} 
courses = list(data_dict.keys()) 
values = list(data_dict.values()) 
fig = plt.figure(figsize = (10, 5))
# Bar plot 
plt.bar(courses, values, color ='green', 
 width = 0.5) 
plt.xlabel("Courses offered") 
plt.ylabel("No. of students enrolled") 
plt.title("Students enrolled in different courses") 
plt.show()

###

import pandas as pd
plotdata = pd.DataFrame({ 
 "2018":[57,67,77,83],
 "2019":[68,73,80,79],
 "2020":[73,78,80,85]},
 index=["Django", "Gafur", "Tommy", "Ronnie"]) 
plotdata.plot(kind="bar",figsize=(15, 8))
plt.title("FIFA ratings") 
plt.xlabel("Footballer") 
plt.ylabel("Ratings")
plt.show()

###

#Creating the dataset 
df = sns.load_dataset('titanic') 
df_pivot = pd.pivot_table(df, 
values="fare",index="who",columns="class", aggfunc=np.mean) 
#Creating a grouped bar chart 
ax = df_pivot.plot(kind="bar",alpha=0.5) 
#Adding the aesthetics 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title') 
# Show the plot 
plt.show()

###

#Reading the dataset 
titanic_dataset = sns.load_dataset('titanic') 
#Creating column chart 
sns.barplot(x = 'who',y = 'fare',data = titanic_dataset,palette = "Blues") 
#Adding the aesthetics 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title') 
# Show the plot 
plt.show()

###

#Reading the dataset 
titanic_dataset = sns.load_dataset('titanic') 
#Creating the bar plot grouped across classes 
sns.barplot(x = 'who',y = 'fare',hue = 'class',data = titanic_datase
t, palette = "Blues") 
#Adding the aesthetics 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title') 
# Show the plot 
plt.show()

###

#Creating the dataset 
cars = ['AUDI', 'BMW', 'NISSAN', 
 'TESLA', 'HYUNDAI', 'HONDA'] 
data = [20, 15, 15, 14, 16, 20] 
#Creating the pie chart 
plt.pie(data, labels = cars) 
#Adding the aesthetics 
plt.title('Chart title') 
#Show the plot 
plt.show()

###

#Creating the dataset 
cars = ['AUDI', 'BMW', 'NISSAN', 
 'TESLA', 'HYUNDAI', 'HONDA'] 
data = [20, 15, 15, 14, 16, 20] 
myexplode = [0.2, 0, 0, 0,0,0.6] 
#Creating the pie chart 
plt.pie(data, labels = cars,explode = myexplode) 
#Adding the aesthetics 
plt.title('Chart title') 
#Show the plot 
plt.show()

###

