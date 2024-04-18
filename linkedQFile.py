class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
#____________________________________________________________________________________________________________________________________________________________________
        
class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None
            
        
    def enqueue(self, card):
        # lägg till ett kort längst ner i kön
        new_card = Node(card)
        # olika metoder om kön är tom eller inte
        if self.__first == None:
            self.__first = new_card
            self.__last = new_card
        else:
            self.__last.next = new_card
            self.__last = new_card


    def dequeue(self):
        # ta ut det översta kortet
        if not self.isEmpty():
            pop = self.__first.value
            self.__first = self.__first.next
            return pop


    def isEmpty(self):
        # kontrollera om korthögen är tom
        return self.__first == None


    def size(self):
        # kolla antalet kort
        count = 0
        if self.__first != None:
            pass
            # fortsättning behövs
    
    def peek(self):
        #tittar på nästa värde i kön utan att skriva ut den
         return self.__first.value
        


""" 
1. vi bygger en BinHeap 
2. Hur vår BinHeap kan vi göra en prioritetskö (där sorteringen kommer in)
3. När vi sedan har gjort det kan vi implementera dijkstraws algorithem
4. Varje gång vi 

1. Hur ska vi sortera? då vi inte får nummer till vår funktion.
2. Vå måste hålla kol på hur vi tar oss tillbaka till den förra staden för att uppdatera vår estimation.
3.

viktiga saker:
1. Alla våra edges måste vara = 1

Backlog: Sorteringen är off.




class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def sortUp(self, i):
        while i // 2 > 0: # Fungerar endast då det är en binary heap.
            if self.heapList[i].value < self.heapList[i//2].value:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    # Den här ska a
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.sortUp(self.currentSize) # Steg 1

    
    # Vi tar sista elementet i vår lista och sorterar ner det igenom för att hålla kvar strukturen
    
    def sortDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i].value > self.heapList[mc].value:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize: # kollar om vi har ett höger värde 
            return i * 2
        else:
            if self.heapList[i*2].value < self.heapList[i * 2 +1].value: # Jämför vänsta värdet med högra värdet
                return i * 2
            else: 
                return i * 2 + 1
    
    def isEmpty(self):
        return self.currentSize == 0
    
    def delMin(self):
        retval = self.heapList[1] # Hämtar första värdet.
        self.heapList[1] = self.heapList[self.currentSize] # hämtar sista elementet i listan och sätter det längst upp
        self.currentSize = self.currentSize - 1
        self.heapList.pop() # tar bort det sista värdet då det läggs längst framm
        self.sortDown(1) # vi vill dra ner vårt värde på index 1
        return retval     
    
class ParentNode:
    def __init__(self, word, parent = None, value=0):
        self.word = word
        self.parent = parent   
        self.value = value # Vikten står för modernoden:
        
    

class PriorityQue(BinHeap):
    
    def __init__(self):
        super().__init__() # init
        
    def enqueue(self, item):
            self.insert(item)
        
    def dequeue(self):
            return self.delMin()
        
    def isEmpty(self):
        # kontrollera om korthögen är tom
            return self.isEmpty()
    """