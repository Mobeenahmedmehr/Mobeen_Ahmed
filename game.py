name=str(input("What is your name ?"))
x=int(input("Enter your first favorite number:"))
y=int(input("Enter your second favorite number:"))
z=int(input("Enter your third favorite number:"))
print(f"Hello,{name}! lets explore your favorite numbers:")
if x%2==0:
    print(f"the number {x} is even")
else:
    print(f"the number {x} is odd")
if y%2==0:
    print(f"the number {y} is even")
else:
    print(f"the number {y} is odd")
if z%2==0:
    print(f"the number {z} is even")
else:
    print(f"the number {z} is odd")
square_x=x**2
print(f"The number {x} and its square{x,square_x}")
square_y=y**2
print(f"The number {y} and its square{y,square_y}")
square_z=z**2
print(f"The number {z} and its square{z,square_z}")
sum=x+y+z
print(f"Amazing! The sum of your favorite numbers is:{sum}")
is_prime=True
if sum<=1:
    is_prime=False
for i in range(2,sum):
    if sum % i == 0:
            is_prime=False
if is_prime:
    print(f"Wow, {sum} is a prime number!")
else:
    print(f"wonderful, {sum} is not a prime number")