import random

class SlotMachine:
    def __init__(self, reelNum, winDict):
        self.reels = [[i for i in range(10)]] * reelNum
        self.wins = winDict

    def spin(self):
        spinResult = ''
        for reel in self.reels:
            spinResult += str(random.choice(reel))
        return spinResult

    def simulation(self, spinCount, potAmount, betAmount):
        self.spinCount, self.potAmount, self.betAmount = spinCount, potAmount, betAmount
        jackpots = 0
        startingPot = potAmount
        totalPaid = 0
        winningSpins = 0

        for i in range(spinCount):
            potAmount += betAmount
            currSpin = self.spin()
            hits = [item for item in self.wins.keys() if item in currSpin]
            if hits:
                multiplier = self.wins[max(hits)]
                payout = betAmount * multiplier
                potAmount -= payout
                totalPaid += payout
                winningSpins += 1
                if multiplier == self.wins[max(self.wins.keys())]:
                    jackpots += 1

        profit = potAmount - startingPot
        returnToPlayer = float(f"{totalPaid / (betAmount * spinCount)}")
        
        if profit > 0:
            profit = f"${float(profit):,.2f}"
            return f"{winningSpins} wins/{spinCount} spins. Simulated profit: {profit}. RTP: {returnToPlayer}"
        elif profit < 0:
            profit = f"${float(profit):,.2f}"
            return f"{winningSpins} wins/{spinCount} spins. Simulated profit: {profit}. RTP: {returnToPlayer}"
        else:
            return f"{winningSpins} wins/{spinCount} spins. Simulated profit: {profit}. RTP: {returnToPlayer}"
