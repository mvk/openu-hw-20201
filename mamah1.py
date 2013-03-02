__author__ = 'stubborn'
# -*- coding: utf8 -*-
import sys
if sys.version_info <= (2,6,0):
   print "This script requires python v2.6 and up"
   sys.exit(1)
from openuhw import OpenUHW, OpenUHWResult
import math

AVOGADRO_CONSTANT = float(6.022141E23) # entities/mol
PI=math.pi

mamah1 = OpenUHW()

def box_volume(l,w=None,h=None):
   '''
   returns l*w*h.
   l length
   w width
   h height

   '''
   length=l
   width=w if w else l
   height=h if h else l
   return length*width*height

# def cube_volume(d):
#    return box_volume(d)

def sphere_volume(r):
   return ((4.0/3.0)*PI)*box_volume(r)


def ex_1():
   '''
   hw1 ex1
   '''
   result = OpenUHWResult(title=u"ex1")
   a=float(1.0E6)
   b=float(5.0E-3)
   c=float(0.5E2)
   result.answers.append(
      dict(
         descr=u"ABC",
         result=a*b*c,
      )
   )
   result.answers.append(
      dict(
         descr=u"AC^(-2)",
         result=(a/(c*c)),
      )
   )
   return result



def ex_2():
   result = OpenUHWResult(title=u"ex2")
   r_atom=float(1.0E-10)
   r_earth=float(6.37E6)
   v_atom=box_volume(r_atom) ## annoying assumption
   v_earth=sphere_volume(r_earth)
   ratio = v_earth/v_atom
   result.answers.append(
      dict(
         descr=u"V(earth)/'V'(atom)",
         result=ratio,
      )
   )
   return result


def ex_3():
   result = OpenUHWResult(title=u"ex3")
   ## box a,b,c
   a=float(9.7E-2) # m
   b=float(5.3E-2) # m
   c=float(4.4E-2) # m
   err=float(0.5E-3) # m
   vol_box=box_volume(a,w=b,h=c)
   ## minimal box
   a_min = a - err
   b_min = b - err
   c_min = c - err
   ## maximal box
   a_max = a + err
   b_max = b + err
   c_max = c + err
   ## compare:
   vol_min=box_volume(a_min, b_min, c_min)
   vol_max=box_volume(a_max, b_max, c_max)
   vol_err = (vol_max-vol_min)/2
   result.answers.append(
      dict(
         descr=u"V(box)±err",
         result=u"{vol_box}m^3±{vol_err}m^3".format(**locals()),
      )
   )
   return result

def ex_4():
   result = OpenUHWResult(title=u"ex4")
   density_hg = float(13.58) # in g/cm^3
   atomic_mass_hg = float(200.59) # in AMU i.e. g/mol

   ## how many atoms of Hg are there in 1 cm^3?
   vol = float(1) # in cm^3
   mass_hg = vol*density_hg ## grams
   molar_mass = mass_hg/atomic_mass_hg # mols
   atoms_count = molar_mass * AVOGADRO_CONSTANT
   result.answers.append(
      dict(
         descr=u"atoms_count(hg, vol=1 cm^3)",
         result=atoms_count,
      )
   )
   molar_mass = 1 # moles
   mass_hg = molar_mass * atomic_mass_hg # grams
   vol = mass_hg / density_hg
   result.answers.append(
      dict(
         descr=u"volume(hg, 1 mol)",
         result=vol,
      )
   )
   return result

def ex_5():
   result = OpenUHWResult(title=u"ex5")
   sound_speed_air = float(333.33) ## m/sec
   light_speed_air = float(3.0E8) ## m/sec

   ## how many orders of magnitude is speed of light higher than speed of sound?
   ### ans: numb. of orders of magnitude := log10 ( ratio )
   ### question is: how many WHOLE orders of magnitude ? it's floor rounding!
   result.answers.append(
      dict(
         descr=u"orders_of_mag(light,sound)",
         # result=math.log10(light_speed_air/sound_speed_air), ## the exact is 5.99 :) so it's 5!
         result=math.floor(math.log10(light_speed_air/sound_speed_air)),
      )
   )
   return result

def ex_6():
   result = OpenUHWResult(title=u"ex6")
   ## work in given units:
   density = float(1.55E-3) # in g/cm^-3
   atomic_density_per_litre = float(2.22E22) # atoms
   atomic_density_per_cubic_cm = atomic_density_per_litre/(1.0E3) # atoms
   mass_of_an_atom_in_gr = atomic_density_per_cubic_cm*density # g
   ### convert to SI:
   kg2amu_coefficient = float(1.660538921E-27)
   mass_of_an_atom = mass_of_an_atom_in_gr*float(1.0E-3)
   ### hence:
   amu = mass_of_an_atom*kg2amu_coefficient
   ## how many orders of magnitude is speed of light higher than speed of sound?
   result.answers.append(
      dict(
         descr=u"AMU(gas)",
         result=u"{}".format(str(amu)),
      )
   )
   return result

def ex_7():
   result = OpenUHWResult(title=u"ex7")
   ## work in given units:
   isotopes_data = [
      dict(mass=float(23.985),   probability=float(0.79), ),
      dict(mass=float(24.9858),  probability=None, ),
      dict(mass=float(25.9826),  probability=None, ),
   ]
   # iso_1_probability = float(0.79)
   std_mass_in_amu   = float(24.305)

   result.answers.append(
      dict(
         descr=u"P(max(mass, {isotopes}))",
         result=u"{}".format(str(amu)),
      )
   )
   return result




solvers_list = [
   ex_1,
   ex_2,
   ex_3,
   ex_4,
   ex_5,
   ex_6,
]

for s in solvers_list:
   mamah1.add_solver(s)

# mamah1.add_solver(ex_1)
# mamah1.add_solver(ex_2)
# mamah1.add_solver(ex_3)
# mamah1.add_solver(ex_4)
# mamah1.add_solver(ex_5)
# mamah1.add_solver(ex_6)


mamah1.solve(print_solution=True)
