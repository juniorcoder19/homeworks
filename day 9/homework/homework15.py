# Merab Tsitskhvaia
# User-ს შემოატანინეთ თავისი სიმაღლე. მიეცით საშუალება მომხმარებელს აირჩიოს ის, 
# თუ რომელ სიდიდეში სურს გაიგოს თავისი სიმაღლე, სანტიმეტრებში თუ ფუნტებში...
# თუ შემოიტანს 180-ს და აირჩევს ფუტებში გადაყვანას თავისი წონის, დაუპრინტეთ რამდენი ფუტია ის. 
height=int(input("Users Height: "))
choose=input("cms or foots: ")
if choose == "cms":
    print(str(height)+"cms")
else:
    print(str(height/30.48)+" "+"foots")