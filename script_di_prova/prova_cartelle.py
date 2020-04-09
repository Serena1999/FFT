from LIB import *


###QUESTA ERA UNA PROVA PER LA CARTELLA IN CUI CI TROVIAMO

#for cartella, sottocartelle, files in os.walk(os.getcwd()):
#    print(f"Ci troviamo nella cartella: '{cartella}'")
#    print(f"Le sottocartelle presenti sono: '{sottocartelle}'")
#    print(f"I files presenti sono: {files}")
#    print()

###ORA SU DATA

#for cartella, sottocartelle, files in os.walk("data"):
#    print(f"Ci troviamo nella cartella: '{cartella}'")
#    print(f"Le sottocartelle presenti sono: '{sottocartelle}'")
#    print(f"I files presenti sono: {files}")
#    print()

##FILE DI FUSO

Directory = "data/iorestoacasa_dati_per_esercizio/"

FileName = []

for cartella, sottocartelle, files in os.walk("data/iorestoacasa_dati_per_esercizio"):
    #print(f"Ci troviamo nella cartella: '{cartella}'")
    #print(f"Le sottocartelle presenti sono: '{sottocartelle}'")
    #print(f"I files presenti sono: {files}")
    FileName.append(files)
    #print()

FileName = numpy.array(FileName)

print(FileName)

