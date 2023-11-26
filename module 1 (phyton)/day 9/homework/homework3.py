#rati murghulia
# მომხმარებელს შემოატანინეთ ორი სახელი და გვარი,
# შეადარეთ ერთი მეორეს,დაითვალეთ a-ს რაოდენობა რომელ სახელში არის მეტი და
# დაპრინტეთ მიღებული შედეგი
name1=input("your fullname: ")
name2=input("your fullname: ")

a_counter = 0
for element in name1,name2:
    for char in element:
        if char=="a":
            a_counter += 1
print(a_counter)