sub1 = int(input("Enter first subject marks"))
sub2 = int(input("Enter second subject marks"))
sub3 = int(input("Enter third subject marks"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33 percentage in one of the subject")

elif(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage is less than 40")

else:
    print("You are passed")
    