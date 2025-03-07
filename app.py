import chess
import chess.engine
import yaml

# Membaca konfigurasi dari config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

STOCKFISH_PATH = config["stockfish_path"]  # Path ke Stockfish
DEPTH = config["depth"]  # Kedalaman analisis
MOVE_TIME = config["move_time"]  # Waktu pencarian per langkah (dalam detik)

# Inisialisasi engine Stockfish
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

def get_best_move(fen: str):
    """Mendapatkan langkah terbaik berdasarkan FEN (Forsyth-Edwards Notation)"""
    board = chess.Board(fen)
    result = engine.play(board, chess.engine.Limit(depth=DEPTH, time=MOVE_TIME))
    return result.move

# Contoh penggunaan
if __name__ == "__main__":
    # Papan awal
    fen_position = chess.STARTING_FEN
    best_move = get_best_move(fen_position)
    print("Best Move:", best_move)

# Tutup engine saat selesai
engine.quit()