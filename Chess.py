from ChessPieces import Rook, Knight, Bishop, King, Queen, Pawn

# Holding a visual reference of the chess board at it's initial state
chessBoard = [["♖", "♘", "♗", "♔", "♕", "♗", "♘", "♖"],
              ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
              ["♜", "♞", "♝", "♚", "♛", "♝", "♞", "♜"]]

# Representing white pieces
whiteRook = "♖"
whiteKnight = "♘"
whiteBishop = "♗"
whiteKing = "♔"
whiteQueen = "♕"
whitePawn = "♙"

# Representing black pieces
blackRook = "♜"
blackKnight = "♞"
blackBishop = "♝"
blackKing = "♚"
blackQueen = "♛"
blackPawn = "♟"


class Chess:
    game_not_over = True
    _emptySpace = " "
    _chessRows = 8
    _chessColumns = 8

    def print_chessBoard(self):
        print("\n\n")
        print("  +---+---+---+---+---+---+---+---+")
        for i in range(self._chessRows):
            chess_cell = str(self._chessRows - i) + self._emptySpace
            for j in range(self._chessColumns):
                if chessBoard[i][j] == self._emptySpace:
                    chess_cell += "|   "
                else:
                    chess_cell += "| {} ".format(chessBoard[i][j])
            chess_cell += "|"
            print(chess_cell)
            print("  +---+---+---+---+---+---+---+---+")
        column_names = "♡,a,b,c,d,e,f,g,h"
        separator = ","
        column_moves = column_names.replace(separator, "   ")
        print(column_moves)
        print("\n\n")

    def begin_chess(self):
        your_turn = True
        pruning_depth = 4
        can_shift = True

        while self.game_not_over:
            self.print_chessBoard()
            if your_turn:
                print("Your turn!")
                user_move = input(
                    "Enter your move - follow the guides on board - [original position → new position e.g (a2a4)\n")
                original_column = user_move[0]
                original_row = user_move[1]
                new_column = user_move[2]
                new_row = user_move[3]

                # Convert values to indexes
                original_column = self.convertingColumnToIndex(original_column)
                new_row = self.convertingRowToIndex(int(new_row))
                original_row = self.convertingRowToIndex(int(original_row))
                new_column = self.convertingColumnToIndex(new_column)

                # Trying to find legal moves per chosen move
                if chessBoard[original_row][original_column] == whiteRook:
                    legal_rook_moves = Rook().getLegalMoves(chessBoard, original_row, original_column, True)
                    print([new_row, new_column], legal_rook_moves)
                    if [new_row, new_column] in legal_rook_moves:
                        chessBoard[original_row][original_column] = self._emptySpace
                        chessBoard[new_row][new_column] = whiteRook
                        can_shift = True
                    else:
                        print("Not a justifiable move for your Rook. Try again")
                        can_shift = False

                elif chessBoard[original_row][original_column] == whiteKnight:
                    legal_knight_moves = Knight().getLegalMoves(chessBoard, original_row, original_column, True)
                    print([new_row, new_column], legal_knight_moves)
                    if [new_row, new_column] in legal_knight_moves:
                        chessBoard[original_row][original_column] = self._emptySpace
                        chessBoard[new_row][new_column] = whiteKnight
                        can_shift = True
                    else:
                        print("Not a justifiable move for your Knight. Try again")
                        can_shift = False

                elif chessBoard[original_row][original_column] == whiteBishop:
                    legal_bishop_moves = Bishop().getLegalMoves(chessBoard, original_row, original_column, True)
                    # print([new_row, new_column], legal_bishop_moves)
                    if [new_row, new_column] in legal_bishop_moves:
                        chessBoard[original_row][original_column] = self._emptySpace
                        chessBoard[new_row][new_column] = whiteBishop
                        can_shift = True
                    else:
                        print("Not a justifiable move for your Bishop. Try again")
                        can_shift = False

                elif chessBoard[original_row][original_column] == whiteKing:
                    legal_king_moves = King().getLegalMoves(chessBoard, original_row, original_column, True)
                    # print([new_row, new_column], legal_king_moves)
                    if [new_row, new_column] in legal_king_moves:
                        chessBoard[original_row][original_column] = self._emptySpace
                        chessBoard[new_row][new_column] = whiteKing
                        can_shift = True
                    else:
                        print("Not a justifiable move for your King. Try again")
                        can_shift = False

                elif chessBoard[original_row][original_column] == whiteQueen:
                    legal_queen_moves = Queen().getLegalMoves(chessBoard, original_row, original_column, True)
                    # print([new_row, new_column], legal_queen_moves)
                    if [new_row, new_column] in legal_queen_moves:
                        chessBoard[original_row][original_column] = self._emptySpace
                        chessBoard[new_row][new_column] = whiteQueen
                        can_shift = True
                    else:
                        print("Not a justifiable move for your Queen. Try again")
                        can_shift = False

                elif chessBoard[original_row][original_column] == whitePawn:
                    legal_pawn_moves = Pawn().getLegalMoves(chessBoard, original_row, original_column, True)

                    # print("Doing this", [new_row, new_column], legal_pawn_moves)

                    if [new_row, new_column] in legal_pawn_moves:
                        chessBoard[original_row][original_column] = self._emptySpace
                        chessBoard[new_row][new_column] = whitePawn
                        can_shift = True
                    else:
                        print("Not a justifiable move for your Pawn. Try again")
                        can_shift = False
                else:
                    print("Illegal move. Try again")
                    can_shift = False

                if can_shift:
                    if self.checkmate(False):
                        print("Checkmate - You win!")
                        self.game_not_over = False
                    else:
                        your_turn = False

            else:
                print("Computer computing turn ...")
                alpha = float('-inf')
                beta = float('inf')

                best_move = self.minimax(pruning_depth, alpha, beta, True, 0)
                orig_row, orig_col, new_r, new_c = best_move

                representation = chessBoard[orig_row][orig_col]
                chessBoard[orig_row][orig_col] = self._emptySpace
                chessBoard[new_r][new_c] = representation
                
                if can_shift:
                    if self.checkmate(True):
                        print("Checkmate - You lose!")
                        self.game_not_over = False
                    else:
                        your_turn = True

    # Min-max Algorithm - Pruning through Alpha Beta Pruning

    def minimax(self, current_depth, alpha, beta, is_computer_player, best_move):
        if current_depth == 0 or not self.game_not_over:
            return best_move

        if is_computer_player:
            max_eval = float('-inf')
            best_move = None

            for move in self.getAllPotentialLegalMoves(True):
                score = self.assigningWeights(move, True)

                if score > max_eval:
                    max_eval = score
                    best_move = move

                alpha = max(alpha, score)
                if beta <= alpha:
                    break

            return self.minimax(current_depth - 1, alpha, beta, True, best_move)

        else:
            min_eval = float('inf')
            best_move = None

            for move in self.getAllPotentialLegalMoves(False):
                score = self.assigningWeights(move, False)
                if score < min_eval:
                    min_eval = score
                    best_move = move

                beta = min(beta, score)
                if beta <= alpha:
                    break

            return self.minimax(current_depth - 1, alpha, beta, False, best_move)

    # My evaluative function - evaluates based on number of pieces on board in accordance to their weights assigned in the game of chess

    def assigningWeights(self, move, isComp):
        user_score = 0
        computer_score = 0

        # Perform move arbitrarily
        representation = chessBoard[move[0]][move[1]]
        chessBoard[move[0]][move[1]] = self._emptySpace
        temp = chessBoard[move[2]][move[3]]
        chessBoard[move[2]][move[3]] = representation

        for row in range(self._chessRows):
            for col in range(self._chessColumns):
                piece = chessBoard[row][col]
                if piece == " ":
                    continue
                if piece == blackPawn:
                    computer_score += 1
                elif piece == blackRook:
                    computer_score += 5
                elif piece == blackQueen:
                    computer_score += 9
                elif piece == blackKing:
                    computer_score += 100
                elif piece == blackBishop:
                    computer_score += 3
                elif piece == blackKnight:
                    computer_score += 3
                elif piece == whitePawn:
                    user_score += 1
                elif piece == whiteRook:
                    user_score += 5
                elif piece == whiteQueen:
                    user_score += 9
                elif piece == whiteKing:
                    user_score += 100
                elif piece == whiteBishop:
                    user_score += 3
                elif piece == whiteKnight:
                    user_score += 3

        # Un-do move
        chessBoard[move[0]][move[1]] = representation
        chessBoard[move[2]][move[3]] = temp

        if not isComp:
            return user_score - computer_score
        else:
            return computer_score - user_score

    # Helper Functions - All miscellaneous functions used as aids in my program

    def convertingColumnToIndex(self, character):
        available_characters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        if character in available_characters:
            return available_characters.index(character)
        else:
            return -1

    def convertingRowToIndex(self, index):
        if 1 <= index <= 8:
            return 8 - index
        else:
            return -1

    def getAllPotentialLegalMoves(self, computer_turn):
        all_legal_moves = []
        if computer_turn:
            for cellInRow in range(self._chessRows):
                for cellInColumn in range(self._chessColumns):
                    piece = chessBoard[cellInRow][cellInColumn]
                    if piece == " ":
                        continue
                    moves = []
                    if piece == blackPawn:
                        moves = Pawn().getLegalMoves(chessBoard, cellInRow, cellInColumn, False)
                    elif piece == blackRook:
                        moves = Rook().getLegalMoves(chessBoard, cellInRow, cellInColumn, False)
                    elif piece == blackQueen:
                        moves = Queen().getLegalMoves(chessBoard, cellInRow, cellInColumn, False)
                    elif piece == blackKing:
                        moves = King().getLegalMoves(chessBoard, cellInRow, cellInColumn, False)
                    elif piece == blackBishop:
                        moves = Bishop().getLegalMoves(chessBoard, cellInRow, cellInColumn, False)
                    elif piece == blackKnight:
                        moves = Knight().getLegalMoves(chessBoard, cellInRow, cellInColumn, False)
                    for move in moves:
                        all_legal_moves.append((cellInRow, cellInColumn, move[0], move[1]))
            return all_legal_moves
        else:
            for cellInRow in range(self._chessRows):
                for cellInColumn in range(self._chessColumns):
                    piece = chessBoard[cellInRow][cellInColumn]
                    if piece == " ":
                        continue
                    moves = []
                    if piece == whiteRook:
                        moves = Rook().getLegalMoves(chessBoard, cellInRow, cellInColumn, True)
                    elif piece == whiteKnight:
                        moves = Knight().getLegalMoves(chessBoard, cellInRow, cellInColumn, True)
                    elif piece == whiteBishop:
                        moves = Bishop().getLegalMoves(chessBoard, cellInRow, cellInColumn, True)
                    elif piece == whiteKing:
                        moves = King().getLegalMoves(chessBoard, cellInRow, cellInColumn, True)
                    elif piece == whiteQueen:
                        moves = Queen().getLegalMoves(chessBoard, cellInRow, cellInColumn, True)
                    elif piece == whitePawn:
                        moves = Pawn().getLegalMoves(chessBoard, cellInRow, cellInColumn, True)
                    for move in moves:
                        all_legal_moves.append((cellInRow, cellInColumn, move[0], move[1]))
            return all_legal_moves

    def checkmate(self, isComp):
        king_checked = True
        if isComp:
            for cellInRow in range(self._chessRows):
                for columnInRow in range(self._chessColumns):
                    piece = chessBoard[cellInRow][columnInRow]
                    if piece != "♔":
                        continue

                    king_checked = False
                    legal_moves = []

                    for rowDirection, columnDirection in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        potentialRowPosition = cellInRow + rowDirection
                        potentialColumnPosition = columnInRow + columnDirection

                        if 6 < potentialRowPosition < 1:
                            continue
                        elif 6 < potentialColumnPosition < 1:
                            continue

                        piece = chessBoard[potentialRowPosition][potentialColumnPosition]

                        if piece in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                            if piece == blackRook:
                                moves = Rook().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == blackKnight:
                                moves = Knight().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == blackBishop:
                                moves = Bishop().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == blackKing:
                                moves = King().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == blackQueen:
                                moves = Queen().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == blackPawn:
                                moves = Pawn().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)

                            for move in moves:
                                legal_moves.append((cellInRow, columnInRow, move[0], move[1]))
                                if [move[0], move[1]] == [cellInRow, columnInRow]:
                                    print("Check")
            return king_checked
        else:
            for cellInRow in range(self._chessRows):
                for columnInRow in range(self._chessColumns):
                    piece = chessBoard[cellInRow][columnInRow]
                    if piece != "♚":
                        continue

                    king_checked = False
                    legal_moves = []

                    for rowDirection, columnDirection in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        potentialRowPosition = cellInRow + rowDirection
                        potentialColumnPosition = columnInRow + columnDirection

                        if potentialRowPosition < 1 or potentialRowPosition > 6 or potentialColumnPosition < 1 or potentialColumnPosition > 6:
                            continue

                        piece = chessBoard[potentialRowPosition][potentialColumnPosition]

                        if piece in ["♖", "♘", "♗", "♔", "♕", "♙"]:
                            if piece == whiteRook:
                                moves = Rook().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == whiteKnight:
                                moves = Knight().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == whiteBishop:
                                moves = Bishop().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == whiteKing:
                                moves = King().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == whiteQueen:
                                moves = Queen().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)
                            elif piece == whitePawn:
                                moves = Pawn().getLegalMoves(chessBoard, potentialRowPosition, potentialColumnPosition, True)

                            for move in moves:
                                legal_moves.append((cellInRow, columnInRow, move[0], move[1]))
                                if [move[0], move[1]] == [cellInRow, columnInRow]:
                                    print("Check")
            return king_checked

    def stalemate(self, isComp):

        legal_moves = []

        if self.checkmate(isComp):
            return

        if isComp:
            for pieceInChessBoardRow in range(self._chessRows):
                for pieceInColumn in range(self._chessColumns):
                    chessPieceInQuestion = chessBoard[pieceInChessBoardRow][pieceInColumn]
                    if chessPieceInQuestion in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                        if chessPieceInQuestion == blackRook:
                            moves = Rook().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == blackKnight:
                            moves = Knight().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == blackBishop:
                            moves = Bishop().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == blackKing:
                            moves = King().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == blackQueen:
                            moves = Queen().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == blackPawn:
                            moves = Pawn().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)

                        for move in moves:
                            legal_moves.append((pieceInChessBoardRow, pieceInColumn, move[0], move[1]))
                        if len(legal_moves) == 0:
                            print("Stalemate - Game Over")
                            self.game_not_over = False
        else:
            for pieceInChessBoardRow in range(self._chessRows):
                for pieceInColumn in range(self._chessColumns):
                    chessPieceInQuestion = chessBoard[pieceInChessBoardRow][pieceInColumn]
                    if chessPieceInQuestion in ["♖", "♘", "♗", "♔", "♕", "♙"]:
                        if chessPieceInQuestion == whiteRook:
                            moves = Rook().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == whiteKnight:
                            moves = Knight().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == whiteBishop:
                            moves = Bishop().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == whiteKing:
                            moves = King().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == whiteQueen:
                            moves = Queen().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)
                        elif chessPieceInQuestion == whitePawn:
                            moves = Pawn().getLegalMoves(chessBoard, pieceInChessBoardRow, pieceInColumn, True)

                        for move in moves:
                            legal_moves.append((pieceInChessBoardRow, pieceInColumn, move[0], move[1]))
                        if len(legal_moves) == 0:
                            print("Stalemate - Game Over")
                            self.game_not_over = False
