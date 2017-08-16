#!/usr/bin/env python
from decimal import *
 
#Module file for the "pathogen" class for EPydemic
 
class pathDef(object):
 def __init__(self, path_name, path_type, taxid, syndrome_name, R0, ip):
  self.path_name = path_name
  self.path_type = path_type
  self.taxid = taxid
  self.syndrome_name = syndrome_name
  self.R0 = int(R0)
  a = Decimal(ip)
  self.ip = round(a,2)
 
 def printPath(self):
  print("Name (Scientific or common): " + self.path_name)
  print("Is of type: " + self.path_type)
  print("NCBI TaxID: " + self.taxid)
  print("Causative agent of " + '"' + self.syndrome_name + '"')
  print("Average infectious period: " + str(self.ip) + " days")
 
 def getR0(self):
  return self.R0
 
 def getB(self):
  b = self.R0 * (1/self.ip)
  return b
 
 def getPeriod(self):
  return self.ip