__author__ = 'stubborn'
# -*- coding: utf8 -*-
import sys
if sys.version_info <= (2,6,0):
   print "This script requires python v2.6 and up"
   sys.exit(1)
from openuhw import OpenUHW
import math

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
   return ((4.0/3.0)*math.pi)*box_volume(r)


def ex_1():
   '''
   hw1 ex1
   '''
   a=float(1.0E6)
   b=float(5.0E-3)
   c=float(0.5E2)
   result = dict(title="ex1")
   answer = []
   answer.append(dict(descr="ABC", result=a*b*c))
   answer.append(dict(descr="AC^(-2)", result=(a/(c*c))))
   result.update(dict(answer=answer))
   return result



def ex_2():
   r_atom=float(1.0E-10)
   r_earth=float(6.37E6)
   v_atom=box_volume(r_atom) ## annoying assumption
   v_earth=sphere_volume(r_earth)
   ratio = v_earth/v_atom
   result = dict(title="ex2")
   answer = []
   answer.append(dict(descr="V(earth)/'V'(atom)", result=ratio))
   result.update(dict(answer=answer))
   return result


def ex_3():
   a=float(9.7E-2)
   b=float(5.3E-2)
   c=float(4.4E-2)
   err=float(0.5E-3)
   vol_box=box_volume(a,w=b,h=c)
   a_min = a - err
   b_min = b - err
   c_min = c - err

   a_max = a + err
   b_max = b + err
   c_max = c + err

   vol_min=box_volume(a_min, b_min, c_min)
   vol_max=box_volume(a_max, b_max, c_max)
   vol_err = (vol_max-vol_min)/2

   result = dict(title=u"ex3")
   answer = []
   answer.append(dict(descr=u"V(box)±err", result=u"{vol_box}m^3±{vol_err}m^3".format(**locals())))
   result.update(dict(answer=answer))
   return result

def ex_4():
   density_hg = float(13.58) # in g/cm^3
   atomic_mass_hg = float(200.59) # in AMU i.e. g/mol
   AVOGADRO_CONSTANT = float(6.022141E23) # entities/mol
   result = dict(title=u"ex4")
   answer = []

   ## how many atoms of Hg are there in 1 cm^3?
   vol = float(1) # in cm^3
   mass_hg = vol*density_hg ## grams
   molar_mass = mass_hg/atomic_mass_hg # mols
   atoms_count = molar_mass * AVOGADRO_CONSTANT
   answer.append(dict(descr=u"atoms_count(hg, vol=1 cm^3)", result=atoms_count))

   molar_mass = 1 # mols
   mass_hg = molar_mass * atomic_mass_hg # grams
   vol = mass_hg / density_hg
   answer.append(dict(descr=u"volume(hg, 1 mol)", result=vol))
   result.update(dict(answer=answer))
   return result




mamah1.add(ex_1())
mamah1.add(ex_2())
mamah1.add(ex_3())
mamah1.add(ex_4())

mamah1.print_out()