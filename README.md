
# ChecSpecc
Python package that checks if computer meets recommended specifications to run python programs
(Few features only work on windows)

## Features
- Creates a json file with recommended requirements based in  developer's system hardware
- takes CPU name ,RAM , GPU details
- Compares it to system hardware of user's pc and tells whether it is idealto run the program
- Has One CPU database with benchmark Scores that will do the comparision (GPU table will be added soon)


## Help Needed

- Creating the pypackage with 3 files > init file for cli , main file with compare function  and data dir with one database (second will be added soon)
- Writing unitTests
- Fixing some issues to get CPU name from MacOS (platform.system == Darwin)

## Current Build

![screen-capture](https://user-images.githubusercontent.com/22007192/127732974-43021c3a-a00f-4bbe-8c98-23bfe158cbb5.gif)

![Screenshot (19)](https://user-images.githubusercontent.com/22007192/127733242-e56e4f8b-e18e-4501-ac79-048ced7b535c.png)
![Screenshot (20)](https://user-images.githubusercontent.com/22007192/127733244-24a37eb7-acf9-4934-a0cb-ac7857e8a382.png)
