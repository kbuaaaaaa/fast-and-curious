import numpy as np
def create_numbered_deck(n):
    """
    Helper function to create a deck of cards numbered from 0 to n-1.

    Args:
    - n (int): Number of cards in the deck.

    Returns:
    - list: List of integers representing the numbered deck.
    """
    return np.arange(n)

def cut(deck, n):
    """
    Helper function to perform a cut operation on the deck.

    Args:
    - deck (list): List representing the deck of cards.
    - n (int): Number of cards to cut from the top to the bottom.

    Returns:
    - list: List representing the deck after performing the cut operation.
    """
    
    return np.concatenate((deck[n:], deck[:n]), axis=0)

def deal(deck):
    """
    Helper function to deal the deck to a new pile, reversing the order of cards.

    Args:
    - deck (list): List representing the deck of cards.

    Returns:
    - list: List representing the deck after performing the deal operation.
    """


    return np.flip(deck)

def faro_shuffle(deck):
    """
    Helper function to perform a Faro out-shuffle on the deck

    A faro out-shuffle (also known as a perfect, or weave, out-shuffle)
    involves splitting the deck into two equal halves and then interleaving them
    perfectly, starting with the top card of the original deck. 

    Args:
    - deck (list or np.ndarray): List or NumPy array representing the deck of cards.

    Returns:
    - np.ndarray: NumPy array representing the deck after performing the Faro shuffle.
    """
    size = len(deck)
    half = size // 2

    # Split the deck into two halves
    first_half = deck[:half]
    second_half = deck[half:]

    # Create an empty array for the shuffled deck
    new_deck = np.empty(size, int)

    # Interleave the two halves
    new_deck[0::2] = first_half
    new_deck[1::2] = second_half

    return new_deck

def find_card_position(deck_size, instructions, card):
    """
    Find the position of a specific card in a deck after applying a series of instructions.

    Args:
    - deck_size (int): Number of cards in the deck.
    - instructions (list of str): List of instructions to apply to the deck.
    - card (int): The card to find the position of.

    Returns:
    - int: Position of the card in the deck after applying all instructions.
    """
    deck = create_numbered_deck(deck_size)

    for instruction in instructions:
        if instruction.startswith("cut"):
            n = int(instruction.split()[-1])
            deck = cut(deck, n)
        elif instruction.startswith("deal"):
            deck = deal(deck)
        elif instruction.startswith("shuffle"):
            deck = faro_shuffle(deck)

    return np.where(deck == card)[0][0]
