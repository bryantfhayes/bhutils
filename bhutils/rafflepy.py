import os, sys, random, math

class Raffle():
    def __init__(self, scores, repeats=False, replace=False):
        self._scores = scores
        self._repeats = repeats
        self._replace = replace

        # List of raffle entries
        self._raffle = []

        # Determine combined score of everyone
        self._combinedScore = 0
        for (_, score) in self._scores.items():
            self._combinedScore += score

        # Determine how many tickets everyone gets
        self._ticketDistribution = {}
        for (participant, score) in self._scores.items():
            # Number of tickets is based on the each participants fraction of the combined score
            self._ticketDistribution[participant] = math.ceil((score / self._combinedScore) * 100)
            # Create raffle ticket entries
            for i in range(0, self._ticketDistribution[participant]):
                self._raffle.append(participant)

        # DEBUG
        print(self._ticketDistribution)

        # Shuffle entries
        random.shuffle(self._raffle)

    def removeParticipant(self, participant):
        # Search raffle entries and remove all participant entries
        self._raffle = list(filter(lambda x: x != participant, self._raffle))

        # Shuffle raffle tickets again, just cause we can
        random.shuffle(self._raffle)

    def draw(self):
        ''' Draw a ticket from the raffle entries '''
        if len(self._raffle) == 0:
            return None
        winner = random.choice(self._raffle)

        print(self._raffle)

        # If replace is not enabled, remove that ticket from future drawings
        if not self._replace:
            self._raffle.remove(winner)

        # If repeats are disabled, remove winner from future drawings
        if not self._repeats:
            self.removeParticipant(winner)

        return winner