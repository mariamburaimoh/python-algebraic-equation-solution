#define function for Bisection Method Table
def BisectionMethodTable():
     print("IMPLEMENTATION OF BISECTION METHOD")
     print("n       a         b         xr         f(a)      f(b)      f(xr)    f(a).f(xr)")

     #declare initial values for variables
     a = num5
     b = num6
     fa = f(a)
     fb = f(b)
     xr = ((a + b)/2)
     fxr = f(xr)
     i = 1
     mulp = fa * fxr
     mullp = round(mulp, 3)

     #print initial values of variables
     print("%d     %0.3f     %0.3f      %0.3f     %0.3f     %0.3f     %0.3f     %0.3f"%(i,a,b,xr,fa,fb,fxr,(mullp + 0.0)))
     i = i + 1
     #set conditions for changing values of a and b
     while(mullp != 0):
           if(mullp < 0):
               #declare new values for changing variables
               b = xr
               fb = fxr
               xr = (a + b)/2
               fxr = round(f(xr), 3)
               mulp = fa * fxr
               mullp = round(mulp, 3)
               print("%d     %0.3f     %0.3f      %0.3f     %0.3f     %0.3f     %0.3f     %0.3f"%(i,a,b,xr,fa,fb,fxr,(mullp + 0.0)))
               i = i + 1
           elif(mullp > 0):
               #declare new values for changing variables
               a = xr 
               fa = fxr
               xr = (a + b)/2
               fxr = round(f(xr), 3)
               mulp = fa * fxr
               mullp = round(mulp, 3)
               print("%d     %0.3f     %0.3f      %0.3f     %0.3f     %0.3f     %0.3f     %0.3f"%(i,a,b,xr,fa,fb,fxr,(mullp + 0.0)))
               i = i + 1
     print("the root is %f"%(xr))
     return

#prompt the user to enter in coefficients for the equation to be solved
num1 = eval(input("enter coefficient for x^3: "))
num2 = eval(input("enter coefficient for x^2: "))
num3 = eval(input("enter coefficient for x: "))
num4 = eval(input("enter constant: "))

#prompt the user to enter in their guesses for the roots of the equation and tolerable error
num5 = eval(input("enter a: "))
num6 = eval(input("enter b: "))


#define function of the equation, f
def f(x):
     result = (((num1) * (x ** 3)) + ((num2) * (x ** 2)) + ((num3) * x) + num4)
     return result

#end program if f(a) * f(b) > 0, continue if f(a) * f(b) < 0
if((f(num5) * f(num6) ) > 0):
    print("invalid input for a and b. f(a) * f(b) must be negative. enter new values for a and b")
    num5 = eval(input("enter a: "))
    num6 = eval(input("enter b: "))
    BisectionMethodTable()
else:
     BisectionMethodTable()
