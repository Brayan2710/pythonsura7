#Crear un menu de empandas inteligentes
print("1.Agregar Empanada")
print("2.Mostrar empanadas ")
print("3. Salir")
menu=0
Empanadas=[]
while(menu!=3):
    empanada={}
    Ingredientes=[]
    menu=int(input("Ingrese la opcion"))
    if(menu==1):
        empanada['Nombre']=input("Ingrese el nombre de la empanada")
        for i in range (3):
            Ingredientes.append(input("Digite ingrediente"))
   
        empanada['Ingredientes']=Ingredientes
        empanada['precio']=int(input("Ingrese  el precio "))
        Empanadas.append(empanada)
    elif(menu==2):
        print(Empanadas)
    elif(menu==3):
        print("Salir")
        break
    else:
        print("Opcion No valida")       



        
        
        

    

