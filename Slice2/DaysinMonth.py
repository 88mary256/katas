
def month(mes):
    meses = {'Enero': '31', 'Febrero': '28', 'Marzo': '31', 'Abril': '30', 'Mayo': '31', 'Junio': '30', 'Julio': '31',
             'Agosto': '31', 'Septiembre': '30', 'Octubre': '31', 'Noviembre': '30', 'Diciembre': '31'}

    if mes in meses:
        valor = meses.get("Enero")
        valor = meses.get("Febrero")
        valor = meses.get("Marzo")
        valor = meses.get("Abril")
        valor = meses.get("Mayo")
        valor = meses.get("Junio")
        valor = meses.get("Julio")
        valor = meses.get("Agosto")
        valor = meses.get("Septiembre")
        valor = meses.get("Octubre")
        valor = meses.get("Noviembre")
        valor = meses.get("Diciembre")
    print (mes + " tiene " + str(valor) + " dias")
mes = raw_input("Ingrese el mes: ")
month(mes)
