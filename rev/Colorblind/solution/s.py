def to_note(scramble):

    cube = scramble.split()

    other = cube[9:-9]

    top = other[:12]
    middle = other[12:24]
    bottom = other[24::]

    colors = {"Y":"F", "B":"R", "G":"L", "W":"B", "R":"U", "O" : "D"}
    # bdr = WOG
    B = top[:3] + middle[:3] + bottom[:3]
    L = top[3:6] + middle[3:6] + bottom[3:6]
    F = top[6:9] + middle[6:9] + bottom[6:9]
    R = top[9::] + middle[9::] + bottom[9::]
    U = cube[0:9]
    D = cube[-9::]


    faces = [B,L,F,R,U,D]
    for i in faces:
        for j in range(9):
            i[j] = colors[i[j]]


    mapp = {"UF": U[7]+F[1], "UR": U[5]+R[1], "UB" : U[1]+B[1], "UL" : U[3] + L[1], "DF" : D[1] + F[7], "DR" : D[5] + R[7], 
            "DL" : D[3]+L[7], "DB" : D[7] + B[7], "FR" : F[5]+R[3], "FL" : F[3] + L[5],"BR" : B[3]+R[5], "BL" : B[5]+L[3], "UFR":U[8]+F[2]+R[0], "URB":U[2]+R[2]+B[0], "UBL": U[0]+B[2]+L[0],
            "ULF" : U[6] + L[2] +F[0],"DRF":D[2]+R[6]+F[8], "DFL" : D[0]+F[6]+L[8], "DLB" : D[6]+L[6]+B[8],"DBR" : D[8]+B[6]+R[8]}     

    xxx =  list(mapp.keys())

    for x in xxx:
        # print(x)
        if len(x) == 2:
            mapp[x[::-1]] = mapp[x][::-1]
        elif len(x)==3:
            tmp = x
            tmp = tmp[1:]+tmp[:1]
            mapp[tmp] = mapp[x][1:] + mapp[x][:1]

            ttt = tmp
            tmp = tmp[1:]+tmp[:1]
            mapp[tmp] = mapp[ttt][1:] + mapp[ttt][:1]
    sample = ""
    for i,val in enumerate(corect_order):
        sample += mapp[val]
        sample += " "
    return sample, mapp

def inverse(sample):

    new = {}
    for i, val in enumerate(sample.split()):
        new[val] = corect_order[i]
    rev = {v: k for k, v in new.items()}

    xxx = list(rev.keys())
    for x in xxx:
        if len(x) == 2:
            rev[x[::-1]] = rev[x][::-1]
        elif len(x)==3:
            tmp = x
            tmp = tmp[1:]+tmp[:1]
            rev[tmp] = rev[x][1:] + rev[x][:1]

            ttt = tmp
            tmp = tmp[1:]+tmp[:1]
            rev[tmp] = rev[ttt][1:] + rev[ttt][:1]

    return rev
