from sys import exit
import random
import time
from textwrap import dedent


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene() 
        last_scene = self.scene_map.next_scene('rescue') # define the last scene
        
        while current_scene != last_scene:
        	current_scene = self.scene_map.next_scene(current_scene.enter())
            #print("\nin engine-play-while, current_scene =", current_scene)
        
        # don't forget the enter() to start the running/reading
        current_scene.enter()


class Death():
	
	def enter(self):
		last_quote = [
			"You suck at surviving! You are done for!",
			"Sorry, it's not your lucky day today. But it is your last...",
			"What a stupid decision! You just died.",
			"GAME OVER!!!!"
			]

		print(last_quote[random.randint(0,3)])
		#return 'beach' # change it back to exit once the big part of the program is done
		exit(1)


class Variables():
	## Here store the variables, which are generated for the game 
	## and call into different classes 
	others = random.randint(2, 50)
	time = time.strftime("%H:%M")
	disappeared = random.randint(1, 6)
	## create a dictionary of tools, that will be randomly picked
	tools = {
			0: 'a pen',
			1: 'your phone',
			2: 'a lighter',
			3: 'a box of matches',
			4: 'knife'		
			}
	tool_choice = random.randint(0,4) # gives a number between 0 and 4
	tool = tools[tool_choice]

class Arrival():
	# First part of the game, introducing the context and arrival to the beach
	
	def enter(self):

		print("\n\t********* RESCUE ISLAND *********")
		
		others = Variables.others
		
		print(dedent(f"""
			It is a terrible night. A storm is raging on the Pacific ocean.
			It should have been only a relaxed cruise. 
			You are thinking that it looks like a nightmare...
		
			Actually it is only the beginning. 
			The boat flips over after trying to break a giant wave. 
			You are suddenly under water, kicked out of the boat. 
			Luckily for you, being ejected from the now wrecked boat is what 
			makes you survive the capsizing, you and {others} people.
			"""))
		input("press Enter to continue or CTRL-C to escape >")

		return 'beach'


class Tools():

	def enter(self):
		 
		## call back the variables tool_choice and tool foorm the Variables
		## and get different messages depending on what tool you get 

		tool_choice = Variables.tool_choice
		tool = Variables.tool

		print("You are checking your pockets to see what you have with you...")

		if tool_choice in range(0, 2):
			print(dedent(f"""
				You got {tool}. Not really handy on a desert island, 
				if you know what I mean.
				"""))


		elif tool_choice in range(2, 4):
			print(dedent(f"""
				You have {tool}, that will be useful to start a fire.
				Well...once it's dry obviously.
				"""))

		else: 
			print(dedent(f"""
				A {tool}! You are happy to not have lost it 
				when you were ejected from the boat. 
				"""))

		input("Press Enter to continue")
		
	
class Beach():

	def enter(self):
				
		time = Variables.time
		
		print("---" * 10)	
		print(dedent(f""" 
			After what seems ages, you arrive exhausted on a beach...
			It's now {time} and you try to get a good view where you are.
			Shall we have a better look..."""))
		choice = input("y/n? >")
		if choice == 'y':
			print(dedent("""
				Well, you are on a beach at the border of a forest.
				A forest on the side of a volcano... 
				It seems that you are on an island. 			
				"""))
			input("Press Enter to continue")

		print("---" * 10)
		Tools.enter(self)
		print("---" * 10)
		print(dedent("""
			After that more or less fruitful harvest of things, 
			you discuss with the other(s) what to do first.
			The group mentions starting a fire, 
			or looking for water...
			What do you think? What should you do first?"""))
		option = input("> ")
		
		if set(option).intersection(set('fire')) == {'f', 'i', 'r', 'e'}:
			print(dedent("""
				A fire!!! What a brilliant idea. 
				The group decided that you need wood to start a fire, 
				so you go to the forest. You hope to find water also 
				on the way, all this salty water made you thirsty.
				"""))
			input("Press Enter to continue")
			return 'forest'
	
		elif set(option).intersection(set('water')) == {'w', 'a', 't', 'e', 'r'}:
			print(dedent("""
				Of course you will need water to survive. 
				You agreed on trying to get water first and 
				collect wood to make a fire.
				Let's go to the forest.
				"""))
			input("Press Enter to continue")
			return 'forest'
	
		else:
			print(dedent("""
				Actually that's not helping your situation. 
				You and the others are not really fitted for survival.
				"""))
			return 'death'



