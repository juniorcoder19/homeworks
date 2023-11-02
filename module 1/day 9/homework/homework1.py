#ანრი ზუბაშვილი
# [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
# იპოვეთ ყველაზე პატარა რიცხვი აქ
# min() ფუნქციის გამოყენების გარეშე

my_list=[ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
for element in my_list:
    if 0<element<3 :
        print(str(element) + " "+"minnum")
    else:
        print(str(element)+" "+"restofnums")