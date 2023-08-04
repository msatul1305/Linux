temp = 10   # global-scope variable
def func():
    global temp
    temp = 20   # local-scope variable
    print(temp)
print(temp)   # output => 10
func()    # output => 20
print(temp)   # output => 20
