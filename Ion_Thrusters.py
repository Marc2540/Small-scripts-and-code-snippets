#!/usr/bin/python
#python 3.3.0
#Marc2540

from time import sleep

configFile = open("config.txt", "r")

print ('Velkommen til 2. fase af Ion-Thrusters')
sleep(2)

print ('')

sleep(1)
Auto=input('Vil du loade resultater fra Fase 1? ')
print('')

if Auto.lower()[:2]=='ja' or Auto.lower()[0]=='y':
    for line in configFile:
        if "score=" in line:
            score=line
#            print (line)
            H_atoms=int(score[8])
            O_atoms=int(score[12])
            Na_atoms=int(score[17])
            Mg_atoms=int(score[22])
            Cl_atoms=int(score[27])
            Br_atoms=int(score[-1])
#    print (score)
#    print (H_atoms)
#    print (O_atoms)
#    print (Na_atoms)
#    print (Mg_atoms)
#    print (Cl_atoms)
#    print (Br_atoms)
#    sleep(20)
    configFile.close()
else:
    try:
        print ('')
        print ('(Skriv venligst kun tal i kommende besvarelser.)')
        sleep(0.5)
        H_atoms=int(input ('Hvor mange H-atomer fik du? '))
        O_atoms=int(input ('Hvor mange O-atomer fik du? '))
        Na_atoms=int(input ('Hvor mange Na-atomer fik du? '))
        Mg_atoms=int(input ('Hvor mange Mg-atomer fik du? '))
        Cl_atoms=int(input ('Hvor mange Cl-atomer fik du? '))
        Br_atoms=int(input ('Hvor mange Br-atomer fik du? '))
    except:
        print('Du skrev noget som ikke er tal. Genstart spillet.')
        sleep(10)
        exit()
print ('')

if type(H_atoms) == int:
    if type(O_atoms) == int:
        if type(Na_atoms) == int:
            if type(Mg_atoms) == int:
                if type(Cl_atoms) == int:
                    if type(Br_atoms) == int:
                        integer_input = 'true'
else:
    integer_input = 'false'

#Spørg efter formel for sammensatte H og O atomer
if integer_input == 'true':
    print ("For det næste spørgsmål, skriv venligst svaret som: 'Antal molekyler' + 'atombogstav' + 'antal af atombogstavet.'")
    sleep(0.2)
    print ("For eksempel: 1H4O9 eller 5Na1O7")
    print ('')
    input('<Enter>')
    print ('')
    print ('Inkluder venligst altid et antal foran, også selvom du kun har 1 af atomet/molekylet.')
    print ('')
    input('<Enter>')
    print ('')
    print ('')
    print ('Hvilket atom, og hvor mange af dem, får du hvis du sætter dine ' + str(H_atoms) + ' H+ atomer sammen med dine ' + str(O_atoms) + ' O-- atomer?')
    print ('')
    H_and_O=input ('Svar: ')
else:
    print('What the fuck did you do? You broke it!')
    sleep(10)
    exit()

score=0
#Tjek hvis H og O passer sammen.
if int(H_and_O[2])/2 == int(H_and_O[4]):
    if int(H_and_O[0])!= 0:
        if int(H_and_O[0])*int(H_and_O[2]) <= H_atoms:
            if int(H_and_O[0])*int(H_and_O[4]) <= O_atoms:
                print ('Korrekt! Godt gået.')
                print ('')
                H2O='true'
                score+=1500
                print ('Score: ' + str(score))
            else:
                print ('Forkert, genstart spillet og prøv igen')
        else:
            print ('Forkert, genstart spillet og prøv igen')
    else:
        print ('Kan du ikke lave nogen af disse atomer?')
        print ('')
        sleep(2)
        print ('Too bad.')


#Spørg efter navn på H2O
if H2O=='true':
    print ('Nu har du lige lavet molekylet H2O, hvad er dens navn?')
    H2O_ans=input('Svar: ')
    if H2O_ans.lower()=='vand':
        print ('Korrekt.')
        score+=1500
        print ('Score: ' + str(score))
        sleep(2)
    elif H2O_ans.lower()=='hydrogenoxid':
        print ('Korrekt.')
        score+=1500
        print ('Score: ' + str(score))
        sleep(2)
    elif H2O_ans.lower()=='dihydrogenoxid':
        print ('Ja, det navn kan også bruges.')
        score+=1000
        print ('Score: ' + str(score))
        sleep(2)
    else:
        print ('Forkert.')
        sleep(4)


