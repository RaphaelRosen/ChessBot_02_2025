
import Chessnut

SQUARE_NAMES = [
    "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
    "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
    "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"
]

piece_value = {
    'P': 100,
    'R': 500,
    'N': 320,
    'B': 330,
    'Q': 900,
    'K': 20000
}

pawnEvalWhite = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, -20, -20, 10, 10,  5,
    5, -5, -10,  0,  0, -10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishopEvalWhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEval = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

kingEvalWhite = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = [
    50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50
]
kingEvalEndGameBlack = list(reversed(kingEvalEndGameWhite))

def is_promotion(move: str) -> bool:
    return move[-1] in ['q', 'r', 'b', 'n']

def get_from_square_move(move: str) -> str:
    return move[:2]

def get_to_square_move(move: str) -> str:
    return move[-2:]

def get_piece_at_square(board: Chessnut.board, square: str) -> str:
    # Convert the square (e.g., 'e2') into the corresponding board coordinate
    square_index = SQUARE_NAMES.index(square)
    
    # Get the piece at the given square (it returns a piece object or None)
    piece = board.get_piece(square_index)
    
    # Return the piece symbol (or None if there's no piece)
    if piece.isupper():
        return piece, 'W'
    else:
        return piece.upper(), 'B'

def is_capture(game, move):
    to_square = get_to_square_move(move)
    piece, color = get_piece_at_square(game.board, to_square)
    if piece is None or len(piece.strip())==0:
        return False
    return True

def is_en_passant(game: Chessnut.Game, move: str) -> bool:
    return get_to_square_move(move) == game.state.en_passant if game.state.en_passant != '-' else False

def move_value(game, move, endgame) -> float:
    """
    How good is a move?
    A promotion is great.
    A weaker piece taking a stronger piece is good.
    A stronger piece taking a weaker piece is bad.
    Also consider the position change via piece-square table.
    """
    if is_promotion(move):
        return -float("inf") if game.state.player == 'b' else float("inf")

    from_square = get_from_square_move(move)
    to_square = get_to_square_move(move)
    from_index = SQUARE_NAMES.index(from_square)
    to_index = SQUARE_NAMES.index(to_square)
    turn = game.state.player
    
    _piece, color = get_piece_at_square(game.board, get_from_square_move(move))
    if _piece:
        _from_value = evaluate_piece(_piece, turn, from_index, endgame)
        _to_value = evaluate_piece(_piece, turn, to_index, endgame)
        position_change = _to_value - _from_value
    else:
        raise Exception(f"A piece was expected at {move.from_square}")

    capture_value = 0.0
    if is_capture(game, move):
        capture_value = evaluate_capture(game, move)

    current_move_value = capture_value + position_change
    if game.state.player == 'b':
        current_move_value = -current_move_value

    return current_move_value

def evaluate_capture(game, move) -> float:
    """
    Given a capturing move, weight the trade being made.
    """
    if is_en_passant(game, move):
        return piece_value['P']
    _to, _to_color = get_piece_at_square(game.board, get_to_square_move(move))
    _from, _from_color = get_piece_at_square(game.board, get_from_square_move(move))
    if _to is None or _from is None:
        raise Exception(
            f"Pieces were expected at _both_ {move.to_square} and {move.from_square}"
        )
    return piece_value[_to] - piece_value[_from]


def evaluate_piece(piece_type, piece_color, square, end_game) -> int:
    mapping = []
    if piece_type == 'P':
        mapping = pawnEvalWhite if piece_color == 'w' else pawnEvalBlack
    if piece_type == 'N':
        mapping = knightEval
    if piece_type == 'B':
        mapping = bishopEvalWhite if piece_color == 'w' else bishopEvalBlack
    if piece_type == 'R':
        mapping = rookEvalWhite if piece_color == 'w' else rookEvalBlack
    if piece_type == 'Q':
        mapping = queenEval
    if piece_type == 'K':
        # use end game piece-square tables if neither side has a queen
        if end_game:
            mapping = (
                kingEvalEndGameWhite
                if piece_color == 'w'
                else kingEvalEndGameBlack
            )
        else:
            mapping = kingEvalWhite if piece_color == 'w' else kingEvalBlack
    return mapping[square]

def check_end_game(game: Chessnut.Game) -> bool:
    """
    Are we in the end game?
    Per Michniewski:
    - Both sides have no queens or
    - Every side which has a queen has additionally no other pieces or one minorpiece maximum.
    """
    queens = 0
    minors = 0

    for square in SQUARE_NAMES:
        piece, color = get_piece_at_square(game.board, square)
        if piece is not None and len(piece.strip()):
            if piece == 'Q':
                queens +=1
            if piece in ['B', 'N']:
                minors += 1
    
    if queens == 0 or (queens == 2 and minors <= 1):
        return True

    return False

def evaluate_board(game: Chessnut.Game) -> float:
    """
    Evaluates the full board and determines which player is in a most favorable position.
    The sign indicates the side:
        (+) for white
        (-) for black
    The magnitude, how big of an advantage that player has
    """
    total = 0
    end_game = check_end_game(game)

    for index, square in enumerate(SQUARE_NAMES):
        piece, color = get_piece_at_square(game.board, square)
        if piece is None or not len(piece.strip()):
            continue

        value = piece_value[piece] + evaluate_piece(piece, color, index, end_game)
        total += value if color == 'w' else -value

    return total


MATE_SCORE     = 1000000000
MATE_THRESHOLD =  999000000

def chess_bot(obs):
    game = Chessnut.Game(obs.board)
    maximize = game.state.player == 'w'
    if maximize:
        bestscore = -float("inf")
    else:
        bestscore = float("inf")    
    legal_moves = game.get_moves()
    maxscore = 0
    bestmove = None
    for move in legal_moves:
        testgame = Chessnut.Game(game.fen_history[-1])
        testgame.apply_move(move)
        if testgame.status == testgame.CHECKMATE:
            return str(move)
            score = MATE_SCORE if maximize else -MATE_SCORE
        elif testgame.status == testgame.STALEMATE:
            score = 0
        #elif board.can_claim_draw():
        #    score = 0
        else:
            score = evaluate_board(testgame)
        if maximize and score >= bestscore:
            bestmove = move
            bestscore = score
        elif not maximize and score <= bestscore:
            bestmove = move
            bestscore = score
    return str(bestmove)
