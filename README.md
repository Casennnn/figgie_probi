# README

## Overview

This repository contains two Python scripts designed to assist players in analyzing their starting hands in the card game [Figgie](https://www.figgie.com/how-to-play.html) which is developed by Jane Street. The scripts utilize different algorithms to provide insights into probabilities and combinations, enhancing gameplay strategy.

## Files

1. **goalsuitquantcal.py**
   - This script calculates the probability of achieving a winning goal suit based on your starting hands. It is flexible and does not limit the number of players, allowing for scenarios with 4 or 5 players, which means the total number of cards can be 8 or 10.
   - The probability is deduced using Monte Carlo simulations, providing a statistical approach to determine the likelihood of success.
   - After outputting a chart of probabilities, the program continuously loops, asking for new input. This feature allows users to adapt their strategy in real-time during the game for each new round.

   **Usage**:
   ```bash
   python goalsuitquantcal.py
   ```
2. **infotelllist.py**
   - This script lists all possible combinations of starting hands, sorted in descending order based on the amount of information each hand contains.
   - The calculations assume a 4-player game with a starting hand of 10 cards, providing a comprehensive overview of potential starting hands.

   **Usage**:
   ```bash
   python infotelllist.py
   ```

