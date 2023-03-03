
def nuevoTema(tema):
    print("\n========", tema,"========\n")

#este es un comentario de una linea


nuevoTema("Operadores aritmeticos ")
print("Operador division entera (10//3):", 10//3)
print("Operador potencia (5**3):", 5**3)



''' este es un
comentario de 
varias lineas '''

nuevoTema("Operadores logicos")
print("Operador and (True and False): ", True and False)

#Actividad: Imprimir la tabla de verdad de los operadores logicos.

print("**And**")
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)

print()
print("**Or**")
print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)

print()
print("**Not**")
print("Not True: ", not True)
print("Not False: ", not False)


print()
nuevoTema("Operadores de comparacion")
print("2==4",2==4)
print("2!=4",2!=4)
print("2<=4",2<=4)
print("2>=4",2>=4)
print("2<4",2<4)
print("2>4",2>4)

nuevoTema("Variable")
variable1=10
_variable2=6.2456
Variable3="juancho"
dosPalabras="hola"
dos_palabras="hello"
print(variable1,_variable2,Variable3,dos_palabras,dosPalabras)

a,b,c=10,5.16,"palabra"
print(a,b,c)

nuevoTema("Enteros")
w=105
x=9898259827985732
y=-256
z=0b00110011
h=0xffa

print(w,type(w))
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(h,type(h))

nuevoTema("Flotantes")
x=1297.5
print(x,type(x))
y=0.5637
print(y,type(y))

nuevoTema("numeros complejos")
x=-46j
y= 12 + 45j
z=2j
print(x,type(x))
print(y,type(y))
print(z,type(z))

nuevoTema("Booleanos")
lis=[8]
print(lis,"es",bool(lis))
new="hello"
print(new,"es",bool(new))
num=99
print(num,"es",bool(num))
comp=1+0j
print(comp,"es",bool(comp))
val=None
print(val,"es",bool(val))

nuevoTema("listas")
a=[10,20.5,"python list"]
print(a)
print(a[1])
a[0]="hola"
print(a)

nuevoTema("tuplas")
t=(25,"tuplas", 1+10j,3.1416)
print(t)
print(t[2])
print("t[0:2]: ", t[0:2])
#t[1]=34, esta operacion no es valida en tuplas

nuevoTema("Conjuntos")
t= {50,20,30,40,10,50}
print("conjunto t= ",t ,type(t) )


nuevoTema("Diccionario")
d= {1:"valor1", "valor2":2}
print(d,type(d))
print("d[valor2]: ", d["valor2"])

nuevoTema("Cadenas")
cadena1= "cadena con comillas dobles"
cadena2= 'cadena con comillas simples'
print(cadena1, type(cadena1))
print(cadena2, type(cadena2) )

cadenaMultilineas='''esta es una cadena     de varias lineas    con 
tabulares y saltos
de
linea'''
print(cadenaMultilineas)
print("segmentacion de cadenas")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1="hola"
cadena4=(cadena1 +" ")*5
print(cadena4)
cadena5= cadena4.upper()
print(cadena5)


