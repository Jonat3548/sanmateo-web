""" 
Nombre: jonathan steven sanchez trilleras 
Tema: 3. punto de parcial validar CORREO PERSONAL 
Fecha: 12/04/2025
Lineas de condigo 8 al 35
Correo: jssanchezt@sanmateo.edu.co
Ej: Calle 45 #12-30 o Carrera 7 No. 80-60.")

"""
import re  

def validar_dirreccion():
    dic = input("Ingrese su dirrecion de de domicilio : ")
    # vamos a validar 
    # 1. calle carrera transversal diagola av
    # 2. numero y letar obcional
    # 3. simbolo # 
    # 4. nuemro con letar obcional seguido - y un numero 

    patron = re.compile(
        r"^(Calle|Carrera|Transversal|Diagonal|Avenida|cll|cr|dig|Av\.?\s?(Calle|Carrera)?)"  
        r"\s?\d+[A-Z]?"                     
        r"(?:\s?#\.?)"                   
        r"\s?\d+[A-Z]?[-]?\d*$",            
        re.IGNORECASE                      
    )

    if patron.match(dic):
        print("la dirrecion de domicielio es correcta.")
    else:
        print("a dirrecion de domicielio es incorrecta ingrese bien los parametros .")
def main():
    validar_dirreccion()
if __name__ == '__main__':
    main()