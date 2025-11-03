hour=int(input("what time is it(put it in a 24 hour format)_"))
if  1<=hour<=11:
    print("so, its morning")
elif 12<=hour<=16:
    print("oh, its afternoon")
elif 17<=hour<=20:
    print("ok, its evening")
elif 21<=hour<=24:
    print("its night, go sleep")
else:
    print("go and put the real time in the format put there")