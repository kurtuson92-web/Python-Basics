my_name = "Kurt Angel D. Uson"
my_age = 22
favourite_subject = "arts"

print(f"My Name is, {my_name},Im {my_age}, years old, and i love {favourite_subject}")\

a = 10
b = 10.5
c = "10"
d = True

#int
#float
#string
#boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))


#2.b

a = 10
c = "5"
num = int(c)
d = 3.9
num2 = int(d)

result = a + num

print(result)
print(num2)

# BONUS: convert 3.9 into an int. What happens to the decimal part?
# thge decimal was not included in whole number

#3

name = input("What's your name? ")
age = input("How old are you? ")   # this comes back as a STRING
sage = str(age)

future = int(age) + 5

hobby = input("What's your favorite hobby? ")

print(f"My Name is, {name},Im {age}, years old, and i love {hobby}")
print(f"Im , {future} , after 5 years")

#4

# TODO: Simple grade checker

score = 85
passing_score = 75

# 1. Check if the student passed (comparison operator)
passed = score >= passing_score

# 2. Check if the score is even (modulo)
is_even = score % passing_score

# 3. Check if the student passed AND scored above 80 ('and')
honor_roll = score & passing_score

print(passed, is_even, honor_roll)

#5

age = 17

if age >= 18:
    print("Welcome in!")
elif age == 17:
    print("Sorry, come back next year.")
else:
    print("You're too young.")

#6
correct_username = "admin"
correct_password = "python123"

username = input("Enter your username ")
password = input("Enter your password ")

if username == correct_username and password == correct_password:
    print("Access granted")
else:
    print("Access denied")
