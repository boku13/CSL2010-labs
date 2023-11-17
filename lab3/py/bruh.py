s = "Aditya"
bruh = 0
term = 0
x = 1
calc = 0
p = 10e9 + 7

for i in s:
    ascii = ord(i)
    term = ascii*x
    x = x*263
    term = term%p
    print(term)
    calc +=term
        
m = 263
calc = calc%m
print(calc)

print(hash(s))