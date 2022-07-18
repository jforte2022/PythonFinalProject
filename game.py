import math
import random
import sys

def main():

    end = False
    # This loop runs until the player quits the game
    while not end:
        print("1. New Game\n")
        print("2. Quick Tutorial (Recommended for New Players)\n")
        print("3. Quit\n")
        print("Please select a menu option: ")
        choice = input()

        match choice:
            # case 1 is the actual game
            case "1":
                # This first section of the game introduces the player to the various classes and asks the user to choose one
                print("INSPIRATION: You arrive at the base of a large snow-tipped mountain. You know what you must do.")
                input()
                print("SUGGESTION: This would be a good place to spend the night. The sun is setting.")
                input()
                print("EGO: But who are you?")
                input()

                # This code below was used to playtest the game and helped me run many trails to balance the classes/encounter formulas. I decided to leave it in the file because I spent so much time in this loop lol
                """                
                while True:
                    # tester = Combatant("Warrior", 250, 19, 5, 6)
                    # tester = Combatant("Assassin", 200, 7, 7, 16)
                    tester = Combatant("Jester", 200, 5, 15, 10)
                    enemy = Combatant("Enemy", 100, random.randint(5, 15), random.randint(5, 15), random.randint(5, 15))
                    # enemy = Combatant("Enemy", 200, 10, 10, 5)
                    tester.encounter(enemy)
                """

                playerClass = chooseClass()
                match playerClass:
                    case 1:
                        print("You are a Warrior. A hefty soldier. No brain.\n")
                        player = Combatant("Warrior", 450, 19, 5, 6)
                    case 2:
                        print("The Assassin, eh? Better clean enemies up quickly, lest your indolence be your downfall.\n")
                        player = Combatant("Assassin", 425, 7, 7, 16)
                    case 3:
                        print("Risky move.. You read the class description, right? This guy's weak! Well, good luck. You'll need it.\n")
                        player = Combatant("Jester", 425, 5, 15, 10)

                # This next section introduces the world and then the first enemy encounter
                print("PERCEPTION: You awake from a deep slumber. Wind rushes through your camp as you slowly adjust to the light.")
                input()
                print("GRIT: You are on a mission. You must reach the summit of this mountain before The Mad Frenchman fulfills his plan to conquer the world.")
                input()
                print("INNER MONOLOGUE: What's this? A Frenchman? The end of the world?")
                input()
                print("NARRATOR: It matters not. Play along.")
                input()
                print("You pack your things and resume your ascent.")
                input()
                print("After hours of climbing you happen upon a simple creature.")
                input()
                print("PERCEPTION: Although you've never seen this creature before, something inside of you knows it isn't friendly.")
                input()
                print("SUGGESTION: Maybe sneak up on it? Attack it from behind?")
                input()
                innocentCreature = Combatant("Mountain Creature", 80, 16, 7, 7)

                match playerClass:
                    case 1:
                        print("STEALTH (FAILURE): As you approach the creature, you trip on a rock, losing your advantage. ")
                        input()
                        print("Nevertheless, you manage to attack the creature first.")

                    case 2:
                        print("STEALTH (SUCCESS): You've done this before. You manage to strike the foe without it even knowing you were there.")

                    case 3:
                        print("STEALTH (SUCCESS): You manage to sneak up on the creature and strike it somewhat weakly. At least it didn't see you coming.")

                player.encounter(innocentCreature)

                # The next section leads to the second encounter
                print("JOIE DE VIVRE: Well, that could have gone worse.. Time to move on.")
                print("You continue up the mountain.")
                input()
                print("Hours pass. The light is nearly gone.")
                print("SELF-PRESERVATION: This looks like a good spot to spend the night.")
                input()
                print("PERCEPTION: As you begin to settle down, you notice in the near distance a faint light.")
                input()
                print("CURIOSITY: You decide to investigate.")
                input()
                print("As you approach the light, the outline of a cabin appears.")
                input()
                print("TREPIDATION: Why is there a cabin in the middle of nowhere on this lonely mountain.")
                input()
                print("METTLE: Despite your concern, you knock loudly on the door.")
                input()
                print("You knock several more times. You know there must be someone, as you can see flames within the cabin's fireplace.")
                input()
                print("Finally, an old man opens the door.")
                input()
                print("OLD MAN: Jean-Luc, come in, come in! I've been waiting for you! Food's almost ready!")
                input()
                print("DISORIENTATION: You stare at the man without saying anything. You definitely aren't Jean-Luc.")
                input("OLD MAN: How was work? Boss still giving you trouble about that issue?")
                input()
                print("EMPATHY: This old man is clearly unwell. Who knows how long he's been here. All alone.")
                input()
                print("OLD MAN: Jean-Luc, take your pick!")
                print("The old man offers you one of three items.")
                input()
                print("A beautiful steak is placed on the table in front of you. It has just been taken off the heat. It is cooked to perfection and smells incredible.")
                print("Surely this will help you recover from that monster you fought earlier.")
                input()
                print("Next to this, the old man pours a glass of tea.")
                print("REVULSION: You've never smelt anything this disgusting before.")
                input()
                print("OLD MAN: Oh, stop with that grimace, Jean-Luc. This will make you stronger!")
                input()
                print("Finally, the old man reaches into his coat pocket and brings out a device.")
                print("TECHNOLOGICAL LITERACY: This looks fancy. Surely it will give you an advantage as you continue your journey.")
                input()
                print("OLD MAN: So which will it be?")
                print("(1) Steak (+75 health)  OR  (2) Tea (+10 strength)  OR  (3) Odd Device (+10 intelligence)  OR  (4) kill the weak, old man and steal all three items")

                # Old man choice/encounter
                oldManChoice = int(input())

                match oldManChoice:
                    case 1:
                        player.health += 75
                        print("SUGGESTION: Surely increasing my health will pay off in the future, right?")
                        print("After choosing the man's gift, he offers you a place to sleep.")

                    case 2:
                        player.strength += 10
                        print("PHYSICALITY: I MUST BECOME STRONGER!!!")
                        print("The old man furls his eyebrow in confusion")
                        input()
                        print("After choosing the man's gift, he offers you a place to sleep.")

                    case 3:
                        player.intelligence += 10
                        print("INNER-EINSTEIN: My brain will one day be bigger than this mountain.")
                        input()
                        print("After choosing the man's gift, he offers you a place to sleep.")

                    case 4:
                        print("DEPRAVED, GREEDY SOUL: I want it all")
                        oldMan = Combatant("Old Man", 50, 5, 9, 7)
                        player.encounter(oldMan)
                        player.health += 75
                        player.strength += 10
                        player.intelligence += 10
                        print("EMPATHY: You are a horrible person.")
                        input()
                        print("DISTURBED: After killing the old man, you steal his gifts and then sleep in his old bed.")
                        input()

                print("WELL-RESTED: You leave the cabin after a long night's rest.")
                input()
                print("GRIT: Even after several days of climbing this mountain, you push onward.")
                input()
                print("PERCEPTION: Something's wrong..")
                input()
                print("CLOAKED FIGURE: Don't move")
                input()
                print("INNER MONOLOGUE: I can't allow him to steal my things.")
                input()

                # Bandit encounter
                while choice != 1 and choice != 2:
                    print("Should you  (1) Attempt to reason with the mysterious figure  OR  (2) Attack without warning")
                    choice = int(input())
                    bandit = Combatant("Cloaked Figure", 125, 16, 10, 14)
                    match choice:
                        case 1:
                            print("SAVOIR FAIRE: What are you doing way up here? I don't want any trouble.")
                            input()
                            print("BANDIT: Hand over your things and there won't be trouble.. Now!")
                            input()
                            print("Please, I need my things. I'm on an important journey.")
                            input()
                            print("NARRATOR: Without warning, the bandit lunges at you!")
                            bandit.encounter(player)

                        case 2:
                            print("GRIT: I'm not about to get robbed when I'm so close to the end!")
                            player.encounter(bandit)

                # safe or risky path divergence
                print("PHYSICALITY: THAT'S WHAT YOU GET FOR TRYING TO ROB ME!")
                input()
                print("INSPIRATION: You look towards the peak of the mountain. It's finally in view.")
                input()
                print("You still have far to go, but the end is finally in sight.")
                input()
                print("As you travel along the edge's of the mountain, a cave comes into view.")
                input()
                print("PERCEPTION: A cave? On a mountain? Why would this be here?")
                input()
                print("Do you  (1) Risk going through the cave?  OR  (2) Continue on your current path?")
                choice = input()

                match choice:
                    case "1":
                        print("CURIOSITY: I have to explore. The cave might shield me from the elements anyway.")
                        input()
                        print("As you venture through the cave for a while, you finally are able to see the sun piercing through another opening in the cave system.")
                        input()
                        print("There's just one problem ... You need to jump across a gap to get to the other side.")
                        input()
                        print("GRIT: You plant your feet into the damp ground, psych yourself up, and run to meet the gap as fast as you can!")
                        if random.randint(1, 2) == 2 and player.strength >= 15:
                            print("CRITICAL SUCCESS: You meet the gap and fly across with ease!")
                            input()
                            print("PHYSICALITY: I NEVER DOUBTED YOU FOR A MOMENT!")
                            input()
                            print("This accomplishment has invigorated you further (+10 strength) (+75 health).")
                            player.health += 75
                            player.strength += 10
                        else:
                            print("As you begin to approach the gap, you know you don't have the skill to get across.")
                            input()
                            print("While flying through the air, you believe this is it, you're going to fall to your death.")
                            input()
                            print("Miraculously, you slam into the wall on the other side of the gap and are able to pull yourself up.")
                            print("This is not without consequence, however, as this escapade has left you injured (-5 strength) (-50 health).")
                            input()
                            print("You continue towards the light and are able to keep traveling up the mountain.")
                            input()
                            if player.health <= 50:
                                player.health -= (player.health - 1)
                            else:
                                player.health -= 50

                            player.strength -= 5

                    case "2":
                        print("PRUDENCE: It's not worth the risk. Besides, how would I even be able to see in there.")
                        input()
                        print("GRIT: You recover slightly from your past adventures (+40 health)")
                        player.health += 40
                        input()

                # Wolf pack encounter
                print("PERCEPTION: As you set up camp for the night, you hear faint howls calling in the night air.")
                input()
                wolfLeader = Combatant("Alpha Wolf", 150, 14, 6, 10)
                wolfCub1 = Combatant("Grey-furred Cub", 125, 11, 4, 12)
                wolfCub2 = Combatant("White-furred Cub", 125, 11, 4, 12)
                print("With a visceral sense of trepidation, you close your eyes and fall into a deep sleep.")
                input()
                print("After an insignificant passage of time, you are jolted awake by the sneers of several animals.")
                input()
                print("GRIT: You must face them. They know you are here. They sound hungry.")
                input()
                print("PERCEPTION: As you rise to meet the hungry beasts, you scan their ranks.")
                input()
                print("You see two cubs and their (much more intimidating) leader.")
                input()
                print("PHYSICALITY: You charge the first cub without fear!")
                player.encounter(wolfCub1)
                print("That's one wolf down, two to go. You turn your attention towards the second cub.")
                player.encounter(wolfCub2)
                print("As you finish off the second cub, the remaining wolf growls in a primal anger.")
                input()
                print("This wolf is bigger than any wolf you've ever seen. It leaps towards you!")
                wolfLeader.encounter(player)
                print("GRIT: Finally. I'm not stopping until I reach that peak.")
                input()

                # Final climb
                print("As you settle down, you fall into a heavy sleep.")
                print("UNCONSCIOUS MIND: You slip into a hazy dream.")
                input()
                print("You hear a voice calling to you. It is above you. You climb towards it.")
                input()
                print("UNKNOWN: Jean-Luc? Jean-Luc, is that you?")
                input()
                print("You climb past the obstacles in your way, cresting the hill.")
                input()
                print("UNKNOWN: Jean-Luc? Stay away from me! Stay away from me!")
                input()
                print("You jolt awake. Only with more questions than answers.")
                input()
                print("JOIE DE VIVRE: You aren't far from the peak. Today is the day this journey finally ends.")
                input()
                print("You begin climbing. Time passes quickly now. You move with purpose.")
                input()
                print("ANTICIPATION: This is it, the peak is less than a mile from your position now.")
                input()
                print("PERCEPTION: As you climb closer, you notice the temperature rise.")
                input()
                print("REALIZATION: You aren't on a mountain. This is a massive volcano!")
                input()

                # various endings
                if oldManChoice != 4:
                    oldManFinalForm = Combatant("Old Man", 100, 5, 9, 7)
                    print("OLD MAN: Ah, I see you took the long way up.")
                    input()
                    print("DISORIENTATION: What, how did you- Who are you?")
                    input()
                    print("OLD MAN: Now is not the time. Do you know what you must do?")
                    input()
                    match playerClass:
                        case 1:
                            print("I don't understand! I DON'T KNOW ANYTHING ANYMORE!")
                            input()
                            print("OLD MAN: You must cast yourself into the fire. It is the only way to free the world from the coming destruction.")
                            input()
                            print("Do you  (1) Accept what the man tells you, throwing yourself into the crater  OR  (2) Defy the man, and kill him  ?")
                            choice = int(input())
                            if choice == 1:
                                print("You give in to the man's demands, close your eyes, and fall into the crater.")
                            else:
                                print("EGO: No, this isn't right. You are the one who plagues this accursed mountain! You charge the man.")
                                player.encounter(oldManFinalForm)
                                print("As the man slumps over, the ground rises to meet your face.")
                                input()
                                print("PERCEPTION: You've fallen over; you're out of energy. This volcano has consumed you.")
                                input()
                                print("You rest for a minute, trying to catch your breath.")
                                input()
                                print("After what feels like only several minutes (but in reality was much longer), you hear the volcanic core roar.")
                                input()
                                print("Oh, no.")
                        case 2:
                            print("I- I don't know.")
                            print(
                                "OLD MAN: You must cast yourself into the fire. It is the only way to free the world from the coming destruction.")
                            input()
                            print(
                                "Do you  (1) Accept what the man tells you, throwing yourself into the crater  OR  (2) Defy the man, and kill him  ?")
                            choice = int(input())
                            if choice == 1:
                                print("You give in to the man's demands, close your eyes, and fall into the crater.")
                            else:
                                print(
                                    "EGO: No, this isn't right. The old man is the one who plagues this accursed mountain! You charge the man.")
                                player.encounter(oldManFinalForm)
                                print("As the man slumps over, the ground rises to meet your face.")
                                input()
                                print("PERCEPTION: You've fallen over; you're out of energy. This volcano has consumed you.")
                                input()
                                print("You rest for a minute, trying to catch your breath.")
                                input()
                                print("After what feels like only several minutes (but in reality was much longer), you hear the volcanic core roar.")
                                input()
                                print("Oh, no.")
                        case 3:
                            print("UNCONSCIOUS MIND: Jean-Luc.. Jean-Luc is me.. I'm the Frenchman..")
                            input()
                            print("I still don't understand.")
                            input()
                            print("With a solemn face, the old man hobbles over to you and rests his hands on your shoulders.")
                            input()
                            print("OLD MAN: One day, maybe.")
                            input()
                            print("His hands guide your shocked body slowly towards the volcanic crater.")
                            input()
                            print("OLD MAN: Goodbye, Jean-Luc")
                            input()
                            print("The man shoves you, plummeting your body into the lava below.")
                            input()
                            print("With a hint of relief in the man's face, he remarks:")
                            print("Goodbye")

                else:
                    print("You reach the top of the volcano. It is surprisingly quiet.")
                    input()
                    print("Where is this Frenchman who will destroy the world?")
                    input()
                    print("PRUDENCE: You decide to camp at the top of the volcano. Some sleep would do you good.")
                    input()
                    print("You awake to violent spasms, explosions, and piercing light.")
                    input()
                    print("PERCEPTION: The volcano is erupting.")
                    print("EGO: I don't understand. I thought it was my destiny-")
                    input()
                    print("Your lamentation is interrupted by lava, explosions, sulfur, and death. Your greed has doomed the world.")

                input()
                print("--------------------Fin--------------------")
                print("Thank you so very much for playing! Your ending is dependent on your class and on certain decisions made throughout the game! Returning to MENU")
                input()

            # MENU case 2 is the tutorial
            case "2":
                tutorial()

            # MENU case 3 exits the window
            case "3":
                sys.exit()

            # This (MENU) case invalidates errors
            case _:
                print("\nYou have not entered a valid choice.\n")

