_whitePieces = ["♖", "♘", "♗", "♔", "♕", "♙"]
_blackPieces = ["♜", "♞", "♝", "♚", "♛", "♟"]


class Rook:
    representation = _whitePieces[0]

    def getLegalMoves(self, chess_board, original_row, original_column, human_turn):
        gettingAllLegalMoves = []
        copyOfOriginalRow = original_row
        copyOfOriginalColumn = original_column

        if human_turn:
            while copyOfOriginalColumn >= 0 and (copyOfOriginalColumn - 1) >= 0:
                if chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalColumn -= 1

            copyOfOriginalColumn = original_column

            while copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalColumn += 1

            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn])
                    break
                copyOfOriginalRow += 1

            copyOfOriginalRow = original_row

            while copyOfOriginalRow >= 0 and (copyOfOriginalRow - 1) >= 0:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn])
                    break
                copyOfOriginalRow -= 1

            return gettingAllLegalMoves
        else:
            while copyOfOriginalColumn >= 0 and (copyOfOriginalColumn - 1) >= 0:
                if chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalColumn -= 1

            copyOfOriginalColumn = original_column

            while copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalColumn += 1

            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn])
                    break
                copyOfOriginalRow += 1

            copyOfOriginalRow = original_row

            while copyOfOriginalRow >= 0 and (copyOfOriginalRow - 1) >= 0:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn])
                    break
                copyOfOriginalRow -= 1

            return gettingAllLegalMoves


class Knight:
    representation = _whitePieces[1]

    def getLegalMoves(self, chess_board, original_row, original_column, human_turn):
        gettingAllLegalMoves = []
        knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

        if human_turn:
            for move in knight_moves:
                rowInQuestion = original_row + move[0]
                columnInQuestion = original_column + move[1]

                if 1 <= rowInQuestion <= 6 and 1 <= columnInQuestion <= 6:
                    if chess_board[rowInQuestion][columnInQuestion] == " ":
                        gettingAllLegalMoves.append([rowInQuestion, columnInQuestion])
                    elif chess_board[rowInQuestion][columnInQuestion] in _whitePieces:
                        continue
                    elif chess_board[rowInQuestion][columnInQuestion] in _blackPieces:
                        gettingAllLegalMoves.append([rowInQuestion, columnInQuestion])

            return gettingAllLegalMoves
        else:
            for move in knight_moves:
                rowInQuestion, columnInQuestion = original_row + move[0], original_column + move[1]

                if 0 <= rowInQuestion < len(chess_board) and 0 <= columnInQuestion < len(chess_board[rowInQuestion]):
                    if chess_board[rowInQuestion][columnInQuestion] == " ":
                        gettingAllLegalMoves.append([rowInQuestion, columnInQuestion])
                    elif chess_board[rowInQuestion][columnInQuestion] in _blackPieces:
                        continue
                    elif chess_board[rowInQuestion][columnInQuestion] in _whitePieces:
                        gettingAllLegalMoves.append([rowInQuestion, columnInQuestion])

            return gettingAllLegalMoves


class Bishop:
    representation = _whitePieces[2]

    def getLegalMoves(self, chess_board, original_row, original_column, human_turn):
        gettingAllLegalMoves = []

        copyOfOriginalRow = original_row
        copyOfOriginalColumn = original_column

        if human_turn:
            while copyOfOriginalRow >= 0 and copyOfOriginalColumn >= 0 and (copyOfOriginalColumn - 1) >= 0 and (
                    copyOfOriginalRow - 1) >= 0:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalRow -= 1
                copyOfOriginalColumn -= 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6 and copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalRow += 1
                copyOfOriginalColumn += 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6 and copyOfOriginalColumn >= 1:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalRow += 1
                copyOfOriginalColumn -= 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow >= 1 and copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalRow -= 1
                copyOfOriginalColumn += 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            return gettingAllLegalMoves
        else:
            while copyOfOriginalRow >= 0 and copyOfOriginalColumn >= 0 and (copyOfOriginalColumn - 1) >= 0 and (
                    copyOfOriginalRow - 1) >= 0:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalRow -= 1
                copyOfOriginalColumn -= 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6 and copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalRow += 1
                copyOfOriginalColumn += 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6 and copyOfOriginalColumn >= 1:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalRow += 1
                copyOfOriginalColumn -= 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow >= 1 and copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalRow -= 1
                copyOfOriginalColumn += 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            return gettingAllLegalMoves


