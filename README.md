
# RPS-exercise
This is a simple Python program for playing Rock, Paper, Scissors using command-line.

## Prerequisites
Anaconda 3.7
Python 3.7
Pip

## Repo Setup
Make a copy of this repo as needed. Clone a copy of the repo onto your local computer using Github Desktop or other equivalent software. Navigate there from the command-line. If you are using Github Desktop, cloned repo might be nested in the following directory.

C:\Users\"username"\Documents\GitHub\RPS-exercise

To navigate to the repo using command-line, first check your current directory by:

```sh
pwd
```
You should see something like:
/c/Users/"username"

Then navigate to the RPG-exercise repo:

```sh
cd ~/Documents/GitHub/RPS-exercise
```

## Virtual environment setup
Create and activate a new Anaconda virtual environment:

```sh
conda create -n rps-env python=3.7
```

```sh
conda activate rps-env
```

## How to start game
Once virtual environment is created and activated, type the following into the command-line to start game.

```sh
python game.py
```

If typed in and executed properly, you should see a welcome message and be prompted to pick your move.

## Play game
You may pick from Rock, Paper or Scissors. Pick one and type into the command-line, then press enter.

```sh
Rock
```
or
```sh
Paper
```
or
```sh
Scissors
```

The program will alternatively accept all-lower case or all-upper case, but will reject mixed cases (eg. rOcK) or other invalid words. If successful, you will see your move, computer's move and the result displayed.

## Invalid moves
If you execute an invalid move, the game will display a message telling you that the move is invalid.
To start a new game, repeat the earlier step by entering:

```sh
python game.py
```