# I decided to just take the scripting for the tutorial out of the main function. There's no particular reason why, I guess.
def tutorial():
    print("\n\n\n\nWelcome! This game is quite simple.")
    print("You will begin by first choosing a class. Your options are: Warrior, Assassin, or Jester.")
    print("(Whenever there's a pause in the dialogue, press enter to continue)")
    input()
    print("These three classes have different stats. Each enemy in the game also has their own stats.")
    input()
    print("The different stats are: Health, Strength, Intelligence, and Stealth.")
    input()
    print("Each class (and enemy) specializes in one or more of these stats.")
    input()
    print("Your class will determine your attack methods, your dialogue, whether you pass certain skill checks, and will inform you on what decisions you should make at various points in the game.")
    input()
    print("Each class has been balanced so that it is possible to complete the game regardless of one's choice (although certain classes are easier than others).")
    input()
    print("You will only use the number pad to select options. The options will be numbered whenever there is a choice for the player to make.")
    input()
    print("When you see dialogue in the game, it may begin with a CAPITALIZED word.")
    input()
    print("These capitalized words represent either a character name, whether you have passed a skill check, or, most often, an aspect of the player's psyche/personality; context will make it clear.")
    input()
    print("Enjoy the game!\n\n\n\n")

# This global function just returns an int representation of the player's choice of class.
def chooseClass():
    choice = 0

    while choice < 1 or choice > 3:
        print("Which class would you like to play as?\n")
        print("1: WARRIOR ->")
        print("The Warrior is headstrong.. And chest-strong, arm-strong, leg-strong, etc. He could use a few more braincells, but that hasn't stopped him yet.")
        print("Starting Stats -> Health: 450  Strength: 19  Intelligence: 5  Stealth: 6\n")
        print("2: ASSASSIN ->")
        print("The assassin prefers to do things quietly. Has prepared for every situation, but cannot take much damage. A delicate flower.")
        print("Starting Stats -> Health: 425  Strength: 7  Intelligence: 7  Stealth: 16\n")
        print("3: JESTER ->")
        print("He won't shut up. Always the smartest person in the room. Will reveal your deepest insecurities to your face. Always talks his way out of every situation.")
        print("Starting Stats -> Health: 425  Strength: 5  Intelligence: 15  Stealth: 10\n")
        print("Please choose class 1, 2, or 3")
        choice = int(input())

    return choice


