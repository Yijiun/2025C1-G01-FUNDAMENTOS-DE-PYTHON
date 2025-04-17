import csv, os, pandas as pd



def ingresar_ventas(lista_ventas):
    while True:
        try:
            curso =  input('Ingrese el nombre del curso:').upper()
            cantidad = int(input('Ingrese la cantidad de curso vendido:'))
            fecha = input('Ingrese la fecha de la venta (AAAA-MM-DD): ')
            precio = float(input('Ingrese el precio del curso:'))
            cliente = input('Ingrese el nombre del cliente').upper()
        except ValueError:
            print('Entradas no validas')
            continue
        
        venta ={
            'curso': curso,
            'cantidad': cantidad,
            'precio' : precio,
            'fecha' : fecha,
            'cliente': cliente
        }
        lista_ventas.append(venta)
            
        continuar = input('Desea ingresar otra venta s/n').lower()
        if continuar == 's':
            print('\n ---- Ingresando otra venta ----')
        elif continuar == 'n':
            break
        else:
            print('Opcion no valida')
            
def guardar_ventas(ventas):
    if not ventas:
        print('No hay ventas que guardar en el CSV')
    else:
        if os.path.exists('ventas.csv'):
            #Si el archvo existe agrego Append
             with open('ventas.csv','a',newline='',encoding='utf-8') as archivo:
                guardar =csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha', 'cliente'])
                guardar.writerows(ventas)
        else: #Si no existe abro en modo escritura 'w'
            with open('ventas.csv','w',newline='',encoding='utf-8') as archivo:
                guardar =csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha', 'cliente'])
                guardar.writeheader()
                guardar.writerows(ventas)
        #limpio las ventas en memoria y muestro el guardado exitoso        
        ventas =[]
        print('Datos guardados exitosamente!')
        
def analisis_venta():
    df = pd.read_csv('ventas.csv')
    print('\n ------------ RESUMEN VENTAS ---------')
    
    
    df['subtotal'] = df['cantidad'] * df['precio']
    total_ingresos = df['subtotal'].sum()
    
    #total de ventas
    print(f'Total de ventas{total_ingresos:.2f}')
    
    #Curso mas vendido
    curso_top = df.groupby('curso')['cantidad'].sum().idxmax()
    print('El curso mas vendido es ', curso_top)
        
    #Cliente con mas compras
    cliente_compra_mayor = df.groupby('cliente')['cantidad'].count().idxmax()
    print('El cliente con mayor compra es: ', cliente_compra_mayor)
    
    #Ventas por fecha
    venta_por_fecha = df.groupby('fecha')['cantidad'].sum()
    print(venta_por_fecha)