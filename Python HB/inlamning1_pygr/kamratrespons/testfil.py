import csv
import matplotlib.pyplot as plt

#Listor för att spara data
lghData = []
villaData = []

#Öppnar CSV fil, lägger i två listor
with open ('villapriser.csv', 'r') as fil:
    csv_reader = csv.reader(fil, delimiter = ';')
    
    for row in csv_reader:
        villaData.append(row)
        
with open ('lghpriser.csv', 'r') as fil:
    csv_reader = csv.reader(fil, delimiter = ';')
    
    for row in csv_reader:
        lghData.append(row)




#listor för att spara data i
fil1 = []
fil2 = []

fil3_resultat = []
fil4_resultat = []

fil_test_sorted = []
fil_SE1_resultat = []
fil_SE2_resultat = []
fil_SE3_resultat = []
fil_SE4_resultat = []
fil_SE1_resultat_lgh = []
fil_SE2_resultat_lgh = []
fil_SE3_resultat_lgh = []
fil_SE4_resultat_lgh = []

lagsta_villa_graf = []
lagsta_lgh_graf = []
hogsta_villa_graf = []
hogsta_lgh_graf = []
medel_villa_graf = []
medel_lgh_graf = []
medel_varde_lgh = []
medel_varde_villa = []

###Funktion som räknar ut medelvärde
def medelvalue1(medel, pris_avtal):
    loop_result = [float(x[pris_avtal]) for x in medel]
    summa = sum(loop_result)
    length = len(medel)
    varde = (float(summa)/(float(length)))
    medel_varde_villa.append(round(varde, 2))
    
###Funktion som räknar ut medelvärde
def medelvalue2(medel, pris_avtal):
    loop_result = [float(x[pris_avtal]) for x in medel]
    summa = sum(loop_result)
    length = len(medel)
    varde = (float(summa)/(float(length)))
    medel_varde_lgh.append(round(varde, 2))


#Indata från användare
pris_avtal = input('Ange prisavtal (R, F1, F3):' )

for column in villaData[1:]:
    fil1.append(column)

for column in lghData[1:]:
    fil2.append(column)

#fil_test_sorted = (sorted(fil_test, key = lambda x: float(x[4])))

if pris_avtal == 'R':
    pris_avtal = ('Rörligt')
    for row in fil1:
        fil3_resultat.append(row)
    for row in fil2:
        fil4_resultat.append(row)

        
#Sorterar på min värde kolumn 4 (SE1 rörligt pris)
    fil_SE1_sorted = (sorted(fil3_resultat, key = lambda x: float(x[4])))
    fil_SE1_resultat.append(fil_SE1_sorted[0][0])
    fil_SE1_resultat.append(fil_SE1_sorted[0][1])
    fil_SE1_resultat.append(fil_SE1_sorted[0][4])
    lagsta_villa_graf.append(fil_SE1_sorted[0][4])
    medelvalue1(fil_SE1_sorted, 4)
#Sorterar på max värde kolumn 4 (SE1 rörligt pris)
    fil_SE1_sorted = (sorted(fil3_resultat, key = lambda x: float(x[4]), reverse=True))
    fil_SE1_resultat.append(fil_SE1_sorted[0][0])
    fil_SE1_resultat.append(fil_SE1_sorted[0][1])
    fil_SE1_resultat.append(fil_SE1_sorted[0][4])
    hogsta_villa_graf.append(fil_SE1_sorted[0][4])
    
#Sorterar på min värde kolumn 7 (SE2 rörligt pris)
    fil_SE2_sorted = (sorted(fil3_resultat, key = lambda x: float(x[7])))
    fil_SE2_resultat.append(fil_SE2_sorted[0][0])
    fil_SE2_resultat.append(fil_SE2_sorted[0][1])
    fil_SE2_resultat.append(fil_SE2_sorted[0][7])
    lagsta_villa_graf.append(fil_SE2_sorted[0][7])
    medelvalue1(fil_SE2_sorted, 7)
