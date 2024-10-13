l = []
while True:
    c =int(input('''
              1 Push Elements
              2 Pop Elements
              3 Peek Element
              4 Display Element
              5 Exit

            '''))
    if c==1:
        n = input("enter the value")
        l.append(n)
        print(l)

    elif c ==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            p = l.pop()
            print(p)
            print(l)
    
    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("last stack element", l[-1])
    elif c==4:
        print("Display stack",l)

    elif c==5:
        break
    else:
        print("Invalid input")