def sh1t(random):
    n = random.split()
    num_note = [0]*54 
    if(1): #12
        e = []
        e.append((n[1],n[10],(1,10)))
        e.append((n[3],n[13],(3,13)))
        e.append((n[5],n[19],(5,19)))
        e.append((n[7],n[16],(7,16)))

        e.append((n[23],n[24],(23,24)))
        e.append((n[26],n[27],(26,27)))
        e.append((n[29],n[30],(29,30)))
        e.append((n[32],n[21],(32,21)))

        e.append((n[34],n[52],(34,52)))
        e.append((n[50],n[43],(50,43)))
        e.append((n[46],n[40],(46,40)))
        e.append((n[48],n[37],(48,37)))
        assert(len(e)==12)

        for x in e: #SOLVE EDGES
            if "O" in x and "G" in x:
                num_note[x[2][x.index("O")]] = 48
                num_note[x[2][x.index("G")]] = 37
            elif "O" in x and "B" in x:
                num_note[x[2][x.index("O")]] = 50
                num_note[x[2][x.index("B")]] = 43
            elif "O" in x and "W" in x:
                num_note[x[2][x.index("O")]] = 52
                num_note[x[2][x.index("W")]] = 34
            elif "O" in x and "Y" in x:
                num_note[x[2][x.index("O")]] = 46
                num_note[x[2][x.index("Y")]] = 40
            elif "B" in x and "W" in x:
                num_note[x[2][x.index("B")]] = 32
                num_note[x[2][x.index("W")]] = 21
            elif "W" in x and "G" in x:
                num_note[x[2][x.index("W")]] = 23
                num_note[x[2][x.index("G")]] = 24
            elif "G" in x and "Y" in x:
                num_note[x[2][x.index("G")]] = 26
                num_note[x[2][x.index("Y")]] = 27
            elif "Y" in x and "B" in x:
                num_note[x[2][x.index("Y")]] = 29
                num_note[x[2][x.index("B")]] = 30
            elif "R" in x and "W" in x:
                num_note[x[2][x.index("R")]] = 1
                num_note[x[2][x.index("W")]] = 10
            elif "R" in x and "G" in x:
                num_note[x[2][x.index("R")]] = 3
                num_note[x[2][x.index("G")]] = 13
            elif "R" in x and "Y" in x:
                num_note[x[2][x.index("R")]] = 7
                num_note[x[2][x.index("Y")]] = 16
            elif "R" in x and "B" in x:
                num_note[x[2][x.index("R")]] = 5
                num_note[x[2][x.index("B")]] = 19

    if(1):#8
        # add coners 8
        c=[]
        c.append((n[0],n[11],n[12],(0,11,12)))
        c.append((n[2],n[20],n[9],(2,20,9)))
        c.append((n[6],n[14],n[15],(6,14,15)))
        c.append((n[8],n[17],n[18],(8,17,18)))
        c.append((n[45],n[38],n[39],(45,38,39)))
        c.append((n[47],n[41],n[42],(47,41,42)))
        c.append((n[51],n[35],n[36],(51,35,36)))
        c.append((n[53],n[44],n[33],(53,44,33)))
        assert(len(c)==8)
        for x in c: #SOLVE CONERS
            if "W" in x and "R" in x and "G" in x:
                num_note[x[3][x.index("R")]] = 0
                num_note[x[3][x.index("W")]] = 11
                num_note[x[3][x.index("G")]] = 12
            elif "R" in x and "W" in x and "B" in x:
                num_note[x[3][x.index("R")]] = 2
                num_note[x[3][x.index("W")]] = 9
                num_note[x[3][x.index("B")]] = 20
            elif "R" in x and "G" in x and "Y" in x:
                num_note[x[3][x.index("R")]] = 6
                num_note[x[3][x.index("G")]] = 14
                num_note[x[3][x.index("Y")]] = 15
            elif "R" in x and "Y" in x and "B" in x:
                num_note[x[3][x.index("R")]] = 8
                num_note[x[3][x.index("Y")]] = 17
                num_note[x[3][x.index("B")]] = 18
            elif "O" in x and "W" in x and "G" in x:
                num_note[x[3][x.index("O")]] = 51
                num_note[x[3][x.index("W")]] = 35
                num_note[x[3][x.index("G")]] = 36
            elif "O" in x and "W" in x and "B" in x:
                num_note[x[3][x.index("O")]] = 53
                num_note[x[3][x.index("W")]] = 33
                num_note[x[3][x.index("B")]] = 44
            elif "O" in x and "Y" in x and "B" in x:
                num_note[x[3][x.index("O")]] = 47
                num_note[x[3][x.index("Y")]] = 41
                num_note[x[3][x.index("B")]] = 42
            elif "O" in x and "Y" in x and "G" in x:
                num_note[x[3][x.index("O")]] = 45
                num_note[x[3][x.index("Y")]] = 39
                num_note[x[3][x.index("G")]] = 38
    if(1):#6
        cc = []
        ORDER = ["R","G","Y","B","W","O"]
        C_DER = [4,25,28,31,22,49]   
        for x in C_DER:
            cc.append((n[x],x))   
        
        for color,idx in cc: #SOLVE centers
            num_note[idx] = C_DER[ORDER.index(color)]
    return num_note
        
