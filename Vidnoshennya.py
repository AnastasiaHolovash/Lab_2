import random

A = ['Andrew', 'Антон', 'Денис', 'Аня', 'Катя', 'Юля']
B = ['Богдан', 'Віталій', 'Юля', 'Даша', 'Оля']
S1 = {("Петро", "Ольга"), ("Іван", "Тетяна"), ("Олег", "Оксана")}

mens = ['Andrew', 'Антон', 'Денис', 'Богдан', 'Віталій', 'Віктор', 'Костя', 'Сергій', 'Вова']
women = ['Настя', 'Маша', 'Аня', 'Катя', 'Юля', 'Даша', 'Оля', 'Люда']



def a_husbend_b():
    menset = set()
    for i in A:
        if i in mens:
            menset.add(i)
    womenset = set()
    for i in B:
        if i in women:
            womenset.add(i)
    S = []
    for i in range(min(len(menset), len(womenset))):
        m = random.choice(list(menset))
        w = random.choice(list(womenset))
        S.append([m, w])
        menset.remove(m)
        womenset.remove(w)
    return S


def a_father_in_law_b():
    mensetA = set()
    for i in A:
        if i in mens:
            mensetA.add(i)
    mensetB = set()
    for i in B:
        if i in mens:
            mensetB.add(i)
    R = []
    for i in range(min(len(mensetA), len(mensetB))):
        m1 = random.choice(list(mensetA))
        m2 = random.choice(list(mensetB))
        if m1 != m2:
            R.append([m1, m2])
        mensetA.remove(m1)
        mensetB.remove(m2)
    return R


def a_universal_father_in_law_b():
    mensetA = set()
    for i in A:
        if i in mens:
            mensetA.add(i)
    mensetB = set()
    for i in B:
        if i in mens:
            mensetB.add(i)
    # Ur=list(map(lambda x: x * , mile_distances))
    Ur = []
    for m1 in mensetA:
        for m2 in mensetB:
            if m1 != m2:
                Ur.append([m1, m2])
    return Ur


# print(a_husbend_b())
# print(a_father_in_law_b())

Ur = list(a_universal_father_in_law_b())
print("Ur > ", a_universal_father_in_law_b())
S = list(a_husbend_b())
print(S)
R = list(a_father_in_law_b())
print(R)


def unionn(s, r):
    U = []
    for i in s:
        U.append(i)
    for i in r:
        if i not in U:
            U.append(i)
    return U


print(unionn(R, S))


# print(S)
# print(R)

def intersectionn(s, r):
    I = []
    for i in s:
        # print(i if i in s else "0")
        if i in r:
            I.append(i)
    return I


print(intersectionn(R, S))


def differ(r, s):
    D = []
    for i in r:
        if i not in s:
            D.append(i)
    return D


print(differ(R, S))


def transposed(s):
    T = []
    for i in range(len(s)):
        T.append([s[i][1], s[i][0]])
    return T


print(transposed(S))
print(differ(Ur, R))
