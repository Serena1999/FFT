#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                           CONFIGURATION(?)_OLD                             #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from LIB import *

Cartella1 = "file_to_use1"

Directory1 = "file_to_use1/"

FileName1 = []

for cartella, sottocartelle, files in os.walk(Cartella1):
    FileName1.append(files)

FileName1 = numpy.array(FileName1[0])

print(FileName1)
