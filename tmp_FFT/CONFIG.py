#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                           CONFIGURATION                             #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from LIB import *

#F perchè non fatte da me
Cartelle = ["data_sinusoidale_F", "data_sinusoidale", "data_oscRLC_F", \
            "data_oscRLC_con_nucleo_F", "data_osc_reazione_F", \
            "smorza_average_F", "data_quadra", "data_triangolare", \
            "esp_6_da_quadra", "esp_6_da_sinusoidale", "esp_6_da_triangolare"]
Directories = []
for i in range(len(Cartelle)):
    Directories.append(Cartelle[i] + "/")
Cartelle = numpy.array(Cartelle)
Directories = numpy.array(Directories)

##per scegliere su quali data voglio fare la trasformata intoduco apposite variabili booleane
bool_sinusoidale = False
bool_oscRLC = False
bool_oscRLCint = False
bool_oscReazione = False
bool_oscAverage = False
bool_quadra = False
bool_triangolare = False
bool_6quadra = False
bool_6sinusoidale = False
bool_6triangolare = True


