#Cambiar GI por nombre de la especie en archivo multifasta 08/05/2013 Perez Villarroya, David 


listaGI = ["163666892", "48994873", "218768969", "342360612", "260207932", "269093698", "283951607", "295647398", "301161079", "347974781", "350278064", "377652989", "49240382", "11612676", "76561771"]

nombEspec = ["Chloroflexus aurantiacus J-10-fl", "Escherichia coli str.K-12 substr. MG1655", "Pseudomonas aeruginosa LESB58", "Shigella flexneri 2a str.301", "Clostridium difficile CD196", "Veillonella parvula DSM 2008", "Acidaminococcus fermentans DSM20731", "Legionella pneumophila 2300/99 Alcoy", "Bacteroides fragilis 638R", "Chlamydia trachomatis A2497", "Acidaminococcus intestini RyC-MR95", "Corynebacterium pseudotuberculosis 316", "Staphylococcus aureus subsp. aureus strain MRSA252", "Deinococcus radiodurans R1 chromosome1", "Streptococcus agalactiae A909"]

nombArch = str (raw_input ("Introduce el nombre del archivo que deseas cambiar la GI:" ))

arch = open ( nombArch, "r")

for i in range ( len ( nombArch )) :
  if nombArch [i] == ".":
		aux = nombArch [:i-1]
		break
nombArchOut = aux + "_esp"+".faa"

archOut = open ( nombArchOut, "w")

pos = 0
for line in arch :
	if line [0] == ">":
		line = list (line) 
		for i in range ( len ( line ) ) :
			if line [i] == "-":
				pos = i 
				break
		
		sep = ""	
		line = sep.join (line)
		a = line [:pos]
		b = line [pos+1:len (line)-1]
		print b 
		for i in range ( len (listaGI) ) :
			
			if listaGI [i] == b :
				b = nombEspec [i]
				
				break
		c = a +"-"+ b 
		archOut.write ("%s\n" %c)
	
		
	else :
		archOut.write ("%s" %line)


arch.close ()
archOut.close ()
