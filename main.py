import json
import os

# Nombre del archivo donde se almacenarán los productos
ARCHIVO = "productos.json"

def cargar_productos():
    """Carga los productos desde el archivo JSON."""
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, 'r') as f:
        return json.load(f)

def guardar_productos(productos):
    """Guarda la lista de productos en el archivo JSON."""
    with open(ARCHIVO, 'w') as f:
        json.dump(productos, f, indent=4)

# Operaciones del CRUD

def crear_producto(producto):
    """Agrega un nuevo producto si el ID no está duplicado."""
    productos = cargar_productos()
    if any(p['id'] == producto['id'] for p in productos):
        raise ValueError("Ya existe un producto con ese ID.")
    productos.append(producto)
    guardar_productos(productos)

def leer_producto(id):
    """Devuelve un producto por su ID."""
    productos = cargar_productos()
    for p in productos:
        if p['id'] == id:
            return p
    raise ValueError("Producto no encontrado.")

def actualizar_producto(id, nuevos_datos):
    """Actualiza los datos de un producto existente por ID."""
    productos = cargar_productos()
    for i, p in enumerate(productos):
        if p['id'] == id:
            productos[i].update(nuevos_datos)
            guardar_productos(productos)
            return
    raise ValueError("Producto no encontrado para actualizar.")

def eliminar_producto(id):
    """Elimina un producto por su ID."""
    productos = cargar_productos()
    nuevos_productos = [p for p in productos if p['id'] != id]
    if len(productos) == len(nuevos_productos):
        raise ValueError("Producto no encontrado para eliminar.")
    guardar_productos(nuevos_productos)
