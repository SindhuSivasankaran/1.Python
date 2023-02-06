class SSLCMarkCalc():
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