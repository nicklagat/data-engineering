nums = [1, 2, 3, 4, 5, 6, 7]

for num in nums:
    if num == 3:
        print('We have found it!')
        break
    print(num)

# loop within a loop

for num in nums:
    for letter in 'ABC':
        print(num, letter)
# loop through a number of times
for i in range(5):
    print(i)

# while loops
x = 0
while x < 10:
    print(x)
    x +=1


orders = [
    {"product": "Apple", "quantity": 5, "price_per_item": 0.5},
    {"product": "Banana", "quantity": 3, "price_per_item": 0.3},
    {"product": "Orange", "quantity": 4, "price_per_item": 0.7},
]

total_cost = 0
for order in orders:
    total_cost += order["quantity"] * order["price_per_item"]
    print(f"The total cost is: {total_cost}")

