import PySimpleGUI as sg
from Sistema_Experto import Recomendar_Dieta 

# VARIABLES

act1= 'Poco o ningún ejercicio'
act2 = 'Ejercicio ligero (1 a 3 días)'
act3 = 'Ejericio moderado (3 a 5 días)'
act4 = 'Deportista (6 - 7 días)'
act5 = 'Atelta (2 veces por día)'

activites = {
    act1: 1.2,
    act2: 1.375,
    act3: 1.55,
    act4: 1.72,
    act5: 1.9,
}

phys_act = tuple(activites.keys())

sg.theme('DarkAmber')
sg.SetOptions(text_justification='right') 

layout = [

    [sg.Text('Sexo'), sg.Radio('Masculino', 'sexo', size=(8,1), default=True, key='masc'), sg.Radio('Femenino', 'sexo', size=(8,1), key='fem')],
    [sg.Text('Edad (años)'), sg.Spin(values=[i for i in range(1,100)], size=(8,1), initial_value=18, key='edad')],
    [sg.Text('Peso (Kg.)'), sg.Spin(values=[i for i in range(1,300)], size=(8,1), key='peso')],
    [sg.Text('Altura (cm.)'), sg.Spin(values=[i for i in range(1, 250)], size=(8,1),  initial_value=170, key='altura')],
    [sg.Text('Actividad Fisica'), sg.Drop(values=phys_act, auto_size_text=True, default_value=act1, key='act')],

    [sg.Button('Submit'), sg.Button('Cancel')],

    [sg.Multiline(size=(45, 11), key='output'+sg.WRITE_ONLY_KEY)]

]

window = sg.Window('Sistema Experto', layout)

def calc(sexo, edad, peso, altura, act):
    print('sexo: ',sexo)
    print('edad: ',edad)
    print('peso: ',peso)
    print('altura: ',altura)
    print('actividad: ',act)


    result= Recomendar_Dieta(peso, altura, edad, sexo, act)
    #if True:
    #    raise Exception("Error generico")

    return result

def main():
    while True:
        event, values = window.read()
        if event not in (None, 'Cancel'):       
            masc=values['masc']
            fem=values['fem']
            edad=values['edad']
            altura=values['altura']
            peso=values['peso']
            act=values['act']

            sexo=None
            phys=activites.get(act)
            if masc: sexo='Masculino'
            if fem: sexo='Femenino'

            try:
                result= calc(sexo,edad,peso,altura,phys)
                
                for name, cal in result:
                    if type(cal) is int:
                        val = name + '\tCalorias:' + cal
                    else:
                        val = name

                    window['output'+sg.WRITE_ONLY_KEY].print(val)
            except:
                sg.popup("Error!", "Error con los datos")
        else:
            break

    window.close()

if __name__ == '__main__':
    main()