def tempr():
    print("function working")
f=float()
c=float()
C=(f-32)*5/9
F=(c*9/5)+32

user=(input("hello! do you want me to convert celcius to farenheit or farenheit to celcius"))
if user== "celcius to farenheit":
    tempr()
    s=float(input("please enter your temperature in celcius"))
    print(" it is equal to",F,"degrees faenheit")
elif user=="farenheit to celcius":
    t=float(input("please enter your temperature in farenheit"))
    print(" it is equal to",C,"degree celcius")
else:
    print("error, incorrect input. try again")    

    
    
        
    
                                                                  