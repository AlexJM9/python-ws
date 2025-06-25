


class Mascota: 
    
    def __init__(selft, tipo):
        selft.tipo = tipo
    
    def hablar(selft, nombre):
        print(f"{nombre} no habla")
        
        
class Perro(Mascota):
    def __init__(selft, nombre):
        selft.nombre = nombre  
        
    def hablar(selft, nombre):
        print(f"{selft.nombre} dice guau")  
        
        
class Gato(Mascota):
    def __init__(selft, nombre):
        selft.nombre = nombre
    def hablar(selft, nombre):
        print(f"{nombre} dice miau")  
    
if __name__=="__main__":
    firulais = Perro("canino","campito")
    firulais.hablar()