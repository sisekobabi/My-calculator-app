#This is a chemistry app#

print("welcome to the LAB! DON'T GET BURNT!")

#element data base#
#Non-metals#

elements = {
 "H": {
   "name": "Hydrogen",
   "atomic_number": 1,
   "atomic_mass": 1.008,
   "group":"Group1(non-metal)",
   "period":1,
   "density": "0.000084 g/cubiic-cm",
   "melting_point": "-259.1 degrees-C",
   "boiling_point": "-252.9 degrees-C", 
 }
}
symbol=input("Enter element symbol:")
 if symbol in elements:
  print(elements[name])
   else:
    print("Element not found"),