# 1st input: enter height in meters e.g: 1.65
import math
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = int(weight / height**2)
print(BMI)