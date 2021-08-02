s = 0
def foo(s) :
    for i in range (len(s)/2) :
        i = 0
        if s[i] != s[len(s)-i-1] :
            print("Bukan foo")
        break
    else :
        print("foo")
foo(s)