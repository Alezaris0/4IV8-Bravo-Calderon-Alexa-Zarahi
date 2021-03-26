import factura
opcion = 0
while opcion != 3:
    print("Solo se puede escoger del 1 al 3.")
    print("1.-Agregar factura")
    print("2.-Pagar facturas")
    print("3.-Salir")
    opcion = int(input())
    if opcion == 1:
        factura.agrfactura()
    elif opcion == 2:
        print("Ingrese su num de factura")
        factura=int(input())
        factura.cobroFact(factura)