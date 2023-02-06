class MultipleFunctions():
    def Subfields():
        fields = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for field in fields:
            print(field)
        
    def OddEven():
        num = int(input("Enter a number: "))
        if (num%2 ==0):
            print(num," is Even number")
        else:
            print(num," is Odd number")
            
    def Eligible():
        gender = input("Your Gender: ")
        age = int(input("Your age: "))
        if (gender.upper() == "MALE" and age >=21) or (gender.upper() == "FEMALE" and age >=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def Marks():
        sub1 = int(input("Subject 1 = "))
        sub2 = int(input("Subject 2 = "))
        sub3 = int(input("Subject 3 = "))
        sub4 = int(input("Subject 4 = "))
        sub5 = int(input("Subject 5 = "))
        total = sub1+sub2+sub3+sub4+sub5
        percentage = total/5
        print("Total : ",total)
        print("Percentage : ",percentage)
        
    def triangle():
        Height = int(input("Height : "))
        Breadth = int(input("Breadth : "))
        print("Area Formula : (Height*Breadth)/2")
        AreaofTraingle = (Height*Breadth)/2
        print("Area of Traingle: ",AreaofTraingle)
        Height1 = int(input("Height1 : "))
        Height2 = int(input("Height2 : "))
        Breadth = int(input("Breadth : "))
        print("Perimeter Formula : Height1+Height2+Breadth")
        perimeterofTraingle = Height1+Height2+Breadth
        print("Perimeter of Traingle: ",perimeterofTraingle)
        