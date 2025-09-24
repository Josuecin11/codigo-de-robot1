# Clase base
class Robot:
    """
    Clase que representa un robot genérico.
    Tiene un nombre y un nivel de batería.
    """

    def _init_(self, nombre, bateria=100):
        self.nombre = nombre
        self.bateria = bateria
        self.encendido = False

    def encender(self):
        if self.bateria > 0:
            self.encendido = True
            print(f"{self.nombre} está encendido.")
        else:
            print(f"{self.nombre} no puede encenderse: batería agotada.")

    def apagar(self):
        self.encendido = False
        print(f"{self.nombre} se apagó.")

    def describir(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"Robot {self.nombre} | Batería: {self.bateria}% | Estado: {estado}"

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
# Subclase 2: RobotDomestico -> renombrado a OptimusPrime (líder, hace "tareas")
class RobotLider(Robot):
    """
    Robot líder que organiza y ejecuta tareas.
    Hereda de Robot y añade una lista de misiones.
    """

    def _init_(self, nombre, bateria=100):
        super()._init_(nombre, bateria)
        self.misiones = []

    def asignar_mision(self, mision):
        if self.encendido and self.bateria > 0:
            self.misiones.append(mision)
            self.bateria = max(0, self.bateria - 10)
            print(f"{self.nombre} completó la misión: {mision}")
        else:
            print(f"{self.nombre} no puede realizar misiones (apagado o sin batería).")

    def describir(self):
        estado = "encendido" if self.encendido else "apagado"
        return (f"RobotLider {self.nombre} | "
                f"Misiones cumplidas: {len(self.misiones)} | "
                f"Batería: {self.bateria}% | Estado: {estado}")

# Subclase 3: RobotGuerrero -> T-800 (Terminator)
class RobotGuerrero(Robot):
    """
    Robot de combate inspirado en T-800.
    Hereda de Robot y añade contador de objetivos neutralizados.
    """

    def __init__(self, nombre, bateria=100):
        super().__init__(nombre, bateria)
        self.objetivos = 0

    def atacar(self, enemigo):
        if self.encendido and self.bateria > 0:
            self.objetivos += 1
            self.bateria = max(0, self.bateria - 20)
            print(f"{self.nombre} neutralizó al objetivo: {enemigo}")
        else:
            print(f"{self.nombre} no puede atacar (apagado o sin batería).")

    def describir(self):
        estado = "encendido" if self.encendido else "apagado"

    # ------------------ PRUEBAS ------------------

# Creamos los robots con nombres icónicos
robot1 = Robot("R2D2", bateria=80)            # Robot genérico
robot2 = RobotMovil("Wall-E", bateria=50)     # Robot móvil
robot3 = RobotLider("OptimusPrime", bateria=70)  # Robot líder
robot4 = RobotGuerrero("T-800", bateria=90)      # Robot guerrero

# Probamos sus métodos
robot1.encender()
print(robot1.describir())

robot2.encender()
robot2.mover(3, 4)
print(robot2.describir())

robot3.encender()
robot3.asignar_mision("Proteger a los Autobots")
robot3.asignar_mision("Defender la Tierra")
print(robot3.describir())

robot4.encender()
robot4.atacar("John Connor")
robot4.atacar("Policía T-1000")
print(robot4.describir())

# Polimorfismo: lista de robots
robots = [robot1, robot2, robot3, robot4]
print("\n--- Estado de todos los robots ---")
for r in robots:
    print(r.describir())
        return (f"RobotGuerrero {self.nombre} | "
                f"Objetivos neutralizados: {self.objetivos} | "
                f"Batería: {self.bateria}% | Estado: {estado}")

