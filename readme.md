# Kollision

This is one of my very first school project, made with [Loric Blanchard](https://github.com/LoricBlanchard).

You can find the original subject [here](./kollision.md).

Note that I didn't modify the code, contrary to the [PPM-Visualiser](https://github.com/GouruRK/PPM-Visualiser) and the [ASCII-ART](https://github.com/GouruRK/ASCII-ART) projects. The code is the same as when we gave back the project, so it might be a bit ugly ...


## Table of content
- [Kollision](#kollision)
  - [Table of content](#table-of-content)
  - [Features](#features)
  - [How to install](#how-to-install)
  - [Known issues](#known-issues)

## Features
* Play the classic Kollision game
* Ball collisions
* Timer

## How to install

```bash
# Clone git repository
git clone https://github.com/GouruRK/Kollision.git

# Go into the repo
cd Kollision

# Launch
python3 kollision.py
```

Optionnals arguments :

```bash
# Show help message
python3 kollision.py -h

# Game mode
python3 kollision.py -m <solide (default) | gazeux>

# Modify game intensity
python3 kollision.py -l <1 (default) | 2 | 3>

# Maximum speed for a ball
python3 kollision.py -max <argument>

# Minimum speed for a ball
python3 kollision.py -min <argument>
```

Note that windows user may type `py` instead of `python3`

Mode informations :
* In game mode `gazeux` mean that red balls can go through each other
* Game mode `solide`, there are collisions between balls

Game intensity :
* Level 1 : new ball each 30s
* Level 2 : new ball each 15s
* Level 3 : new ball each 5s

## Known issues

Some issues are :
* In `gazeux` mode, balls can clip into each other
* The collision between balls aren't eslastic. You can easily see it by changing the balls radius

___

Check out my other projects on github : [Gouru](https://github.com/GouruRK/).