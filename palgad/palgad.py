from modulepalgad1 import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("0-Andmed ekraanile\n1-Andmete lisamine\n2-Andmete kustutamine\n3-Naitab suurima palka\n4-Naitab vaiksema palka\n5-Sorteerib")
    vastus=int(input())
    if vastus==0:
        naita_andmed(inimesed,palgad)
    elif vastus==1:
        inimesed,palgad=andmete_lisamine(inimesed,palgad)
    elif vastus==2:
        inimesed,palgad=andmete_kustutamine(inimesed,palgad)
    elif vastus==3:
        rikkad_inimesed=suurim_palk(inimesed,palgad)
        print(rikkad_inimesed)
    elif vastus==4:
        poor_inimesed=vaiksem_palk(inimesed,palgad)
        print(poor_inimesed)
    elif vastus==5:
        inimesed,palgad=sorteerinime(inimesed,palgad)
        