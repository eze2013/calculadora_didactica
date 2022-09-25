from logging import exception
from datetime import datetime

print ("CALCULADORA DIDACTICA" .center(60,"*"))
hora = datetime.now()
print (f"hola me llamo Ezequiel hoy es {hora} y esa es la hora")
print ("la idea es jugar un rato con numeros")
a = input ("cual es tu nombre?:   ")
ap = input ("y cual tu apellido?:  ")
print("genial!!  ")
print ( a.capitalize() , ap.capitalize() )
print ("veamos", a.capitalize() )
print("¿ juguemos al mayor y menor ?"  )
try:
    x = int(input ("si queres jugar escribi 1 ...  " ))
except Exception as e:
    print("no escribiste un numero","vamos a otra cosa")
else:
    if x == 1:
        print ("haber si sabes cual es el numero mayor y cual el menor")
        num1 = int( input ("escribi el primer numero:  "   ))
        num2 = int( input ("a ver ahora el segundo numero:  "))
        num3 = int( input ("tu ultimo numero sera :  "))
        S = max (num1 , num2, num3)
        I = min (num1 , num2, num3)
        print("el numero mayor es:  ", S)    
        print("y el menor es:  ", I)
        print ("adivinaste?.... espero que si!!")
    else:
        print("bueno si no queres vamos a otra cosa")
adivina = int (input ("ahora veamos si sos adivino advina que numero estoy pensando entre 0 y 10:  "))
list_numsecreto = [0,1,2,3,4,5,6,7,8,9,10]
from random import choice
num_secreto = choice(list_numsecreto)
while (num_secreto != adivina):
    adivina = int ( input ( "jaja no adivinaste!!! a ver otra oportunidad : " ))
print ("si le adivinaste!!!")
print("bueno queres que veamos que tal andas para las cuentas: ")
print("a ver", a.capitalize() )
print("te doy las opciones vos decime cual queres hacer")
print("""
..: Elegi cual queres del siguiente Menu :..
1 - Sumar
2 - Restar
3 - Multiplicar
4 - Dividir
5 - Ninguna
""")
opcion = int(input("elije cual de las anteriores queres hacer: "))
if opcion == 1:
    num_sumados = int(input("dime cuantos numeros quieres sumar:  "))
    lst_sum = []
    while len(lst_sum) < num_sumados:
        suma = int(input("escribe tu numero: "))
        lst_sum.append(suma)
    print("los numeros a sumar entonces son: ", lst_sum)
    resultado = sum(lst_sum)
    print("El resultado de la suma es: ", resultado)
elif opcion == 2 :
    nr = int(input("Escribe el numero al que vas a restarle loa otros:  "))
    num_a_restar = int(input("Ahora escribe cuantos numeros vas a restarle al numero anterior:  "))
    lst_resta = []
    while len(lst_resta) < num_a_restar:
        resta = int(input("Escribe el primer numero que vas a usar para restar:  "))
        lst_resta.append(resta)
    print(f"Entonces a {nr} le vas a restar los siguientes numeros:  ", lst_resta)
    rst = sum(lst_resta)
    resultado = nr - rst
    print("El resultado de la resta es : ", resultado)
elif opcion == 3 :
    n1 = int(input("escribi el primer numero a multiplicar: "))
    n2 = int(input("escribe el segundo numero: "))
    resultado = n1 * n2
    print("el resultado de la multiplicacion es: ", resultado)
elif  opcion == 4 :
    n1 = int(input("escribe el primer numero de dividir: "))
    n2 = int(input("escribe el segundo numero: "))
    resultado = n1 / n2
    print("el resultado de la division es: ", resultado)
elif  opcion == 5 :
    print("no quisiste hacer nada jaja")
else:
    print("escribiste cualquiera")    
print("PROGRAMA TERMINADO AL MOMENTO")        




    
    