#Sorterar på max värde kolumn 7 (SE2 rörligt pris)
    fil_SE2_sorted = (sorted(fil3_resultat, key = lambda x: float(x[7]), reverse=True))
    fil_SE2_resultat.append(fil_SE2_sorted[0][0])
    fil_SE2_resultat.append(fil_SE2_sorted[0][1])
    fil_SE2_resultat.append(fil_SE2_sorted[0][7])
    hogsta_villa_graf.append(fil_SE2_sorted[0][7])
#Sorterar på min värde kolumn 10 (SE3 rörligt pris)
    fil_SE3_sorted = (sorted(fil3_resultat, key = lambda x: float(x[10])))
    fil_SE3_resultat.append(fil_SE3_sorted[0][0])
    fil_SE3_resultat.append(fil_SE3_sorted[0][1])
    fil_SE3_resultat.append(fil_SE3_sorted[0][10])
    lagsta_villa_graf.append(fil_SE3_sorted[0][10])
    medelvalue1(fil_SE3_sorted, 10)
# Sorterar på max värde kolumn 10 (SE3 rörligt pris)
    fil_SE3_sorted = (sorted(fil3_resultat, key = lambda x:float(x[10]), reverse=True))
    fil_SE3_resultat.append(fil_SE3_sorted[0][0])
    fil_SE3_resultat.append(fil_SE3_sorted[0][1])
    fil_SE3_resultat.append(fil_SE3_sorted[0][10])
    hogsta_villa_graf.append(fil_SE3_sorted[0][10])
# Sorterar på min värde kolumn 13 (SE4 rörligt pris)
    fil_SE4_sorted = (sorted(fil3_resultat, key = lambda x: float(x[13])))
    fil_SE4_resultat.append(fil_SE4_sorted[0][0])
    fil_SE4_resultat.append(fil_SE4_sorted[0][1])
    fil_SE4_resultat.append(fil_SE4_sorted[0][13])
    lagsta_villa_graf.append(fil_SE4_sorted[0][13])
    medelvalue1(fil_SE4_sorted, 13)
# Sorterar på max värde kolumn 13 (SE4 rörligt pris)
    fil_SE4_sorted = (sorted(fil3_resultat, key = lambda x: float(x[13]), reverse=True))
    fil_SE4_resultat.append(fil_SE4_sorted[0][0])
    fil_SE4_resultat.append(fil_SE4_sorted[0][1])
    fil_SE4_resultat.append(fil_SE4_sorted[0][13])
    hogsta_villa_graf.append(fil_SE4_sorted[0][13])


####LGH DATA####

# Sorterar på min värde kolumn 4 (SE1 rörligt pris)
    fil_SE1_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[4])))
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][0])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][1])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][4])
    lagsta_lgh_graf.append(fil_SE1_sorted_lgh[0][4])
    medelvalue2(fil_SE1_sorted_lgh, 4)
#Sorterar på max värde kolumn 4 (SE1 rörligt pris)
    fil_SE1_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[4]), reverse=True))
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][0])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][1])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][4])
    hogsta_lgh_graf.append(fil_SE1_sorted_lgh[0][4])
#Sorterar på min värde kolumn 7 (SE2 rörligt pris)
    fil_SE2_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[7])))
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][0])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][1])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][7])
    lagsta_lgh_graf.append(fil_SE2_sorted_lgh[0][7])
    medelvalue2(fil_SE2_sorted_lgh, 7)
#Sorterar på max värde kolumn 7 (SE2 rörligt pris)
    fil_SE2_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[7]), reverse=True))
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][0])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][1])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][7])
    hogsta_lgh_graf.append(fil_SE2_sorted_lgh[0][7])
#Sorterar på min värde kolumn 10 (SE3 rörligt pris)
    fil_SE3_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[10])))
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][0])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][1])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][10])
    lagsta_lgh_graf.append(fil_SE3_sorted_lgh[0][10])
    medelvalue2(fil_SE3_sorted_lgh, 10)
