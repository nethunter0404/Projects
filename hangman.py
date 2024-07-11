hosgeldin = print("Let's play hangman!")
gizli_kelime = "Slipknot"
bosliste = ["_"] * len(gizli_kelime)
kalan_can = 5
while kalan_can > 0:
    tahmin = input("Harf Gir : ")
    if tahmin in gizli_kelime:
        for i in range(len(gizli_kelime)):
            if gizli_kelime[i].lower() and gizli_kelime[i].upper() == tahmin.lower() and tahmin.upper():
                bosliste[i] = gizli_kelime[i]
        print("Doğru")
    else:
        kalan_can -= 1
        print("Yanlış. Kalan can:", kalan_can)
    
    print("_".join(bosliste))
    
    if "_" not in bosliste:
        print("Tebrikler! Gizli kelimeyi buldunuz:", gizli_kelime)
        break
else:
    print("Maalesef, kaybettiniz. Gizli kelime:", gizli_kelime)
