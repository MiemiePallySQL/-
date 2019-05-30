from random import shuffle
from math import ceil

class Deck:
    def __init__ (self):
        self._n = 54 # maintain the count of remaining cards
        self._deck = [i + 1 for i in range (0, 54)] # fundamental structure to maintain cards 

    def shuffle (self):
        shuffle(self._deck)

    def card_left (self):
        return self._n
    
    def remove_joker (self):
        if 53 in self._deck:           
            self._deck.remove(53)
            self._n += -1
        if 54 in self._deck:
            self._deck.remove(54)
            self._n += -1

    def draw (self):
        card_drawn = self._deck.pop(0)
        self._n += -1
        return card_drawn

    def distribute (self, party):
        if party >= 10:
            raise ValueError ('Too many headcounts.')
        else:
            distribution = []
            for i in range (party):
                distribution .append([])
            for j in range (ceil(self._n/party)):
                for k in range(party):
                    if self._n == 0:
                        break
                    else:
                        distribution[k].append(self.draw())
            return distribution
