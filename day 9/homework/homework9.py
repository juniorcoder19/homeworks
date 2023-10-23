# ninosolomonia 
# შექმენით მეოთხე ჯგუფის წევრების სია .დაწერეთ კოდი ისე,
# რომ გაიგოთ ყველა სახელსა და გვარში ერთად რამდენი  ,,ი" და ,,ა"   იქნება.
g4_members=["ako mitaishvili","aleksandre tordia","anri zubashvili","beqa giorgobiani",
"chxitunidze luka"]
a_counter=0
i_counter=0
for element in g4_members:
    for char in element:
        a_counter+=1
        i_counter+=1
        print(a_counter+i_counter)