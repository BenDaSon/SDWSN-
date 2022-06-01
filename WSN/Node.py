# This basic ass python script will do the following:
#
# 1. Read CSV files with the title 'pi-<number>-temp-data.csv'
# 2. Grab all power values from the CSV file and put them into an array
# 3. Sum all values within the array
# 4. Calculate power average by dividing the sum by the number of values in the array
#
#

# ---------------------IMPORTANT--------------------------------------
# ENSURE THAT THE PI's IDs RANGE FROM [0,3] (4 UNIQUE IDs TOTAL)

import csv
import numpy as np


# Open a specified file and return the column values in an array, including the header
def get_column(file_name, col_index):
    col_values = []

    try:
        with open(str(file_name), newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if len(row) >= col_index:
                    col_values.append(row[col_index])
                else:
                    print("Index mismatch")
                    pass
    except FileNotFoundError:
        print("\nFileNotFoundError: File,  " + file_name+ " doesn't exist, array will return empty.\n")
    finally:
        return col_values


# Removes the first value in the array (assumed to be the header) and sums all values in the array
def sum_array(value_array):
    sum = 0

    for i in range(1, len(value_array)):
        sum = sum + int(value_array[i])

    return sum


# Essentially is the get_column() function.
# Uses a pi_id parameter to obtain the power values of the CSV specified
def get_node_power(node_id):
    power_array = get_column('pi-' + str(node_id) + '-temp-data.csv', 5)
    return power_array

def min_value(array):
    min_node_power_value = array[0]

    global min_node

    for i in range(0,len(array)):
        if min_node_power_value > array[i]:
            min_node_power_value = array[i]
            min_node = i + 1

    return min_node_power_value
# --------------------------------------------------- DEMO

# Read CSV file and obtain power_array values
node1 = get_node_power(1)
node2 = get_node_power(2)
node3 = get_node_power(3)

print(node1)
print(node2)
print(node3)

# Sum all values in the array (first value in array is removed)
node1_power_sum = sum_array(node1)
node2_power_sum = sum_array(node2)
node3_power_sum = sum_array(node3)

print(node1_power_sum)
print(node2_power_sum)
print(node3_power_sum)

# Place node#_power_sum values into array
node_power_array = (node1_power_sum, node2_power_sum, node3_power_sum)
print(node_power_array)
print("\n\n")

# Find min value and output node
minValue = min_value(node_power_array)
print("Node " + str(min_node) + " consumes the least amount of power")



