#Modificar_Dictionaries_Tarea
mi_inventario=[
    {"id":"lapiz","cantidad":50,"precio":5},
    {"id":"libreta","cantidad":40,"precio":20},
    {"id":"borrador","cantidad":30,"precio":3}
]

def delete_producto(inventario,producto):
    for dict_aux in inventario:
        if dict_aux["id"]==producto:
            inventario.remove(dict_aux)
            return
def actualizar_stock(inventario,producto,cantidad):
    for dict_aux in inventario:
        if dict_aux["id"]==producto:
            dict_aux["cantidad"]=cantidad
            return
def cambiar_precio(inventario,producto,new_price):
    for dict_aux in inventario:
        if dict_aux["id"]==producto:
            dict_aux["precio"]=new_price
            return
        
delete_producto(mi_inventario,"lapiz")
actualizar_stock(mi_inventario,"libreta",80)
cambiar_precio(mi_inventario,"borrador",6)

print("\nEl inventario con los cambios realizados es:",mi_inventario)
