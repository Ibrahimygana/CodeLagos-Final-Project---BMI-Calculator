#BMI Calculator
#Metric=weight/height**2
#Imperial=weight/height**2*703


#TeamVebra

#Vera Ikejiobi  email: ikejiobichidera@gmail.com 
#Ibrahim Gana   email: ibrahimygana@gmail.com   

unit=int(input("Choose your preferred unit: \n1. metric(kilogram,metres) \n2. Imperial(Pound,Inches) \n"))

if(unit==1):
  met_weight=int(input("Input your weight (kg) "))
  met_height=float(input("input your height (m) "))
  BMI=met_weight/met_height**2
  print("Your BMI is:" ,round(BMI,1))
  
elif(unit==2):
  imp_weight=int(input("input your weight (lbs) "))
  imp_height=float(input("input your height  (in) "))
  BMI=(imp_weight*703)/imp_height**2
  print("Your BMI is:",round(BMI,1))
  
if(BMI<18.5):
    print("You are underweight")
    
elif(BMI>=18.5 and BMI<25):
    print("Your weight is fine")
    
elif(BMI>=25 and BMI==29.9):
    print("You are overweight")
    
elif(BMI>30):
    print("Your are obese")
