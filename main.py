import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1. Create a NumPy array and calculate the mean
numbers = np.arange(1, 11)
mean_value = np.mean(numbers)
print("NumPy Array:", numbers)
print("Mean of numbers 1 to 10:", mean_value)

# 2. Create a small pandas DataFrame and show summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

# 3. Fetch data from a public API
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()  # Check if the request was successful
    bitcoin_data = response.json()
    price_usd = bitcoin_data['bpi']['USD']['rate']
    print(f"\n🪙 Current Bitcoin Price in USD: ${price_usd}")
except requests.exceptions.RequestException as e:
    print("\nError fetching data from the API:", e)
except KeyError:
    print("\nError: Couldn't find the required data in the API response.")

# 4. Plot a simple line graph using matplotlib
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker='o', linestyle='-', color='teal')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.savefig("line_plot.png")  # Saves the plot as an image
plt.show()  # Displays the plot
