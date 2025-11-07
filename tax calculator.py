def tax():
    print("system is working...")
income = float(input("hello, please enter your income in birr and i'll calculate your net income and tax:_ "))
tax()

if income<=2000:
    tax_rate=0
elif 2001<=income<=4000:
    tax_rate=0.15
elif 4001<=income<=7000:
    tax_rate=0.2
elif 7001<=income<=10000:
    tax_rate=0.25
elif 10001<=income<=14000:
    tax_rate=0.3
elif income>=14001:
    tax_rate=0.35
else:
    print("ERR...please try again")
tax=income*tax_rate
net_income=income-tax
print("your tax is",tax,"and your net income is",net_income)


    
    
    