#Sorterar på max värde kolumn 10 (SE3 rörligt pris)
    fil_SE3_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[10]), reverse=True))
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][0])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][1])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][10])
    hogsta_lgh_graf.append(fil_SE3_sorted_lgh[0][10])
#Sorterar på min värde kolumn 13 (SE4 rörligt pris)
    fil_SE4_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[13])))
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][0])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][1])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][13])
    lagsta_lgh_graf.append(fil_SE4_sorted_lgh[0][13])
    medelvalue2(fil_SE3_sorted_lgh, 13)
#Sorterar på max värde kolumn 13 (SE4 rörligt pris)
    fil_SE4_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[13]), reverse=True))
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][0])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][1])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][13])
    hogsta_lgh_graf.append(fil_SE4_sorted_lgh[0][13])


if pris_avtal == 'F1':
    pris_avtal = ('Fast 1 år')

    for row in fil1:
        fil3_resultat.append(row)
    for row in fil2:
        fil4_resultat.append(row)

#Sorterar på min värde kolumn 4 (SE1 FAST 1 år pris)
    fil_SE1_sorted = (sorted(fil3_resultat, key = lambda x: float(x[2])))
    fil_SE1_resultat.append(fil_SE1_sorted[0][0])
    fil_SE1_resultat.append(fil_SE1_sorted[0][1])
    fil_SE1_resultat.append(fil_SE1_sorted[0][2])
    lagsta_villa_graf.append(fil_SE1_sorted[0][2])
    medelvalue1(fil_SE1_sorted, 2)

# Sorterar på max värde kolumn 4 (SE1 FAST 1 år pris)
    fil_SE1_sorted = (sorted(fil3_resultat, key = lambda x: float(x[2]), reverse=True))
    fil_SE1_resultat.append(fil_SE1_sorted[0][0])
    fil_SE1_resultat.append(fil_SE1_sorted[0][1])
    fil_SE1_resultat.append(fil_SE1_sorted[0][2])
    hogsta_villa_graf.append(fil_SE1_sorted[0][2])

#Sorterar på min värde kolumn 7 (SE2 FAST 1 år pris)
    fil_SE2_sorted = (sorted(fil3_resultat, key = lambda x: float(x[5])))
    fil_SE2_resultat.append(fil_SE2_sorted[0][0])
    fil_SE2_resultat.append(fil_SE2_sorted[0][1])
    fil_SE2_resultat.append(fil_SE2_sorted[0][5])
    lagsta_villa_graf.append(fil_SE2_sorted[0][5])
    medelvalue1(fil_SE2_sorted, 5)

#Sorterar på max värde kolumn 7 (SE2 FAST 1 år pris)
    fil_SE2_sorted = (sorted(fil3_resultat, key = lambda x: float(x[5]), reverse=True))
    fil_SE2_resultat.append(fil_SE2_sorted[0][0])
    fil_SE2_resultat.append(fil_SE2_sorted[0][1])
    fil_SE2_resultat.append(fil_SE2_sorted[0][5])
    hogsta_villa_graf.append(fil_SE2_sorted[0][5])

#Sorterar på min värde kolumn 10 (SE3 FAST 1 år pris)
    fil_SE3_sorted = (sorted(fil3_resultat, key = lambda x: float(x[8])))
    fil_SE3_resultat.append(fil_SE3_sorted[0][0])
    fil_SE3_resultat.append(fil_SE3_sorted[0][1])
    fil_SE3_resultat.append(fil_SE3_sorted[0][8])
    lagsta_villa_graf.append(fil_SE3_sorted[0][8])
    medelvalue1(fil_SE3_sorted, 8)