class King:
    representation = _whitePieces[3]

    def getLegalMoves(self, chess_board, original_row, original_column, human_turn):
        gettingAllLegalMoves = []
        if human_turn:
            if 1 <= original_row <= 6:
                if chess_board[original_row + 1][original_column] not in _whitePieces:
                    gettingAllLegalMoves.append([original_row + 1, original_column])
                if chess_board[original_row - 1][original_column] not in _whitePieces:
                    gettingAllLegalMoves.append([original_row - 1, original_column])
            if 1 <= original_column <= 6:
                if chess_board[original_row][original_column + 1] not in _whitePieces:
                    gettingAllLegalMoves.append([original_row, original_column + 1])
                if chess_board[original_row][original_column - 1] not in _whitePieces:
                    gettingAllLegalMoves.append([original_row, original_column - 1])
            if 1 <= original_row <= 6 and 1 <= original_column <= 6:
                if chess_board[original_row + 1][original_column + 1] not in _whitePieces:
                    gettingAllLegalMoves.append([original_row + 1, original_column + 1])
                if chess_board[original_row + 1][original_column - 1] not in _whitePieces:
                    gettingAllLegalMoves.append([original_row + 1, original_column - 1])
                if chess_board[original_row - 1][original_column + 1] not in _whitePieces:
                    gettingAllLegalMoves.append([original_row - 1, original_column + 1])
                if chess_board[original_row - 1][original_column - 1] not in _whitePieces:
                    gettingAllLegalMoves.append([original_row - 1, original_column - 1])
            return gettingAllLegalMoves
        else:
            if 1 <= original_row <= 6:
                if chess_board[original_row + 1][original_column] not in _blackPieces:
                    gettingAllLegalMoves.append([original_row + 1, original_column])
                if chess_board[original_row - 1][original_column] not in _blackPieces:
                    gettingAllLegalMoves.append([original_row - 1, original_column])
            if 1 <= original_column <= 6:
                if chess_board[original_row][original_column + 1] not in _blackPieces:
                    gettingAllLegalMoves.append([original_row, original_column + 1])
                if chess_board[original_row][original_column - 1] not in _blackPieces:
                    gettingAllLegalMoves.append([original_row, original_column - 1])
            if 1 <= original_row <= 6 and 1 <= original_column <= 6:
                if chess_board[original_row + 1][original_column + 1] not in _blackPieces:
                    gettingAllLegalMoves.append([original_row + 1, original_column + 1])
                if chess_board[original_row + 1][original_column - 1] not in _blackPieces:
                    gettingAllLegalMoves.append([original_row + 1, original_column - 1])
                if chess_board[original_row - 1][original_column + 1] not in _blackPieces:
                    gettingAllLegalMoves.append([original_row - 1, original_column + 1])
                if chess_board[original_row - 1][original_column - 1] not in _blackPieces:
                    gettingAllLegalMoves.append([original_row - 1, original_column - 1])
            return gettingAllLegalMoves


