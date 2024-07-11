
def isBisextile(year):
    return( year%4==0 and not (year%100==0 and year%400!=0))

def verifDate(jour, mois, annee):
    if jour>31 or jour<1 or mois<1 or mois>12:
        return False
    elif (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12):
        return jour<=31
    elif (mois!=2): #( elif : le code rentre dans elif mais pas dans les autres conditions)
        return jour <=30
    else:   
        if isBisextile(annee):
            return jour <=29
        else:
            return jour <=28
    

jour = int(input("jour :"))
mois = int(input("mois :"))
annee = int(input("annee :"))

if( verifDate(jour, mois, annee)):
    print("la date est bonne")
else:
    print("la date n'est pas bonne")
