total_sum = 0
product = 1

num = int(input("Enter an integer: "))
total_sum += num
product *= num
min_num = num
max_num = num

for i in range(3):
    num = int(input("Enter an integer: "))
    total_sum += num
    product *= num
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

average = total_sum / 4

print("Sum:",total_sum)
print("Average:",average)
print("Product:",product)
print("Smallest:",min_num)
print("Largest:",max_num)
