# Freestyle: Champions are Coming

## Instalation

Fork this repository and then use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

Navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd ~/Desktop/Freestyle
```

## Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n game-env Pytho=3.7 #first time only
conda activate game-env #after creation
```

Install the requirements.txt file in the environment:

```sh
pip install -r requirements.txt
```

## Playing the Game

From within the virtual environment, use the following command to run the Python script from the command-line:

```sh
python game/main.py
```
