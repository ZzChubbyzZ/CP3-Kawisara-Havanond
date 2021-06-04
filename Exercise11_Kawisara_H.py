number = int(input())
for x in range(number):
    text = ""
    for y in range(x+1):
        text = (" "*(number-x-1)+ ("*"*(2*x+1)))

    print(text)