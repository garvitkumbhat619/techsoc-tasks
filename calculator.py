def add():
    n1=float(input('enter 1st number:'))
    n2=float(input('enter 2nd number:'))
    n3=n1+n2
    print(n3)
    menu()

def sub():
    n1=float(input('enter 1st number:'))
    n2=float(input('enter 2nd number:'))
    n3=n1-n2
    print(n3)
    menu()

def mul():
    n1=float(input('enter 1st number:'))
    n2=float(input('enter 2nd number:'))
    n3=n1*n2
    print(n3)
    menu()

def dev():
    n1=float(input('enter numertor:'))
    n2=float(input('enter denominator:'))
    n3=n1/n2
    print(n3)
    menu()

def exp():
    n1=float(input('enter 1st number:'))
    n2=float(input('enter 2nd number:'))
    n3=n1**n2
    print(n3)
    menu()

def tri():
    print('1.sin()')
    print('2.cos()')
    print('3.tan()')

    o=int(input('choose an option:'))

    if o==1:
        i=float(input('enter angle in radians:'))
        w=i-(i**3)/6 + (i**5)/120
        print('sin('+str(i)+'):'+str(w))
    if o==2:
        i=float(input('enter angle in radians:'))
        w=1-(i**2)/2 + (i**4)/24
        print('cos('+str(i)+'):'+str(w))
    if o==3:
        i=float(input('enter angle in radians:'))
        w=i+(i**3)/3 + (2*(i**5))/15
        print('tan('+str(i)+'):'+str(w))
    menu()

def menu():

    print(' '*30+'MENU'+' '*30)
    print(' ')
    print('1.addition')
    print('2.subtraction')
    print('3.multiplication')
    print('4.division')
    print('5.exponentiation')
    print('6.trigonometric function')

    p=int(input('choose an option:'))
    if p==1:
        add()
    if p==2:
        sub()
    if p==3:
        mul()
    if p==4:
        dev()
    if p==5:
        exp()
    if p==6:
        tri()

menu()

    
    



    
        
        
    




    

    
    
    
    
    
           
    
