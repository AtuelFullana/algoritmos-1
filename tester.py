class Persona:
    def __init__(self, nombre, hijos=None):
        self.nombre = nombre
        self.hijos = hijos if hijos is not None else []

    def obtener_hijos(self):
        return self.hijos


def contar_descendientes(persona):
    hijos = persona.obtener_hijos()
    descendientes = len(hijos)
    print(descendientes,"descencientes")

    for hijo in hijos:
        descendientes += contar_descendientes(hijo)
    
    print(descendientes)

    return descendientes

# Crear instancias de Persona
juan = Persona("Juan")
ana = Persona("Ana")
carlos = Persona("Carlos", [juan, ana])
maria = Persona("Maria")
luisa = Persona("Luisa", [carlos, maria])

# Contar descendientes de Luisa
total_descendientes = contar_descendientes(luisa)
print("Total de descendientes de Luisa:", total_descendientes)

