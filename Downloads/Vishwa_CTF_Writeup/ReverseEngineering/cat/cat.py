
def Kitty(inp):
    return str(int(inp)*v1)

def enc(inp, cats):
    print(inp, cats)
    cat1 = 0
    cat2 = 0
    catcat = 0
    cAt = ""
    while cat1 < len(inp) and cat2 < len(cats):
        if catcat%v1 == v3//v2:
            cAt += cats[cat2]
            cat2 += 1
        else:
            cAt += inp[cat1]
            cat1 += 1
        catcat += 1
    return cAt

def catt(inp):
    return inp[::v1-v2]

def caT(inp):
    return Kitty(inp[:v1]) + catt(inp)

def rAT(inp):
    return inp

def Rat(inp):
    return "Cat" + str(len(inp)) + inp[:v1]

def Cat(inp):
    if len(inp) == 9:
        if str.isdigit(inp[:v1]) and\
            str.isdigit(inp[len(inp)-v1+1:]):
                catcat = enc(caT(inp), Rat(rAT(catt(inp))))
                if catcat == "C20a73t0294t0ac2194":
                    flag = "runner_" + inp
                    print("So here you are!! VishwaCTF{",flag,"}")
                    print(inp)
                    exit(0)
                else:
                    print("You are using right format, but answer is not correct\n>>", catcat)
        else:
            print("You are not using correct format :(\
            \n(A small help from out side, Format should be like 123xyz789)")
    else:
        print("Wrong answer, check length :(")

print("What'S tHe aNsWer")

for a in range(1000):
    for b in range(1000):
        inp = "%.3icat%.3i" % (a, b)
        v1 = len(inp)//3
        v2 = v1+1
        v3 = v1-1
        print(v1, v2, v3)
        Cat(inp)

# 691cat420
# VishwaCTF{runner_691cat420}
