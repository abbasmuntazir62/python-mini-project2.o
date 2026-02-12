import random
import string

pass_len = 8

charValues = string.ascii_letters + string.digits + string.punctuation

# Generate password using list comprehension and join
password = "".join(random.choice(charValues) for i in range(pass_len))

print("Your random password is:", password)
