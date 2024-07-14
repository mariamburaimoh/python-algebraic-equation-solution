num1 = eval(input("enter coefficient for x^3: " ))
num2 = eval(input("enter coefficient for x^2: " ))
num3 = eval(input("enter coefficient for x: " ))
num4 = eval(input("enter constant: " ))
num5 = eval(input("enter a: "))
num6 = eval(input("enter tolerable error: "))

def f(x):
     result = (((num1) * (x ** 3)) + ((num2) * (x ** 2)) + ((num3) * x) + num4)
     return result

def g(x):
     result = (3 * num1 * (x ** 2)) + (2 * num2 * x) + num3
     return result

def h(x):
     result = (f(x)/g(x))
     return result


if((g(num5) == 0)):
     print("error, pick another number")
else:
     print("NEWTON RAHPSON TABLE")
     print("n       a            f(a)         f'(a)         f(a)/g(a)       Xn")

     a = num5
     fa = f(a)
     ga = g(a)
     ha = h(a)
     xn = a - ha
     fxn = f(xn)
     gxn = g(xn)
     hxn = h(xn)
     i = 1
     error = num6
     print("%d     %f     %f      %f     %f     %f"%(i,a,fa,ga,ha,xn))
     i = i + 1
     
     while (abs(fxn) > error):
               a = xn
               fa = fxn
               ga = gxn
               ha = hxn
               xn = (a - ha)
               fxn = f(xn)
               gxn = g(xn)
               hxn = h(xn)
               print("%d     %f     %f      %f     %f     %f"%(i,a,fa,ga,ha,xn))
               i = i + 1

          
     print("The root is %f"%(xn))     
