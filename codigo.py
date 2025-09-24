# Subclase 1: RobotMovil
class RobotMovil(Robot):
    """
    Robot que puede moverse en un plano 2D.
    Hereda de Robot y añade atributos x, y.
    """

    def _init_(self, nombre, bateria=100, x=0, y=0):
        super()._init_(nombre, bateria)
        self.x = x
        self.y = y

    def mover(self, dx, dy):
        if self.encendido and self.bateria > 0:
            self.x += dx
            self.y += dy
            self.bateria = max(0, self.bateria - 10)
            print(f"{self.nombre} se movió a ({self.x}, {self.y}).")
        else:
            print(f"{self.nombre} no puede moverse (apagado o sin batería).")

    def describir(self):
        estado = "encendido" if self.encendido else "apagado"
        return (f"RobotMovil {self.nombre} | Posición: ({self.x}, {self.y}) | "
                f"Batería: {self.bateria}% | Estado: {estado}")
