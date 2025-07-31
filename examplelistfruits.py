print()
fruits = ["apple", "banana"]
print("Original Fruits:", fruits)

fruits.append("orange")
print("After Append:", fruits)

print()

fruits.insert(1, "mango")
print("After Insert:", fruits)

print()

more_fruits = ["kiwi", "grapes"] # List to extend ที่ต้องการเพิ่มเข้าlist
fruits.extend(more_fruits)
print("After Extend:", fruits)

print()

#Original Fruits: ['apple', 'banana']
#After Append: ['apple', 'banana', 'orange']
#After Insert: ['apple', 'mango', 'banana', 'orange']
#After Extend: ['apple', 'mango', 'banana', 'orange', 'kiwi', 'grapes']

#extend() คืออะไร? extend() เป็นเมธอดที่ใช้สำหรับเพิ่มองค์ประกอบหลายๆ ตัวจาก iterable (เช่น ลิสต์, ทูเพิล, สตริง) เข้าไปในลิสต์ที่มีอยู่.
#ทำงานอย่างไร? เมธอด extend() จะวนซ้ำผ่าน iterable ที่เป็นอาร์กิวเมนต์ และเพิ่มแต่ละองค์ประกอบเข้าไปในลิสต์ ณ ตำแหน่งสุดท้าย.