# შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი,
# 8 სიმბოლოიანი,სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#,
# 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347
# მაგ: !n8391k*



import random 
my_arr = []
chars = list("qwertyuiopasdfghjklzxcvbnm")
symbols = list("!@#$%^&*")
numbers = list("1234567890")
for i in range(9):
    random_num = random.choice(numbers)
    my_arr.append(random_num)
    numbers.remove(random_num)
    
for i in range(25):
    random_char = random.choice(chars)
    my_arr.append(random_char)
    chars.remove(random_char)
    
for i in range(6):
    random_symbol = random.choice(symbols)
    my_arr.append(random_symbol)
    symbols.remove(random_symbol)


print("the program chose these characters:" , my_arr)
final_password = ""
for i in range(len(my_arr)):
    current_char = random.choice(my_arr)
    final_password += current_char
    my_arr.remove(current_char) #რათა my_arr სიაში არსებული ყველა სიმბოლო ერთხელ გამოვიყენოთ
    
print("the final password is:", final_password)

