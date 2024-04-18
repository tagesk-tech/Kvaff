from molgrafik import *
from linkedQFile import LinkedQ
from tkinter import *
from atomweights import *

# Molekyler som vi vill rita upp: O, CO2 och (CH3)2(CH2)4.
# Vill ha pekarna next och down i binärträdet.


class Syntax_error(Exception): # skapa en exception för syntaxfel
    pass 


def rest_molecule(molecule): # skapa en sträng av resten av molekylen
    atom_str = ""
    while molecule.peek()!= ".":
        atom_str += molecule.dequeue()
    return atom_str


# skapa en lista med alla atomer som är 'korrekta'
atomer = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Fl", "Lv"]


def check_atomlist(atom, molecule): # Kontrollera om atomen finns i atomlistan
    if atom in atomer:
        return
    else:
        raise Syntax_error("Okänd atom vid radslutet " + rest_molecule(molecule))


# det första vi gör är att bryta ned molekylen till en kö
def check_syntax(molecule):
    molecule = break_molecule(molecule) # Bryt ned molekylen till en kö
    try:
        mg = Molgrafik()
        mol = read_formula(molecule)
        weight = total_weight(mol)
        mg.show(mol)
        print('Vikt: ' + str(weight))
        return "Formeln är syntaktiskt korrekt"
    except Syntax_error as error:
        return str(error)
    

def break_molecule(molecule):
    formula = LinkedQ()
    for char in molecule: # Iterera över varje tecken
        formula.enqueue(char)
    formula.enqueue(".") # Lägg till en punkt i slutet som markerar slutet på molekylen
    return formula


def read_formula(molecule): # Kontrollera formeln
    mol = read_molecule(molecule)
    if not molecule.isEmpty() and molecule.peek() == ")":
        raise Syntax_error("Felaktig gruppstart vid radslutet " + rest_molecule(molecule))
    return mol


def read_molecule(molecule):
    mol = read_group(molecule) # Kontrollera grupp
    return mol
    

    
def read_group(molecule): # Kontrollera grupp
    square = Ruta() # Skapa en ruta
    if molecule.peek() == "(": # Kontrollera om det är en vänsterparentes
        molecule.dequeue()
        square.down = read_group(molecule)
        if molecule.peek() == ")": # Kontrollera om det är en högerparentes
            molecule.dequeue()
            if molecule.peek().isdigit(): # Kontrollera om det är en siffra efter högerparentesen
                square.num = read_numbers(molecule)
                if molecule.peek() == "(":# om det kommer ännu fler parenteser efter att de föregående har stängts
                    square.next = read_group(molecule)
            else:
                    raise Syntax_error("Saknad siffra vid radslutet " + rest_molecule(molecule))
        else:
            raise Syntax_error("Saknad högerparentes vid radslutet " + rest_molecule(molecule))
    elif molecule.peek().isdigit():
        raise Syntax_error("Felaktig gruppstart vid radslutet " + rest_molecule(molecule))
    else:
        square.atom, square.num = read_atom(molecule, square)
        if molecule.peek() != '.' and molecule.peek() != ')':
            square.next = read_group(molecule)

    return square


def read_atom(molecule, square): # Kontrollera atom
    atom = read_letters(molecule) # Kontrollera bokstäver
    if molecule.peek().isdigit(): # Kontrollera om det är en siffra efter bokstäverna
        num = read_numbers(molecule)
        if molecule.peek() != "." and molecule.peek() != ")":
            square.next = read_group(molecule)
        return atom, num
    else:
        if molecule.peek() != "." and molecule.peek() != ")" and molecule.peek() != "(":
            square.next = read_group(molecule)
    num = 1
    return atom, num
    

def read_letters(molecule): # kontrollera bokstäver
    big_letter = molecule.peek()
    if big_letter.isupper(): # Kontrollera att det är en stor bokstav
        atom_Aa = ""
        atom_Aa += molecule.dequeue()
        if molecule.peek().isalpha() and molecule.peek().islower(): 
            atom_Aa += molecule.dequeue() # ta bort stor bokstav
            check_atomlist(atom_Aa, molecule) # Kontrollera atomlistan
            return atom_Aa
        check_atomlist(big_letter, molecule) # Kontrollera atomlistan
        return atom_Aa
    raise Syntax_error("Saknad stor bokstav vid radslutet " + rest_molecule(molecule))


def read_numbers(molecule): # kontrollera nummer
    nr_str = ""
    while molecule.peek() != "." and molecule.peek().isdigit(): # Samla alla siffror för att kontrollera värdet
        char = molecule.dequeue()
        nr_str += char
    num = int(nr_str)
    if num > 1 and nr_str[0] != "0": # Kontrollera att numret är större än 1 och att det inte börjar med 0
        return num
    raise Syntax_error("För litet tal vid radslutet " + nr_str[1:] + rest_molecule(molecule)) 

    

def total_weight(mol): # fungerar ej med parenteser
    if mol.atom !='()':
        atom_weight = atom_weights[mol.atom]  
        weight = atom_weight * mol.num
        if mol.next is not None:
            weight += total_weight(mol.next)
    elif mol.atom == '()' and mol.down is not None and mol.next is not None:
        weight_down = total_weight(mol.down) * mol.num
        weight_next = total_weight(mol.next)
        weight = weight_down + weight_next
    elif mol.atom == '()' and mol.down is not None and mol.next is None:
        weight = total_weight(mol.down) * mol.num

    return weight
    


def main(): # Huvudfunktionen
    molecule = '(CH3)2(CH2)4' 
    while molecule != "#": # Om det inte är en hashtag så körs funktionen
        result = check_syntax(molecule)
        print(result)
        molecule = input("Ange en molekyl: ")


# Kör huvudfunktionen
#main()


import unittest
class SyntaxTest(unittest.TestCase):
    
    # Testet fungerar på det sättet att du skriver given input och förklarar vad som ska komma ut från det
    def testSubjmolekyl(self):
        self.assertEqual(check_syntax('O(C2(HOOH)2)2'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('NaCl(H2)2'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('(CH3)2(CH2)4'), "Formeln är syntaktiskt korrekt") # ska väga 86.17
        self.assertEqual(check_syntax('Si(H5(OH2)4)2(NaCl)2'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('Si(C3(COOH)2)4(H2O)7'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('H)H'), "Felaktig gruppstart vid radslutet )H")
        self.assertEqual(check_syntax("C(Xx4)5"), "Okänd atom vid radslutet 4)5")

if __name__ == '__main__':
    unittest.main()
