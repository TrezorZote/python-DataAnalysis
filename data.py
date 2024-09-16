import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv(r'C:\Users\sonia\Downloads\food.csv')

print(data.head(10))
median_value = data['Data.Vitamins.Vitamin E'].median()
maxx_value=data['Data.Vitamins.Vitamin E'].max()
max_row = data.loc[data['Data.Vitamins.Vitamin E'].idxmax()]
min_row = data.loc[data['Data.Vitamins.Vitamin E'].idxmin()]

#exmaple of a dataset
example = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [30, 25, 35, 28, 22],
     'Weight': [90, 85, 80, 100, 82]
}
df = pd.DataFrame(example)

# Get the highest value in the 'Age' column
max_age = df['Age'].max()

# Print the highest value
print(f"Highest value in the Age column: {max_age}")
# Print the median
print(f"Median of the column: {median_value}")
# Print the row with max
print(f"row with max of the column: {max_row}")
# Print the row with max
print(f"row with min of the column: {min_row}")

summary = data.describe()
print(summary)

#histogram
#using import seaborn as sns
#import matplotlib.pyplot as plt
sns.histplot(df['Age'])
plt.show()

sns.histplot(data['Data.Vitamins.Vitamin E'])
plt.show()

#filter based on  condition 
filtered_df = df[df['Age'] > 20]
print(filtered_df)

#merging dataframes on  common column
#filtered_df = df[df['column_name'] > threshold]
#print(filtered_df)


#correlation between colums
correlation = df['Age'].corr(df['Weight'])

# Print the correlation
print(f"Correlation between Age and Weight: {correlation}")

vitaminKE = data['Data.Vitamins.Vitamin E'].corr(data['Data.Vitamins.Vitamin K'])
print(f"Correlation between vitamin E and Vitamin K: {vitaminKE}")

#function to output based on number passed
def check_value(number):
    if isinstance(number, int):
        if number == 1 :
           print(data['Data.Vitamins.Vitamin K'].max())
        elif number == 2:
            print(data['Data.Vitamins.Vitamin K'].min())
        else:
           print(data['Data.Vitamins.Vitamin K'].median())
    else:
        print("Please provide an integer.")

try:
    user_input = int(input("Enter an integer: "))
    check_value(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")