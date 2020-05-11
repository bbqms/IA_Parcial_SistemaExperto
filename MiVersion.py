from kanren import *
import pandas as pd


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
print(run(0,(Plato,CA),Calorias(Plato,CA)))


for i in range(len(P2)):
    fact(EsTipo,P2[i],T2[i])
print(run(0,(PL,T),EsTipo(PL,T)))


print(run(0,(Plato,CA,T),Calorias(Plato,CA), EsTipo(Plato,T)))

#Te devuelve un tipo lista
a = run(0,(CA),Calorias(Plato,CA))








peso = 90
altura = 180
edad = 19

#Hombres: 
TMB = 66 + (13.7 * peso) + (5 * altura) - (6.75 * edad)

#Mujeres
#Mujeres: TMB = 655 + (9.6 * peso) + (1.8 x altura) - (4.7 x edad)

#TMB x 1,2: Poco o ningún ejercicio
#TMB x 1,375: Ejercicio ligero (1 a 3 días a la semana)
#TMB x 1,55: Ejercicio moderado (3 a 5 días a la semana)
#TMB x 1,72: Deportista (6 -7 días a la semana)
#TMB x 1,9: Atleta (Entrenamientos mañana y tarde)


print( 5 + a[0])

print(TMB)





"""for i in range(len(P1)):
    fact(Ingrediente,P1[i],M1[i])
print(run(0,(P,E),Ingrediente(P,E)))

for i in range(len(M2)):
    fact(Estipo,M2[i],T2[i])
print(run(0,(P,E),Estipo(P,E)))

for i in range(len(P3)):
    fact(Bueno,P3[i],E3[i])
print(run(0,(P,E),Bueno(P,E)))"""

#Enfermedad = "stress"

# REGLQAS DE MOTOR DE INFERENCIAS
#print(run(0,(Enfermedad,T,M),Bueno(A,Enfermedad), Ingrediente(A,M),Estipo(M,T)))

## todo alimento es bueno para alguna enfermedad y este alimento es ingrediente de algun menu y el menu es un tipo de plato que se puede servir
## para todo A, Existe enfermedad, Existe M, Existe T [Bueno(A,Enfermedad) y Ingrediente(A,M) y Estipo(M,T)=> (T,M)]