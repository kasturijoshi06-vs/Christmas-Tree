# Christmas-Tree
# Christmas-Tree
## Overview
This application starts the redlight-greenlight game when a user utters sentences like "Santa, start the game" containing words "game", "betsy" or "santa" or "play" 
Th application plays the instructions and notifies the game application to start the game
## Instructions
1. Provide authentication credentials by setting the environment variable GOOGLE_APPLICATION_CREDENTIALS
```sh 
export GOOGLE_APPLICATION_CREDENTIALS="$PATH/key_file.json" 
```
Replace $PATH with the directory where the key file is stored

2. Download the audio file

3. Run the **tree_start.py** file

4. Speak sentences containing the word "play" or "game" or "santa" or "betsy" to start the game.
