def CDT(usuario=str, monto=int, tiempo=int):
    if tiempo >2:
        valorintereses=(monto*0.03*tiempo)/12
        valorTotal= valorintereses + monto 
        return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {monto} para un tiempo de {tiempo} meses es: {valorTotal}") 
    if tiempo <=2:
        valorperdida= (monto * 0.02)
        valorTotal= monto-valorperdida
        return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {monto} para un tiempo de {tiempo} meses es: {valorTotal}") 