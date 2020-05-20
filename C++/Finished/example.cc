#include <iostream>
#include <fstream>
#include <cmath>
#include <stdlib.h>
#include <vector>

// We can set TMAX either here or in the Makefile 
#ifndef TMAX
#define TMAX 100  // in Code Einheiten
#endif

#ifndef OUTPUT_FREQENCY
#define OUTPUT_FREQENCY 0.01 // in Code Einheiten
#endif

using namespace std;

#include "example.h"
#include "const.h"

// For time variable steps
const double dt_factor_time_dependent=0.1;


// Aufsetzen des Sonnensystems. Wir speichern alles in einem 'state' vector
void initialize_sol_system(vector<state> &start)
{
  // Sonne
  start.push_back(state(1.988544e33 / m_unit,
                        4.685928291891263e+05 / (l_unit / 1.e5), // x
                        9.563194923290641e+05 / (l_unit / 1.e5), 
                       -1.533341587127076e+04 / (l_unit / 1.e5),
                       -1.278455768585727e-02 / (v_unit / 1.e5), 
                        6.447692564652730e-03 / (v_unit / 1.e5), 
                        3.039394044840682e-04 / (v_unit / 1.e5)
                  ));
  // Merkur
  start.push_back(state(3.302e26/m_unit,
                       -4.713579828527527e+07 / (l_unit / 1.e5),
                       -4.631957178347297e+07 / (l_unit / 1.e5),
                        5.106488259447999e+05 / (l_unit / 1.e5),
                        2.440414864241152e+01 / (v_unit / 1.e5),
                       -3.230927714856684e+01 / (v_unit / 1.e5),
                       -4.882735649260043e+00 / (v_unit / 1.e5)
                  ));
  // Venus
  start.push_back(state(4.8685e27 / m_unit,
                        1.087015383199374e+08 / (l_unit / 1.e5), 
                       -7.281577953082427e+06 / (l_unit / 1.e5), 
                       -6.381857167679189e+06 / (l_unit / 1.e5),
                        2.484508425171419e+00 / (v_unit / 1.e5), 
                        3.476687455583895e+01 / (v_unit / 1.e5), 
                        3.213482419270903e-01 / (v_unit / 1.e5)
                  ));
  // Erde
  start.push_back(state(5.97219e27 / m_unit,
                       -4.666572753335893e+07 / (l_unit / 1.e5), 
                        1.403043145802726e+08 / (l_unit / 1.e5), 
                        1.493509552154690e+04 / (l_unit / 1.e5),
                       -2.871599709379560e+01 / (v_unit / 1.e5), 
                       -9.658668417740959e+00 / (v_unit / 1.e5), 
                       -2.049066619477902e-03 / (v_unit / 1.e5)
                        ));    
  // Mars
  start.push_back(state(6.4185e26 / m_unit,
                        7.993300729834399e+07 / (l_unit / 1.e5), 
                       -1.951269688004358e+08 / (l_unit / 1.e5), 
                       -6.086301544224218e+06 / (l_unit / 1.e5),
                        2.337340830878404e+01 / (v_unit / 1.e5), 
                        1.117498287104724e+01 / (v_unit / 1.e5), 
                       -3.459891064580085e-01 / (v_unit / 1.e5)
                        ));   
  // Jupiter
  start.push_back(state(1.89813e30 / m_unit,
                       -4.442444431519640e+08 / (l_unit / 1.e5), 
                       -6.703061523285834e+08 / (l_unit / 1.e5), 
                        1.269185734527490e+07 / (l_unit / 1.e5),
                        1.073596630262369e+01 / (v_unit / 1.e5), 
                       -6.599122996686262e+00 / (v_unit / 1.e5), 
                       -2.139417332332738e-01 / (v_unit / 1.e5)
                        ));           
  // Saturn
  start.push_back(state(5.68319e29 / m_unit,
                       -4.890566777017240e+07 / (l_unit / 1.e5), 
                       -1.503979857988314e+09 / (l_unit / 1.e5), 
                        2.843053033246052e+07 / (l_unit / 1.e5),
                        9.121308225757311e+00 / (v_unit / 1.e5), 
                       -3.524504589006163e-01 / (v_unit / 1.e5), 
                       -3.554364061038437e-01 / (v_unit / 1.e5)
                        ));                                                   
  // Uranus
  start.push_back(state(8.68103e28 / m_unit,
                       -9.649665981767261e+08 / (l_unit / 1.e5), 
                       -2.671478218630915e+09 / (l_unit / 1.e5), 
                        2.586047227024674e+06 / (l_unit / 1.e5),
                        6.352626804478141e+00 / (v_unit / 1.e5), 
                       -2.630553214528946e+00 / (v_unit / 1.e5), 
                       -9.234330561966453e-02 / (v_unit / 1.e5)
                        ));    
  // Neptun
  start.push_back(state(1.0241e27 / m_unit,
                        2.238011384258528e+08 / (l_unit / 1.e5), 
                        4.462979506400823e+09 / (l_unit / 1.e5), 
                       -9.704945189848828e+07 / (l_unit / 1.e5),
                       -5.460590042066011e+00 / (v_unit / 1.e5), 
                        3.078261976854122e-01 / (v_unit / 1.e5), 
                        1.198212503409012e-01 / (v_unit / 1.e5)
                        ));
  // Pluto
  start.push_back(state(1.307e25 / m_unit,
                        1.538634961725572e+09 / (l_unit / 1.e5), 
                        6.754880920368265e+09 / (l_unit / 1.e5), 
                       -1.168322135333601e+09 / (l_unit / 1.e5),
                       -3.748709222608039e+00 / (v_unit / 1.e5), 
                        3.840130094300949e-01 / (v_unit / 1.e5), 
                        1.063222714737127e+00 / (v_unit / 1.e5)
                        ));
}

