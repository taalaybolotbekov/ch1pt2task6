def number():
    n = int(input('vvedite:'))
    tens = n%100-n%10
    new = tens // 10
    return(str(new))
print(number())