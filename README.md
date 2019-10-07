# Hearts

A client that plays the Hearts card game with 4 people.

## Installation

Clone the git repository and navigate into the directory
Run the following:
```python
python3 Game.py
```

**NOTE**: Make sure the game is run on as large a screen as possible, otherwise the cards will not display well. Zoom in if necessary.

**Optional**: 

To run the game automatically (no interaction), change the ```automated```variable in Game.py to ```True```.

To run the game with no delay (if you do not want the plays made gradually), set the ```delay``` to ```False```.

## Rules

### Objective
End with the least number of points.

### Scoring
At the end of each hand, players count the number of hearts they have taken as well as the queen of spades, if applicable. 

Each heart - 1 point

The Queen of Spades - 13 points

The game is played until one player reaches 100 points.

When a player takes all 13 hearts AND the queen of spades in one hand, instead of losing 26 points, that player scores zero and each of his opponents score an additional 26 points. This is called *shooting the moon*.

### The Deal

Deal the cards one at a time, face down, clockwise. Everyone will have 13 cards.

### Gameplay

The player with the two of spades plays their card down first. The person to their left must "follow suit" by playing any one of their club cards. If they do not have a club card, they can play any card except for a point card (that is, they cannot play a hearts card or the Queen of Spades).

Then the next person to the left follows suit, and finally, the last person does. This sequence of 4 cards being played is called a "trick".

The person who played the highest-ranking card of the suit that was led (clubs, in this case) takes the four cards. For example, if the cards were played like this: 2♣, A♣, 10♣, 5♣, then the person who played the Ace - A♣ - will take the trick, because the Ace is the highest-ranking card.

The person who takes the trick leads the next trick by placing any card from their hand, except a point card, in the middle. You cannot lead with a point card until hearts are broken, as discussed in a following section.

### Rules

Each player must follow the suit of the first card in the trick if possible. If a player is void of the suit led, a card of any other suit may be discarded. However, if a player has no clubs when the first trick is led, a heart or the queen of spades **cannot** be discarded. The highest card of the suit led wins a trick and the winner of that trick leads next. There is no trump suit.

You can never open a trick with a hearts unless *hearts has been broken* or if you have nothing but point cards (point cards are any hearts or the Queen of spades)

#### Rules adapted from:

worldofcardgames.com/hearts-card-game-rules.html

bicyclecards.com/how-to-play/hearts/

## Design

### Data Structures
Card implemented with two attributes: CardValue and Suit

Deck implemented as a stack

Hand implemented as a deque where sorting performed on insertion.

Trick implemented as basic array

## Tooling

Python used for quick data structure implementation using deque from collections library as well as other libraries including time and random.

Testing done case by case (due to randomness of dealt cards). Monitored 75+ games without issue.