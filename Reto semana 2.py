def cliente (informacion:dict)-> dict:
    if informacion ['edad']>18:
        atraccion="X-Treme"
        apto= True
        if informacion ['primer_ingreso'] == True: 
            total_boleta= 20000-(20000*0.05)
        else:
            total_boleta= 20000   
   
    elif informacion['edad']>=15 and informacion['edad']<=18:
        atraccion="Carros chocones"
        apto=True
        if informacion ['primer_ingreso'] == True: 
            total_boleta= 5000-(5000*0.07)
        else:
            total_boleta= 5000 
        
    elif informacion['edad']>=7 and informacion['edad']<=15:
        atraccion= "Sillas voladoras"
        apto=True
        if informacion ['primer_ingreso'] == True: 
            total_boleta= 10000-(10000*0.05)
        else:
            total_boleta= 10000 
            
    else:
        atraccion = 'N/A'
        total_boleta='N/A'
        apto=False 

    diccionario_resultado= {}

    diccionario_resultado ['nombre'] = informacion ['nombre'] 
    diccionario_resultado ['edad'] = informacion ['edad']
    diccionario_resultado ['atraccion'] = atraccion
    diccionario_resultado ['apto'] = apto
    diccionario_resultado ['primer_ingreso'] = informacion ['primer_ingreso']
    diccionario_resultado ['total_boleta'] = total_boleta
         
    return diccionario_resultado

informacion1= {'id_cliente':1, 'nombre': 'Johana Fernandez', 'edad': 20, 'primer_ingreso': True}

print(cliente(informacion1))

#informacion= {'nombre': 'Johana Fernandez', 'edad': 20, 'atraccion': 'X-Treme','apto': True, 'primer_ingreso': False, 'total_boleta': 20000}
#informacion= {'nombre': 'Gloria Suarez', 'edad': 3, 'atraccion': 'N/A', 'apto': False,'primer_ingreso': True, 'total_boleta': 'N/A'}
#informacion= {'nombre': 'Tatiana Suarez', 'edad': 17, 'atraccion': 'Carros_chocones', 'apto': True, 'primer_ingreso': True, 'total_boleta':4650.0} 
#informacion= {'nombre': 'Tatiana Suarez', 'edad': 17, 'atraccion': 'Carros_chocones', 'apto': True, 'primer_ingreso': False, 'total_boleta': 5000}
#informacion= {'nombre': 'Tatiana Ruiz', 'edad': 8, 'atraccion': 'Sillas voladoras','apto': True, 'primer_ingreso': True, 'total_boleta': 9500.0}
#informacion= {'nombre': 'Tatiana Ruiz', 'edad': 8, 'atraccion': 'Sillas voladoras','apto': True, 'primer_ingreso': False, 'total_boleta': 10000}

