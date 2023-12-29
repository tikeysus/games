class DurakCards:
    def __init__(self, suit, rank):
        self.suit = suit 
        self.rank = rank 

    def card_suit(self):
        return self.suit 
        
    def card_rank(self):
        return self.rank

    def __str__(self):
        if self.card_suit(self):
            return f"The suit of the card is {self.suit}"
        if self.card_rank(self):
            return f"The rank of the card is {self.rank} "