#Sorterar på max värde kolumn 10 (SE3 FAST 1 år pris)
    fil_SE3_sorted = (sorted(fil3_resultat, key = lambda x: float(x[8]), reverse=True))
    fil_SE3_resultat.append(fil_SE3_sorted[0][0])
    fil_SE3_resultat.append(fil_SE3_sorted[0][1])
    fil_SE3_resultat.append(fil_SE3_sorted[0][8])
    hogsta_villa_graf.append(fil_SE3_sorted[0][8])

#Sorterar på min värde kolumn 13 (SE4 FAST 1 år pris)
    fil_SE4_sorted = (sorted(fil3_resultat, key = lambda x: float(x[11])))
    fil_SE4_resultat.append(fil_SE4_sorted[0][0])
    fil_SE4_resultat.append(fil_SE4_sorted[0][1])
    fil_SE4_resultat.append(fil_SE4_sorted[0][11])
    lagsta_villa_graf.append(fil_SE4_sorted[0][11])
    medelvalue1(fil_SE4_sorted, 11)

#Sorterar på max värde kolumn 13 (SE4 FAST 1 år pris)
    fil_SE4_sorted = (sorted(fil3_resultat, key = lambda x: float(x[11]), reverse=True))
    fil_SE4_resultat.append(fil_SE4_sorted[0][0])
    fil_SE4_resultat.append(fil_SE4_sorted[0][1])
    fil_SE4_resultat.append(fil_SE4_sorted[0][11])
    hogsta_villa_graf.append(fil_SE4_sorted[0][11])

######LGH DATA###########

# Sorterar på min värde kolumn 4 (SE1 FAST 1 år pris)
    fil_SE1_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[2])))
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][0])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][1])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][2])
    lagsta_lgh_graf.append(fil_SE1_sorted_lgh[0][2])
    medelvalue2(fil_SE1_sorted_lgh, 2)
    
#Sorterar på max värde kolumn 4 (SE1 FAST 1 år pris)
    fil_SE1_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[2]), reverse=True))
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][0])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][1])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][2])
    hogsta_lgh_graf.append(fil_SE1_sorted_lgh[0][2])
#Sorterar på min värde kolumn 7 (SE2 FAST 1 år pris)
    fil_SE2_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[5])))
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][0])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][1])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][5])
    lagsta_lgh_graf.append(fil_SE2_sorted_lgh[0][5])
    medelvalue2(fil_SE2_sorted_lgh, 5)
#Sorterar på max värde kolumn 7 (SE2 FAST 1 år pris)
    fil_SE2_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[5]), reverse=True))
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][0])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][1])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][5])
    hogsta_lgh_graf.append(fil_SE2_sorted_lgh[0][5])
#Sorterar på min värde kolumn 10 (SE3 FAST 1 år pris)
    fil_SE3_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[8])))
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][0])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][1])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][8])
    lagsta_lgh_graf.append(fil_SE3_sorted_lgh[0][8])
    medelvalue2(fil_SE3_sorted_lgh, 8)
#Sorterar på max värde kolumn 10 (SE3 FAST 1 år pris)
    fil_SE3_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[8]), reverse=True))
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][0])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][1])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][8])
    hogsta_lgh_graf.append(fil_SE3_sorted_lgh[0][8])
#Sorterar på min värde kolumn 13 (SE4 FAST 1 år pris)
    fil_SE4_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[11])))
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][0])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][1])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][11])
    lagsta_lgh_graf.append(fil_SE4_sorted_lgh[0][11])
    medelvalue2(fil_SE4_sorted_lgh, 11)
#Sorterar på max värde kolumn 13 (SE4 FAST 1 år pris)
    fil_SE4_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[11]), reverse=True))
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][0])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][1])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][11])
    hogsta_lgh_graf.append(fil_SE4_sorted_lgh[0][11])
    
if pris_avtal == 'F3':
    pris_avtal = ('Fast 3 år')
    for row in fil1:
        fil3_resultat.append(row)
    for row in fil2:
        fil4_resultat.append(row)

