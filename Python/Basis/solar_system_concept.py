# import libaries

# basic math capabilities
import numpy as np

# plot library
import matplotlib.pyplot as plt


"""
    Einheitensystem definieren
"""

# Ein paar Einheiten zur Auswahl
M_sun = 1.989e33        # Sun mass in g
M_moon = 7.342e25       # Moon mass in g
M_earth = 5.97219e27    # Earth mass in g
AU = 1.495978707e13     # AU in cm
R_earth = 6371e5        # Earth diameter in cm
d_moon = 384400e5       # distance moon in cm
yr = 3.1556926e7        # year in s
pc = 3.085678e18        # parsec in cm
kpc = 3.085678e21       # kiloparsec in cm
Mpc = 3.085678e24       # megaparsec in cm

m_unit = # <>
l_unit = # <>
t_unit = # <>
v_unit = l_unit / t_unit

# Gravitationskonstante in internen Einheiten
G = 6.674e-8 * m_unit * t_unit * t_unit / l_unit / l_unit / l_unit


"""
    Es ist praktisch eine 'Particle' class zu definieren um die Daten zu sortieren.
    Ansonsten könnt ihr auch mit großen Arrays arbeiten.
"""



"""
    Massen, Positionen und Geschwindigkeiten vom Sonnensystem.
    
    Massen sind in g
    Positionen in km
    Geschwindigkeiten in km/s

    Das müsst ihr in interne Einheiten umrechnen!
"""

# Sonne
m = 1.988544e33
x = np.array( [  4.685928291891263e+05, 9.563194923290641e+05, -1.533341587127076e+04 ] )
v = np.array( [ -1.278455768585727e-02, 6.447692564652730e-03,  3.039394044840682e-04 ] )

# Merkur
m = 3.302e26
x = np.array( [ -4.713579828527527e+07, -4.631957178347297e+07,  5.106488259447999e+05 ] )
v = np.array( [  2.440414864241152e+01, -3.230927714856684e+01, -4.882735649260043e+00 ] )

# Venus
m = 4.8685e27
x = np.array( [  1.087015383199374e+08, -7.281577953082427e+06, -6.381857167679189e+06 ] )
v = np.array( [  2.484508425171419e+00,  3.476687455583895e+01,  3.213482419270903e-01 ] )

# Erde
m = 5.97219e27
x = np.array( [ -4.666572753335893e+07,  1.403043145802726e+08,  1.493509552154690e+04 ] )
v = np.array( [ -2.871599709379560e+01, -9.658668417740959e+00, -2.049066619477902e-03 ] )

# Mars
m = 6.4185e26
x = np.array( [  7.993300729834399e+07, -1.951269688004358e+08, -6.086301544224218e+06] )
v = np.array( [  2.337340830878404e+01,  1.117498287104724e+01, -3.459891064580085e-01] )

# Jupiter
m = 1.89813e30
x = np.array( [ -4.442444431519640e+08, -6.703061523285834e+08,  1.269185734527490e+07] )
v = np.array( [  1.073596630262369e+01, -6.599122996686262e+00, -2.139417332332738e-01] )

# Saturn
m = 5.68319e29
x = np.array( [ -4.890566777017240e+07, -1.503979857988314e+09,  2.843053033246052e+07] )
v = np.array( [  9.121308225757311e+00, -3.524504589006163e-01, -3.554364061038437e-01] )

# Uranus
m = 8.68103e28
x = np.array([ -9.649665981767261e+08, -2.671478218630915e+09,  2.586047227024674e+06] )
v = np.array([  6.352626804478141e+00, -2.630553214528946e+00, -9.234330561966453e-02] )

# Neptun
m = 1.0241e27
x = np.array( [  2.238011384258528e+08,  4.462979506400823e+09, -9.704945189848828e+07] )
v = np.array( [ -5.460590042066011e+00,  3.078261976854122e-01,  1.198212503409012e-01] )

# Pluto
m = 1.307e25
x = np.array( [  1.538634961725572e+09,  6.754880920368265e+09, -1.168322135333601e+09] )
v = np.array( [ -3.748709222608039e+00,  3.840130094300949e-01,  1.063222714737127e+00] )


"""
    Zuletzt müsst ihr noch einen Störer aufsetzen
"""
m = # <>
x = # <>
v = # <>


"""
    Funktionen für die zeitliche Entwicklung.
    Wir benutzen einen 'KDK-Leapfrog Integrator':
    https://de.wikipedia.org/wiki/Leapfrog-Verfahren
"""

# Leapfrog kick für Geschwindigeit update
def kick( <> ):

    # loop über alle Sonnen/Planeten im System
    # <> v_i = a_i * dt

    return # <>


# Leapfrog drift für Position update
def drift( <> ):

    # loop über alle Sonnen/Planeten im System
    # <> x_i = v_i * dt

    return # <>


"""
    Gravitationsbeschleunigung berechnen
"""
def grav_acc( <> ):

    # loop über alle Teilchen im System
    
        # Beschleunigung von Teilchen i auf 0 setzen
        # <> a_i = 0

        # Teilchen i hat Gravitationswechselwirkung mit
        # allen anderen Teilchen j
        
            # wir wollen keine Selbswechselwirkung!    

                # Abstand zwischen Teilchen i und j
                # <> r = x_i - x_j

                # Gravitationsbeschleunigung ausrechnen
                # <> a_i = -G * m_j / (sqrt( |r|^3 ) ) * r


    return # <>



def run():

    # Setup
    # Hier solltet ihr die Variablen der Simulation definieren:
    # - Einheitensystem
    # - maximale Zeit, Zeitschritt, output intervall
    # - Sterne / Planeten definieren

    # erste Berechnung der Grav. Beschleunigung
    # <> 

    # Anfangszeit definieren
    t = 0.0
    next_output_time = 0.0

    # Läuft so lang bis die maximale Zeit erreicht ist
    while ( t < t_max ):

        # Wir müssen nicht an jedem Zeitschritt einen Output schreiben
        # sondern nur in den definierten Intervallen
        if ( t >= next_output_time ):

            # output schreiben, zB in ein Text file
            # <>

            # update für die nächste Output Zeit
            next_output_time += dt_output

        
        

        # System zeitlich entwickeln
        # - kick
        # - drift
        # - Gravitationsbeschleunigung ausrechnen
        # - kick
        #
        # https://de.wikipedia.org/wiki/Leapfrog-Verfahren

        # Zeit update
        t += dt


if __name__ == "__main__":

    print("Starting Simulation")
    run()
    print("Done!")
