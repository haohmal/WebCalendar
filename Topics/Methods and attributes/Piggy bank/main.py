class PiggyBank:
    def __init__(self, deposit_dollars, deposit_cents):
        self.dollars = deposit_dollars
        self.cents = deposit_cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100