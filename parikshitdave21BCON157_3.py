import string
import random
characters=string.ascii_uppercase+string.punctuation + string.digits
password="".join(random.choice(characters) for x in range(random.randint(8,16)))
print("The latest password is",password)
