import json

def archivos():
    with open('biblioteca.json', mode= 'r')as archivos:
        datos = archivos
        datos = json.load(archivos)
    return(datos)

def buscar_autor(datos):
    """ ID_autor = input('ingrese un autor a buscra: ') """
    for dato in datos['Autor']:
        datos = dato
        print(datos)
        

def Agrear_Autor(datos):
    autor_id = int(input('ingrese una id: '))
    nombre = input('ingrese un nombre: ')
    nacionalidad = input('ingrese su nacionalidad: ')

    for dato in datos['Autor']:
        
        dicionario = {
            'id':autor_id,
            'Nombre':nombre,
            'Nacionalidad':nacionalidad
            }
    datos['Autor'].append(dicionario)
    return(datos)

def eliminar_autor(datos):
    autor_eliminar = input('ingrese un id a eliminar: ')
    for dato in datos['Autor']:
        if dato['AutorID'] == autor_eliminar:
            datos['Autor'].remove(dato)
        return(datos)
        
def editar_autor(datos):
    buscar_id = int(input('ingrese una id: '))
    nombre = input('ingrese un nombre: ')
    nacionalidad = input('ingrese su nacionalidad: ')

    for dato in datos['AutorID']:
        if dato['AutorID'] == buscar_id:
            dato['Nombre'] = nombre
            dato['Nacionalidad'] = nacionalidad
            print(datos)
    return


datos = archivos()
#editar_autor(datos)
eliminar_autor(datos)
buscar_autor(datos)


#__________________
Agrear_Autor(datos)
buscar_autor(datos)