class Queen:
    representation = _whitePieces[4]

    def getLegalMoves(self, chess_board, original_row, original_column, human_turn):
        gettingAllLegalMoves = []
        copyOfOriginalRow = original_row
        copyOfOriginalColumn = original_column

        if human_turn:
            while copyOfOriginalColumn >= 0 and (copyOfOriginalColumn - 1) >= 0:
                if chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalColumn -= 1

            copyOfOriginalColumn = original_column

            while copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalColumn += 1

            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn])
                    break
                copyOfOriginalRow += 1

            copyOfOriginalRow = original_row

            while copyOfOriginalRow >= 0 and (copyOfOriginalRow - 1) >= 0:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn])
                    print("hi")
                    break
                copyOfOriginalRow -= 1

            copyOfOriginalRow = original_row

            while copyOfOriginalRow >= 0 and copyOfOriginalColumn >= 0 and (copyOfOriginalColumn - 1) >= 0 and (
                    copyOfOriginalRow - 1) >= 0:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalRow -= 1
                copyOfOriginalColumn -= 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6 and copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalRow += 1
                copyOfOriginalColumn += 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6 and copyOfOriginalColumn >= 0 and (copyOfOriginalColumn - 1) >= 0:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalRow += 1
                copyOfOriginalColumn -= 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow >= 0 and copyOfOriginalColumn <= 6 and (copyOfOriginalRow - 1) >= 0:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] in _whitePieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] in ["♜", "♞", "♝", "♚", "♛", "♟"]:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalRow -= 1
                copyOfOriginalColumn += 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            return gettingAllLegalMoves
        else:
            while copyOfOriginalColumn >= 1:
                if chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn - 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalColumn -= 1

            copyOfOriginalColumn = original_column

            while copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow][copyOfOriginalColumn + 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalColumn += 1

            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn])
                    break
                copyOfOriginalRow += 1

            copyOfOriginalRow = original_row

            while copyOfOriginalRow >= 1:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn])
                    break
                copyOfOriginalRow -= 1

            copyOfOriginalRow = original_row

            while copyOfOriginalRow >= 1 and copyOfOriginalColumn >= 1:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn - 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalRow -= 1
                copyOfOriginalColumn -= 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6 and copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn + 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalRow += 1
                copyOfOriginalColumn += 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow <= 6 and copyOfOriginalColumn >= 1:
                if chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn - 1])
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow + 1][copyOfOriginalColumn - 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow + 1, copyOfOriginalColumn - 1])
                    break
                copyOfOriginalRow += 1
                copyOfOriginalColumn -= 1

            copyOfOriginalRow = original_row
            copyOfOriginalColumn = original_column

            while copyOfOriginalRow >= 1 and copyOfOriginalColumn <= 6:
                if chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] == " ":
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn + 1])
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] in _blackPieces:
                    break
                elif chess_board[copyOfOriginalRow - 1][copyOfOriginalColumn + 1] in _whitePieces:
                    gettingAllLegalMoves.append([copyOfOriginalRow - 1, copyOfOriginalColumn + 1])
                    break
                copyOfOriginalRow -= 1
                copyOfOriginalColumn += 1

            return gettingAllLegalMoves


class Pawn:
    representation = _whitePieces[5]

    def getLegalMoves(self, chess_board, original_row, original_column, human_turn):
        gettingAllLegalMoves = []

        if human_turn:
            if original_row <= 6:
                if chess_board[original_row + 1][original_column] == " ":
                    gettingAllLegalMoves.append([original_row + 1, original_column])

            # Implementing En Passante

            if original_row <= 5:
                if original_row == 1 and chess_board[original_row + 1][original_column] == " " and \
                        chess_board[original_row + 2][original_column] == " ":
                    gettingAllLegalMoves.append([original_row + 2, original_column])

            if original_row <= 6 and original_column >= 1:
                if chess_board[original_row + 1][original_column - 1] in _blackPieces and original_column >= 1:
                    gettingAllLegalMoves.append([original_row + 1, original_column - 1])

            if original_row <= 6 and original_column <= 6:
                if chess_board[original_row + 1][original_column + 1] in _blackPieces and original_column <= 6:
                    gettingAllLegalMoves.append([original_row + 1, original_column + 1])

            return gettingAllLegalMoves
        else:
            if original_row >= 1 and chess_board[original_row - 1][original_column] == " ":
                gettingAllLegalMoves.append([original_row - 1, original_column])

            if original_row == 6 and original_row >= 1 and chess_board[original_row - 1][original_column] == " " and \
                    chess_board[original_row - 2][original_column] == " ":
                gettingAllLegalMoves.append([original_row - 2, original_column])

            if original_row >= 1 and original_column >= 1 and chess_board[original_row - 1][
                original_column - 1] in _whitePieces:
                gettingAllLegalMoves.append([original_row - 1, original_column - 1])

            if original_row >= 1 and original_column <= 6 and chess_board[original_row - 1][
                original_column + 1] in _whitePieces:
                gettingAllLegalMoves.append([original_row - 1, original_column + 1])

            return gettingAllLegalMoves
