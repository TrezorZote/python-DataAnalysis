import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv(r'C:\Users\sonia\Downloads\food.csv')


#function to output based on number passed
def check_value(number):
    min_value=data['Data.Vitamins.Vitamin K'].min()
    max_value=data['Data.Vitamins.Vitamin K'].max()
    median_value=data['Data.Vitamins.Vitamin K'].median()
    if isinstance(number, int):
        if number == 1 :
            print(f" max vitamin K concentrations of the column: {max_value}")
        elif number == 2:
            print(f" min vitamin K concentrations of the column: {min_value}")
        else:
            print(f"the median of vitamin K concentrations of the column: {median_value}")
    else:
        print("Please provide an integer.")

try:
    user_input = int(input("Enter an integer: "))
    check_value(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")