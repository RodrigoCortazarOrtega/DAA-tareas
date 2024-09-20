def sum_pares(m):
    s=0
    for sub_m in m:  
        for i in sub_m:
            if i%2==0:
                s+=i
    return s


matriz = [[1,2,3],[4,5,6],[7,8,9]] # Matriz para ejemplo
print("Suma: ",sum_pares(matriz))
