import string
from random import *
ch = string.ascii_letters + string.punctuation  + string.digits
pass =  "".join(choice(ch) for y in range(randint(9, 15)))
print pass
