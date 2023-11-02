#DAVALEBA 1
# დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.
# რენდომად გამოიძახებთ ერთ ჯგუფელს, 
# თუ კითხვაზე უპასუხებს მოემატება 10 ქულა და გადავალთ შემდეგზე
#(ოღონდ ეს ვეღარ უპასუხებს იმ დღეს)( ანუ remove დაგჭირდებათ),

# answer = input("did the student answer correctly: ")
#     if answer == "yes":
#         ............ moematos 10 qula 
#         if answer == "no"
#                     daakldes 10 qula
# ცალკე უნდა იყოს ქულების სიაც
import random

students= ["luka","dachi","dato","demetre","gabrieli","ekaterine","salome","nini","giorgi","nika"]
lucky = random.choice(students)
question = input("axla gvipasuxebs" + " " + lucky)
answer = input("did the student answer correctly: ")
if answer == "yes":
    print(lucky + " " + "+10 qula")
if answer == "no":
    print(lucky + " " + "-10 qula")
students.remove(lucky)           