class MarriageEligibility():
    def Eligible():
        gender = input("Your Gender: ")
        age = int(input("Your age: "))
        if (gender.upper() == "MALE" and age >=21) or (gender.upper() == "FEMALE" and age >=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")