#Sorterar på min värde kolumn 4 (SE1 FAST 3 år pris)
    fil_SE1_sorted = (sorted(fil3_resultat, key = lambda x: float(x[3])))
    fil_SE1_resultat.append(fil_SE1_sorted[0][0])
    fil_SE1_resultat.append(fil_SE1_sorted[0][1])
    fil_SE1_resultat.append(fil_SE1_sorted[0][3])
    lagsta_villa_graf.append(fil_SE1_sorted[0][3])
    medelvalue1(fil_SE1_sorted, 3)
#Sorterar på max värde kolumn 4 (SE1 FAST 3 år pris)
    fil_SE1_sorted = (sorted(fil3_resultat, key = lambda x: float(x[3]), reverse=True))
    fil_SE1_resultat.append(fil_SE1_sorted[0][0])
    fil_SE1_resultat.append(fil_SE1_sorted[0][1])
    fil_SE1_resultat.append(fil_SE1_sorted[0][3])
    hogsta_villa_graf.append(fil_SE1_sorted[0][3])
    #Sorterar på min värde kolumn 7 (SE2 FAST 3 år pris)
    fil_SE2_sorted = (sorted(fil3_resultat, key = lambda x: float(x[6])))
    fil_SE2_resultat.append(fil_SE2_sorted[0][0])
    fil_SE2_resultat.append(fil_SE2_sorted[0][1])
    fil_SE2_resultat.append(fil_SE2_sorted[0][6])
    lagsta_villa_graf.append(fil_SE2_sorted[0][6])
    medelvalue1(fil_SE2_sorted, 6)
#Sorterar på max värde kolumn 7 (SE2 FAST 3 år pris)
    fil_SE2_sorted = (sorted(fil3_resultat, key = lambda x: float(x[6]), reverse=True))
    fil_SE2_resultat.append(fil_SE2_sorted[0][0])
    fil_SE2_resultat.append(fil_SE2_sorted[0][1])
    fil_SE2_resultat.append(fil_SE2_sorted[0][6])
    hogsta_villa_graf.append(fil_SE2_sorted[0][6])
#Sorterar på min värde kolumn 10 (SE3 FAST 3 år pris)
    fil_SE3_sorted = (sorted(fil3_resultat, key = lambda x: float(x[9])))
    fil_SE3_resultat.append(fil_SE3_sorted[0][0])
    fil_SE3_resultat.append(fil_SE3_sorted[0][1])
    fil_SE3_resultat.append(fil_SE3_sorted[0][9])
    lagsta_villa_graf.append(fil_SE3_sorted[0][9])
    medelvalue1(fil_SE3_sorted, 9)
#Sorterar på max värde kolumn 10 (SE3 FAST 3 år pris)
    fil_SE3_sorted = (sorted(fil3_resultat, key = lambda x: float(x[9]), reverse=True))
    fil_SE3_resultat.append(fil_SE3_sorted[0][0])
    fil_SE3_resultat.append(fil_SE3_sorted[0][1])
    fil_SE3_resultat.append(fil_SE3_sorted[0][9])
    hogsta_villa_graf.append(fil_SE3_sorted[0][9])
#Sorterar på min värde kolumn 13 (SE4 FAST 3 år pris)
    fil_SE4_sorted = (sorted(fil3_resultat, key = lambda x: float(x[12])))
    fil_SE4_resultat.append(fil_SE4_sorted[0][0])
    fil_SE4_resultat.append(fil_SE4_sorted[0][1])
    fil_SE4_resultat.append(fil_SE4_sorted[0][12])
    lagsta_villa_graf.append(fil_SE4_sorted[0][12])
    medelvalue1(fil_SE4_sorted, 12)
#Sorterar på max värde kolumn 13 (SE4 FAST 3 år pris)
    fil_SE4_sorted = (sorted(fil3_resultat, key = lambda x: float(x[12]), reverse=True))
    fil_SE4_resultat.append(fil_SE4_sorted[0][0])
    fil_SE4_resultat.append(fil_SE4_sorted[0][1])
    fil_SE4_resultat.append(fil_SE4_sorted[0][12])
    hogsta_villa_graf.append(fil_SE4_sorted[0][12])

