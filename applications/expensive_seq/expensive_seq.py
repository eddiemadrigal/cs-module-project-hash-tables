# Your code here

# from readme doc
# def exps(x, y, z):
#      if x <= 0: 
#          y + z
#      if x >  0: 
#          exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

cache = {}
def expensive_seq(x, y, z):
    key = (x, y, z)
    if x <= 0:
        return y + z
    if x > 0 and key not in cache:
        cache[key] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    return cache[key]

def rot13(strInput):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    strOutput = ''
    for i in strInput.lower():
        if i == " ":
            strOutput += " "
        elif i == ",":
            strOutput += ","
        elif i == ".":
            strOutput += "."
        else:
            strOutput += abc[(abc.find(i) + 13) % 26]
    return strOutput

hint = 'Va Clguba, n qvpg xrl pna or nal vzzhgnoyr glcr ... vapyhqvat n ghcyr.'
print(rot13(hint))

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
