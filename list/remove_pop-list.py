numbers = [1, 2, 3, 4, 5,6,3,3,3,3,]
print("Original Numbers:", numbers)

numbers.remove(3)  # Remove the first occurrence of 3
print("After Remove3:", numbers)

removed_number = numbers.pop(2)  # Remove and return the last item
print("After Pop (2):", numbers)
print("Removed Number:", removed_number)
print()

last_item = numbers.pop()  # Remove and return the last item
print("After Pop Last Item:", numbers)
print("Last Item Removed:", last_item)
