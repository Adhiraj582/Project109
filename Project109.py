import plotly.express as px
import plotly.figure_factory as ff
import statistics
import csv
import pandas as pd


df = pd.read_csv('StudentsPerformance.csv')
data = df['reading score'].to_list()

# calculating the mean, median, mode and the standard deviation
std = statistics.stdev(data)

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("Standard Deviation of this data is {}".format(std))

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))

# finding 1 std and end values , 2 std and end values, 3 std and end values
first_std_d_start, first_std_d_end = mean-std, mean+std
second_std_d_start, second_std_d_end = mean-(2*std), mean+(2*std)
third_std_d_start, third_std_d_end = mean-(3*std), mean+(3*std)

list_of_data_within_one_std_deviation = [
    result for result in data if result > first_std_d_start and result < first_std_d_end]
list_of_data_within_second_std_deviation = [
    result for result in data if result > second_std_d_start and result < second_std_d_end]
list_of_data_within_third_std_deviation = [
    result for result in data if result > third_std_d_start and result < third_std_d_end]

print("{}% of data lies within 1 Standard Deviation".format(
    len(list_of_data_within_one_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 Standard Deviation".format(
    len(list_of_data_within_second_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 Standard Deviation".format(
    len(list_of_data_within_third_std_deviation)*100.0/len(data)))


fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.show()
