# Battlemetrics-Squad-Info
A script which will gather all the details it can using the BattleMetrics API of a Squad server and parse the .json file. All details are stored separately purposely for people who dont understand the API but would like to get their server details and then implement them into one of their own projects somewhere else.

## Developers:
- LukeeSucks

## Required Libs:
- Requests (pip install requests)

## What This Is For:
The script alone doesnt exactly have a purpose or good use unless you just wanted to view the details of a server quickly, the main reason this was made was to allow for people to use this code and implement it somewhere in another one of their projects, the API can be a bit confusing at first for some so this skips that part and allows them to get the details that are stored ready as variables so it can just be thrown stright into whatever they desire. The Current input is just taking the servers Battlemetric Uniqie Server ID, the output is just being printed in terminal, however they are both intended to be changed to fit the project at hand.

## Usage:
You will need to get your API key from Battlemetrics after creating your account and will need to pase it into **API_TOKEN** in **APIScript.py** near the bottom of the file.

<img width="510" alt="Screenshot 2023-12-25 at 21 13 22" src="https://github.com/LukeeSucks/Battlemetrics-Squad-Info/assets/105941171/1765a5ae-b910-43e3-bdb3-52489c4ab958">

You will be able to then run the script to which in terminal it will ask you for a the Unique Server ID just copy and paste it in from the Battlemetrics website URL of your desired server.

<img width="305" alt="Screenshot 2023-12-25 at 20 53 31" src="https://github.com/LukeeSucks/Battlemetrics-Squad-Info/assets/105941171/44cff880-390e-4d01-902d-3c905a905b81">

<img width="331" alt="Screenshot 2023-12-25 at 21 17 27" src="https://github.com/LukeeSucks/Battlemetrics-Squad-Info/assets/105941171/4c3935ed-6b7c-4ddd-82e9-0edace76775c">

Once you press enter it will grab the JSON from the dsired server info and parse it and paste the details into terminal for you to see, additionally from the code you can see each individual varible name or each of the data.

<img width="810" alt="Screenshot 2023-12-25 at 20 53 41" src="https://github.com/LukeeSucks/Battlemetrics-Squad-Info/assets/105941171/39b1e86a-6d89-47a5-8dee-57324a51c6ce">

