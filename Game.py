import time, random

class Game:
    def __init__(self, playerStarted):
        self.currentNumber = random.randint(3,7)
        self.lowerBound = self.currentNumber * 12 + 4
        self.upperBound = self.currentNumber * 18
        self.possibleMoves = [2,3,4]
        self.playerStarted = playerStarted
        self.player = playerStarted
        self.done = False
        self.winner = None
        # generation of the game tree
        self.gameTree = self.generateGameTree(self.currentNumber)
        self.evaluatedTree = self.evaluateTree(self.gameTree)
        self.currentStage = self.evaluatedTree

    def generateGameTree(self, current, depth=0):
        # checks if the game is over at this node
        if current > self.lowerBound:
            return {
                'number': current,
                'children': [],
                'value': 1 if current < self.upperBound else -1,
                'depth': depth
            }
        currentChildren = []
        # generates the children of the current node
        for move in self.possibleMoves:
            currentChildren.append(self.generateGameTree(current*move, depth+1))
        return {
            'number': current,
            'children': currentChildren,
            'value': 0,
            'depth': depth
        }

    def evaluateTree(self, tree, depth=0):
        # determines if the node's player is the maximizer or minimizer
        player = depth % 2 + 1
        possibleOutcomes = [child['value'] for child in tree['children']]
        if len(possibleOutcomes) > 0:
            # determines the value of the node based on the player
            tree['value'] = max(possibleOutcomes) if player == 1 else min(possibleOutcomes)
        for child in tree['children']:
            self.evaluateTree(child, depth+1)
        return tree

    def printTree(self, tree, depth=0):
        player = 1 if depth % 2 == 0 else -1
        print('  '*depth + str(tree['number']) + ' ' + str(tree['value']) + ' ' + str(player))
        for child in tree['children']:
            self.printTree(child, depth+1)

    def getBestMove(self, tree):
        possibleMoves = [child['number'] for child in tree['children']]
        possibleOutcomes = [child['value'] for child in tree['children']]
        player = 1 if tree['depth'] % 2 == 0 else -1
        # determines the best move based on the player
        if player == 1:
            return possibleMoves[possibleOutcomes.index(max(possibleOutcomes))]
        else:
            return possibleMoves[possibleOutcomes.index(min(possibleOutcomes))]

    def playerMove(self, move):
        if self.player and move in self.possibleMoves:
            self.currentNumber *= move
            print('Player move: ' + str(self.currentNumber))
            if self.currentNumber >= self.lowerBound:
                self.determineWinner()
                return
            self.player = False
            self.currentStage = self.currentStage['children'][move-2]
        else:
            print('Invalid input!')

    def computerMove(self):
        time.sleep(1)
        if not self.player:
            bestMove = self.getBestMove(self.currentStage)
            print('Computer move: ' + str(bestMove))
            self.currentNumber = bestMove
            if self.currentNumber >= self.lowerBound:
                self.determineWinner()
                return
            self.player = True
            self.currentStage = next(obj for obj in self.currentStage['children'] if obj['number'] == bestMove)
        else:
            print('Not your turn!')

    def printCurrentStage(self):
        return {
            'number': self.currentNumber,
            'depth': self.currentStage['depth'],
            'possibleMoves': [child['number'] for child in self.currentStage['children']]
        }

    def determineWinner(self):
        self.done = True
        if self.playerStarted:
            if self.currentNumber <= self.upperBound and self.currentNumber >= self.lowerBound:
                self.winner = 'player'
            else:
                self.winner = 'computer'
        else:
            if self.currentNumber <= self.upperBound and self.currentNumber >= self.lowerBound:
                self.winner = 'computer'
            else:
                self.winner = 'player'
        return self.winner
