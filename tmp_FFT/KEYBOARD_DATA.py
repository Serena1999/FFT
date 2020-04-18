#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                          DATA_PREFERENCES                           #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from CONFIG import *

print("NOMI DEI FILE CHE USO:\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                        ONDE SINUSOIDALI                             #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
if(bool_sinusoidale):
    print("%s e %s:" %(Cartelle[0], Cartelle[1]))
    FileNameSin1 = []
    FileNameSin2 = []
    for cartella, sottocartelle, files in os.walk(Cartelle[0]):
            FileNameSin1.append(files)
    FileNameSin1 = numpy.array(FileNameSin1[0])
    for cartella, sottocartelle, files in os.walk(Cartelle[1]):
            FileNameSin2.append(files)
    FileNameSin2 = numpy.array(FileNameSin2[0])
    print(FileNameSin1)
    print(FileNameSin2)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                           OSCILLATORE RLC                           #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_oscRLC):
    print("%s:" %Cartelle[2])
    FileNameSmorz = []
    for cartella, sottocartelle, files in os.walk(Cartelle[2]):
            FileNameSmorz.append(files)
    FileNameSmorz = FileNameSmorz[0]
    FileNameSmorz = numpy.array(FileNameSmorz)
    print(FileNameSmorz)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                       OSCILLATORE RLC CON NUCLEO                    #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_oscRLCint):
    print("%s:" %Cartelle[3])
    FileNameSmorzInt = []
    for cartella, sottocartelle, files in os.walk(Cartelle[3]):
            FileNameSmorzInt.append(files)
    FileNameSmorzInt = FileNameSmorzInt[0]
    FileNameSmorzInt = numpy.array(FileNameSmorzInt)
    print(FileNameSmorzInt)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                         OSCILLATORE A REAZIONE                      #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_oscReazione):
    print("%s:" %Cartelle[4])
    FileNameOscRea = []
    for cartella, sottocartelle, files in os.walk(Cartelle[4]):
            FileNameOscRea.append(files)
    FileNameOscRea = FileNameOscRea[0]
    FileNameOscRea = numpy.array(FileNameOscRea)
    print(FileNameOscRea)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                     OSCILLATORE RLC CON ERRORI                      #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_oscAverage):
    print("%s:" %Cartelle[5])
    FileNameOscPlusErr = []
    for cartella, sottocartelle, files in os.walk(Cartelle[5]):
            FileNameOscPlusErr.append(files)
    FileNameOscPlusErr = FileNameOscPlusErr[0]
    FileNameOscPlusErr = numpy.array(FileNameOscPlusErr)
    print(FileNameOscPlusErr)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                               ONDA QUADRA                           #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_quadra):
    print("%s:" %Cartelle[6])
    FileNameSquare = []
    for cartella, sottocartelle, files in os.walk(Cartelle[6]):
            FileNameSquare.append(files)
    FileNameSquare = FileNameSquare[0]
    FileNameSquare = numpy.array(FileNameSquare)
    print(FileNameSquare)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                          ONDA TRIANGOLARE                           #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_triangolare):
    print("%s:" %Cartelle[7])
    FileNameTria = []
    for cartella, sottocartelle, files in os.walk(Cartelle[7]):
            FileNameTria.append(files)
    FileNameTria = FileNameTria[0]
    FileNameTria = numpy.array(FileNameTria)
    print(FileNameTria)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                      ESP_6 QUADRA IN INGRESSO                       #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_6quadra):
    print("%s:" %Cartelle[8])
    FileNameSixQuadra = []
    for cartella, sottocartelle, files in os.walk(Cartelle[8]):
            FileNameSixQuadra.append(files)
    FileNameSixQuadra = FileNameSixQuadra[0]
    FileNameSixQuadra = numpy.array(FileNameSixQuadra)
    print(FileNameSixQuadra)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                    ESP_6 SINUSOIDALE IN INGRESSO                    #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_6sinusoidale):
    print("%s:" %Cartelle[9])
    FileNameSixSin = []
    for cartella, sottocartelle, files in os.walk(Cartelle[9]):
            FileNameSixSin.append(files)
    FileNameSixSin = FileNameSixSin[0]
    FileNameSixSin = numpy.array(FileNameSixSin)
    print(FileNameSixSin)
    print("\n")

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                    ESP_6 TRIANGOLARE IN INGRESSO                    #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

if(bool_6triangolare):
    print("%s:" %Cartelle[10])
    FileNameSixTri = []
    for cartella, sottocartelle, files in os.walk(Cartelle[10]):
            FileNameSixTri.append(files)
    FileNameSixTri = FileNameSixTri[0]
    FileNameSixTri = numpy.array(FileNameSixTri)
    print(FileNameSixTri)
    print("\n")

###DOPO PROCEDI CON SCRIPT... ATTENTA A NOMI E RACCOLTA INFO IN DOCUMENTI ESTERNI
