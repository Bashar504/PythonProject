# thirty-one
#### Video Demo:  <https://youtu.be/g1tyny-7Lio>

#### Description:
This project is a simple card game implemented in Python. The game is played by multiple players who take turns drawing cards from a deck and trying to avoid going over a total score of 31. Players can choose to draw a card or pass on their turn. The game continues until all players have either passed or gone out (exceeded 31). The player with the highest score (without exceeding 31) wins the game.

## How to Use:
1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Run the `card_game.py` file to start the game.
4. Follow the on-screen instructions to play the game.

## Features:
- Random card distribution to players at the beginning of the game.
- Playerschoose to draw a card or pass.

## Future Enhancements:
- Implementing a graphical user interface (GUI) for better user experience.
- Adding more advanced gameplay features such as special cards.
- Allowing for customizable game settings such as the difficulty level.

## Code Explanation:

### `CardGame` Class:

The `CardGame` class serves as the backbone of the card game implementation, providing essential functionalities for managing the game flow and player interactions.

- **Initialization ( __init__ method)**:
  - The `__init__` method initializes a new instance of the `CardGame` class.
  - `cardSet`: Represents the deck of cards, which is initialized using the `createCardSet` method.
  - `passes`: A list that keeps track of players who have passed their turn.
  - `out`: A list that records players who have exceeded the total score of 31.
  - `numberOfPlayers`: Stores the total number of players participating in the game.
  - `playerDict`: A dictionary mapping player names to their respective card sets.

- **Main Logic (main method)**:
  - The `main` method serves as the entry point for the game, coordinating player setup, game execution, and end-game analysis.
  - It prompts users to input the number of players, distributes cards, starts the game, and provides a summary of results.

- **Gameplay Logic**:
  - Methods such as `startTheGame`, `playerTurn`, `continueGambling`, `endOfTurn`, and `endOfGame` handle various aspects of gameplay.
  - `startTheGame`: Controls the game rounds until all players have either passed or gone out.
  - `playerTurn`: Manages the turn sequence for each player, allowing them to draw cards or pass.
  - `continueGambling`: Simulates a player drawing a card and updates their card set accordingly.
  - `endOfTurn`: Signals the conclusion of a player's turn.
  - `endOfGame`: Presents the final game results, including players who went out or passed, and determines the winner(s).

### Test Suite:

The test suite ensures the reliability and correctness of the implemented functionalities through various test cases.

- **Fixture Setup**:
  - The `game` fixture creates a `CardGame` instance, ensuring a consistent setup for each test case.

- **Test Cases**:
  - `test_CreateCardSet`: Validates the `createCardSet` method by ensuring the deck contains the correct number of cards.
  - `test_getPlayerSet`: Confirms that each player receives the expected number of cards.
  - `test_continueGambling`: Verifies that a player's card set increases in size after drawing a card.
  - `test_findWinner`: Ensures that the `findWinner` method correctly identifies the winner or winners based on their scores.

## Conclusion:

The `CardGame` class provides a comprehensive framework for playing the "thirty-one" card game, while the accompanying test suite guarantees the accuracy and reliability of its functionalities. With a well-defined structure and thorough testing, the code serves as a solid foundation for further development and customization. It offers an excellent starting point for expanding the card game's features and improving the user experience. By adhering to best practices in software development and continuous testing, the codebase maintains its robustness and scalability, making it suitable for both casual gameplay and more advanced applications.