#Spørg efter formel for sammensatte Na og Cl atomer
if integer_input == 'true':
    print ('')
    print ('Hvilket atom, og hvor mange af dem, får du hvis du sætter dine ' + str(Na_atoms) + ' Na+ atomer sammen med dine ' + str(Cl_atoms) + ' Cl- atomer?')
    print ('')
    Na_and_Cl=input ('Svar: ')
else:
    print('What the fuck did you do? You broke it!')


#Tjek hvis Na og Cl passer sammen.
if int(Na_and_Cl[3]) == int(Na_and_Cl[6]):
    if int(Na_and_Cl[0])!= 0:
        if int(Na_and_Cl[0])*int(Na_and_Cl[3]) <= Na_atoms:
            if int(Na_and_Cl[0])*int(Na_and_Cl[6]) <= Cl_atoms:
                print ('Korrekt! Godt gået.')
                print ('')
                NaCl='true'
                score+=1500
                print ('Score: ' + str(score))
            else:
                print ('Forkert, genstart spillet og prøv igen')
        else:
            print ('Forkert, genstart spillet og prøv igen')
    else:
        print ('Kan du ikke lave nogen af disse atomer?')
        print ('')
        sleep(2)
        print ('Too bad.')

#Spørg efter navn på NaCl
if NaCl=='true':
    print ('Nu har du lige lavet molekylet NaCl, hvad er dens navn?')
    NaCl_ans=input('Svar: ')
    if NaCl_ans.lower()=='natriumchlorid':
        print ('Korrekt!')
        score+=1500
        print ('Score: ' + str(score))
        sleep(4)
    elif NaCl_ans.lower()=='salt':
        print ('Ja, det navn kan også bruges.')
        score+=1000
        print ('Score: ' + str(score))
        sleep(4)
    elif NaCl_ans.lower()=='køkkensalt':
        print ('Ja, det navn kan også bruges.')
        score+=1000
        print ('Score: ' + str(score))
        sleep(4)
    else:
        print ('Forkert')
        sleep(4)




#Spørg efter formel for sammensatte Mg++ og Br- atomer
if integer_input == 'true':
    print ('')
    print ('Hvilket atom, og hvor mange af dem, får du hvis du sætter dine ' + str(Mg_atoms) + ' Mg++ atomer sammen med dine ' + str(Br_atoms) + ' Br- atomer?')
    print ('')
    Mg_and_Br=input ('Svar: ')
else:
    print('What the fuck did you do? You broke it!')


#Tjek hvis Mg og Br passer sammen.
if int(Mg_and_Br[3]) == int(Mg_and_Br[6])/2:
    if int(Mg_and_Br[0])!= 0:
        if int(Mg_and_Br[0])*int(Mg_and_Br[3]) <= Mg_atoms:
            if int(Mg_and_Br[0])*int(Mg_and_Br[6]) <= Br_atoms:
                print ('Korrekt! Godt gået.')
                print ('')
                MgBr2='true'
                score+=1500
                print ('Score: ' + str(score))
            else:
                print ('Forkert, genstart spillet og prøv igen')
        else:
            print ('Forkert, genstart spillet og prøv igen')
    else:
        print ('Kan du ikke lave nogen af disse atomer?')
        print ('')
        sleep(2)
        print ('Too bad.')


#Spørg efter navn på MgBr2
if MgBr2=='true':
    print ('Nu har du lige lavet molekylet MgBr2, hvad er dens navn?')
    MgBr2_ans=input('Svar: ')
    if MgBr2_ans.lower()=='magnesiumbromid':
        print ('Korrekt')
        score+=1500
        print ('Score: ' + str(score))
        sleep(2)
    elif MgBr2_ans.lower()=='magnesiumdibromid':
        print ('Ja, det navn kan også bruges.')
        score+=1000
        print ('Score: ' + str(score))
        sleep(2)
    else:
        print ('Forkert')
        sleep(4)


#High-score printing
print ('')
print ('')
print ('')
print ('')
print ('')
sleep(0.2)
print ('Your score: ' + str(score) + ' points.')
sleep(2)
print ('')
print ('Highscore list:')
print ('')
sleep(1)
print ('   Marcus: 9001 points.')
sleep(1)
print ('   Alf:    7777 points.')
sleep(1)
print ('   Mads H: 1337 points.')
sleep(1)
print ('   Rune:   666  points.')
sleep(10)