// Aufsetzen des Störers.
void initialize_perturber(vector<state> &start)
{
  start.push_back(state(0.0,                              // Masse
                        15.0, 0.0, 15.0,                  // x, y, z
                        0.0, 0.0, -50.0 / (v_unit / 1.e5) // vx, vy, vz
                        ));
}

// Calculate acceleration of a given state. This is a procedure which gets a state as an argument
void calculate_acceleration(vector<state> &here)
{
  for(int i=0; i<here.size(); i++)
    {
      here[i].a = vec( 0.0, 0.0, 0.0);

      for (int j = 0; j < here.size(); j++)
      {
        if (i != j)
        {
          vec dist_vec = here[i].x - here[j].x;
          double r = dist_vec.abs();
          here[i].a += -G * here[j].m / ( r * r * r) * dist_vec;
        }
      }
      
    }
}

// update velocities of a given state. This is a procedure which gets a state and a deltaT as arguments
void kick(vector<state> &here, double mydt)
{
  for(int i=0;i<here.size();i++)
    here[i].v += here[i].a * mydt;
}

// update positions of a given state. This is a procedure which gets a state and a deltaT as argument
void drift(vector<state> &here, double mydt)
{
  for(int i=0;i<here.size();i++)
    here[i].x += here[i].v * mydt;
}



int main (int argc, const char **argv)
{
  /* state is a structure (we defined it in example.h) which contains all quantities (like position, velocity etc)
     needed to describe a test particle.
     We want to create one instance of it which we call current for or actual time step */
  
  vector<state> system;          // Vector of our particle system
  double next_output_time = 0;    // Time for next output
  double t = 0.0, dt = 0;         // Timestep to be defined later
  ofstream outfile;               // Lets use directly a file to output the data

  initialize_sol_system(system);
  initialize_perturber(system);

  // Lets output at the beginning some useful information ... 
  cout << "# L = " << l_unit << endl;
  cout << "# T = " << t_unit << endl;
  cout << "# M = " << m_unit << endl;
  cout << "# V = " << v_unit << endl;
  cout << "# G = " << G      << endl;

  outfile.open("solar_system.txt", ios::out | ios::trunc);

  // Now we calculate the acceleration of the initial state
  calculate_acceleration(system);

  // This is loop which is done until integration of t reaches our defined TMAX
  while(t < TMAX)
  {
    // Write output (trick: do it only if time defined by OUTPUT_FREQUENCY is reached !)
    if(t > next_output_time)
    {
      cout << t << " " << dt << " " << next_output_time << endl;

      outfile << t;
      for( int i=0; i < system.size(); i++)
        outfile << system[i].x << system[i].v;
      outfile << endl;
      next_output_time += OUTPUT_FREQENCY;
    }

    // Variable Timestep (trick: first find largest acceleration and convert to timestep at the end !)
    double a_max=0;
    for(int i=0; i< system.size(); i++)
      if(system[i].a.abs() > a_max)
        a_max = system[i].a.abs();

    dt = dt_factor_time_dependent / a_max;


    // KDK Scheme
    kick(system, 0.5 * dt);
    drift(system, 1.0 * dt);
    calculate_acceleration(system);
    kick(system, 0.5 * dt);

    // Finally we update the time t
    t += dt;

  }

  outfile.close();
  
  return(0);
}


/* How to get it running:
  1) make
  2) ./myprogram 
*/
