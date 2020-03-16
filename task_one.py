import pandas as pd
import csv


file_one = pd.read_csv('file_1.csv')
file_two = pd.read_csv('file_2.csv')

# File header.
result = [['date', 'zephyr_line_item_id', 'impressions_all', 'impressions_per_day', 'cpm', 'cpm_in_place']]

# I combined file 1 and file 2 by date and line_item_id. To remove float inaccuracies I used round.
if file_one.date.all() == file_two.date.all():
    if file_one.zephyr_line_item_id.all() == file_two.network_line_item_id.all():
        for i in range(len(file_one.date)):
            result.append([file_one.date[i], file_one.zephyr_line_item_id[i], file_two.impressions[i], file_one.impressions[i],
                           round(file_two.cpm[i], 4), round(file_two.cpm[i]*file_one.impressions[i]/1000, 6)])

# Write data in result.csv
with open('result.csv', "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(result)

# Check result
file_result = pd.read_csv('result.csv')
print(file_result.head())
