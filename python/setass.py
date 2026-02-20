# Question 10
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers.remove(3)
print(odd_numbers)

# Question 11
vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)

# Question 12
letters = {"a", "b", "c"}
another_set = {"b", "c", "d"}
set3 = letters.symmetric_difference(another_set)
print(set3)

# Question 13
tech_brands = {"Apple", "Google", "Microsoft"}
another_set = {"Amazon", "Facebook"}
tech_brands.update(another_set)
print(tech_brands)

# Question 14
students = {"Alice", "Bob", "Charlie", "David"}
students.remove("Charlie")
students.discard("Eve")
# Question 15
numbers_list = [1, 2, 3, 4, 4, 5, 5] 
print(set(numbers_list))
# Question 16 
text = "hello"
text = set(text)
print(text)

# Question 17 
vehicles = {"car", "bike", "bus", "train"}
print(len(vehicles))

# Question 18 

gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}
print(len(gadgets))