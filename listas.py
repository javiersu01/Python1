#Crea una lista llamada elementos
#introduce los siguientes valores 
#1 - "madrid" - True - 19.95
#¿es posible introducir de diferentes tipos de datos?
#Muestra por consola, el segundo elemento. Debe salir madrid
#Muestra por consola, el último elemento. Debe salir 19.95

#Muestra por consola todos los elementos con la frase
#el elemento x es tal

#Añade sevilla
#dónde se añade?
#vuelve a mostar la lista por consola. usando funciones.


elementos=['1',"madrid",'True','19.95']
print(elementos)
print(elementos[1])
print(elementos[-1])
            

    #eg
            
def mostrar():
        for elemento in elementos:
            print(f'el elemento{elemento} su valor es {elemento}')
    
mostrar()


elementos.append("sevilla")
mostrar()
     

#collections (3)
#list: datos que pueden repetirse y en orden: numero de telf
#set : datos sin repeticion y sin orden: numero de loteria
#Map(dictionary) : k,v :nif alumno  -  nota media