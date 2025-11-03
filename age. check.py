classify_person=int(input("please enter your age_"))
if 0<=classify_person<=12:
    print("so you're a child")
elif 13<=classify_person<=17:
    print("so your'e a teenager even though you're still a minor")
elif 18<=classify_person<=64:
    print("you my friend, you're an adult")
elif 65<=classify_person<=100:
    print("you are a senior")
else:
    print("uhhh...are you human?")

if classify_person>100:
    print("please be human and go back and enter your real age")