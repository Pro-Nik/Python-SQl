l = []
while True:
    c =int(input('''
              1 Push Elements
              2 Pop First Elements
              3 Front Element
              4 Last Element
              5 Display
              6 Exit

            '''))
    if c==1:
        n = input("enter the value")
        l.append(n)
        print(l)

    elif c ==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            del l[0]
            print(l[0])
            print(l)
    
    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("First Queue element", l[0])

    elif c==4:
        if len(l)==0:
            print("Empty queue")
        else:
            print("Last Queue Element:",l[-1])
    
    elif c==5:
        print("Display Element:",l)

    elif c==6:
        break
    else:
        print("Invalid input")