def solver():
    ct = [47,24,9,40,4,29,14,50,53,20,23,42,41,46,15,6,43,33,44,30,2,16,22,32,21,25,27,26,28,13,3,31,7,35,1,39,45,48,8,18,5,11,0,52,51,17,19,12,37,49,34,38,10,36]
    '''
              6 3 0
              7 4 1
              8 5 2
d e f  g h f  i j k  a b c
W W W  G G G  Y Y Y  B B B
W W W  G G G  Y Y Y  B B B
              O O O
              O O O
              O O O
    ''' 
    ttt = [x for x in range(54)]
    ct = [6,3,0,7,4,1,8,5,2,12,13,14,15,16,17,18,19,20,9,10,11]
    # ct = [2,5,8,1,4,7,0,3,6,18,19,20,9,10,11,12,13,14,15,16,17]
    ct = ct+ttt[len(ct):]
    return ct

def mapping(random,scramb):
    
    iii ='''
                R R R
                R R R
                R R R
    G G G  Y Y Y  B B B  W W W
    W W W  G G G  Y Y Y  B B B
    W W W  G G G  Y Y Y  B B B
                O O O
                O O O
                O O O
    '''
    # nr,_ = to_note(random)
    # print(nr)

    shit_random = sh1t(random)
    shit_scramb = sh1t(scramb)
    solved = iii.split()
    # print(shit_random)
    # print(shit_scramb)
    f1 = {}
    for x in range(54):
        f1[x] = shit_random.index(shit_scramb[x])
    print(f1)
    new = [0]*54
    for x in range(54):
        new[f1[x]] = x
    def fkk(l):
        res = []
        for x in l:
            if x in [0,1,2,3,4,5,6,7,8]:
                res.append("R")
            elif x in [15,16,17,27,28,29,39,40,41]:
                res.append("Y")
            elif x in [18,19,20,30,31,32,42,43,44]:
                res.append("B")
            elif x in [9,10,11,21,22,23,33,34,35]:
                res.append("W")
            elif x in [12,13,14,24,25,26,36,37,38]:
                res.append("G")
            else:
                res.append("O")
        return " ".join(res)
    
    fkkkkk,_ = to_note(fkk(new))
    print(fkkkkk)
    exit(1)
    # f2 = {}
    # for x in range(54):
    #     f2[shit_solved[x]] = shit_random[x]
    # random = random.split()

    # mapping_res = solver()

    # res = [0] *54
    # for x in range(54):
    #     res[x] = random[mapping_res.index(x)]
    #     # res[mapping_res.index(x)] = random[x]
    # print(res)
    # return " ".join(res)
    # for x in range(54):
    #     random

'''
              0 1 2
              3 4 5
              6 7 8
a b c  d e f  g h f  i j k
W W W  G G G  Y Y Y  B B B
W W W  G G G  Y Y Y  B B B
              O O O
              O O O
              O O O

              6 3 0
              7 4 1
              8 5 2
d e f  g h f  i j k  a b c
W W W  G G G  Y Y Y  B B B
W W W  G G G  Y Y Y  B B B
              O O O
              O O O
              O O O

              2 5 8
              1 4 7
              0 3 6
i j k  9 a b  c d e  f g h
W W W  G G G  Y Y Y  B B B
W W W  G G G  Y Y Y  B B B
              O O O
              O O O
              O O O
'''


scramble = """
              O G W
              Y R Y
              G O O
B W B  Y O Y  R B W  B B R
Y W B  W G Y  G Y G  R B R
W R Y  O O R  B R W  R O O
              Y B G
              G O W
              G W G


"""

random  = """
              G W B
              B R Y
              Y Y O
O G W  O W R  G R W  B B Y
R W O  Y G B  O Y G  R B W
Y G G  Y Y W  B R W  R O B
              R B G
              G O W
              O O R

"""
corect_order = ["UF", "UR", "UB", "UL", "DF", "DR", "DB","DL", "FR", "FL","BR","BL","UFR","URB","UBL","ULF","DRF","DFL","DLB","DBR"]

random_prime = mapping(random,scramble)

sample, _ = to_note(random_prime)
print(sample)
# exit(1)

# sample, mapping = to_note(scramble)
# rev = inverse(sample)


# sample, mapping2 = to_note(random)

# for x in rev.keys():
#     print(x,rev[x])
# news = ""
# for i in sample.split():
#     news += rev[i]
#     news += " "

# print(news)
