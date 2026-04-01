# 1: input age(years), weight, Cr, and gender
age = int(input("Enter your age in years:"))
weight =float(input("Enter your weight in kg:"))
Cr = float(input("Enter your creatine concentration in µmol/L:"))
gender = input("Enter your gener(male/female):")
# 2: check their range, ask the user to reenter if the value is invalid
inputvalue = True
if age >= 100:
    print("Age must be no more than 100")
    inputvalue = False
if weight<20 or weight>80:
    print("Weight must be in between 20kg to 80kg")
    inputvalue = False
if Cr<0 or Cr>100:
    print("Creatine concentration must be in between 0-100 µmol/L")
    inputvalue = False
if gender!="male" and gender!="female":
    print("Gender must be either male or female")
    inputvalue = False
# 3: Use if statements to calculate male and female differently, only if all the inputs are valid
if inputvalue:
    if gender == "male":
        Crcl = (140-age)*weight/(72*Cr)
        print("Your creatine clearance rate is:",Crcl)
    if gender == "female":
        Crcl = (140-age)*weight*0.85/(72*Cr)
        print("Your creatine clearance rate is:",Crcl)

