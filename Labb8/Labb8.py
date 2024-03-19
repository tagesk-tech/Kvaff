
from linkedQFile import LinkedQ

""" 
1. Vårt mål här är att bryta ned alla fraser rekursivt och kontrollera att allting stämmer
 

"""

class GrammatikFel(Exception):
    pass # Läs sedan vad det här är och vad det betyder?



def kontrolleraMolekyl(molekyl):
    kontrolleraAtom(molekyl)
    if molekyl.peek() == ".":
        molekyl.dequeue()
    else:
        kontrolleraNummer(molekyl)

    

def kontrolleraAtom(molekyl):
    kontrolleraStorBokstav(molekyl)
    if molekyl.peek().isalpha():
        kontrolleraLitenBokstav(molekyl)
    
        

def kontrolleraStorBokstav(molekyl):
    storBokstav = molekyl.dequeue()
    if storBokstav.isupper():
        return
    raise GrammatikFel("Fel alla molekyler måste börja med stor bokstav: " + storBokstav)

def kontrolleraLitenBokstav(molekyl):
    litenBokstav = molekyl.dequeue()
    if litenBokstav.islower():
        return
    raise GrammatikFel("Fel alla andra bokstäver måste vara liten: " + litenBokstav)

def kontrolleraNummer(molekyl):
    # Jag förstår inte riktigt men jag tror att det kan lösa sig senare.
    nr_str = ""
    while molekyl.peek() != ".":
        char = molekyl.dequeue()
        nr_str += char
    num = int(nr_str)
    if num > 1:
        return    
    raise GrammatikFel("för litet tal vid radslutet" + str(num))
        
    

def kollaGrammatiken(molekyl):
    molekyl = bryt_Ned_Molekyl(molekyl)
    
    try:
        kontrolleraMolekyl(molekyl)
        return "Följer vår syntax"
    except GrammatikFel as fel:
        return str(fel)

def bryt_Ned_Molekyl(molekyl):
    q = LinkedQ()
    for char in molekyl: # Iterera över varje tecken
        q.enqueue(char)
    q.enqueue(".")
    return q

def main():
    molekyl = input("Skriv ditt MolekylNamn: ")
    resultat = kollaGrammatiken(molekyl)
    print(resultat)

import unittest


class SyntaxTest(unittest.TestCase):
    
    # Testet fungerar på det sättet att du skriver given input och förklarar vad som ska komma ut från det
    def testSubjmolekyl(self):
        self.assertEqual(kollaGrammatiken("He25"), "Följer vår syntax")

    def testFelmolekyl(self):
        self.assertEqual(kollaGrammatiken("HE25"), "Fel alla andra bokstäver måste vara liten: E")

if __name__ == '__main__':
    unittest.main() 

