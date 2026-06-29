def un_decorador(func):

    def envoltura():

        print("pan arriba")

        func() # Llama a la función original que fue pasada a mi_primer_decorador'

        print("pan abajo")

    return envoltura # Retorna la función 'envoltura'

 

# Ahora, definimos una función y la "decoramos"

@un_decorador

def salchicha():

    print("slchicha")

    # Llamamos a la función decorada

salchicha()