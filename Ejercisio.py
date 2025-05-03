import random 

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.p_ganados = 0
        self.p_perdidos = 0
        self.sets_ganados = 0

    def reiniciar_sets(self):
        self.sets_ganados = 0

class TorneoVoley:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    def generar_puntos_set(self):
        return random.randint(10, 28)

    def sumar_puntos_extra(self):
        return random.randint(0, 6)

    def actualizar_set(self, quien_gano):
        ganador = self.equipo1 if quien_gano == 1 else self.equipo2
        perdedor = self.equipo2 if quien_gano == 1 else self.equipo1

        ganador.sets_ganados += 1

        if ganador.sets_ganados == 3:
            ganador.p_ganados += 1
            perdedor.p_perdidos += 1

    def jugar_p(self):
        print("\n*** Inicia un nuevo partido ***")
        while self.equipo1.sets_ganados < 3 and self.equipo2.sets_ganados < 3:
            pa = self.generar_puntos_set()
            pb = self.generar_puntos_set()

            print(self.equipo1.nombre + ": " + str(pa) + " pts | " + self.equipo2.nombre + ": " + str(pb) + " pts")

            if pa >= 25 or pb >= 25:
                if pa > pb:
                    print("Set para " + self.equipo1.nombre)
                    self.actualizar_set(1)
                elif pb > pa:
                    print("Set para " + self.equipo2.nombre)
                    self.actualizar_set(2)
                else:
                    print("Empate en el set, se repite")
            else:
                while pa <= 25 and pb <= 25:
                    pa += self.sumar_puntos_extra()
                    pb += self.sumar_puntos_extra()
                    print("Puntos extra -> " + self.equipo1.nombre + ": " + str(pa) + ", " + self.equipo2.nombre + ": " + str(pb))
                if pa > pb:
                    print("Set para " + self.equipo1.nombre)
                    self.actualizar_set(1)
                else:
                    print("Set para " + self.equipo2.nombre)
                    self.actualizar_set(2)

        self.equipo1.reiniciar_sets()
        self.equipo2.reiniciar_sets()

    def ver_resultados(self):
        print("\n**** Resultados del Torneo ***")
        print(self.equipo1.nombre + " → Ganados: " + str(self.equipo1.p_ganados) + " | Perdidos: " + str(self.equipo1.p_perdidos))
        print(self.equipo2.nombre + " → Ganados: " + str(self.equipo2.p_ganados) + " | Perdidos: " + str(self.equipo2.p_perdidos))

def inicio():
    print("Simulador de partidos de Vóley")
    nombre1 = input("Nombre del equipo A: ")
    nombre2 = input("Nombre del equipo B: ")

    eq1 = Equipo(nombre1)
    eq2 = Equipo(nombre2)

    torneo = TorneoVoley(eq1, eq2)

    try:
        cantidad = int(input("¿Cuántos partidos se jugarán?: "))
        for i in range(cantidad):
            torneo.jugar_p()
        torneo.ver_resultados()
    except:
        print("Número no válido. Intente de nuevo.")

inicio()