"""
Exercice de programation de la méthode ispalindrome()
"""
#### Fonction secondaire


def ispalindrome(p):
    """
    Permet de vérifier si la phrase ou le mot mis en paramètre est un palindrome

        Args:
            p: palindrome à vérifier

        Returns:
            True : p est un palindrome
            False : p n'est pas un palindrome
    """

    x = "éèàçùïöüäîôâëê"
    y = "eeacuiouaioaee"
    z = " '-_,!?;:/()|}{[]#&"
    modif = str.maketrans(x,y,z)
    smin = p.lower()
    scompare = smin.translate(modif)
    spalin = scompare[::-1]

    if spalin == scompare :
        return True
    return False

#### Fonction principale


def main():
    """
    Testes pour la méthode ispalindrome()
    """

    # vos appels à la fonction secondaire ici
    print(ispalindrome("Je vais à l'ESIEE"))
    print(ispalindrome("Rêver"))
    print(ispalindrome("TnT"))

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
