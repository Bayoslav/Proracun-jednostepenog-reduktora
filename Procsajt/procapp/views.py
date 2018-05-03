from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from procapp.forms import ProcForm
# Create your views here.
import math
class Index(View):
    def get(self, request):
        form = ProcForm()
        return render(request,'index.html',{
        'form' : ProcForm})
    def post(self,request):
        form = ProcForm(request.POST)
        #dic[form)
        #dic[request.POST)
        #dic[dir(request.POST))
        dic = {}
        p =  int(request.POST.get('p'))
        n =  int(request.POST.get('n'))
        i =  float(request.POST.get('i'))
        z1 =  int(request.POST.get('z1'))
        β = int(request.POST.get('beta'))
        φ = float(request.POST.get('fi'))
        x = int(request.POST.get('x'))
        ka = float(request.POST.get('ka'))
        w = (math.pi*n)/30
        dic['w'] = w
        t1 = int((p/w)*1000*1000)
        dic["t1"] = t1
        σd = 320
        kvβ = 1.02
        khβ = 1.03
        kh = ka*kvβ*khβ
        dic["kh"] = kh
        ze = 189 
        #math.cos(math.radians(1)) - stim sto je jedan ugao
        z = 2.5 * ze * math.cos(math.radians(β))
        dic["z"]= z
        dic["cos"]= math.cos(math.radians(β))
        d1_neb = ((2*t1*(i+1)*kh*z**2)/(φ*σd**2*i))**(1/3)
        dic["d1_neb"]= d1_neb
        mn = int((d1_neb*math.cos(math.radians(β)))/z1)
        dic["mn"]= mn
        mt = mn/math.cos(math.radians(β))
        dic["mt"]= mt

        αn = 20
        tgαt = math.tan(math.radians(αn))/math.cos(math.radians(β))
        dic["tgαt"]= tgαt
        αt = math.degrees(math.atan(tgαt))
        dic["αt"]= αt
        z2 = z1*i 
        dic["z2"]= z2
        zn1 = (z1/(math.cos(math.radians(β))**3))
        dic["zn1"]= zn1
        zn2 = (z2/(math.cos(math.radians(β))**3))
        dic["zn2"]= zn2
        d1_zup = z1*mt
        dic["d1_zup"]= d1_zup
        d2_zup = z2*mt
        dic["d2_zup"]= d2_zup
        b1 = φ*d1_zup
        b2 = b1-10
        dic["b1"]= b1
        dic["b2"]= b2
        r1 = d1_zup/2
        r2 = d2_zup/2
        dic["r1"]= r1
        dic["r2:"]= r2
        db1 = d1_zup * math.cos(math.radians(αt))
        db2 = d2_zup * math.cos(math.radians(αt))
        dic["db1"]= db1
        dic["db2"]= db2
        rb1 = db1/2 
        rb2 = db2/2
        dic["rb1"]= rb1
        dic["rb2"]= rb2
        a = r1 + r2 
        df1 = d1_zup-2*mn*1.25
        df2 = d2_zup-2*mn*1.25
        dic["df1"]= df1
        dic["df2"]= df2
        da1 = d1_zup + 2*mn 
        da2 = d2_zup + 2*mn 
        dic["da1"]= da1
        dic["da2"]= da2
        ra1 = da1/2
        ra2 = da2/2 
        dic['ra1']=ra1
        dic['ra2']= ra2
        pn = mn*math.pi 
        dic['pn']= pn
        pt = mt*math.pi 
        dic['pt']= pt
        #dic['math.sqrt(5)']= math.sqrt(9))
        pb = pt*math.cos(math.radians(αt))
        dic['pb']= pb
        qα = math.sqrt(ra1**2-rb1**2)+math.sqrt(ra2**2-rb2**2)-a*math.sin(math.radians(αt))
        dic['qα']= qα
        εα = qα/pb 
        dic['εα']= εα
        εβ = b1*math.tan(math.radians(β))/pb 
        dic['εβ']= εβ
        ε = εα+εβ 
        dic['ε']= ε
        #1b

        ye = 0.25 + (0.75/εα)
        dic['ye']= ye
        yb = 1-εβ-β/120
        yfa=2.91 
        ysa = 1.65
        ft = (2*t1)/d1_zup
        dic['yb']= yb
        dic['yfa']= yfa
        dic['ysa']= yfa
        dic['ft']= ft
        σf = yfa*ysa*ye*(ft/(b1*mn))*ka*kvβ*khβ
        dic['σf']= σf
        s1 = (1.7*192)/σf
        dic['s1']= s1
        invαt = math.tan(math.radians(αt)) - (αt*math.pi)/180
        dic['invαt']= invαt
        zw1 = (z1/math.pi)*(math.tan(math.radians(αt))-invαt)+0.5
        zw2 = (z2/math.pi)*(math.tan(math.radians(αt))-invαt)+0.5
        dic['zw1']= zw1
        dic['zw2']= zw2
        w1 = (mn*math.cos(math.radians(αn)))*(math.pi*(zw1-0.5)+z1*invαt)
        w2 = (mn*math.cos(math.radians(αn)))*(math.pi*(zw2-0.5)+z2*invαt)
        dic['w1']= w1
        dic['w2']= w2

        #B PRORACUN VRATILA 
        dic['text'] = "\nPRORACUN VRATILA\n"

        ft1 = ((2*t1)/d1_zup)*ka
        dic['ft1']= ft1
        β = math.radians(β)
        αn = math.radians(αn)
        fr1 = ft1*(math.tan(αn)/math.cos(β))
        dic['fr1']= fr1
        fa1 = ft1*(math.tan(β))
        dic['fa1']= fa1
        fbh = (fa1*(d1_zup/2)+fr1*90)/180
        dic['fbh']= fbh
        fah=((fr1*90)-(fa1*(d1_zup/2)))/180
        dic['fah']= fah
        #V - RAVAN 

        fav = ft1/2
        fbv = fav
        fa = math.sqrt(fbh**2+fbv**2)
        fb = math.sqrt(fbh**2+fbv**2)

        #print()
        dic['text2'] = "\nMOMENTI SAVIJANJA NA VRATILU 1"
        ms1vc = -fav*90
        dic['Ms1vc']= ms1vc
        ms1hc1 = -fah*90
        ms1hc2 = -fah*90-fa1*(d1_zup/2)
        dic['Ms1hc1']= ms1hc1
        dic['Ms1hc2']= ms1hc2
        σsd = 54
        tud = 57
        αo = 0.965
        ms1l = math.sqrt(ms1vc**2 + ms1hc1**2)

        mil = math.sqrt((ms1l**2+0.965/2)*t1) 
        dic['Ms1l']= ms1l
        dic['mil']= mil
        dia = ((16*t1)/(math.pi*tud))**(1/8)
        dil = ((32*mil)/(math.pi*σsd))**(1/3)
        ds = 1.1 * dia 
        da = 1.2*dia 
        d1_vrat1 = 1.2*dil
        dic['dia'] = dia
        dic['dil']= dil
        dic['ds']= ds
        dic['da']= da
        dic['d1_vrat1']= d1_vrat1

        dic['text3'] = "\n3. Proracun za vezu sa zupcanikom za d=60mm\n"
        t3 = 6.8
        dic['t3']= t3
        h=11
        t_1 = h-t3
        ft_3 =  (2*t1*ka)/60
        p = ft_3/(72*t_1)
        dic['t_1']= t_1
        dic['ft_3']= ft_3
        dic['p']= p
        βk = 2.17 
        ksi1 = 0.9 
        ksi2 = 0.74 
        ksi2u = 0.66 

        w = 14774.56 
        wp = 29549.12
        τd_2 = t1/wp 
        σsd_2 = ms1l/w
        sσ = 220*0.9*0.74/(2.17*σsd_2)
        sτ = (170*0.9*0.66)/(βk*τd_2)
        s_2 = (sσ*sτ)/math.sqrt(sσ**2+sτ**2)
        dic['w']= w
        dic['wp']= wp
        dic['τd_2']= τd_2
        dic['σsd_2']= σsd_2
        dic['sσ']= sσ
        dic['sτ']= sτ
        dic['s_2']= s_2

        #print()
        dic['text4'] = "\nPRORACUN VRATILA 2"
        fdh = (fr1*90-fa1*d1_neb)/180 #fa1*d1_zup daje dobar rezultat a to ne bi trebalo da je tako
        dic["fa1"] =fa1
        dic["fr1"] = fr1
        dic['fdh']= fdh

        #fch*180-fa2*d2/2-fr2*90

        fch = (-fa1*(d1_neb)-fr1*90)/180
        fch = fch*(-1)
        dic['fch']= fch
        #dic[ft_3)
        
        #dic[ft)
        fcv = ft1/2
        dic['fcv']= fcv
        fdv = fcv
        fcr = math.sqrt(fcv**2+fch**2)
        fdr = math.sqrt(fdv**2+fdh**2)
        dic['fcr']= fcr
        dic['fdr']= fdr

        dic['text5'] = ("\n MOMENT SAVIJANJA NA VRATILU 2\n")
        msl2v = fcv*90
        msl2h = fch*90
        msd2h = fdh*90
        msl2 = math.sqrt(msl2v**2+msl2h**2)
        msld = math.sqrt(msl2v**2+msd2h**2)
        #mil2 = 
        mil2 = math.sqrt((msl2**2+0.965/2)*t1) 

        dis = ((16*t1)/(math.pi*tud))**(1/3)
        dic['Msl2v']= msl2v
        dic['Msl2h']= msl2h
        dic['Msd2h']= msd2h
        dic['Msl2']= msl2
        dic['Msld']= msld
        dic['mil2']= mil2
        dic['dis']= dis
        dic['t1']= t1
        dil_2 = ((32*mil2)/(math.pi*σsd))**(1/3)
        ds_2 = 1.1*dis
        dl = 1.2*dis
        d_2_2vratilo = 1.2*dil 

        dic['dil_2']= dil_2
        dic['ds_2']= ds_2
        dic['dl']= dl
        dic['d_2_2vratilo']= d_2_2vratilo

        return render(request,'index.html',{
        'dic' : dic})
        #pass