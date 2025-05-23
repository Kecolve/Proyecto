import unittest
import main

class TestCRUDProductos(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba. Limpia la 'base de datos'."""
        main.guardar_productos([])

    # -------- CREAR --------
    def test_crear_producto_exitoso(self):
        producto = {
            "id": 1,
            "nombre": "Monitor",
            "descripcion": "Monitor LED 24 pulgadas",
            "precio": 500.0,
            "cantidad": 10
        }
        main.crear_producto(producto)
        productos = main.cargar_productos()
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0]["nombre"], "Monitor")

    def test_crear_producto_duplicado(self):
        producto = {"id": 1, "nombre": "Teclado", "descripcion": "RGB", "precio": 100.0, "cantidad": 5}
        main.crear_producto(producto)
        with self.assertRaises(ValueError):
            main.crear_producto(producto)

    # -------- LEER --------
    def test_leer_producto_exitoso(self):
        producto = {"id": 2, "nombre": "Mouse", "descripcion": "Inalámbrico", "precio": 60.0, "cantidad": 15}
        main.crear_producto(producto)
        resultado = main.leer_producto(2)
        self.assertEqual(resultado["nombre"], "Mouse")

    def test_leer_producto_inexistente(self):
        with self.assertRaises(ValueError):
            main.leer_producto(99)

    # -------- ACTUALIZAR --------
    def test_actualizar_producto_exitoso(self):
        producto = {"id": 3, "nombre": "Webcam", "descripcion": "HD", "precio": 200.0, "cantidad": 8}
        main.crear_producto(producto)
        main.actualizar_producto(3, {"precio": 180.0})
        actualizado = main.leer_producto(3)
        self.assertEqual(actualizado["precio"], 180.0)

    def test_actualizar_producto_inexistente(self):
        with self.assertRaises(ValueError):
            main.actualizar_producto(999, {"precio": 100.0})

    # -------- ELIMINAR --------
    def test_eliminar_producto_exitoso(self):
        producto = {"id": 4, "nombre": "Tablet", "descripcion": "Android", "precio": 700.0, "cantidad": 3}
        main.crear_producto(producto)
        main.eliminar_producto(4)
        with self.assertRaises(ValueError):
            main.leer_producto(4)

    def test_eliminar_producto_inexistente(self):
        with self.assertRaises(ValueError):
            main.eliminar_producto(888)

if __name__ == "__main__":
    unittest.main()
