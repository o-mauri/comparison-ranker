# comparison-ranker
A simple python script for helping you rank a list of things by prompting you to put them up against eachother. First created to help my girlfriend find her favourite Taylor Swift songs.

## Features

- **Elo-based ranking:** Items are ranked using the Elo rating system, commonly used in chess and competitive games.
- **Interactive comparisons:** The program repeatedly asks you to choose between two items, updating their scores after each choice.
- **Easy data management:** Start with a simple list of items, and the program manages their scores in a data file.
- **Backup support:** Optionally back up your current rankings before resetting or starting a new session.

## File Structure

- `main.py` — The main script for running the ranking process. Presents pairs of items for comparison and updates their Elo scores.
- `startup.py` — Initializes or resets the ranking data. Reads a list of items from `input.txt` and creates a fresh `data.txt` with starting Elo scores. Optionally backs up the current data.
- `input.txt` — A plain text file listing the items to be ranked, one per line.
- `data.txt` — Stores the current Elo scores for each item, in the format `ItemName:::Score`.
- `backups/` — Contains backup copies of previous `data.txt` files.

## Getting Started

### Prerequisites

- Python 3.x

### Setup

1. **Prepare your list of items:**

   - Edit `input.txt` and add each item you want to rank on a new line.
2. **Initialize the data file:**

   - Run `startup.py` to generate `data.txt` from your `input.txt` list. You will be prompted to optionally back up the current data.

   ```bash
   python startup.py
   ```
3. **Start ranking:**

   - Run `main.py` to begin the interactive ranking process.

   ```bash
   python main.py
   ```

   - The program will repeatedly show you two items and ask which you prefer. Enter `1` or `2` to select your favorite. Rankings are updated after each choice.

### Backups

- Before resetting or re-initializing your data, you can create a backup. Backups are stored in the `backups/` directory and can be restored manually if needed.

## Example

- `input.txt`:

  ```
  Lampard
  Drogba
  Hazard
  Cahill
  Kalou
  Malouda
  ```
- After running `startup.py`, `data.txt` will look like:

  ```
  Lampard:::1600
  Drogba:::1600
  Hazard:::1600
  Cahill:::1600
  Kalou:::1600
  Malouda:::1600
  ```
- As you use `main.py`, the Elo scores in `data.txt` will change based on your preferences.

## Customization

- You can change the starting Elo score in `startup.py` by modifying the `STARTING_SCORE` variable.
- The Elo K-factor (which determines how much scores change per comparison) can be adjusted in `main.py` via the `K_FACTOR` variable.
