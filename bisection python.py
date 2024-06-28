num1 = eval(input("enter coordinate for x^3:" ))
num2 = eval(input("enter coordinate for x^2:" ))
num3 = eval(input("enter coordinate for x:" ))
num4 = eval(input("enter constant:" ))
num5 = eval(input("enter a:"))
num6 = eval(input("enter b:"))

def f(x):
     result = (((num1) * (x ** 3)) + ((num2) * (x ** 2)) + ((num3) * x) + num4)
     return result



if((f(num5) * f(num6) ) > 0):
    print("invalid input for a and b. f(a) * f(b) must be negative")
else:
     a = num5
     b = num6
     fa = f(a)
     fb = f(b)
     xr = ((a + b)/2)
     fxr = f(xr)
     i = 0
     mulp = fa * fxr
     mullp = round(mulp, 3)
     while(mullp != 0):
          if(mullp < 0):
               b = xr
               fb = fxr
               xr = (a + b)/2
               fxr = round(f(xr), 3)
               mulp = fa * fxr
               mullp = round(mulp, 3)
               print(a,b)
          elif(mullp > 0):
               a = xr 
               fa = fxr
               xr = (a + b)/2
               fxr = round(f(xr), 3)
               mulp = fa * fxr
               mullp = round(mulp, 3)
               print(a,b)