class Forest():

	def enter(self):
		others = Variables.others
		print("---" * 10)
		print(dedent("""
			You and the other(s) are entering the forest. 
			But you start to wonder if you should split the group 
			to spread the search. 
			"""))
		split = input("Shall we split the group? y/n > ")

		if split == 'y':
			group = round((others + 1) /2)
			second_group = others + 1 - group
			#print('group = ', group, '2nd group = ', second_group)
			print(dedent(f"""
				You all agree that the first group of {group} people, 
				you included, should go up North. 
				While the other {second_group} go South. 
				You decide to meet at the same place within 2 hours, 
				if not possible at the beach later.
				"""))
		else:
			print(dedent(f"""
				Maybe it was not a good idea. Moving in such a group, 
				{others + 1} people, takes definitely longer. But you were 
				scared to lose each others.
				"""))
			time.sleep(3)

		print("You are hearing something... probably a water fall.")
		water = input("Do you go check? y/n > ")

		if water == 'y' or water == 'yes':
			print(dedent(""" 
				Water!!! You are so thirsty that you jump in the water, 
				and drink as much as you can. Now refreshed, you collect 
				wood. There is plenty here. You will be able to start 
				a big fire. Let's go back.
				"""))
			input("Press Enter to continue")

			return 'disappearence'

		else: 
			print(dedent("""
				You are walking around. Never finding anything. 
				Never finding your way back.
				"""))
			return 'death'


class Disappearence():

	def enter(self):
		others = Variables.others
				
		disappeared = Variables.disappeared
		
		print("---" * 10)
		print("In this already terrifying situation, ")
		if others >= disappeared:
			others = others - disappeared
			if disappeared == 1:
				print(f"you realize that {disappeared} person disappeared")
			else:
				print(f"you realize that {disappeared} people disappeared")
			print("How that can be? Is there a monster gobbing people?")
	
		elif others == disappeared:
			print("The others disappeared. You are left alone. You need to survive this.")
	
		else:
			if others == 1:
				print("you can still count on this one person")
				the_other = input("What is her name actually? >" )
				print(f"At least you can count on {the_other}.")
			else:
				print(f"you still have {others} people with you. The more the merrier.")
	
		decision = input("What should we do? Go back to the forest or go to the beach? > ")
	
		if decision == 'beach':
			return 'fire'
		
		else:
			print("What a bad idea! You just have been caught by the monster.")
			return 'death'
		

class Fire():

	def enter(self):
		
		tool = Variables.tool

		print("---" * 10)
		print(dedent(f"""
			You arrive on the beach and gather the wood to start the fire.
			Now you just need...
			"""))
		if tool == 'a lighter' or tool == 'a box of matches':
			print(f"You had {tool} in your pockets, right?")
			correct = input("y/n > ")
			if correct == 'y' or correct == 'yes':
				print("That's awesome. Let's start the fire.")
				return 'boat'
			else:
				print(dedent(f"""
					What a little brain you have?
					You're checking your pockets and find {tool}.
					it's even dry by now.
					Let's start the fire.
					"""))
		else:
			print(dedent(f"""
				Too bad, you have only {tool} with you. 
				Let's see if you can find a solution to light up 
				a good fire."""))
			solution = input("What do you do? > ")
			print("We will see if that works out.")
			input("Press Enter to continue")
			return 'boat'


class Boat():

	def enter(self):

		print("---" * 10)
		print(dedent("""
			You see a boat in the horizon. 
			You yell and wave at the boat like they could actually see you.
			"""))
		fire = input("Did you finally start a fire? y/n > ")

		if fire == 'y':
			print("The fire is bright enough. The rescue boat is coming for you.")
			return 'rescue'
		else:
			print("Too bad. The rescue boat does not see you...")
			return 'death'


class Rescue():

	def enter(self):
		print(dedent("""
			After so much stress you are finally in the rescue boat.
			You are safe now. Everything will be okay. Good job!
			"""))
		return 'rescue'
		

class Map(object):

    scenes = {
        'arrival': Arrival(),
        'beach': Beach(),
		'forest': Forest(),
		'fire': Fire(),
		'disappearence': Disappearence(),
		'boat': Boat(),
        'rescue': Rescue(),
        'death': Death()
    }
    #print(list(scenes))

    def __init__(self, start_scene):
        self.start_scene = start_scene
        #print("in map at init, start_scene=", start_scene)

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        #print("val=", val)
        return val
    
    #print("in map, next_scene", next_scene)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        #print("in map, opening_scene", self.next_scene(self.start_scene)


a_map = Map('arrival')
a_game = Engine(a_map)
a_game.play()