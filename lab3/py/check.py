def compute_hash(string):
    term = 0
    x = 1
    calc = 0
    p = 10e9 + 7
    count = 0 

    for i in string:
        ascii = ord(i)
        term = ascii*x
        x = x*263
        term = term%p
        calc +=term
        print(count, ":", calc)
        count+=1
            
    m = 263
    calc = calc%m
    return int(calc)

print(compute_hash("Rodriguez"))
print(compute_hash("Akshay"))
