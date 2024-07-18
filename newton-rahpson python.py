#define function for Newton Raphson Table
def NewtonRaphsonTable():
    #print value table
     print("NEWTON RAPHSON TABLE")
     print("n       a            f(a)         f'(a)        -f(a)/f'(a)       Xn")

     #declare initial values for variables
     a = num5
     fa = f(a)
     ga = g(a)
     ha = h(a)
     xn = a + ha
     fxn = f(xn)
     gxn = g(xn)
     hxn = h(xn)
     i = 1
     error = num6
     print("%d     %f     %f      %f     %f     %f"%(i,a,fa,ga,ha,xn))
     i = i + 1
     
     #set condition for changing values of variables
     while (abs(fxn) > error):
               a = xn
               fa = fxn
               ga = gxn
               ha = hxn
               xn = (a + ha)
               fxn = f(xn)
               gxn = g(xn)
               hxn = h(xn)
               print("%d     %f     %f      %f     %f     %f"%(i,a,fa,ga,ha,xn))
               i = i + 1

     #print root     
     print("The root is %f"%(xn))
     return 

#prompt user to enter coefficients for the equation to be solved
num1 = eval(input("enter coefficient for x^3: " ))
num2 = eval(input("enter coefficient for x^2: " ))
num3 = eval(input("enter coefficient for x: " ))
num4 = eval(input("enter constant: " ))

#prompt user to enter in guess for root and tolerable error
num5 = eval(input("enter a: "))
num6 = eval(input("enter tolerable error: "))

#define function of the equation, f
def f(x):
     result = (((num1) * (x ** 3)) + ((num2) * (x ** 2)) + ((num3) * x) + num4)
     return result

#define the differential of the function f, g
def g(x):
     result = (3 * num1 * (x ** 2)) + (2 * num2 * x) + num3
     return result

#define f(x)/g(x), h(x)
def h(x):
     result = (-(f(x)/g(x)))
     return result

#end program if g(a) = 0, continue if g(0) != 0
if((g(num5) == 0)):
     print("error, pick another number")
     num5 = eval(input("enter another number for a: "))
     NewtonRaphsonTable()
else:
     NewtonRaphsonTable()  
