from Crypto.Util.number import *
from secret import flag
import random

module_bit = 512
beta = 0.6

class PRNG:
    def __init__(self) -> None:
        self.n1 = getPrime(module_bit)
        self.n2 = getPrime(module_bit)

        self.A_l = [random.randrange(1,self.n1) for _ in range(2)]
        self.B_l = [random.randrange(1,self.n2) for _ in range(2)]

        self.x_state = [random.randrange(1,self.n2) for _ in range(2)]
        self.y_state = [random.randrange(1,self.n2) for _ in range(2)]

        self.z_state = [(self.x_state[i] - self.y_state[i]) % self.n1 for i in range(2)]

    def clock(self):
        x_next = (self.A_l[0] * self.x_state[-1] + self.A_l[1] * self.x_state[-2]) % self.n1
        self.x_state.append(x_next)

        y_next = (self.B_l[0] * self.y_state[-1] + self.B_l[1] * self.y_state[-2]) % self.n2
        self.y_state.append(y_next)

        z_next = (x_next-y_next) % self.n1
        self.z_state.append(z_next)

        return x_next,y_next,z_next

prng = PRNG()
A_l,B_l,n1,n2 = prng.A_l,prng.B_l,prng.n1,prng.n2
ret_xs = []
ret_ys = []
ret_zs = []

for _ in range(5):
    ret_x,ret_y,ret_z = prng.clock()
    ret_xs.append(ret_x & (2 ** int(module_bit * beta) - 1))
    ret_zs.append(ret_z >> int(module_bit * (1-beta)) << int(module_bit * (1-beta)))

m = bytes_to_long(flag)
a = prng.clock()[1]

print("a0,a1 = " , A_l)
print("b0,b1 = " , B_l)
print("n1 = " , n1)
print("n2 = " , n2)
print("xs = " , ret_xs)
print("zs = " , ret_zs)
print("encflag = " , long_to_bytes(a ^ m))

'''
a0,a1 =  [9919754465736816172569173052425931289517829891854342593290927744542118133847348662406222547572947297178727236300405992491684375909305177189047780739423811, 2558159371069956421749072997341298610563190398496109008773995596731281585562821740934514052081914548707643961639133075782257512937408016925625816701379184]
b0,b1 =  [2605193676009044327751542404995552395651364785430784591434496675113980641629822868464738894812540539614357309531957125239722030117295601326651054134997855, 3197045230062951998763856325415663842943082118997359612045648551897230423045976716318651375603679498159844171771317291574116847000481449039959441081514627]
n1 =  11681289596798868397030596649789726767285990000843272211957420810019522067387532211264897471096909399295930769738569665286430964000906934541163352714344519
n2 =  10557965421921341302784057525127038885537939006621468287750526343357317493360177624286054901157989185048184920439519551848192429179141349006037985539214071
xs =  [258466590698311071331247037930868824798600351331801120333006455557946900924072178631112955877, 9821442718613283840479818314015332171481079398147839951441986495105073061641539763228587316, 44840961768274714901326962447354283020302651991130253647924461474246517162698016799008370900, 4181026132314144744475531197443398345060712084263169112302700944672100108051705214872237804, 165146543464042899162832236414189105534540273973129205248892886798269176015886688299461120067]
zs =  [11425495409956732054927782736077190158254288269207497569801502736793464884202670506015379318738941018498330797528225268357863433326525610294847934650384384, 6493331726937754866196531134748756985061780536063848814074103775547995272554729994318400024248625477632819500830464284078877134996898279637865644465061888, 993089766452002806192286220960438231942075399393023941745370499613681022868865277955412695258671518735133398965459541404411563617841529593232577007714304, 9947918164778455706315062500056819613968192691484842758450452417155875586535345223342626196771965216296162822961357707526761812463743778564968870859243520, 6798568953150532649740005658966557905457680624368167498216858785007123058363282156005182480229608829437870473084370507240870801760529936705635869020651520]      
encflag =  b'\x84\x0bk\xfbmp\x1aV\x95q\r\x9bZ/s\xe5\xb4\xa5Y~y\xac\xaa\xd1\xff\xf1\xf1\xee#\xbd\x07:n\x9c\xd6\xcdV*\xfc\xbe0\x96\xff\xff\xa1E\xdd\xb3\x96\xa2\xb2\x8cW\xc2#6Y\xa0\xf2\xd7\xb7*\xbb\xfb'
'''