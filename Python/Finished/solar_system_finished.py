# import libaries

# basic math capabilities
import numpy as np
import functools as ft
import os

# plot library
import matplotlib.pyplot as plt


"""
    Definiere eine Config 'class' um Simulationsparameter zu speichern.
"""
class Config:
    def __init__(self, t_max, dt0, dt_output, output_file):
        self.t_max       = t_max
        self.dt0         = dt0
        self.dt_output   = dt_output
        self.output_file = output_file


def init_config(unit_system):

    t_max = 100.0       # yrs
    dt0   = 0.1         # minimum timestep
    dt_output = 0.1     # output interval
    output_file = "solar_system.txt"

    return Config(t_max, dt0, dt_output, output_file)


def init_output(filename):
    if os.path.exists(filename):
        os.remove(filename)

"""
    Definiere eine 'class' für das Einheitensystem
    Damit lässt es sich leichter ändern
"""
class Unitsystem:

    # Einheitensystem definieren
    def __init__(self, m_unit, l_unit, t_unit):
        self.m_unit = m_unit
        self.l_unit = l_unit
        self.t_unit = t_unit
        self.v_unit = l_unit/t_unit
        self.G      = 6.674e-8 * m_unit * t_unit * t_unit / l_unit / l_unit / l_unit    # Gravitationskonstante in Code Einheiten
        self.c      = 2.99792458e+10 * t_unit / l_unit                                  # Lichtgeschwindigkeit in Code Einheiten


# Einheitensystem definieren
def init_units():

    # Ein paar Einheiten zur Auswahl
    M_sun = 1.989e33       # Sun mass in g
    M_moon = 7.342e25       # Moon mass in g
    M_earth = 5.97219e27     # Earth mass in g
    AU = 1.495978707e13  # AU in cm
    R_earth = 6371e5         # Earth diameter in cm
    d_moon = 384400e5       # distance moon in cm
    yr = 3.1556926e7    # year in s
    pc = 3.085678e18    # parsec in cm
    kpc = 3.085678e21    # kiloparsec in cm
    Mpc = 3.085678e24    # megaparsec in cm

    # Hier ändern für andere Einheiten!
    unit_system = Unitsystem(M_sun, AU, yr)

    return unit_system



"""
    Definiere eine 'Particle' class die Masse, Position, Geschwindigkeit usw für jeden Planeten beinhaltet.

    Wir initiiert mit:

        p = Particle(m, x, v, a, dt, t)
"""
class Particle:

    # Damit setzt man ein Teilchen auf
    def __init__(self, m, x, v, a):
        self.m  = m     # Masse
        self.x  = x     # Position
        self.v  = v     # Geschwindigkeit
        self.a  = a     # Beschleunigung


    def a_abs(self):
        return np.sqrt(self.a[0]**2 + self.a[1]**2 + self.a[2]**2)

    # gibt x und v als output array zurück
    def output(self):

        out_str = []
        out_str += [f"{self.x[i]:0.6e}\t" for i in range(0, 3)]
        out_str += [f"{self.v[i]:0.6e}\t" for i in range(0, 3)]

        return out_str


def write_output(filename, system, t):

    # Öffnet die output Datei, oder erstellt sie, falls sie nicht existiert.
    f = open(filename, "a+")

    # Als Erstes schreiben wir die Zeit
    out_str = [f"{t:0.6e}\t"]

    # Dann x und v für jedes Teilchen
    for p in system:
        out_str += p.output()

    # neue Zeile
    out_str += ["\n"]

    # Einen einzelnen String erstellen
    out_str = ft.reduce(lambda a, b: a+b, out_str)

    # string in die Datei schreiben
    f.write(out_str)

    # Datei schliessen
    f.close()




