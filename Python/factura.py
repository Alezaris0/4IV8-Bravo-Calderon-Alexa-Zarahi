def agrfactura():
    liFact = {}
    print("Ingrese el num de factura:")
    facturas = int(input())
    print("Ingrese el costo de la factura:")
    cobro = int(input())
    liFact["Num de factura"] = facturas
    liFact["Costo de la factura"] = cobro
    listFactura.append(liFact)
    print(("Numero de factura: ") + str(facturas) + " Se cobrará: " + str(cobro))


def cobroFact(no):
    print("Ingrese su num de factura")
    for x in listFactura:
        if x["Num de la factura"] == no:
            listFactura.remove(x)
            print("Cobro realizado")
        else:
            print("Num de factura no existente")