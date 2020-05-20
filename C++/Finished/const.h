
// Some constants useful in solar system
#define mmoon 7.342e25           // Moon mass in g
#define mearth 5.97219e27        // Earth mass in g 
#define msun 1.989e33            // Sun mass in g 
#define au 1.495978707e13        // au in cm 
#define rearth 6371e5            // Earth dameter in cm 
#define dmoon 384400e5           // Distance moon in cm 
#define sec_per_year 3.1556926e7 // seconds per year 
#define parsec 3.085678e18       // cm per parsec
#define kparsec 3.085678e21      // cm per kilo parsec
#define mparsec 3.085678e24      // cm per mega parsec

// unit system of the simulation (solar system)
#define m_unit msun
#define l_unit au
#define t_unit sec_per_year     // Years


// resulting velocity units
#define v_unit (l_unit / t_unit)

// Gravitational constant and c in internal units 
#define G 6.672e-8 * m_unit * t_unit * t_unit / l_unit / l_unit / l_unit

