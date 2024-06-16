def _sum(x, y):
    result = int(x) + int(y)
    return result

def mul(x, y):
    result = int(x) * int(y)
    return result

def sub(x, y):
    result = int(x) - int(y)
    return result

def greeting():
    result = "salam man injam"
    return result

def find_max(x, y):
    result = int(x) - int(y)
    return result


commands = {
    "sum": _sum,
    "mul": mul,
    "sub": sub,

    "hello": greeting,

    "max": find_max
}


while True:

    user_inp = input().split(" ")

    if user_inp[0] == "exit":
        print("program ended successfully!")
        break
    else:
        function = commands[user_inp[0]]

    if len(user_inp) == 3:
        print(function(x=user_inp[1], y=user_inp[2]))

    elif len(user_inp) == 1:
        print(function())