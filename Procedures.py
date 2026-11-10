class MultipleFunctions():
    
    def Subfields():
        Sub = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for name in Sub:
            print(name)

    def OddEven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print(num,"is Even number")
            message="is Even number"
        else:
            print(num,"is Odd number")
            message="is Odd number"
        return message

    def Eligible():
        Gender=input("Your Gender:")
        age=int(input("Your age:"))
        if Gender == "Female" and age < 18:
            print("NOT ELIGIBLE")
            message = "NOT ELIGIBLE"
        elif Gender =="Male" and age < 21:
            print("NOT ELIGIBLE")
            message = "NOT ELIGIBLE"
        else:
            print("ELIGIBLE")
            message="ELIGIBLE"
        return message

    def percentage():
        Sub1=int(input("Subject1:"))
        Sub2=int(input("Subject2:"))
        Sub3=int(input("Subject3:"))
        Sub4=int(input("Subject4:"))
        Sub5=int(input("Subject5:"))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        Percentage=Total/5
       
        print("Total:", Total)
        print("Percentage:", Percentage)
     
        return Percentage

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        
        Area=(Height*Breadth)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",Area)
        
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
            
        Perimeter=Height1+Height2+Breadth
        print("Perimeter formula:(Height1+Height2+Breadth)")
        print("Perimeter of Triangle:",Perimeter)
        
        message=Area, Perimeter
        
        return message

    