# Gargoyles-Game.py
Project 1 Disney’ Gargoyles: Awakening Board Game  With plan to be redone as a python game.  
Theme and Basic Storyline: 
The game is set in the mystical world of New York City, where ancient stone gargoyles come to life at night. 
These noble protectors awaken from their stone slumber to defend the city against supernatural threats. The storyline revolves around a critical mission: collecting powerful artifacts scattered throughout Manhattan before the villainous Xanatos can exploit them for nefarious purposes. 
Characters (Players): 
1.	Goliath: The fearless leader of the gargoyles. He possesses immense strength and wisdom. As the leader, Goliath can inspire his allies, granting them extra actions or dice rerolls. 
2.	Brooklyn: Agile and quick, Brooklyn excels at scouting and navigating the city. Brooklyn is agile and can move quickly across the board. His special ability allows him to reposition and engage enemies efficiently. 
3.	Lexington: The tech-savvy gargoyle who can manipulate gadgets and devices. Lexington is techsavvy. His ability lets him manipulate gadgets and devices, providing strategic advantages. 
4.	Broadway: Strong and resilient, Broadway is the muscle of the group. Broadway is strong and resilient. His special ability enhances his combat prowess, allowing him to deal more damage. 
5.	Hudson: The wise elder gargoyle with knowledge of ancient lore. Hudson is wise and experienced. His ability allows him to share knowledge with other players, granting them insights into upcoming challenges. 
6.	Elisa Maza: The human NYPD detective who aids the gargoyles with her investigative skills. As a detective, Elisa can gather information about the villains. Her special ability helps reveal their plans and weaknesses. 
Rooms and Locations (Minimum of Eight): 
1.	Clock Tower: The gargoyles' home base atop the clock tower. 
2.	Central Park: A vast green expanse where secrets hide. 
3.	Xanatos Enterprises: Xanatos's corporate headquarters, shrouded in mystery. 
4.	Art Museum: A place of culture and intrigue. 
5.	Underground Tunnels: Dark passages connecting key locations. 
6.	Library: Hudson's favorite haunt for research. 
7.	Skyscraper Rooftop: A strategic vantage point. 
8.	Hidden Crypt: A forgotten chamber with ancient artifacts. 
Items (Minimum of Six): 
1.	Eye of Avalon: A mystical gem that enhances magical abilities. 
2.	Steel Wing: A gargoyle relic that grants flight. 
3.	Pendant of Shadows: Allows the wearer to move unseen. 
4.	Scroll of Protection: Provides temporary invulnerability. 
5.	Phoenix Feather: A rare ingredient for powerful spells. 
6.	Silver Key: Unlocks hidden doors and passages. 
Villain: David Xanatos: A cunning billionaire with his own agenda. He seeks the artifacts to gain ultimate power and control over the city. Xanatos is not to be underestimated! 
 Basic original Game Play: Disney Gargoyles: Awakening is a cooperative strategy board game inspired by the 1990s Disney cartoon series Gargoyles. Here are the key details: 
•	Players: 2 to 5 players 
•	Characters: You can play as one of six Gargoyles characters: Goliath, Brooklyn, Lexington, Broadway, Hudson, or NYPD detective Elisa Maza. 
•	Objective: Work together to defend Manhattan against iconic villains like Xanatos and Demona. 
•	Gameplay: The 3D cityscape board features Manhattan as depicted in the cartoon. There are four different “episodes” to play, including one where a player controls the villains. 
•	Miniatures: The game includes miniatures of the Gargoyles characters. 
•	Learn to Play: You can find a video tutorial titled “Watch It Played! Disney Gargoyles Awakening” online1. The game was released by Wonder Forge and is suitable for ages 10 and up. 
 Player Order: Determine the player order for the round. Players take turns clockwise. Activation Phase: 
1.	The active player chooses one of the Gargoyles characters to activate. 
2.	They can move their character up to their movement value (usually indicated on the character card). 
3.	If they encounter a villain or an event space, they resolve the encounter. 
7. Combat Phase: 
1.	If the active player is adjacent to a villain, they can engage in combat. 
2.	Roll the custom dice to attack. Symbols on the dice represent hits, misses, and special 
abilities. 
3.	Apply damage to the villain based on successful hits. 
8. Special Abilities and Cooperation: 
1.	Players can use their character’s special abilities during their turn. 
2.	Communication is crucial! Discuss strategies, share information, and decide collectively how to tackle challenges. 
9. Villain Activation: 
1.	After all players have taken their turns, activate the villains. 
2.	Villains move, attack, and carry out their schemes based on the scenario rules. 
10. Event Resolution: 
	1. 	Resolve any ongoing events or effects based on the scenario. 
11. End of Turn: 
	1. 	Pass the turn to the next player. 
Remember, working together and using each character’s abilities strategically will lead to victory!     
Map Design: 
Here is a simple map layout and a picture of the game elements: 
   +-------------------+ 
   |    Start Room             |  
   |                   | 
   |    Clock Tower    |                         
   +----+-------+------+ 
        |       | 
        |       | 
+-------+-------+-------+ 
|  Central Park         | 
|                       | 
|  Art Museum           | 
+-------+-------+-------+ 
        |       | 
        |       | 
+-------+-------+-------+ 
|  Xanatos Enterprises  | 
|                       | 
|  Underground Tunnels  | 
+-------+-------+-------+ 
        |       | 
        |       | 
+-------+-------+-------+ 
|  Library              | 
|                       | 
|  Skyscraper Rooftop   | 
+-------+-------+-------+ 
        |       | 
        |       | 
+-------+-------+-------+ 
|  Hidden Crypt         | 
|                       | 
|  Villain's Lair       | 
+-----------------------+ 
If players fail to complete the objectives in the Disney Gargoyles: Awakening board game, they lose the scenario. The game typically has consequences for failure, such as advancing the villain’s schemes or worsening the situation in Manhattan. However, players can learn from their mistakes and try again!  Remember, the game's success hinges on teamwork, strategy, and resourcefulness. Good luck with your pitch, and may the gargoyles prevail!  
 A simple pseudocode for the game mechanics of your Disney’s Gargoyles: Awakening text-based game. It covers movement between rooms and item collection. 
1. Initialize game state:
   - Create a list of rooms (with names and descriptions).
   - Assign items to specific rooms.
   - Set the player's starting room.

2. Display the game introduction:
   - Welcome the player to the world of gargoyles.
   - Explain the mission: Collect artifacts before Xanatos does.

3. Main game loop:
   - Repeat until the player wins or encounters the villain:
       a. Display the current room description.
       b. Prompt the player for their action (e.g., "Move" or "Get item").
       c. Handle the player's input:
           - If "Move":
               i. Ask the player which direction (North, South, East, West).
               ii. Update the player's current room based on the chosen direction.
           - If "Get item":
               i. Check if there's an item in the current room.
               ii. If yes, add it to the player's inventory.
               iii. Remove the item from the room.
       d. Check victory conditions (all items collected).
       e. Randomly trigger villain encounters (based on room or chance).

4. Victory or Defeat:
   - If the player collects all items before encountering Xanatos:
       - Display a victory message.
   - If the player encounters Xanatos:
       - Display a defeat message.

5. End the game. 
