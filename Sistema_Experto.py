from kanren import *
import pandas as pd
import random as rn

Recomendacion = []
TotalCal = 0


ArchCalorias = pd.read_excel('Calorias.xlsx')
ArchTipo = pd.read_excel('TipoM.xlsx')


P1 = ArchCalorias['Platos'].values
C1 = ArchCalorias['Calorías(kcal)'].values


P2 =  ArchTipo['Platos'].values
T2 = ArchTipo['Tipo'].values


#base de conocimiento
PL = var()
CA = var()
T = var()

Calorias = Relation()
EsTipo = Relation()

Plato = 'Empanada de carne'




for i in range(len(P1)):
    fact(Calorias,P1[i],C1[i])
#print(run(0,(Plato,CA),Calorias(Plato,CA)))


for i in range(len(P2)):
    fact(EsTipo,P2[i],T2[i])
#print(run(0,(PL,T),EsTipo(PL,T)))


#Te devuelve un tipo lista
a = run(0,(CA),Calorias(Plato,CA))


Tipo1 = "Desayuno"
desayuno = run(0,(PL,CA),Calorias(PL,CA),EsTipo(PL,Tipo1))


Tipo2 = "Almuerzo"
almuerzo = run(0,(PL,CA),Calorias(PL,CA),EsTipo(PL,Tipo2))


Tipo3 = "Cena"
cena = run(0,(PL,CA),Calorias(PL,CA),EsTipo(PL,Tipo3))








def Generar_Dieta():
    global TotalCal 
    global Recomendacion
    Recomendacion = []
    TotalCal = 0
    r1 = rn.randint(0,len(desayuno)-1)
    r2 = rn.randint(0,len(desayuno)-1)
    r3 = rn.randint(0,len(almuerzo)-1)
    r4 = rn.randint(0,len(desayuno)-1)
    r5 = rn.randint(0,len(cena)-1)

    Recomendacion.append(('DESAYUNO', '\n'))
    Recomendacion.append(desayuno[r1])
    Recomendacion.append(desayuno[r2])
    Recomendacion.append(('\nALMUERZO', '\n'))
    Recomendacion.append(almuerzo[r3])
    Recomendacion.append(almuerzo[r4])
    Recomendacion.append(('\nCENA', '\n'))
    Recomendacion.append(cena[r5])

    for i in Recomendacion:
        if type(i[1]) is not str:
            TotalCal = TotalCal + i[1]



def Recomendar_Dieta(peso, altura, edad, sexo, actividad):
    global TotalCal
    if sexo == 'Masculino':
        TMB = 66 + (13.7 * peso) + (5 * altura) - (6.75 * edad)
    else:
        TMB = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad)
    print("Calorias Maximas: ",TMB)

    TMB = TMB * actividad
    
    while TotalCal > TMB + 100 or TotalCal < TMB - 400:
        Generar_Dieta()
    print("Total Calorias en las comidas:", TotalCal)
    return Recomendacion



print(Recomendar_Dieta(90, 182, 19, 'Masculino',1))





