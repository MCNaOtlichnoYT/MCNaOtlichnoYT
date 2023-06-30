import os
import time
os.system('color 0a')

def distance(s1, s2):
    c = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            c += 1
    return c


while True:
    print('Welcome to IGS Software (TM) TermHack')
    print('==========')
    x = int(input('Enter number of possible passwords: '))
    print('Enter possible passwords:')
    p = []
    for i in range(x):
        p.append(input().upper())
    os.system('cls')
    checked = {}
    for i in range(4):
        print('Welcome to IGS Software (TM) TermHack')
        print('==========')
        print('Attempts remaining:' + (' █' * (4 - i)))
        print('Possible passwords: ')
        for pas in p:
            print(pas)
        if len(p) == 0:
            print('Error')
            time.sleep(2)
            break
        print('Try: ', p[-1])
        d = int(input('Likeness (-1 if correct): '))
        if d == -1:
            print('Succeeded!')
            time.sleep(2)
            break
        checked[p[-1]] = d
        p.pop()
        p2 = []
        for word in p:
            r = True
            for fail in checked:
                if distance(word, fail) != checked[fail]:
                    r = False
            if r:
                p2.append(word)
        p = p2
        time.sleep(1)
        os.system('cls')
    os.system('cls')
    


x = int(input('Number of passwords: '))
p = []
checked = {}
for i in range(x):
    p.append(input('Password '+str(i+1)+': '))
for i in range(4):
    print('Possible:', *p)
    print('Try: ', p[-1])
    d = int(input('Likeness: '))
    checked[p[-1]] = d
    p.pop()
    p2 = []
    for word in p:
        r = True
        for fail in checked:
            #print(word, fail, distance(word, fail), checked[fail])
            if distance(word, fail) != checked[fail]:
                r = False
        if r:
            p2.append(word)
    p = p2

'''
11
REPUTATION
PRODUCTION
RECRUITING
CONTENDING
ENCOURAGED
ADMIRATION
DESCENDING
PROCESSING
CAMOUFLAGE
SCAVENGING
TELEVISION
3
1 5
'''
