#program v pythonu 3.8 na fitovani velikosti vodivosti RLV obvodu. Vykresluje take fazi. Je potreba nainstalovat balicky numpy a lmfit
import matplotlib.pyplot as plt   #nacteni knihovny pro kresleni, instalace pomocí příkazu: pip install matplotlib
import numpy as np    #nacteni numericke knihovny numpy, instalace pomocí příkazu: pip install numpy
from lmfit import Minimizer, Parameters, fit_report   #nacteni knihovny pro fitovani LMfit, instalace pomocí příkazu: pip install numpy
from uncertainties import ufloat #balicek na vypocet propagace chyb, instalace pomocí příkazu: pip install uncertainties
from uncertainties.umath import *

#definice funkci
def Gabs(F,omega0,alpha,omega):   #absolutni velikost vodivosti, vyjadreno pomoci F, omega0 a alpha. Pri fitovani pomoci R,L,C hodnoty L a C velmi silne antikoreluji
	return omega*F/np.sqrt((omega0**2-omega**2)**2+(2*alpha*omega)**2)
def Gphi(omega0,alpha,omega):  #faze ve stupnich
	return np.arctan((omega0**2-omega**2)/(2*alpha*omega))/np.pi*180
def residual(pars, omega, Gdata):    #definice residualu: rozdilu fitovane funkce a dat
	return Gabs(pars['F'],pars['omega0'],pars['alpha'],omega) - Gdata  #zde se fituje jen rozdil absolutni hodnoty vodivosti mezi teorii a daty, ne faze

#nacteni dat
data=np.loadtxt('RLCfrekv.dat', skiprows=1)   #nacteni exprimentalnich dat do pole "data", preskakuje prvni radek
fdata=data[:,0]   #nacte frekvenci z prvniho sloupce
odata=fdata*2*np.pi  #prepocteni na kruhovou frekvenci
Gdata=data[:,1]  #nacte amplitudy vodivosti z druheho sloupce 
Phase=data[:,2]  #nacteni amplitudu faze z tretiho sloupce 

R=60 #[Ohm], odhad hodnoty odporu, 
L=0.110 #[H], odhad hodnoty indukce
C=200E-9 #[F], odhad hodnoty kapacity.
ParsStart = Parameters()   #definice objektu fitovacich parametru 
#pri nelinearnim fitovani by mely byt startovaci hodnoty parametru relativne blizko konecnym, jinak fit nemusi dobre zkonvergovat
#zavedeni jednotlivych fitovacich parametru se startovaci fitovaci hodnotou a informaci, zda se fituje nebo ne (vary=True/False)
ParsStart.add('F', value=1/L,vary=True)   
ParsStart.add('omega0', value=1/np.sqrt(L*C),vary=True)  
ParsStart.add('alpha', value=R/(2*L),vary=True)  

#fitovani
minner = Minimizer(residual, ParsStart, fcn_args=(odata,Gdata))  #samotne fitovani. Vola funkci residual, pouziva parametrky k fitovani Parstart
results = minner.minimize()  #ulozeni vysledku fitovani do promenne result
ParsFit= results.params   #ulozeni vyslednych hodnot fitovacich parametru do promenne ParsFit

#vypsani statistiky na obrazovku a ulozeni do souboru
print(fit_report(results))  # write error report, alternative result.params.pretty_print()
FileStatistika= open('Statistika.dat', 'w+')  #ulozeni statistiky do souboru
print(fit_report(results),file=FileStatistika)
FileStatistika.close()

#vytvoreni promennych ufloat z knihovny uncertainties pro vypocet nejen hodnot, ale i chyb. Prvni parametr je hodnota, druhy chyba
F=ufloat(ParsFit['F'], ParsFit['F'].stderr)  
omega0=ufloat(ParsFit['omega0'], ParsFit['omega0'].stderr)
alpha=ufloat(ParsFit['alpha'], ParsFit['alpha'].stderr)
# vypocet dalcich hodnot. Knihovna uncertainties k tomu automaticky vypocte chyby dle zakona sireni chyb 
L=1/F
R=2*L*alpha
C=1/(L*omega0**2)
Q=omega0/(2*alpha)
f0=omega0/(2*np.pi)
print("")
print("Vypoctene dalsi hodnoty vcetne chyb dle zakona sireni chyb s pomoci balicku uncertainties")
print("R=", R,"Ohm, L=", L*1000,"mH, C=", C*1E9,"nF,  Q=",Q, "f0=", f0, "Hz")

#vypocet startovacich a fitovacich funkci
ftheor = np.arange(np.amin(fdata), np.amax(fdata), 1)  # vytvoreni osy frekvence pro teoreticky vypocet v ramci merenych dat s krokem 1 Hz
otheor=ftheor*2*np.pi   #prepcet na kruhovou frekvenci
# vypocet startovaci funkce Gabs (v nelinerarnim fitovani by nemela by byt moc daleko od experimentalnich dat
GabsStart = Gabs(ParsStart["F"],ParsStart["omega0"],ParsStart["alpha"],otheor)  
GphiStart = Gphi(ParsStart["omega0"],ParsStart["alpha"],otheor)  # vypocet startovaci funkce Gphi
GabsFit = Gabs(ParsFit["F"],ParsFit["omega0"],ParsFit["alpha"],otheor)  # vypocet nafitovane funkce Gabs
GphiFit = Gphi(ParsFit["omega0"],ParsFit["alpha"],otheor)  # vypocet nafitovane funkce Gphi

#ulozeni startovaci a nafitovanych zavislosti do souboru
FileFitSpekta= open('FitSpekta.dat', 'w+')
print ("f[Hz]", "\t", "GabsStart",  "\t", "GphiStart", "\t", "GabsFit",  "\t", "GphiFit", file=FileFitSpekta)
for i in range(len(ftheor)):
    print (ftheor[i],"\t",GabsStart[i],  "\t",GphiStart[i], "\t", GabsFit[i],  "\t",GphiFit[i], file=FileFitSpekta)
FileFitSpekta.close()

#vykresleni obrazku amplitudy a faze
fig, (ax1, ax2) = plt.subplots(1, 2)  
#levy obrazek amplitudy
ax1.plot(ftheor,GabsStart,'k-',label='|G| Start')
ax1.plot(ftheor,GabsFit,'b-',label=' |G| Fit')
ax1.plot(fdata,Gdata,'r*',label='|G| Data')
ax1.legend(loc='upper right', shadow=False)
ax1.set(xlabel='f [Hz]', ylabel='amplituda G [Ohm-1]')
#pravy obrazek faze
ax2.plot(ftheor,GphiStart,'k-',label='Faze Start')
ax2.plot(ftheor,GphiFit,'b-',label='Faze Fit')
ax2.plot(fdata,Phase,'r*',label='Faze Data')
ax2.legend(loc='upper right', shadow=False)
ax2.set(xlabel='f [Hz]', ylabel='faze [deg]')
plt.savefig('vodivost.pdf')
plt.show()

