#!/usr/bin/env python
 
#Simple epidemiology simulator
from pathdat import pathDef
from decimal import *
 
p1 = pathDef("Measles virus", "Virus", "11234", "Measles", 18, 8)
 
def popCreate(p):
 print("-----------------------------------")
 print("\nPathogen selected:")
 p.printPath()
 t = 10
 print("-----------------------------------")
 print("Test population creation.")
 print("EPyDEMIC currently does not assume demographic change in the population.\n")
 n = int(input("Input total number of individuals in population: "))
 s = int(input("Input number of susceptible individuals: "))
 i = int(input("Input number of initial infected individuals: "))
 r = int(input("Input number of immune or 'recovered' individuals: "))
 print("\nTest population consists of {0} susceptible, {1} infected,".format(str(s), str(i)))
 print("and {0} recovered/immune. \n".format(str(r)))
 t1 = int(input("Input the simulation length in days, or 0 for the default (10 days): "))
 if t1 != 0:
  t = t1
 b = p.getB()
 y = 1/p.getPeriod()
 print("-----------------------------------")
 print("Day 0: {0} susceptible, {1} infected, {2} recovered/immune, {3} total.".format(str(s),str(i),str(r),str(n)))
 for day in range(1,t+1):
  s1 = s
  i1 = i
  r1 = r
  if (s1 - ((b*s1*i1)/n)) < 0:
   s = 0.0
  else:
   s = round((s1 - ((b*s1*i1)/n)),1)
  i = round((i1 + (((b*s1*i1)/n) - (y*i1))),1)
  r = n - s - i
  print("Day {0}: {1} susceptible, {2} infected, {3} recovered/immune, {4} total.".format(str(day),str(s),str(i),str(r),str(n)))
 r0 = float(p.getR0())
 ip = p.getPeriod()
 th = round((1/r0),3)
 si = round((th*n),1)
 ii = n-si
 print("-----------------------------------")
 print("Recap and Statistics: \n")
 print("Pathogen R0 in wholly susceptible population: {0}".format(str(r0)))
 print("Pathogen period of infectivity: {0} days".format(str(ip)))
 print("Susceptibility threshold: {0} individuals".format(str(si)))
 print("Immune individuals needed to prevent epidemic: {0} individuals".format(str(ii)))
 print("Threshold ratio: {0}".format(str(th)))
 print("-----------------------------------\n")
 print("Thank you for using!")
 print("******************************************************************************")
 
print("******************************************************************************")
print("=========================================")
print("|                EPyDEMIC               |")
print("|      Pathogen dynamics simulator      |")
print("|      V.1.0.0 - Released 8/9/2017      |")
print("| Copyright 2017 Omar Tibi ('Qunetira') |")
print("=========================================")
print("This program is distributed under the terms of the GNU General Public License.")
print("This program can be copied as according to the terms of the license.")
print("Note: EPyDEMIC uses the SIR model for epidemic simulation.")
print("-----------------------------------\n")
print("Welcome! This attempts to simulate the dynamics of a pathogen in a population.")
print("This is a very new project, so feel free to contact me with any")
print("suggestions, recommendations, or general comments.\n")
print("To continue, please make your selection from the following list:\n")
print("1. Custom population with a default pathogen.")
print("2. Custom population with a custom pathogen.")
print("3. Licensing information.")
print("4. Exit this script.\n")
swch = int(input("Enter the number of your selection: "))
if swch == 3:
 print("-----------------------------------")
 print("This program is free software: you can redistribute it and/or modify")
 print("it under the terms of the GNU General Public License as published by")
 print("the Free Software Foundation, either version 3 of the License, or")
 print("(at your option) any later version.\n")
 print("This program is distributed in the hope that it will be useful,")
 print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
 print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
 print("GNU General Public License for more details.\n")
 print("You should have received a copy of the GNU General Public License")
 print("along with this program.  If not, see <http://www.gnu.org/licenses/>.")
 print("******************************************************************************")
elif swch == 1:
 print("-----------------------------------")
 print("        Default Pathogens \n")
 print("Please select a pathogen from the following list:\n")
 print("1. Measles virus.")
 print("- A highly contagious pathogen, well known for causing disease in children.")
 ps = int(input("Enter the number of your selection: "))
 if ps == 1:
  pc = p1
  popCreate(pc)
 
elif swch == 2:
 print("-----------------------------------")
 print("     Custom Pathogen Creation \n")
 name = input("Please input the name of the pathogen: ")
 pType = input("Please input the type of pathogen: ")
 taxID = input("Please input the NCBI Taxonomy ID (if applicable): ")
 disease = input("Please input the disease name: ")
 R0 = input("Please input the pathogen's R0: ")
 per = input("Please input the pathogen's infectivity period: ")
 pc = pathDef(name,pType,taxID,disease,R0,per)
 popCreate(pc)
 
elif swch == 4:
 print("")
else:
 print("-----------------------------------")
 print("Bad entry, please try again.")
 print("******************************************************************************")