class Combatant:

    # Constructor function
    def __init__(self, name, health, strength, intelligence, stealth):
        self.name = name
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.stealth = stealth

    # This is the encounter function. This is the "game" part of the program. It is the most important part of the game. It manages each encounter by calculating attacker damage and damage blocked by the defender
    def encounter(self, nonaggressor):

        # This first block of code dictates the attacker's offensive damage and the defender's defensive blocked damage
        # This block loops while also switching between each combatant attacking the other until one of them dies
        # To clear this up: The "Attacker" is not always the user's character. The user first attacks (if they are entered first into the attacker spot of the encounter function, of course), but on the next iteration, defends.
        input()
        encounterAttackTotal = 1
        combatantList = [self, nonaggressor]
        currentAttacker = 0

        # The enemy's name and stats are displayed to the player
        if self.name == "Warrior" or self.name == "Assassin" or self.name == "Jester":
            print(f"NAME: {nonaggressor.name} --> STRENGTH: {nonaggressor.strength}, INTELLIGENCE: {nonaggressor.intelligence}, STEALTH: {nonaggressor.stealth}")
        else:
            print(f"NAME: {self.name} --> STRENGTH: {self.strength}, INTELLIGENCE: {self.intelligence}, STEALTH: {self.stealth}")

        while self.health > 0 and nonaggressor.health > 0:

            # These first few lines randomly dictate whether the attacker and defender independently get a critical hit/block and also determines attack damage variance
            damageVariance = random.randint(5, 25)
            criticalAttack = 0
            criticalBlock = 0
            # 25% chance for critical attack
            if random.randint(1, 4) == 4:
                criticalAttack = 20
            # 20% chance for critical block
            if random.randint(1, 5) == 5:
                criticalBlock = 35

            # This line calculates the "offensiveDamage" done by the attacker. The stats of the attacker and defender determine this variable.
            offensiveDamage = damageVariance + (2 * combatantList[currentAttacker].strength) + (1 * (combatantList[currentAttacker].intelligence - combatantList[abs(currentAttacker - 1)].intelligence)) + ((4 * combatantList[currentAttacker].stealth) / encounterAttackTotal) + criticalAttack

            # This line calculates the blocked damage by the defender. The stats of the attacker and defender determine this variable.
            defensiveGuard = (0.9 * offensiveDamage * random.random()) + criticalBlock

            # The actual damage done is the rounded down offensiveDamage minus the defensiveGuard
            damage = math.floor(offensiveDamage - defensiveGuard)

            # If the damage is negative, it just counts as a missed attack
            if criticalAttack != 0:
                print("CRITICAL HIT!")
            if criticalBlock != 0:
                print("CRITICAL BLOCK!")
            if damage > 0:
                combatantList[abs(currentAttacker - 1)].health -= damage
                print(
                    f"{combatantList[currentAttacker].name} HAS DEALT {damage} DAMAGE TO {combatantList[abs(currentAttacker - 1)].name}!")
                if self.health > 0:
                    print(f"{self.name} HAS {self.health} HEALTH")
                if nonaggressor.health > 0:
                    print(f"{nonaggressor.name} HAS {nonaggressor.health} HEALTH")
                # print(f"offDmg = {math.floor(offensiveDamage)} and guard = {math.floor(defensiveGuard)}")  <-- This line was used when balancing the game
                encounterAttackTotal += 1
            else:
                print(f"{combatantList[currentAttacker].name} HAS MISSED!")
                # print(f"offDmg = {math.floor(offensiveDamage)} and guard = {math.floor(defensiveGuard)}")  <-- This line was used when balancing the game
                encounterAttackTotal += 1

            # This bit will cycle the attacker and defender for the next iteration of the while loop
            if currentAttacker == 0:
                currentAttacker = 1
            else:
                currentAttacker = 0

            input()

        # Once one of the combatants has died, this block lets the player know
        if self.health <= 0 and (self.name == "Warrior" or self.name == "Assassin" or self.name == "Jester"):
            print("You have died.. It's a shame you'll never reach the summit.")
            # print(f"encounter = {encounterAttackTotal}")   <-- This line was used when balancing the game
            input()
            sys.exit()
        elif nonaggressor.health <= 0 and (nonaggressor.name == "Warrior" or nonaggressor.name == "Assassin" or nonaggressor.name == "Jester"):
            print("You have died.. It's a shame you'll never reach the summit.")
            # print(f"encounter = {encounterAttackTotal}")   <-- This line was used when balancing the game
            input()
            sys.exit()
        else:
            print(f"{combatantList[currentAttacker].name} has died. You have {combatantList[abs(currentAttacker - 1)].health} health remaining!")
            # print(f"encounter = {encounterAttackTotal}")   <-- This line was used when balancing the game

        input()


main()

