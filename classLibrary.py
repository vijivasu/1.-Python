class multipleFunctions():
    def agecate():
        age=int(input("Enter your age:"))
        if(age<=15):
            print("Children")
            cate = "Children"
        elif(age<=35):
             print("Adult")
             cate="Adult"
        elif(age<59):
             print("Citizen")
             cate="Citizen"
        else:
            print("Senior Citizen") 
            cate="Senior Citizen"
        return cate

    def number():
        num = int(input("Enter any number:"))
        if(num>0):
            print("No is positive:", num)
            message = "Positive"
        if(num<0):
            print("No is negative:", num)
            message ="Negative"
        return message

    def BMI():
        BMI = int(input("Enter the BMI index:"))
        if(BMI<18.5):
            print("Underweight")
            message = "Underweight"
        elif(BMI<24.9):
            print("Normal")
            message= "Normal"
        elif(BMI<30):
            print("Over Weight")
            message="Overweight"
        else:
            print("Very OverWeight")
            message="Very Overweight"
        return message
            
    def oddeven():
        list=[20,10,16,19,25,1,276,188]
        for temp in list:
            if temp%2!=0:
                print( temp,"is Odd Number")
                message="odd Number"
            else:
                print(temp, "is Even Number")
                message= "Even Number"
        return message            
        

    def divisibleby5():
        num = int(input("Enter any number:"))
        if(num%5==0):
            print("Number is divisible by 5:", num)
            message="Number is divisible by 5"
        else:
            print("Number is not divisible by 5")
            message="Number is NOT divisible by 5"
        return message

    def tuple():
        tup=(1, 'Welcome', 2, 'Hope')
        print(tup)

    def nestedTuple():
        tup1=(0,1,2,3)
        tup2=('Python', 'Hope')
        tup3=(tup1,tup2)
        print(tup3)

    def charPrint():
        print("Artificial Intelligence")
        text="Artificial Intelligence"
        print("Length of the word:", len(text)) 
        for char in text:
            print(char)