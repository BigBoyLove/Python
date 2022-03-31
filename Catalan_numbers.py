def TakeSumsFromA(a):
    m = []
    s = 0
    for i in a:
        if i == "|":
            m.append(s)
            s = 0
        else:
            s+=i
    m.append(s)
    return m

def MakePermsByM(m, n):
    if len(allPermutations) < n:
        allPermutations.append([])
    permutations = [""]
    for i in m:
        for j in range(len(permutations)):
            permutations[j] += "("
            if i != 0:
                for k in range(1,len(allPermutations[i-1])):
                    permutations.append(permutations[j]+allPermutations[i-1][k]+")")
                permutations[j] += allPermutations[i-1][0]+")"
            elif i == 0:
                permutations[j] += ")"
    for p in permutations:
        allPermutations[n-1].append(p)

def dividePairBrackets(a, finalLenA, pairBracketsAmount, wantingPairOfBrackets):
    if len(a) == finalLenA:
        if pairBracketsAmount == wantingPairOfBrackets:
            m = TakeSumsFromA(a)  # содержит кол-во пар скобок для каждой группы
            MakePermsByM(m, finalLenA + 1)
    else:
        new_a1 = []
        new_a2 = []
        for i in a:
            new_a1.append(i)
            new_a2.append(i)
        new_a1.append(1) #  1 = pair of brackets
        new_a2.append("|")
        dividePairBrackets(new_a1, finalLenA, pairBracketsAmount + 1, wantingPairOfBrackets)
        dividePairBrackets(new_a2, finalLenA, pairBracketsAmount, wantingPairOfBrackets)
def fac(n):
    s = 1
    for i in range(2,n+1):
        s*=i
    return s
n = 5
allPermutations = []
for i in range(1,n+1):
    for kolvoGroop in range(1,i+1):
        peregorogki = kolvoGroop - 1
        elements = i - kolvoGroop
        dividePairBrackets([], peregorogki + elements, 0, elements)
# print(fac(2.txt*n)/(fac(n+1)*fac(n)),len(allPermutations[n-1])) # Сравниваем формулу для n-го числа Каталана с длиной получившегося массива скобочных последовательностей
for per in allPermutations[n-1]:
    print(per)