####LGH DATA####
                      

#Sorterar på min värde kolumn 4 (SE1 FAST 3 år pris)
    fil_SE1_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[3])))
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][0])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][1])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][3])
    medelvalue2(fil_SE1_sorted_lgh, 3)
#Sorterar på max värde kolumn 4 (SE1 FAST 3 år pris)
    fil_SE1_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[3]), reverse=True))
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][0])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][1])
    fil_SE1_resultat_lgh.append(fil_SE1_sorted_lgh[0][3])

#Sorterar på min värde kolumn 7 (SE2 FAST 3 år pris)
    fil_SE2_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[6])))
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][0])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][1])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][6])
    medelvalue2(fil_SE3_sorted_lgh, 6)
#Sorterar på max värde kolumn 7 (SE2 FAST 3 år pris)
    fil_SE2_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[6]), reverse=True))
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][0])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][1])
    fil_SE2_resultat_lgh.append(fil_SE2_sorted_lgh[0][6])
#Sorterar på min värde kolumn 10 (SE3 FAST 3 år pris)
    fil_SE3_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[9])))
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][0])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][1])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][9])
    medelvalue2(fil_SE3_sorted_lgh, 9)
#Sorterar på max värde kolumn 10 (SE3 FAST 3 år pris)
    fil_SE3_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[9]), reverse=True))
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][0])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][1])
    fil_SE3_resultat_lgh.append(fil_SE3_sorted_lgh[0][9])
#Sorterar på min värde kolumn 13 (SE4 FAST 3 år pris)
    fil_SE4_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[12])))
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][0])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][1])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][12])
    medelvalue2(fil_SE4_sorted_lgh, 12)
#Sorterar på max värde kolumn 13 (SE4 FAST 3 år pris)
    fil_SE4_sorted_lgh = (sorted(fil4_resultat, key = lambda x: float(x[12]), reverse=True))
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][0])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][1])
    fil_SE4_resultat_lgh.append(fil_SE4_sorted_lgh[0][12])
    
#Gör om float till str för att presentera i graf
for i in range(0, len(medel_varde_villa)):
    medel_varde_villa[i] = str(medel_varde_villa[i])

for i in range(0, len(medel_varde_lgh)):
    medel_varde_lgh[i] = str(medel_varde_lgh[i])


print('=================================================================================================================')
print('\n')
print(f'{"Lägsta, högsta- och medelvärden av elpriserna":>80}')
print(f'{"under tidsperioden 2018-2023 för ":>70}{pris_avtal}')

