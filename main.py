#contador k

#kj es vector de rotacion
#ki es eñ momento
import math
X=[1,0.95,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.15,0.1,0.0750,0.050,0.0250,0.0125,0.000,0.0125,0.0250,0.05,0.075,0.1,0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1]
Y=[-0.0012,-0.01027,-0.01867,-0.03320,-0.04480,-0.05320,-0.05827,-0.06,-0.058,-0.05093,-0.04493,-0.03653,-0.03133,-0.02493,-0.01680,-0.01133,0.0,0.01133,0.01680,0.02493,0.03133,0.03653,0.04493,0.05093,0.058,0.06,0.05827,0.05320,0.04480,0.03320,0.01867,0.01027,0.0012]
S=[]
FI=[]
#V=200.777km/h
V=55.77  #m/s
BETA=[]
i=0
K=[]
Ki=[]
n=len(X)
print(n)
for i in range(n-1):# el ki
    Ki=[]
    FI1=math.atan((Y[i+1]-Y[i])/(X[i+1]-X[i]))
    j=0
    BETA=[]
    for j in range(n-1):
        if i!=j:
            S=((X[j+1]-X[j])*(X[j+1]-X[j])+(Y[j+1]-Y[j])*(Y[j+1]-Y[j]))*(1/2)
            FI2=math.atan((Y[j+1]-Y[j])/(X[j+1]-Y[j]))
            A=-(X[i]-X[j])*math.cos(FI2)-(Y[i]-Y[j])*math.sin(FI2)
            B=((X[i]-X[j])*(X[i]-X[j]))+((Y[i]-Y[j])*(Y[i]-Y[j]))
            Cn=-math.cos(FI1-FI2)
            Dn=(X[i]-X[j])*math.cos(FI2)+(Y[i]-Y[j])*math.sin(FI2)
            E=math.sqrt(B-A*A)
            Kij=(Cn/2)*(math.log1p(((S*S)+2*A*S+B)/B))+((Dn-A*Cn)/E)*((math.atan((S+A)/E))-(math.atan(A/E)))
            Ki.append(Kij)
            beta=math.radians(FI2+90-5.4239)
            BETA.append(beta)
        else:
            Ki.append(0)
            FI2=math.atan((Y[j+1]-Y[j])/(X[j+1]-Y[j]))
            beta=math.radians(FI2+90-5.4239)
            BETA.append(beta)
            
        j=j+1
    K.append(Ki)
    

    i=i+1



print(K)
print(len(K))
print(len(K[0]))

MATRIZCOSENOS=[]
u=0
for u in range(n-1):
   beta
   co=V*math.cos(BETA[u])
   MATRIZCOSENOS.append(co)
   u=u+1

print(MATRIZCOSENOS)
print(len(MATRIZCOSENOS))



#trasnpueta de K
    
n=len(K)
print(len(K))
b=[]
B=[]#NUEBA MATRIZ K(TRAASPUESTA)
i=0
j=0
for i in range(n):
    for j in range(n):
        z=K[j][i]
        
        b.append(z)
    
    B.append(b)
    b=[]

print(B)

#multiplicar  B POR MATRIZCOSENOS


i=0
j=0
ALFA=[]
for i in range(len(MATRIZCOSENOS)):
    uni=0
    for j in range(len(B)):
        aux=B[i][j]*MATRIZCOSENOS[i]
        uni=uni+aux
        j=j+1

    ALFA.append(uni)    
    i=i+1

print(ALFA)


i=0
aux=0
suma=0
for i in range(len(ALFA)):
    aux=ALFA[i]
    suma=suma+aux
    i=i+1

print(suma)

#sua es gama y lo vamos a mulriplicar por la densidad y la velocidad
densidad=1.0267
lift=suma*densidad*V
print(lift)

print(len(K),len(K[0]),len(B),)
