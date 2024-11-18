from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def to_float(self):
        return self.numerator / self.denominator
    
    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by a fraction with a numerator of zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

# Example usage
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print("Fraction 1:", fraction1)
print("Fraction 2:", fraction2)

result_add = fraction1.add(fraction2)
print("Addition:", result_add)

result_subtract = fraction1.subtract(fraction2)
print("Subtraction:", result_subtract)

result_multiply = fraction1.multiply(fraction2)
print("Multiplication:", result_multiply)

result_divide = fraction1.divide(fraction2)
print("Division:", result_divide)

print("Fraction 1 as float:", fraction1.to_float())
print("Fraction 2 as float:", fraction2.to_float())