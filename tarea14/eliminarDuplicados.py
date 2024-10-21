 
def eliminarRepetidos(a: list, t: int)-> int:
    #a ->Array
    #t ->Tamaño Array
    i=0
    n=0
    aux=0
    while i<t: #While Elimina repetidos y cuenta elementos unicos
        if i!=t-1:
            if(aux!=a[i]):
                n+=1
                aux=a[i]
            else:
                a[i]=None
        else:
            if aux==a[i]:
                a[i]=None
        i+=1
    
    #print(a)#Descomentar!   
    return n

myArray=[1,2,3,3,3,4,7,7,7,9,11,11,15,15,16,16]
size=len(myArray)
print(f"Cantidad de elementos unicos: {eliminarRepetidos(myArray,size)}")

