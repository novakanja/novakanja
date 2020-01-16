from math import*

print(f"")
print(f"PRETVORBA KOORDINAT")
print(f"za samo pretvorbo samo sledi navodilo, ki se ti izpisujejo")
print(f"po vsaki podani koordinati, pa pritisni 'ENTER'")
print(f"(pazi na enote, ki jih moraš uporabiti)")
print(f"")
print(f"PRETVORBA ELIPSOIDNIH KOORDINAT V KARTEZIČNE:")
t= float(input("Podaj elipsoidno sirino tocke v 0.00 °: φ:")) #-podaš v stopinjah
u= float(input("Podaj elipsoidno dolzino tocke v 0.00 °: λ:")) #-podaš v stopinjah
h= float(input("Podaj elipsoidno visino tocke v 0.00 m:"))

fi = radians(t)
la = radians(u)

a= 6378137
b= 6356752.3141
finv= 298.257222101
f= 0.00335281068118
R= 6371007.1810

e2= (2*f-f*f)
N = int(a/(sqrt(1-e2*(sin(fi)**2))))

x= (N+h)*cos(fi)*cos(la)
y= (N+h)*cos(fi)*sin(la)
z= (N*(1-e2)+h)*sin(fi)
print(f"")
print(f"Rezultat: ")
print(f"x: {x:.3f}")
print(f"y: {y:.3f}")
print(f"z: {z:.3f}")
print(f"")
print(f"PRETVORBA KARTEZIČNIH KOORDINAT V ELIPSOIDNE:")
x1= float(input("Podaj koordinato x v 0.00 m:"))
y1= float(input("Podaj koordinato y v 0.00 m:"))
z1= float(input("Podaj koordinato z v 0.00 m:"))

p= sqrt((x1**2)+(y1**2))
th= atan((z1*a)/(p*b))
e2crtica= e2/(1-e2)

fiiii= atan((z1+e2crtica*b*sin(th)**3)/(p-e2*a*cos(th)**3) )
hh= p/cos(fiiii) -N
laaaa= atan((y1/x1)) 

fii= degrees(fiiii)
laa=degrees(laaaa)
print(f"")
print(f"Rezultat: ")
print(f"φ: {fii:.4f}")
print(f"λ: {laa:.4f}")
print(f"h: {hh:.4f}")
print(f"")
print(f"hvala za uporabo mojega programa in lep dan še naprej")