'''
        TIC TAC TOE GAME

        3by3 - Beginner, Expert and User vs User
        4by4 - Beginner, Expert and User vs User

        Author: Avinash Vootkuri
'''

import random

def beginner4by4():


    def gameBoard(board):


        print('  |   |   |')
        print(' ' + board[1] + '|' + ' ' + board[2] + ' |' + ' ' + board[3] + ' |' + ' ' + board[4])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[5] + '|' + ' ' + board[6] + ' |' + ' ' + board[7] + ' |' + ' ' + board[8])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[9] + '|' + ' ' + board[10] + ' |' + ' ' + board[11] + ' |' + ' ' + board[12])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[13] + '|' + ' ' + board[14] + ' |' + ' ' + board[15] + ' |' + ' ' + board[16])
        print('  |   |   |')

    def playerInput():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want X or O ?')
            letter = input().upper()
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']

    def whoGoesFirst():
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def makeMove(board, letter, move):
        board[move] = letter

    def winner(bo, le):
        return ((bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le) or
                (bo[5] == le and bo[6] == le and bo[7] == le and bo[8] == le) or
                (bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or
                (bo[13] == le and bo[14] == le and bo[15] == le and bo[16] == le) or
                (bo[1] == le and bo[5] == le and bo[9] == le and bo[13] == le) or
                (bo[2] == le and bo[6] == le and bo[10] == le and bo[14] == le) or
                (bo[3] == le and bo[7] == le and bo[11] == le and bo[15] == le) or
                (bo[4] == le and bo[8] == le and bo[12] == le and bo[16] == le) or
                (bo[1] == le and bo[6] == le and bo[11] == le and bo[16] == le) or
                (bo[4] == le and bo[7] == le and bo[10] == le and bo[13] == le)
                )

    def gameBoardCopy(board):
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        return board[move] == ' '

    def getPlayerMove(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move ? (1-16)')
            move = input()
        return int(move)

    def chooseRandomeMove(board, movesList):
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(board, AILetter):
        if AILetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # check if computer can win in one move
        for i in range(1, 17):
            copy = gameBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, AILetter, i)
                if winner(copy, AILetter):
                    return i

        # choose a random number
        move = chooseRandomeMove(board, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        if move != None:
            return move

        return chooseRandomeMove(board, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

        # check if board is full

    def isBoardFull(board):
        for i in range(1, 17):
            if isSpaceFree(board, i):
                return False
        return True

    print('Playing Tic Tac Toe 4by4 Beginner')

    while True:
        theBoard = [' '] * 17
        playerLetter, AILetter = playerInput()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                gameBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if winner(theBoard, playerLetter):
                    gameBoard(theBoard)
                    print('Yeyy You won the game')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove(theBoard, AILetter)
                makeMove(theBoard, AILetter, move)

                if winner(theBoard, AILetter):
                    gameBoard(theBoard)
                    print('Computer Won')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'player'

        break


def expert4by4():
    def gameBoard(board):
        print('  |   |   |')
        print(' ' + board[1] + '|' + ' ' + board[2] + ' |' + ' ' + board[3] + ' |' + ' ' + board[4])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[5] + '|' + ' ' + board[6] + ' |' + ' ' + board[7] + ' |' + ' ' + board[8])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[9] + '|' + ' ' + board[10] + ' |' + ' ' + board[11] + ' |' + ' ' + board[12])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[13] + '|' + ' ' + board[14] + ' |' + ' ' + board[15] + ' |' + ' ' + board[16])
        print('  |   |   |')

    def playerInput():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want X or O ?')
            letter = input().upper()
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']

    def whoGoesFirst():
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def makeMove(board, letter, move):
        board[move] = letter

    def winner(bo, le):
        return ((bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le) or
                (bo[5] == le and bo[6] == le and bo[7] == le and bo[8] == le) or
                (bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or
                (bo[13] == le and bo[14] == le and bo[15] == le and bo[16] == le) or
                (bo[1] == le and bo[5] == le and bo[9] == le and bo[13] == le) or
                (bo[2] == le and bo[6] == le and bo[10] == le and bo[14] == le) or
                (bo[3] == le and bo[7] == le and bo[11] == le and bo[15] == le) or
                (bo[4] == le and bo[8] == le and bo[12] == le and bo[16] == le) or
                (bo[1] == le and bo[6] == le and bo[11] == le and bo[16] == le) or
                (bo[4] == le and bo[7] == le and bo[10] == le and bo[13] == le)
                )

    def gameBoardCopy(board):
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        return board[move] == ' '

    def getPlayerMove(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move ? (1-16)')
            move = input()
        return int(move)

    def chooseRandomeMove(board, movesList):
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(board, AILetter):
        if AILetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # check if computer can win in one move
        for i in range(1, 17):
            copy = gameBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, AILetter, i)
                if winner(copy, AILetter):
                    return i

        # check if player can win in one move
        for i in range(1, 17):
            copy = gameBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, playerLetter, i)
                if winner(copy, playerLetter):
                    return i

        # check for one of the corners if they are free
        move = chooseRandomeMove(board, [1, 4, 13, 16])
        if move != None:
            return move

        # check for center if it is free
        move = chooseRandomeMove(board, [6, 7, 10, 11])
        # if isSpaceFree(board, move):
        #    return move
        if move != None:
            return move

        return chooseRandomeMove(board, [2, 3, 5, 8, 9, 12, 14, 15])

        # check if board is full

    def isBoardFull(board):
        for i in range(1, 17):
            if isSpaceFree(board, i):
                return False
        return True

    print('Play Tic Tac Toe 4by4 Expert')

    while True:
        theBoard = [' '] * 17
        playerLetter, AILetter = playerInput()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                gameBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if winner(theBoard, playerLetter):
                    gameBoard(theBoard)
                    print('Yeyy You won the game')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove(theBoard, AILetter)
                makeMove(theBoard, AILetter, move)

                if winner(theBoard, AILetter):
                    gameBoard(theBoard)
                    print('Computer Won')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'player'

        break

