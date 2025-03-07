import streamlit as st
import chess
import chess.engine
from PIL import Image
import chess.svg
import cairosvg
from io import BytesIO

def get_board_image(board):
    # Convert chess board to SVG and then to PNG
    svg_data = chess.svg.board(board=board, size=400)
    png_data = BytesIO()
    cairosvg.svg2png(bytestring=svg_data.encode('utf-8'), write_to=png_data)
    return Image.open(png_data)

def evaluate_position(board):
    with chess.engine.SimpleEngine.popen_uci("stockfish") as engine:
        evaluation = engine.analyse(board, chess.engine.Limit(time=0.1))
        return evaluation["score"].relative
def main():
    st.title("Chess Analysis App")
    board = chess.Board()
    
    # User Input: Move
    move = st.text_input("Enter your move (e.g., e2e4):")
    if st.button("Make Move"):
        if chess.Move.from_uci(move) in board.legal_moves:
            board.push(chess.Move.from_uci(move))
        else:
            st.error("Invalid move! Try again.")
    
    # Display Chess Board
    st.image(get_board_image(board))
    
    # Evaluation of Position
    evaluation = evaluate_position(board)
    st.write(f"Position Evaluation: {evaluation}")
    
    # Best Move Suggestion
    with chess.engine.SimpleEngine.popen_uci("stockfish") as engine:
        best_move = engine.play(board, chess.engine.Limit(time=0.1)).move
        st.write(f"Suggested Best Move: {best_move}")

if __name__ == "__main__":
    main()
