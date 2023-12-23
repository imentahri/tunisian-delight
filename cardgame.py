import random
random.seed(619)

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "Jack", "Queen", "King"]:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

class Game:
    def __init__(self,game_name):
        self.game_name = game_name

    def play(self,deck):
        pass

    def rank_to_value(self,rank):
        if rank == "Ace":
            return 1
        elif rank == "Jack":
            return 11
        elif rank == "Queen":
            return 12
        elif rank == "King":
            return 13
        else:
            return int(rank)
        
class SaharaAce(Game):
    def __init__(self):
        Game.__init__(self,"Sahara Ace")

    def play(self):
        deck = Deck()
        deck.shuffle()
        card = deck.draw()
        if card.rank == "Ace":
            return [True,10]
        else:
            return [False,0]

class TunisianTwins(Game):
    def __init__(self):
        Game.__init__(self,"Tunisian Twins")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        if card1.rank == card2.rank and card1.suit == card2.suit:
            return [True,50]
        else:
            return [False,0]
        
class MedinaBiggie(Game):
    def __init__(self):
        Game.__init__(self,"Medina Biggie")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        if self.rank_to_value(card2.rank) > self.rank_to_value(card1.rank):
            return [True,2]
        
        else:
            return [False,0]
        
class DesertHearts(Game):
    def __init__(self):
        Game.__init__(self,"Desert Hearts")
    def play(self):
        nb = 0
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        card3 = deck.draw()
        for card in [card1,card2,card3]:
            if card.suit == "Hearts":
                nb = nb + 1
        if nb>0:
            return [True,nb]
        else:
            return [False,0]

class OasisRunny(Game):
    def __init__(self):
        Game.__init__(self,"Oasis Runny")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        card3 = deck.draw()
        card4 = deck.draw()
        card5 = deck.draw()
        list = [card1,card2,card3,card4,card5]
        list.sort(key=lambda x: self.rank_to_value(x.rank))
        for i in range(0,len(list)-2):
            if self.rank_to_value(list[i+2].rank) - self.rank_to_value(list[i].rank) == 2:
                return [True,5]
        return [False,0]
    
class StudentGame(Game):
    def __init__(self):
        Game.__init__(self,"Student Game")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card1=deck.draw()
        card2=deck.draw()
        if (self.rank_to_value(card1.rank) + self.rank_to_value(card2.rank)) % 2 == 0:
            return [True,10]
        else:
            return [False,0]
        
class MonteCarlo:
    def __init__(self, iterations):
        self.iterations = iterations

    def run(self):
        games = [
            SaharaAce(),
            TunisianTwins(),
            MedinaBiggie(),
            DesertHearts(),
            OasisRunny(),
            StudentGame()
        ]

        for game in games:
            wins = 0
            expected_winnings = 0
            for _ in range(2):
                for _ in range(self.iterations):
                    result = game.play()
                    if result[0]:
                        wins += 1
                    expected_winnings += result[1]

            win_probability = wins / (2 * self.iterations) * 100
            expected_winnings_per_play = expected_winnings / (2 * self.iterations)
            
            print(f"Results for {game.__class__.__name__}:")
            print(f"Win probability: {win_probability:.2f}%")
            print(f"Expected winnings per play: {expected_winnings_per_play:.2f} Dinars per play")
            print("--------------------------------")

    
    
if __name__ == "__main__":
    simuliation=MonteCarlo(iterations=100000)
    simuliation.run()