def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(f"{'Celsius':<10} {'Fahrenheit':<10}")

for celsius in range(0,101):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:<10} {fahrenheit:.1f}")
