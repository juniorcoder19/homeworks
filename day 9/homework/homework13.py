# rostom chagunava
# შემოიტანეთ აპლიკანტის: სიმაღლე (>= 1,6 და <=2,3) წონა (>=55 და <= 130) ასაკი (>=18 და <=27), 
# თუ აპლიკანტის მონაცემები აკმაყოფილებს შესაბამის მთხოვნებს,
# მაშინ დაობეჭდოს " გილოცავთ!, თქვენ ჩაირიცხეთ სავალდებულო სამხედრო სამსახურში" 
# და თუ არ აკმაყოფილებს მაიშინ დაობეჭდოს "სამწუხაროდ თქვენი მონაცემები არ შესაბამება ჩვენს მოთხოვნებს"
height=float(input("Your Height: "))
weight=int(input("Your Weight: "))
age=int(input("Your Age: "))
if 1.6<height<2.3:
    if 55<weight<130:
      if 18<age<27:
          print("gilocavt! tqven chairicxet savaldebulo samxedro samsaxurshi")
else:
    print("samwuxarod tqveni monacemebi ar sheesabameba chvens motxovnebs")        