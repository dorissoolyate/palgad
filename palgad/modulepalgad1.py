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