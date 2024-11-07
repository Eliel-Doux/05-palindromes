#### Fonction secondaire
'''on importe unidecode'''
import string
from unidecode import unidecode
def ispalindrome(p):
    '''fonction'''
    p = unidecode(p.replace(" ", "")).lower()
    p = p.translate(str.maketrans("", "", string.punctuation))
    if p == p[::-1]:
        return True
    return False
#### Fonction principale
def main():
    '''fonction'''
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
if __name__ == "__main__":
    main()
