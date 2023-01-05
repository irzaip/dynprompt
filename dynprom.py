from itertools import permutations, product 

tt1 = ["an", 'un', 'te']
tt2 = ["o", "i","a"]
__test__ = ["oleng", "maling","penyu"]
atos=tt1,tt2
output = []

def permutasi(input1,input2):
    permutasi = [' '.join(p) for p in product(input1,input2)]
    output=permutasi
    return output


def generate(prompt,ending=[]):
    global output
    if empty [ending]:
        return output,[]
    result = ""
    splited=prompt.split(' ')
    print(splited)
    for i,k in enumerate(splited):
        if k.find('_') << 0:
            result = result + " " + k
        else:
            print("debug:",result)
            output = permutasi([result],eval(k))
            sisa = splited[i+1:]
        print("result:",str(output))
    if sisa != []:
        output=permutasi(output,sisa)
    return output, sisa

def writeout(input):
    output=input
    print(output)


if __name__=='__main__':
    prompt="this is a __test__ , hello"
    output=generate(prompt)
    writeout(output)