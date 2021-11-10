#I got inspired by reading a blog from CSDN and discuss with Ding Chen and Zhan Yang

#5.1
def strings(n):
    if n ==1:
        return ['1']
    result = []
    for s in strings(n-1):
        result.append(s + str(n))
        result.append(s + "+" + str(n))
        result.append(s + '-' + str(n))
    return result

def find_expression(n,sum):
    solutions = strings(n)
    result = []
    for s in solutions:
        if eval(s) == sum:
            result.append(s + '=' + str(sum))
    return result


total_solutions = find_expression(9,100) #9为1~9，50为random integer number
print("Total solutions are as follows:")
for solution in total_solutions:
    print(f"\n{solution}")

print(f"\nHere we have {len(total_solutions)} kinds of different solutions.")