def uservsuser4by4():
    def gameBoard(board):
        print('  |   |   |')
        print(' ' + board[1] + '|' + ' ' + board[2] + ' |' + ' ' + board[3] + ' |' + ' ' + board[4])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[5] + '|' + ' ' + board[6] + ' |' + ' ' + board[7] + ' |' + ' ' + board[8])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[9] + '|' + ' ' + board[10] + ' |' + ' ' + board[11] + ' |' + ' ' + board[12])
        print('  |   |   |')
        print('-------------------')
        print('  |   |   |')
        print(' ' + board[13] + '|' + ' ' + board[14] + ' |' + ' ' + board[15] + ' |' + ' ' + board[16])
        print('  |   |   |')

    def playerInput():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want X or O ?')
            letter = input().upper()
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']

    def whoGoesFirst():
        if random.randint(0, 1) == 0:
            return 'user1'
        else:
            return 'user2'

    def makeMove(board, letter, move):
        board[move] = letter

    def winner(bo, le):
        return ((bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le) or
                (bo[5] == le and bo[6] == le and bo[7] == le and bo[8] == le) or
                (bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or
                (bo[13] == le and bo[14] == le and bo[15] == le and bo[16] == le) or
                (bo[1] == le and bo[5] == le and bo[9] == le and bo[13] == le) or
                (bo[2] == le and bo[6] == le and bo[10] == le and bo[14] == le) or
                (bo[3] == le and bo[7] == le and bo[11] == le and bo[15] == le) or
                (bo[4] == le and bo[8] == le and bo[12] == le and bo[16] == le) or
                (bo[1] == le and bo[6] == le and bo[11] == le and bo[16] == le) or
                (bo[4] == le and bo[7] == le and bo[10] == le and bo[13] == le)
                )

    def gameBoardCopy(board):
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        return board[move] == ' '

    def getPlayer1Move(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move USER1 ? (1-16)')
            move = input()
        return int(move)

    def getPlayer2Move(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move USER2 ? (1-16)')
            move = input()
        return int(move)

        # check if board is full

    def isBoardFull(board):
        for i in range(1, 17):
            if isSpaceFree(board, i):
                return False
        return True

    print('Playing Tic Tac Toe 4by4 USER1 VS USER2')

    while True:
        theBoard = [' '] * 17
        user1Letter, user2Letter = playerInput()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'user1':
                gameBoard(theBoard)
                move = getPlayer1Move(theBoard)
                makeMove(theBoard, user1Letter, move)

                if winner(theBoard, user1Letter):
                    gameBoard(theBoard)
                    print('Yeyy user1 WON the GAME')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'user2'
            else:
                gameBoard(theBoard)
                move = getPlayer2Move(theBoard)
                makeMove(theBoard, user2Letter, move)

                if winner(theBoard, user2Letter):
                    gameBoard(theBoard)
                    print('Yeyy user2 WON the GAME')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'user1'

        break


def beginner3by3():
    def gameBoard(board):
        print('  |   |')
        print(' ' + board[1] + '|' + ' ' + board[2] + ' |' + ' ' + board[3])
        print('  |   |')
        print('-----------')
        print('  |   |')
        print(' ' + board[4] + '|' + ' ' + board[5] + ' |' + ' ' + board[6])
        print('  |   |')
        print('-----------')
        print('  |   |')
        print(' ' + board[7] + '|' + ' ' + board[8] + ' |' + ' ' + board[9])
        print('  |   |')

    def playerInput():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want X or O ?')
            letter = input().upper()
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']

    def whoGoesFirst():
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def makeMove(board, letter, move):
        board[move] = letter

    def winner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
                (bo[4] == le and bo[5] == le and bo[6] == le) or
                (bo[1] == le and bo[2] == le and bo[3] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[9] == le and bo[6] == le and bo[3] == le) or
                (bo[7] == le and bo[5] == le and bo[3] == le) or
                (bo[9] == le and bo[5] == le and bo[1] == le))

    def gameBoardCopy(board):
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        return board[move] == ' '

    def getPlayerMove(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move ? (1-9)')
            move = input()
        return int(move)

    def chooseRandomeMove(board, movesList):
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(board, AILetter):
        if AILetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # check if computer can win in one move
        for i in range(1, 10):
            copy = gameBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, AILetter, i)
                if winner(copy, AILetter):
                    return i

        # check for one of the corners if they are free
        move = chooseRandomeMove(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        if move != None:
            return move

        return chooseRandomeMove(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])

        # check if board is full

    def isBoardFull(board):
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True

    print('Play Tic Tac Toe 3by3 beginner')

    while True:
        theBoard = [' '] * 10
        playerLetter, AILetter = playerInput()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                gameBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if winner(theBoard, playerLetter):
                    gameBoard(theBoard)
                    print('Yeyy You won the game')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove(theBoard, AILetter)
                makeMove(theBoard, AILetter, move)

                if winner(theBoard, AILetter):
                    gameBoard(theBoard)
                    print('Computer Won')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'player'

        break


def expert3by3():
    def gameBoard(board):
        print('  |   |')
        print(' ' + board[1] + '|' + ' ' + board[2] + ' |' + ' ' + board[3])
        print('  |   |')
        print('-----------')
        print('  |   |')
        print(' ' + board[4] + '|' + ' ' + board[5] + ' |' + ' ' + board[6])
        print('  |   |')
        print('-----------')
        print('  |   |')
        print(' ' + board[7] + '|' + ' ' + board[8] + ' |' + ' ' + board[9])
        print('  |   |')

    def playerInput():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want X or O ?')
            letter = input().upper()
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']

    def whoGoesFirst():
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def makeMove(board, letter, move):
        board[move] = letter

    def winner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
                (bo[4] == le and bo[5] == le and bo[6] == le) or
                (bo[1] == le and bo[2] == le and bo[3] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[9] == le and bo[6] == le and bo[3] == le) or
                (bo[7] == le and bo[5] == le and bo[3] == le) or
                (bo[9] == le and bo[5] == le and bo[1] == le))

    def gameBoardCopy(board):
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        return board[move] == ' '

    def getPlayerMove(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move ? (1-9)')
            move = input()
        return int(move)

    def chooseRandomeMove(board, movesList):
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(board, AILetter):
        if AILetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # check if computer can win in one move
        for i in range(1, 10):
            copy = gameBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, AILetter, i)
                if winner(copy, AILetter):
                    return i

        # check if player can win in one move
        for i in range(1, 10):
            copy = gameBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, AILetter, i)
                if winner(copy, playerLetter):
                    return i

        # check for one of the corners if they are free
        move = chooseRandomeMove(board, [1, 3, 7, 9])
        if move != None:
            return move

        # check for center if it is free
        if isSpaceFree(board, 5):
            return 5

        return chooseRandomeMove(board, [2, 4, 6, 8])

        # check if board is full

    def isBoardFull(board):
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True

    print('Play Tic Tac Toe 3by3 Expert')

    while True:
        theBoard = [' '] * 10
        playerLetter, AILetter = playerInput()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                gameBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if winner(theBoard, playerLetter):
                    gameBoard(theBoard)
                    print('Yeyy You won the game')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove(theBoard, AILetter)
                makeMove(theBoard, AILetter, move)

                if winner(theBoard, AILetter):
                    gameBoard(theBoard)
                    print('Computer Won')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'player'

        break


