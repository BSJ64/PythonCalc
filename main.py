# Original code by Brenden St. Juste


def baseCalc(starter, base):
    codeList = []
    while starter != 0:
        result = starter % base
        codeList.append(result)
        starter = round(starter / base)
    codeList.reverse()
    print(*codeList)


print("Input a whole number.")
starter = int(input())
print("Input a base to convert to.")
base = int(input())
baseCalc(starter, base)
