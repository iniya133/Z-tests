import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Mean of the population is ", mean)
print("Standard Deviation of the population is ", std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range (0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
std_deviation = statistics.stdev(mean_list)

first_std_deviation_start, first_std_deviation_end =  mean- std_deviation,  mean+ std_deviation
second_std_deviation_start, second_std_deviation_end =  mean-( std_deviation * 2),  mean+( std_deviation * 2)
third_std_deviation_start, third_std_deviation_end =  mean-( std_deviation * 3),  mean+( std_deviation * 3)

df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
meanofsample1 = statistics.mean(data)
print("Mean of Sample 1 is ", meanofsample1)

fig = ff.create_distplot([mean_list], ["Students with learning Material"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [ meanofsample1, meanofsample1], y = [0, 0.17], mode = "lines", name =  "Mean of Sample 1"))
fig.add_trace(go.Scatter(x = [ first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name =  "First Standard Deviation"))
fig.show()

zscore = (meanofsample1 - mean) / std_deviation
print(" Z Score is ", zscore)

