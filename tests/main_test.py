from game.send_text import text_content
from dotenv import load_dotenv


def test_text_content():
    result = text_content(1.22)
    return "Thank you so much for playing Champions are Coming. In total, you have been playing for 1.22 seconds. Play again to beat your time!"

