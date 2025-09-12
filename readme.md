# Mastermind

A Python implementation of the *Mastermind* puzzle game.

## Requirements:

Must have python installed. Python can be installed [here](https://www.python.org/downloads/).

## Installation: 
If you have GIT installed, you can use the below command-line installation:  

```bash
git clone https://github.com/JohnP2025/Mastermind_Game_Project.git
cd Mastermind_Game_Project
```

Alternatively, from the main page of this repository, you can select Code -> Download ZIP. Then extract the files to a desired directory, navigate to the install location in file explorer, right click the project directory, and select Open in Terminal.

## Usage:
    
Once in the project directory, the script can be run from the command line using `python mastermind.py`

The terminal will then accept input for your first guess. Valid guess syntax is explained on startup or on an invalid guess.

## Testing: 

The current stable version was manually tested, and test case outputs can be found in the project directory. Future versions will support automated testing.

## Version History and Changelog: 
- v1: CLI implementation
- v2: Overhaul of existing logic for modularity and integration with Flask API
- v3+: Interactive web interface, database integration

TODO: 
1. Add checking for guesses that have already been entered
2. Replace existing dictionary memory system with proper database integration
3. Build in support for game customization (sequence length, possible color options, maximum guesses)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
    
