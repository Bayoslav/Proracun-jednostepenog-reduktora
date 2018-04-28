import math

#snaga - p
'''
p = (int(input("Unesi snagu(kW): ")))
n = (int(input("Br obrtaja pogonskog zupc. : ")))
i = (float(input("Prenosni odnos: ")))
z1 = (int(input("z1: ")))


cofx = (int(input("x: ")))
ka = (float(input("Ka: ")))
beta = (int(input("beta: ")))
#Proracun zupcanika
fi = (float(input("faktor sirine zupc. : ")))
'''

p=40 
n=500
i=2.2
z1=20 
beta = 5
fi = 0.5
ka=1.55
x=0
w = (math.pi*n)/30
t1 = int((p/w)*1000*1000)
print(t1)
sigmad = 320
kvbeta = 1.02
khbeta = 1.03
kh = ka*kvbeta*khbeta
print(kh)
ze = 189 
#math.cos(math.radians(1)) - stim sto je jedan ugao
z = 2.5 * ze * math.cos(math.radians(beta))
print("z: ", z)
print("cos: ", math.cos(math.radians(beta)))
d1_neb = ((2*t1*(i+1)*kh*z**2)/(fi*sigmad**2*i))**(1/3)
print("d1_neb: ", d1_neb)
mn = int((d1_neb*math.cos(math.radians(beta)))/z1)
print("mn: ", mn)
mt = mn/math.cos(math.radians(beta))
print("mt: ", mt)

alfan = 20
tgalfat = math.tan(math.radians(alfan))/math.cos(math.radians(beta))
print("tgalfat: ", tgalfat)
alfat = math.degrees(math.atan(tgalfat))
print("alfat: ", alfat)
z2 = z1*i 
print("z2: ", z2)
zn1 = (z1/(math.cos(math.radians(beta))**3))
print("zn1: ", zn1)
zn2 = (z2/(math.cos(math.radians(beta))**3))
print("zn2: ", zn2)
d1_zup = z1*mt
print("d1_zup: ", d1_zup)
d2_zup = z2*mt
print("d2_zup: ", d2_zup)
b1 = fi*d1_zup
b2 = b1-10
print("b1: ", b1)
print("b2: ", b2)
r1 = d1_zup/2
r2 = d2_zup/2
print("r1: ", r1)
print("r2:", r2)
db1 = d1_zup * math.cos(math.radians(alfat))
db2 = d2_zup * math.cos(math.radians(alfat))
print("db1: ", db1)
print("db2: ", db2)
rb1 = db1/2 
rb2 = db2/2
print("rb1", rb1)
print("rb2", rb2)
a = r1 + r2 
df1 = d1_zup-2*mn*1.25
df2 = d2_zup-2*mn*1.25
print("df1", df1)
print("df2", df2)
da1 = d1_zup + 2*mn 
da2 = d2_zup + 2*mn 
print("da1", da1)
print("da2", da2)
ra1 = da1/2
ra2 = da2/2 
print('ra1',ra1)
print('ra2', ra2)
pn = mn*math.pi 
print('pn', pn)
pt = mt*math.pi 
print('pt', pt)
#print('math.sqrt(5):', math.sqrt(9))
pb = pt*math.cos(math.radians(alfat))
print('pb', pb)
qalfa = math.sqrt(ra1**2-rb1**2)+math.sqrt(ra2**2-rb2**2)-a*math.sin(math.radians(alfat))
print('qalfa', qalfa)
etaalfa = qalfa/pb 
print('etaalfa:', etaalfa)
etabeta = b1*math.tan(math.radians(beta))/pb 
print('etabeta:', etabeta)
eta = etaalfa+etabeta 
print('eta:', eta)
#1b

ye = 0.25 + (0.75/etaalfa)
print('ye:', ye)
yb = 1-etabeta-beta/120
yfa=2.91 
ysa = 1.65
ft = (2*t1)/d1_zup
print('yb:', yb)
print('yfa:', yfa)
print('ysa:', yfa)
print('ft:', ft)
sigmaf = yfa*ysa*ye*(ft/(b1*mn))*ka*kvbeta*khbeta
print('sigmaf:', sigmaf)
s1 = (1.7*192)/sigmaf
print('s1:', s1)
invalfat = math.tan(math.radians(alfat)) - (alfat*math.pi)/180
print('invalfat:', invalfat)
zw1 = (z1/math.pi)*(math.tan(math.radians(alfat))-invalfat)+0.5
zw2 = (z2/math.pi)*(math.tan(math.radians(alfat))-invalfat)+0.5
print('zw1:', zw1)
print('zw2:', zw2)
w1 = (mn*math.cos(math.radians(alfan)))*(math.pi*(zw1-0.5)+z1*invalfat)
w2 = (mn*math.cos(math.radians(alfan)))*(math.pi*(zw2-0.5)+z2*invalfat)
print('w1:', w1)
print('w2:', w2)

#B PRORACUN VRATILA 
print("\nPRORACUN VRATILA\n")

ft1 = ((2*t1)/d1_zup)*ka
print('ft1:', ft1)
beta = math.radians(beta)
alfan = math.radians(alfan)
fr1 = ft1*(math.tan(alfan)/math.cos(beta))
print('fr1:', fr1)
fa1 = ft1*(math.tan(beta))
print('fa1:', fa1)
fbh = (fa1*(d1_zup/2)+fr1*90)/180
print('fbh:', fbh)
fah=((fr1*90)-(fa1*(d1_zup/2)))/180
print('fah:', fah)

#V - RAVAN 

fav = ft1/2
fa = math.sqrt(fbh**2+fbv**2)
fb = math.sqrt(fbh**2+fbv**2)

print("\nMOMENTI SAVIJANJA NA VRATILU 1")

ms1vc = -fav*90
print('ms1vc:', ms1vc)
ms1hc1 = -fah*90
ms1hc2 = -fah*90-fa1*(d1_zup/2)
print('ms1hc1:', ms1hc1)
print('ms1hc2:', ms1hc2)
sigmasd = 54
tud = 57
alfao = 0.965
ms1l = math.sqrt(ms1vc**2 + mas1hc1**2)

mil = math.sqrt((ms1l**2+0.965/2)*t1) 
print('ms1l:', ms1l)
print('mil:', mil)
dia = ((16*t1)/(math.pi*tud))**(1/8)
dil = ((32*mil)/(math.pi*sigmasd))**(1/3)
ds = 1.1 * dia 
da = 1.2*dia 
d1_vrat1 = 1.2*dil
print('dia:', dia)
print('dil:', dil)
print('ds:', ds)
print('da:', da)
print('d1_vrat1:', d1_vrat1)

print("\n3. Proracun za vezu sa zupcanikom za d=60mm\n")
t3 = 6.8
print('t3:', t3)
t_1 = h-t3
ft_3 =  (2*t1*ka)/60
p = ft_3/(72*t_1)
print('t_1:', t_1)
print('ft_3:', ft_3)
print('p:', p)
betak = 2.17 
ksi1 = 0.9 
ksi2 = 0.74 
ksi2u = 0.66 
sigmasd_2 = ms
w = 14774.56 
wp = 29549.12
taud_2 = t1/wp 
ssigma = 220*0.9*0.74/2.17*











