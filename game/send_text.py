from dotenv import load_dotenv

def text_content(seconds):
    """
    Returns text content containing game stats to be sent to user
    Parameters: 
        seconds (int): the amount of time played
    """ 
    content = "Thank you so much for playing Champions are Coming. In total, you have been playing for " + str(seconds) + " seconds. Play again to beat your time!"
    return content

