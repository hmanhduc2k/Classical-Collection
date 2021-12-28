KEYWORD_ALL = "All"

from ..models import Piece

class PieceSearch():
    def match(piece, key, period, difficulty):
        cond1 = key in piece.name
        cond2 = period == piece.period.era or period == KEYWORD_ALL
        cond3 = difficulty == piece.difficulty.rating or difficulty == KEYWORD_ALL
        return cond1 and cond2 and cond3