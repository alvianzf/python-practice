# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

num = input("Please enter your number:\n ")

n = int(num)
nn = int(f"{num}{num}")
nnn = int(f"{num}{num}{num}")

print(f"The result of {n} + {nn} + {nnn} is {n+nn+nnn}")