# Setzt das Sonnensystem im richtigen Einheitensystem auf und gibt ein Array der Sonne/Planeten zurück
def init_solar_system(unit_system):

    # Sonne
    sun     = Particle(1.988544e33/unit_system.m_unit,
                        np.array([  4.685928291891263e+05/(unit_system.l_unit/1.e5), 9.563194923290641e+05/(unit_system.l_unit/1.e5), -1.533341587127076e+04/(unit_system.l_unit/1.e5)]),
                        np.array([ -1.278455768585727e-02/(unit_system.v_unit/1.e5), 6.447692564652730e-03/(unit_system.v_unit/1.e5), 3.039394044840682e-04/(unit_system.v_unit/1.e5)]),
                        np.array([  0.0, 0.0, 0.0])
                        )

    # Merkur
    mercury = Particle(3.302e26/unit_system.m_unit,
                        np.array( [ -4.713579828527527e+07/(unit_system.l_unit/1.e5),-4.631957178347297e+07/(unit_system.l_unit/1.e5),5.106488259447999e+05/(unit_system.l_unit/1.e5)] ),
                        np.array( [  2.440414864241152e+01/(unit_system.v_unit/1.e5),-3.230927714856684e+01/(unit_system.v_unit/1.e5),-4.882735649260043e+00/(unit_system.v_unit/1.e5)] ),
                        np.array( [  0.0, 0.0, 0.0] )
                        )

    # Venus
    venus   = Particle( 4.8685e27/unit_system.m_unit,
                        np.array( [  1.087015383199374e+08/(unit_system.l_unit/1.e5), -7.281577953082427e+06/(unit_system.l_unit/1.e5), -6.381857167679189e+06/(unit_system.l_unit/1.e5)] ),
                        np.array( [  2.484508425171419e+00/(unit_system.v_unit/1.e5),  3.476687455583895e+01/(unit_system.v_unit/1.e5),  3.213482419270903e-01/(unit_system.v_unit/1.e5)] ),
                        np.array( [  0.0, 0.0, 0.0] )
                        )

    # Earth
    earth   = Particle( 5.97219e27/unit_system.m_unit,
                        np.array( [ -4.666572753335893e+07/(unit_system.l_unit/1.e5),  1.403043145802726e+08/(unit_system.l_unit/1.e5), 1.493509552154690e+04/(unit_system.l_unit/1.e5)] ),
                        np.array( [ -2.871599709379560e+01/(unit_system.v_unit/1.e5), -9.658668417740959e+00/(unit_system.v_unit/1.e5), -2.049066619477902e-03/(unit_system.v_unit/1.e5)] ),
                        np.array( [  0.0, 0.0, 0.0] )
                        )

    # Mars
    mars    = Particle( 6.4185e26/unit_system.m_unit,
                        np.array( [  7.993300729834399e+07/(unit_system.l_unit/1.e5), -1.951269688004358e+08/(unit_system.l_unit/1.e5), -6.086301544224218e+06/(unit_system.l_unit/1.e5)] ),
                        np.array( [  2.337340830878404e+01/(unit_system.v_unit/1.e5),  1.117498287104724e+01/(unit_system.v_unit/1.e5), -3.459891064580085e-01/(unit_system.v_unit/1.e5)] ),
                        np.array( [  0.0, 0.0, 0.0] )
                        )

    # jupiter
    jupiter = Particle( 1.89813e30/unit_system.m_unit,
                        np.array( [ -4.442444431519640e+08/(unit_system.l_unit/1.e5), -6.703061523285834e+08/(unit_system.l_unit/1.e5),  1.269185734527490e+07/(unit_system.l_unit/1.e5)] ),
                        np.array( [  1.073596630262369e+01/(unit_system.v_unit/1.e5), -6.599122996686262e+00/(unit_system.v_unit/1.e5), -2.139417332332738e-01/(unit_system.v_unit/1.e5)] ),
                        np.array( [0.0, 0.0, 0.0] )
                        )

    # Saturn
    saturn  = Particle( 5.68319e29/unit_system.m_unit,
                        np.array( [ -4.890566777017240e+07/(unit_system.l_unit/1.e5), -1.503979857988314e+09/(unit_system.l_unit/1.e5),  2.843053033246052e+07/(unit_system.l_unit/1.e5)] ),
                        np.array( [  9.121308225757311e+00/(unit_system.v_unit/1.e5), -3.524504589006163e-01/(unit_system.v_unit/1.e5), -3.554364061038437e-01/(unit_system.v_unit/1.e5)] ),
                        np.array( [0.0, 0.0, 0.0] )
                        )

    # Uranus
    uranus  = Particle( 8.68103e28/unit_system.m_unit,
                        np.array( [ -9.649665981767261e+08/(unit_system.l_unit/1.e5), -2.671478218630915e+09/(unit_system.l_unit/1.e5),  2.586047227024674e+06/(unit_system.l_unit/1.e5)] ),
                        np.array( [  6.352626804478141e+00/(unit_system.v_unit/1.e5), -2.630553214528946e+00/(unit_system.v_unit/1.e5), -9.234330561966453e-02/(unit_system.v_unit/1.e5)] ),
                        np.array( [0.0, 0.0, 0.0] )
                        )

    # Neptun
    neptune = Particle( 1.0241e27/unit_system.m_unit,
                        np.array( [  2.238011384258528e+08/(unit_system.l_unit/1.e5),  4.462979506400823e+09/(unit_system.l_unit/1.e5), -9.704945189848828e+07/(unit_system.l_unit/1.e5)] ),
                        np.array( [ -5.460590042066011e+00/(unit_system.v_unit/1.e5),  3.078261976854122e-01/(unit_system.v_unit/1.e5),  1.198212503409012e-01/(unit_system.v_unit/1.e5)] ),
                        np.array( [0.0, 0.0, 0.0] )
                        )

    # Neptun
    pluto   = Particle( 1.307e25/unit_system.m_unit,
                        np.array( [  1.538634961725572e+09/(unit_system.l_unit/1.e5),  6.754880920368265e+09/(unit_system.l_unit/1.e5), -1.168322135333601e+09/(unit_system.l_unit/1.e5)] ),
                        np.array( [ -3.748709222608039e+00/(unit_system.v_unit/1.e5),  3.840130094300949e-01/(unit_system.v_unit/1.e5),  1.063222714737127e+00/(unit_system.v_unit/1.e5)] ),
                        np.array( [0.0, 0.0, 0.0] ))

    # Gibt das Sonnensystem als array der Planeten zurück
    return [ sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto ]