def uservsuser3by3():
    def gameBoard(board):
        print('  |   |')
        print(' ' + board[1] + '|' + ' ' + board[2] + ' |' + ' ' + board[3])
        print('  |   |')
        print('-----------')
        print('  |   |')
        print(' ' + board[4] + '|' + ' ' + board[5] + ' |' + ' ' + board[6])
        print('  |   |')
        print('-----------')
        print('  |   |')
        print(' ' + board[7] + '|' + ' ' + board[8] + ' |' + ' ' + board[9])
        print('  |   |')

    def playerInput():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want X or O ?')
            letter = input().upper()
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']

    def whoGoesFirst():
        if random.randint(0, 1) == 0:
            return 'user1'
        else:
            return 'user2'

    def makeMove(board, letter, move):
        board[move] = letter

    def winner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
                (bo[4] == le and bo[5] == le and bo[6] == le) or
                (bo[1] == le and bo[2] == le and bo[3] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[9] == le and bo[6] == le and bo[3] == le) or
                (bo[7] == le and bo[5] == le and bo[3] == le) or
                (bo[9] == le and bo[5] == le and bo[1] == le))

    def gameBoardCopy(board):
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        return board[move] == ' '

    def getPlayer1Move(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move USER1 ? (1-9)')
            move = input()
        return int(move)

    def getPlayer2Move(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move USER2 ? (1-9)')
            move = input()
        return int(move)

    # check if board is full
    def isBoardFull(board):
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True

    print('Play Tic Tac Toe 3by3 User1 vs User2')

    while True:
        theBoard = [' '] * 10
        user1Letter, user2Letter = playerInput()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'user1':
                gameBoard(theBoard)
                move = getPlayer1Move(theBoard)
                makeMove(theBoard, user1Letter, move)

                if winner(theBoard, user1Letter):
                    gameBoard(theBoard)
                    print('Yeyy user1 WON the GAME')
                    gameIsPlaying = False
                    break
                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'user2'
            else:
                gameBoard(theBoard)
                move = getPlayer2Move(theBoard)
                makeMove(theBoard, user2Letter, move)

                if winner(theBoard, user2Letter):
                    gameBoard(theBoard)
                    print('Yeyy user2 WON the GAME')
                    gameIsPlaying = False

                else:
                    if isBoardFull(theBoard):
                        gameBoard(theBoard)
                        print('Game is a tie')

                    else:
                        turn = 'user1'
        break

def playAgain():
    print('Do you want to play again?  (yes or no)')
    if input().lower().startswith('y'):
        menu()
    else:
        exit()

print('WELCOME! Begin playing TIC TAC TOE\n')


def menu():

    print('CHOOSE FROM THE "MENU"')

    print('1. USER VS COMPUTER')
    print('2. USER VS USER')
    print('3. TIC TAC TOE on 4by4 grid')
    print('4. Quit')

while True:
    menu()
    playing = True

    while playing:
        number = ''
        number = input()

        option = ''
        if number == '1':
            print('Choose strategy\n')
            print('1. Beginner')
            print('2. EXPERT')
            option = input()

            if option == '1':
                beginner3by3()
                playAgain()

            elif option == '2':
                expert3by3()
                playAgain()
            else:
                print('NOT A VALID CHOICE')
                playing = False

        elif number == '2':
            uservsuser3by3()
            playAgain()

        elif number == '3':
            print('Choose strategy\n')
            print('1. Beginner')
            print('2. EXPERT')
            print('3. User1 vs User2')
            option = input()

            if option == '1':
                beginner4by4()
                playAgain()

            elif option == '2':
                expert4by4()
                playAgain()
            elif option == '3':
                uservsuser4by4()
                playAgain()
            else:
                print('NOT A VALID CHOICE')
        elif number == '4':
            exit()

        else:
            print('Enter a valid option(1-4)')
            menu()

    if not playAgain():
        break
