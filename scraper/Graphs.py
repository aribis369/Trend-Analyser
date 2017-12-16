import matplotlib.pyplot as plt
import pandas as pd


df= pd.read_csv("/home/anubhav10/Desktop/Trend-Analyzer-master/scraper/testfile2.csv")
movie_name= list(df["name"].unique())
color = ["red", "purple", "green", "blue", "pink", "brown", "orange", "violet", "magenta", "yellow"]
x= list(df["time"].unique())
for j in range(len(movie_name)):
	y= list(df.loc[df['name'] == movie_name[j]]['share in %'])
	for i in range(len(y)):
		y[i]= float(y[i].strip('%'))
	

	plt.plot(x,y, color= color[j], label= movie_name[j])


plt.ylabel("Share in %")
plt.xlabel("Date")

plt.title("Popularity Vs. Time")
plt.grid(True)


plt.legend()

plt.show()

#Individual movie

for j in range(len(movie_name)):
	y= list(df.loc[df['name'] == movie_name[j]]['share in %'])
	for i in range(len(y)):
		y[i]= float(y[i].strip('%'))
	

	plt.plot(x,y)
	plt.title(movie_name[j]+" Popularity Vs. Time")
	plt.show()


plt.ylabel("Share in %")
plt.xlabel("Date")

plt.grid(True)