"""
    Hier wird die zusätzliche Sonne definiert.
    Ihr müsst auf das Einheitensystem achten!
"""
def init_perturber(unit_system):

    m = 0.0
    x = np.array( [ 15.0, 0.0, 15.0 ] ) # in AU
    v = np.array( [ 0.0, 0.0, -50.0/(unit_system.v_unit/1.e5) ] ) # in km/s -> code-units

    # Das muss 0 bleiben
    a = np.array( [ 0.0, 0.0, 0.0 ] )

    return Particle( m, x, v, a )


"""
    Funktionen für die zeitliche Entwicklung.
    Wir benutzen einen 'KDK-Leapfrog Integrator': https://de.wikipedia.org/wiki/Leapfrog-Verfahren
"""

# Leapfrog kick für Geschwindigeit update
def kick(system, dt):

    # loop über alle Sonnen/Planeten im System
    for planet in system:
        planet.v += planet.a * dt

    return system


# Leapfrog drift für Position update
def drift(system, dt):

    # loop über alle Sonnen/Planeten im System
    for planet in system:
        planet.x += planet.v * dt

    return system


"""
    Gravitationsbeschleunigung berechnen
"""
def grav_acc(system, G):

    # loop über alle Teilchen im System
    for i in range(0, len(system)):

        # Beschleunigung von Teilchen i auf 0 setzen
        system[i].a = np.zeros(3)

        # Teilchen i hat Gravitationswechselwirkung mit
        # allen anderen Teilchen j
        for j in range(0, len(system)):

            # wir wollen keine Selbswechselwirkung!
            if (i != j):

                # Abstand zwischen Teilchen i und j
                dist_vec = system[i].x - system[j].x

                # Wurzel aus dem absoluten Abstand
                r = np.sqrt( dist_vec[0]**2 + dist_vec[1]**2 + dist_vec[2]**2 )

                # Grav. Beschleunigung update
                system[i].a += -G * system[j].m / ( r*r*r ) * dist_vec


    return system


# Wir brauchen den größten Wert der absoluten Beschleunigung um den richtigen Zeitschritt zu finden
def find_a_max(system):
    return max( [ p.a_abs() for p in system ] )


def run():

    # Setup
    unit_system  = init_units()
    conf         = init_config(unit_system)
    solar_system = init_solar_system(unit_system)
    perturber    = init_perturber(unit_system)

    system = solar_system + [perturber]

    init_output(conf.output_file)

    # erste Berechnung der Grav. Beschleunigung
    system = grav_acc(system, unit_system.G)

    t = 0.0
    next_output_time = 0.0

    # Läuft so lang bis die maximale Zeit erreicht ist
    while ( t < conf.t_max ):

        # Wir müssen nicht an jedem Zeitschritt einen Output schreiben
        if ( t >= next_output_time ):

            print(f"t = {t:0.3f}")

            write_output(conf.output_file, system, t)

            next_output_time += conf.dt_output

        # maximalen Wert der Grav. Beschl. finden für adaptiven Zeitschritt
        a_max = find_a_max(system)

        # Zeitschritt update
        dt = conf.dt0 / a_max

        # System zeitlich entwickeln
        system = kick(system, 0.5*dt)
        system = drift(system, dt)
        system = grav_acc(system, unit_system.G)
        system = kick(system, 0.5*dt)

        # Zeit update
        t += dt


if __name__ == "__main__":

    print("Starting Simulation")
    run()
    print("Done!")
