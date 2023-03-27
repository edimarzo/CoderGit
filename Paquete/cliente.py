class cliente:
  #Para el alta de los clientes debe ingresarse un nombre, un apellido, un dni y una diracción.

  #Creamos un diccionario con los productos que el cliente agregará al carrito de su compra.
  productos = {}


  # En la variable total parcial guardaremos el monto correspondiente a lo que progresivamente vaya agregando al carrito.
  totalparcial = 0

  def __init__(self, nombre,apellido,dni,direccion):
    #Cargamos los datos del cliente
    self.nombre = nombre.capitalize()
    self.apellido = apellido.capitalize()
    self. dni = dni
    self.direccion = direccion.capitalize()
    

  def agregar_productos(self,producto,precio,cantidad):
    # A través de este método sumaremos los productos al carrito. Debemos detallar, el producto, su precio y las cantidades.

    precio = int(precio)
    cantidad = int(cantidad)

    self.productos[producto] = int(precio) * int(cantidad)
  
  def __iter__(self):
    for producto in self.productos:
      yield producto

  def subtotal(self):
    # Con el método subtotal podremos ver el listado de lo que lleva gastado por cada producto y una leyenda donde indica el total.
    self.totalparcial = 0
    for x,y in self.productos.items():

      print(str(x)+'----$'+str(y))
      y = int(y)
      self.totalparcial = self.totalparcial + y

    print('El cliente debe un total de '+ str(self.totalparcial) +' pesos')


  def __str__(self):
    # Con este método podremos imprimir el nombre, apellido y el total que lleva acumulado el cliente.
    return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nTotal: {self.totalparcial}'.__str__()