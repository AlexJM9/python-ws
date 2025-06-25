# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre         # nombre del producto (ej: Pan)
        self.precio = float(precio)  # precio por unidad
        self.stock = int(stock)      # unidades disponibles

    # Muestra la información del producto
    def mostrar_info(self):
        print(f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")

    # Actualiza el stock sumando o restando la cantidad
    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    # Vende una cantidad del producto si hay suficiente stock
    def vender(self, cantidad):
        if cantidad <= self.stock:
            total = self.precio * cantidad
            self.stock -= cantidad
            return f"Total a pagar: ${total:.2f}"
        else:
            return f"No hay suficiente stock de {self.nombre}."


# Clase Tienda: representa una tienda que contiene varios productos
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre         # nombre de la tienda
        self.productos = []          # lista de productos disponibles

    # Agrega un producto a la tienda
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Lista todos los productos disponibles
    def listar_productos(self):
        print("Productos disponibles:")
        for produdispo in self.productos:
            print(produdispo.nombre, "- Precio: $", produdispo.precio, "- Stock:", produdispo.stock)


    # Vende un producto por nombre, si está disponible
    def vender_producto(self, nombre_producto, cantidad):
        for p in self.productos:
            if p.nombre.lower() == nombre_producto.lower():
                print("Vendiendo", cantidad, p.nombre)
                print(p.vender(cantidad))
                return
        print("El producto no está en la tienda.")


# Bloque principal: crea tienda, agrega productos y simula una venta
if __name__ == "__main__":
    # Crear tienda
    tienda = Tienda("Super Market")

    # Crear productos
    pan = Producto("Pan", 0.50, 20)
    jugo = Producto("Jugo", 1.25, 10)

    # Agregar productos a la tienda
    tienda.agregar_producto(pan)
    tienda.agregar_producto(jugo)

    # Mostrar productos disponibles
    tienda.listar_productos()

    # Simular una venta
    tienda.vender_producto("Jugo", 3)

    # Mostrar el stock actualizado
    print("\nStock actualizado:")
    jugo.mostrar_info()