print('\n')
print(f'{"Prisomr.":<10}{"lägsta":>10}{"år":>10}{"mån":>10}{"högsta":>10}{"år":>10}{"mån":>10}{"medel":>15}')
print('------------------------------------------------------------------------------------------------------------------')
print('Kategori lägenhetskund:')
print(f'{"SE1"}{fil_SE1_resultat_lgh[2]:>16}{fil_SE1_resultat_lgh[0]:>13}{fil_SE1_resultat_lgh[1][:3]:>8}{fil_SE1_resultat_lgh[5]:>12}{fil_SE1_resultat_lgh[3]:>8}{fil_SE1_resultat_lgh[4][:3]:>10}{medel_varde_lgh[0]:>14}')
print(f'{"SE2"}{fil_SE2_resultat_lgh[2]:>16}{fil_SE2_resultat_lgh[0]:>13}{fil_SE2_resultat_lgh[1][:3]:>8}{fil_SE2_resultat_lgh[5]:>12}{fil_SE2_resultat_lgh[3]:>8}{fil_SE2_resultat_lgh[4][:3]:>10}{medel_varde_lgh[1]:>14}')
print(f'{"SE3"}{fil_SE3_resultat_lgh[2]:>16}{fil_SE3_resultat_lgh[0]:>13}{fil_SE3_resultat_lgh[1][:3]:>8}{fil_SE3_resultat_lgh[5]:>12}{fil_SE3_resultat_lgh[3]:>8}{fil_SE3_resultat_lgh[4][:3]:>10}{medel_varde_lgh[2]:>14}')
print(f'{"SE4"}{fil_SE4_resultat_lgh[2]:>16}{fil_SE4_resultat_lgh[0]:>13}{fil_SE4_resultat_lgh[1][:3]:>8}{fil_SE4_resultat_lgh[5]:>12}{fil_SE4_resultat_lgh[3]:>8}{fil_SE4_resultat_lgh[4][:3]:>10}{medel_varde_lgh[3]:>14}')
print('Kategori villakund:')
print(f'{"SE1"}{fil_SE1_resultat[2]:>16}{fil_SE1_resultat[0]:>13}{fil_SE1_resultat[1][:3]:>8}{fil_SE1_resultat[5]:>12}{fil_SE1_resultat[3]:>8}{fil_SE1_resultat[4][:3]:>10}{medel_varde_villa[0]:>14}')
print(f'{"SE2"}{fil_SE2_resultat[2]:>16}{fil_SE2_resultat[0]:>13}{fil_SE2_resultat[1][:3]:>8}{fil_SE2_resultat[5]:>12}{fil_SE2_resultat[3]:>8}{fil_SE2_resultat[4][:3]:>10}{medel_varde_villa[1]:>14}')
print(f'{"SE3"}{fil_SE3_resultat[2]:>16}{fil_SE3_resultat[0]:>13}{fil_SE3_resultat[1][:3]:>8}{fil_SE3_resultat[5]:>12}{fil_SE3_resultat[3]:>8}{fil_SE3_resultat[4][:3]:>10}{medel_varde_villa[2]:>14}')
print(f'{"SE4"}{fil_SE4_resultat[2]:>16}{fil_SE4_resultat[0]:>13}{fil_SE4_resultat[1][:3]:>8}{fil_SE4_resultat[5]:>12}{fil_SE4_resultat[3]:>8}{fil_SE4_resultat[4][:3]:>10}{medel_varde_villa[3]:>14}')






plt.figure().set_figwidth(12)
plt.subplot(1,2,1)
x = [0,2,4,6]

SES = ['SE1', 'SE2', 'SE3', 'SE4' ]


#plt.xlim(0, 800)

# Skapa diagram1 och lägg till staplarna
plt.tight_layout()
plt.plot(x, lagsta_lgh_graf[:4], 'o', label='rörlig min')
plt.plot(x, medel_varde_lgh, 'o', label='rörlig medel')
plt.plot(x, hogsta_lgh_graf[:4], 'o', label='rörlig max')
plt.subplots_adjust(wspace=.2)
plt.xticks(x, SES, rotation=90 ) #
plt.ylabel('Pris[öre/KWh]')
plt.title(f'Elpriser\nLägsta-, högsta och medelvärde under 2018-2023.\nKategori Lägenhetskund - {pris_avtal} avtal.')
 

plt.xlabel('Prisområden')
plt.grid()


#Skapa diagram2 och lägg till staplarna
plt.subplot(1,2,2)

plt.plot(x, lagsta_villa_graf[:4], 'o', label='fast 3år - min')
plt.plot(x, medel_varde_villa, 'o', label='fast 3år - medel')
plt.plot(x, hogsta_villa_graf[:4], 'o',  label='fast 3år - max')


plt.ylabel('Pris[öre/KWh]')
plt.title(f'Elpriser\nLägsta-, högsta och medelvärde under 2018-2023.\nKategori Villakund - {pris_avtal} avtal.')
plt.xticks([i + 0.50 for i in x], ['SE1', 'SE2', 'SE3', 'SE4' ])
plt.xticks(rotation=90)
plt.xlabel('Prisområden')
plt.grid()



# Visa diagrammet


plt.show()