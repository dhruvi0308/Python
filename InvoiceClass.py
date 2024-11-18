class Invoice:
    def __init__(self, part_number, part_description, quantity, price_per_item):
        self.part_number = part_number
        self.part_description = part_description
        self.quantity = max(0, quantity)  # Ensure non-negative quantity
        self.price_per_item = max(0.0, price_per_item)  # Ensure non-negative price per item

    def calculate_invoice(self):
        return self.quantity * self.price_per_item

    def __str__(self):
        return (f"Part Number: {self.part_number}\n"
                f"Description: {self.part_description}\n"
                f"Quantity: {self.quantity}\n"
                f"Price per Item: ${self.price_per_item:.2f}\n"
                f"Invoice Amount: ${self.calculate_invoice():.2f}")

# Example usage
invoice1 = Invoice("1234", "Hammer", 10, 15.75)
invoice2 = Invoice("5678", "Nails (100 pack)", 5, 3.99)

# Display the invoices
print("Invoice 1:")
print(invoice1)
print("\nInvoice 2:")
print(invoice2)