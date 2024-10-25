def ultimaPalabra(arreglo,n):
    subArreglo=[]
    k=0
    for i in range(n-1, -1,-1):
        
        if arreglo[i]!=" ":
            subArreglo.append(arreglo[i])
            k+=1
        else:
            break
    cad=""
    for i in range(k-1,-1,-1):
        cad+=subArreglo[i]
    
    return cad
cadena1="Hola Mundo"
cadena2="Estados Unidos Mexicanos"
print(ultimaPalabra(cadena1,len(cadena1)))
print(ultimaPalabra(cadena2,len(cadena2)))