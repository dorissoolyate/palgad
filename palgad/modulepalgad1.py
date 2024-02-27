# 1
def lisa_inimene_ja_palk(inimesed:str, palgad:float)->any:
    """Lisab uue inimese ja palka.

    """
    inimene=input("Sisestage uue inimese nimi: ")
    palk=float(input("Sisestage selle inimese palk: "))
    inimesed.append(inimene)
    palgad.append(palk)

# 3
def suurim_palk(inimesed:str, palgad:float)->any:
   """Leiab kõrgeima palgaga inimese.
   
   """
   if not inimesed:
       print("Andmelist on tühi.")
       return None, None
   max_salary=max(inimesed)
   max_index=inimesed.index(max_salary)
   max_person=inimesed[max_index]
   return max_person, max_salary

# 4
def vaikseim_palk(inimesed:str, palgad:float)->any:
   """Leiab miinimumpalga ja selle saaja.
   
   """
   min_palk=min(palgad)
   indeks=palgad.index(min_palk)
   saaja=inimesed[indeks]
   return min_palk, saaja

# 6
def inimesed_sama_palgaga(inimesed:str, palgad:float)->any:
   """Leiab ja kuvab teavet samapalgaliste inimeste kohta.
   
   """
   sama_palgaga = {}
   for i in range(len(inimesed)):
       inimene=inimesed[i]
       palk=palgad[i]
       if palk in sama_palgaga:
           sama_palgaga[palk].append(inimene)
       else:
           sama_palgaga[palk]=[inimene]  
   for palk, inimesed in sama_palgaga.items():
       if len(inimesed) > 1:
           print(f"Palk: {palk},inimeste arv : {len(inimesed)}")
           print("Inimesi:", end=" ")
           for inimene in inimesed:
               print(inimene, end=", ")
           print()

# 7
def otsi_palk_nime_jargi(inimesed:str, palgad:float, nimi:str)->any:
   """Leiab ja väljastab kõik palgad konkreetse nime jaoks.
   
   """
   leitud = False
   for i in range(len(inimesed)):
       if inimesed[i]==nimi:
           if not leitud:
               print(f"Palgad nimele {nimi}:")
               leitud=True
           print(palgad[i])
   if not leitud:
       print(f"Nimi {nimi} pole leitud nimekirjast.")