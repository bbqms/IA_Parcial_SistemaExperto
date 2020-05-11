from kanren import *
import pandas as pd

ArchIngrediente = pd.read_excel('Ingredientes.xlsx')
ArchTipo = pd.read_excel('Tipo.xlsx')
ArchBueno = pd.read_excel('Bueno.xlsx')

P1 = ArchIngrediente['Producto_I'].values
M1 = ArchIngrediente['Menu_I'].values


M2 = ArchTipo['Menu_T'].values
T2 = ArchTipo['Tipo_T'].values

P3 = ArchBueno['Producto_B'].values
E3 = ArchBueno['Enfermedad_E'].values

#base de conocimiento

Ingreso = var()
E = var()
T = var()
P = var()
M = var()
A = var()
Ingrediente = Relation()
Estipo = Relation()
Bueno = Relation()
Prueba = Relation()

for i in range(len(P1)):
    fact(Ingrediente,P1[i],M1[i])
#print(run(0,(P,E),Ingrediente(P,E)))

for i in range(len(M2)):
    fact(Estipo,M2[i],T2[i])
#print(run(0,(P,E),Estipo(P,E)))

for i in range(len(P3)):
    fact(Bueno,P3[i],E3[i])
#print(run(0,(P,E),Bueno(P,E)))

Enfermedad = "stress"

# REGLQAS DE MOTOR DE INFERENCIAS
print(run(0,(Enfermedad,T,M),Bueno(A,Enfermedad), Ingrediente(A,M),Estipo(M,T)))

## todo alimento es bueno para alguna enfermedad y este alimento es ingrediente de algun menu y el menu es un tipo de plato que se puede servir
## para todo A, Existe enfermedad, Existe M, Existe T [Bueno(A,Enfermedad) y Ingrediente(A,M) y Estipo(M,T)=> (T,M)]