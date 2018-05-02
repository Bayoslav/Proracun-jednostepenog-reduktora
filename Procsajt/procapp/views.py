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
        beta = int(request.POST.get('beta'))
        fi = float(request.POST.get('fi'))
        x = int(request.POST.get('x'))
        ka = float(request.POST.get('ka'))
        w = (math.pi*n)/30
        dic['w'] = w
        t1 = int((p/w)*1000*1000)
        dic["t1"] = t1
        sigmad = 320
        kvbeta = 1.02
        khbeta = 1.03
        kh = ka*kvbeta*khbeta
        dic["kh"] = kh
        ze = 189 
        #math.cos(math.radians(1)) - stim sto je jedan ugao
        z = 2.5 * ze * math.cos(math.radians(beta))
        dic["z"]= z
        dic["cos"]= math.cos(math.radians(beta))
        d1_neb = ((2*t1*(i+1)*kh*z**2)/(fi*sigmad**2*i))**(1/3)
        dic["d1_neb"]= d1_neb
        mn = int((d1_neb*math.cos(math.radians(beta)))/z1)
        dic["mn"]= mn
        mt = mn/math.cos(math.radians(beta))
        dic["mt"]= mt

        alfan = 20
        tgalfat = math.tan(math.radians(alfan))/math.cos(math.radians(beta))
        dic["tgalfat"]= tgalfat
        alfat = math.degrees(math.atan(tgalfat))
        dic["alfat"]= alfat
        z2 = z1*i 
        dic["z2"]= z2
        zn1 = (z1/(math.cos(math.radians(beta))**3))
        dic["zn1"]= zn1
        zn2 = (z2/(math.cos(math.radians(beta))**3))
        dic["zn2"]= zn2
        d1_zup = z1*mt
        dic["d1_zup"]= d1_zup
        d2_zup = z2*mt
        dic["d2_zup"]= d2_zup
        b1 = fi*d1_zup
        b2 = b1-10
        dic["b1"]= b1
        dic["b2"]= b2
        r1 = d1_zup/2
        r2 = d2_zup/2
        dic["r1"]= r1
        dic["r2:"]= r2
        db1 = d1_zup * math.cos(math.radians(alfat))
        db2 = d2_zup * math.cos(math.radians(alfat))
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
        pb = pt*math.cos(math.radians(alfat))
        dic['pb']= pb
        qalfa = math.sqrt(ra1**2-rb1**2)+math.sqrt(ra2**2-rb2**2)-a*math.sin(math.radians(alfat))
        dic['qalfa']= qalfa
        etaalfa = qalfa/pb 
        dic['etaalfa']= etaalfa
        etabeta = b1*math.tan(math.radians(beta))/pb 
        dic['etabeta']= etabeta
        eta = etaalfa+etabeta 
        dic['eta']= eta
        #1b

        ye = 0.25 + (0.75/etaalfa)
        dic['ye']= ye
        yb = 1-etabeta-beta/120
        yfa=2.91 
        ysa = 1.65
        ft = (2*t1)/d1_zup
        dic['yb']= yb
        dic['yfa']= yfa
        dic['ysa']= yfa
        dic['ft']= ft
        sigmaf = yfa*ysa*ye*(ft/(b1*mn))*ka*kvbeta*khbeta
        dic['sigmaf']= sigmaf
        s1 = (1.7*192)/sigmaf
        dic['s1']= s1
        invalfat = math.tan(math.radians(alfat)) - (alfat*math.pi)/180
        dic['invalfat']= invalfat
        zw1 = (z1/math.pi)*(math.tan(math.radians(alfat))-invalfat)+0.5
        zw2 = (z2/math.pi)*(math.tan(math.radians(alfat))-invalfat)+0.5
        dic['zw1']= zw1
        dic['zw2']= zw2
        w1 = (mn*math.cos(math.radians(alfan)))*(math.pi*(zw1-0.5)+z1*invalfat)
        w2 = (mn*math.cos(math.radians(alfan)))*(math.pi*(zw2-0.5)+z2*invalfat)
        dic['w1']= w1
        dic['w2']= w2

        #B PRORACUN VRATILA 
        print("\nPRORACUN VRATILA\n")

        ft1 = ((2*t1)/d1_zup)*ka
        dic['ft1']= ft1
        beta = math.radians(beta)
        alfan = math.radians(alfan)
        fr1 = ft1*(math.tan(alfan)/math.cos(beta))
        dic['fr1']= fr1
        fa1 = ft1*(math.tan(beta))
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

        print("\nMOMENTI SAVIJANJA NA VRATILU 1")

        ms1vc = -fav*90
        dic['ms1vc']= ms1vc
        ms1hc1 = -fah*90
        ms1hc2 = -fah*90-fa1*(d1_zup/2)
        dic['ms1hc1']= ms1hc1
        dic['ms1hc2']= ms1hc2
        sigmasd = 54
        tud = 57
        alfao = 0.965
        ms1l = math.sqrt(ms1vc**2 + ms1hc1**2)

        mil = math.sqrt((ms1l**2+0.965/2)*t1) 
        dic['ms1l']= ms1l
        dic['mil']= mil
        dia = ((16*t1)/(math.pi*tud))**(1/8)
        dil = ((32*mil)/(math.pi*sigmasd))**(1/3)
        ds = 1.1 * dia 
        da = 1.2*dia 
        d1_vrat1 = 1.2*dil
        dic['dia'] = dia
        dic['dil']= dil
        dic['ds']= ds
        dic['da']= da
        dic['d1_vrat1']= d1_vrat1

        print("\n3. Proracun za vezu sa zupcanikom za d=60mm\n")
        t3 = 6.8
        dic['t3']= t3
        h=11
        t_1 = h-t3
        ft_3 =  (2*t1*ka)/60
        p = ft_3/(72*t_1)
        dic['t_1']= t_1
        dic['ft_3']= ft_3
        dic['p']= p
        betak = 2.17 
        ksi1 = 0.9 
        ksi2 = 0.74 
        ksi2u = 0.66 

        w = 14774.56 
        wp = 29549.12
        taud_2 = t1/wp 
        sigmasd_2 = ms1l/w
        ssigma = 220*0.9*0.74/(2.17*sigmasd_2)
        stau = (170*0.9*0.66)/(betak*taud_2)
        s_2 = (ssigma*stau)/math.sqrt(ssigma**2+stau**2)
        dic['w']= w
        dic['wp']= wp
        dic['taud_2']= taud_2
        dic['sigmasd_2']= sigmasd_2
        dic['ssigma']= ssigma
        dic['stau']= stau
        dic['s_2']= s_2

        print("\nPRORACUN VRATILA 2")

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

        print("\n MOMENT SAVIJANJA NA VRATILU 2\n")
        msl2v = fcv*90
        msl2h = fch*90
        msd2h = fdh*90
        msl2 = math.sqrt(msl2v**2+msl2h**2)
        msld = math.sqrt(msl2v**2+msd2h**2)
        #mil2 = 
        mil2 = math.sqrt((msl2**2+0.965/2)*t1) 

        dis = ((16*t1)/(math.pi*tud))**(1/3)
        dic['msl2v']= msl2v
        dic['msl2h']= msl2h
        dic['msd2h']= msd2h
        dic['msl2']= msl2
        dic['msld']= msld
        dic['mil2']= mil2
        dic['dis']= dis
        dic['t1']= t1
        dil_2 = ((32*mil2)/(math.pi*sigmasd))**(1/3)
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