import random

def rearrange():
    user_input = input().strip().split(' ')
    random.shuffle(user_input)

    output = " ".join(user_input)
    print(output)

rearrange()
