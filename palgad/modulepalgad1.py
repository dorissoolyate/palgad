def andmete_lisamine(i:list,p:list)->any:
    """Lisab inimesi ja andmeid    
    
    """
    while True:
        try:
            n=int(input("Mitu inimest"))
            if n>0: break
        except:
            print("viga")
    for j in range(n):
        nimi=input("nimi: ")
        palk=int(input("palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p
def naita_andmed(i:list,p:list):
    """Naitab infot
    
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])        
def andmete_kustutamine(i:list,p:list)->any:
    """kustutab inimesi ja palka    
    """
    nimi=input("keda kustutame?(nimi)")
    if nimi not in i:
        print(f"{nimi} puudub")
    else:
        for j in range(len(i)):
            if nimi in i:
                p.pop(i.index(nimi))
                i.remove(nimi)
    return i,p            
def suurim_palk(i:list,p:list)->list:
    """naitab kellel on suurim palk
    
    """
    nimed=[]
    max_palk=max(p)
    ind=p.index(max_palk)
    for palk in p:
        if max_palk==palk:
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
            ind+=1
    return nimed 
def vaiksem_palk(i:list,p:list)->list:
    """naidab kellel on vaiksem palk
    """
    nimed=[]
    min_palk=min(p)
    ind=p.index(min_palk)
    for palk in p:
        if min_palk==palk:
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
            ind=1
    return nimed, min_palk
def sorteerinime(i:list,p:list)->any:
    """Sorteerib kasvavas ja kahanevas järjekorras koos nimedega
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[n],p[m]==p[m],p[n]
                i[n],i[m]==i[m],i[n]
    return i,p
def vornde_palk(i:list,p:list)->any:
    """Teada saada, kes saavad võrdset palka
    """
    if len(p)<2:
        print("Ei nae kes saavad võrdset palka")
    vornde_palk={}
    for i, p in zip(i,p):
        if p in vornde_palk:
            vornde_palk[p].append(i)
        else:
            vornde_palk[p]=[i]
    for p, persons in vornde_palk.items():
        if len(persons)>1:
            print(f"Palk {p}: {', '.join(i)}")
    return i,p 
def palgaotsing(i:list,p:list)->any:
    """Otsib palka nime jargi
    """
    nimi=input("Kelle palka otsime?")
    if nimi in i:
        index = i.index(nimi)
        print(f"{nimi} palk on {p[index]}.")
    else:
        print("Nimi ei ole leitud")
    return i,p    
def filtreerimine(i:list,p:list)->any:
    """Väljundab nimekirja inimestest (koos palgaga), kes saavad rohkem/vähem kui määratud summa
    """
    tingimus=input("Maara palga summa: ")
    if tingimus=="suurem":
        filtreeritud=[(i,p) for i,p in zip(i,p) if p>tingimus]
    elif tingimus == "vaiksem":
        filtreeritud = [(i,p) for i,p in zip(i,p) if p<tingimus]
    else:
        print("viga")    
    if filtreeritud:
        [print(f"{i}: {p}") for i,p in filtreeritud]
    else:
        print("Ei ole leitud")
    return i,p
def vaeseima_rikkamad(i:list,p:list)->any:
    """ T vaeseimad ja rikkamad inimesed
    """
    if i and p:
        sorted_data=sorted(zip(i,p), key=lambda x: x[1])
        print("Top vaesemaid:")
        for i,p in sorted_data[:3]:
            print(f"{i}: {p}")
        
        print("Top rikkamaid:")
        for i,p in sorted_data[-3:]:
            print(f"{i}: {p}")
    else:
        print("viga.")
    return i,p
def keskmine_palk(i:list,p:list)->any:
    """Keskmine palk ja selle saaja nimi/nimed
    """
    if p:
        keskmine=sum(p)/len(p)
        ala_kesk=[i for i,p in zip(i,p) if p>keskmine]
        inimene_kesk=[i for i,p in zip(i,p) if p==keskmine]
        print(f"Keskmine palk: {keskmine}")
        if ala_kesk:
            print("Keskmisest suurem:", ', '.join(ala_kesk))
        else:
            print("Ei ole sellist")
        if inimene_kesk:
            print("Inimene keskmise palgaga:", ', '.join(inimene_kesk))
        else:
            print("Ei ole sellist.")
    else:
        print("Viga")
    return i,p    