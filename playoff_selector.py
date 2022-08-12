import random
import time

playoff = []

name = input("What is your name? ")
time.sleep(1)
types = {1:"Lawful Good", 2:"Neutral Good", 3:"Chaotic Good", 4:"Lawful Neutral",
        5:"Chaotic Neutral", 6:"Lawful Evil", 7:"Neutral Evil", 8:"Chaotic Evil"}
neutrals = {1:"Army", 2:"Cal", 3:"Cincinnati", 4:"Florida State",
            5:"Kansas State", 6:"Miami", 7:"Nebraska", 8:"Ohio State",
            9:"Pitt", 10:"Texas", 11:"UAB", 12:"Utah", 13:"Wisconsin",
            14:"Central Michigan", 15:"Fresno State", 16:"Penn State",
            17: "Washington", 18:"Vanderbilt", 19:"Louisiana-Monroe", 20:"Wyoming"}


choice = input("""
        Hello worthy traveler {name}! College football needs you to pick its playoff teams! Please select which type of team you would like to choose! Please use either the number or the name!
        {types}
        
        You may not pick a type more than once. Good Luck! 
        """.format(name=name, types=types))
time.sleep(1)

def college_team(choice):
    choice = choice.strip()
    length = len(types)
    global playoff
    types_c = types.copy()
    roll = random.randint(1,20)
    print("You have rolled a " + str(roll) + "!")
    if roll == 1:
        print("Ouch!")
    elif roll == 20:
        print("Wow!")
    time.sleep(1)
    for k, v in types_c.items():
        if choice == str(k) or choice.lower() == v.lower():
            if choice == "1" or choice.lower() == "lawful good":
                if roll == 1:
                    playoff.append("Illnois")
                    del types[1]
                elif 2 <= roll <= 7:
                    playoff.append("Navy")
                    del types[1]
                elif 8 <= roll <= 13:
                    playoff.append("Oklahoma State")
                    del types[1]
                elif 14 <= roll <= 19:
                    playoff.append("Iowa")
                    del types[1]
                elif roll == 20:
                    playoff.append("Georgia")
                    del types[1]
            elif choice == "2" or choice.lower() == "neutral good":
                if roll == 1:
                    playoff.append("Bowling Green")
                    del types[2]
                elif 2 <= roll <= 7:
                    playoff.append("Boston College")
                    del types[2]
                elif 8 <= roll <= 13:
                    playoff.append("Air Force")
                    del types[2]
                elif 14 <= roll <= 19:
                    playoff.append("Notre Dame")
                    del types[2]
                elif roll == 20:
                    playoff.append("Michigan")
                    del types[2]
            elif choice == "3" or choice.lower() == "chaotic good":
                if roll == 1:
                    playoff.append("South Florida")
                    del types[3]
                elif 2 <= roll <= 7:
                    playoff.append("Hawaii")
                    del types[3]
                elif 8 <= roll <= 13:
                    playoff.append("East Carolina")
                    del types[3]
                elif 14 <= roll <= 19:
                    playoff.append("UTSA")
                    del types[3]
                elif roll == 20:
                    playoff.append("Baylor")
                    del types[3]
            elif choice == "4" or choice.lower() == "lawful neutral":
                if roll == 1:
                    playoff.append("Auburn")
                    del types[4]
                elif 2 <= roll <= 7:
                    playoff.append("Indiana")
                    del types[4]
                elif 8 <= roll <= 13:
                    playoff.append("NC State")
                    del types[4]
                elif 14 <= roll <= 19:
                    playoff.append("Texas A&M")
                    del types[4]
                elif roll == 20:
                    playoff.append("Alabama")
                    del types[4]
            elif choice == "5" or choice.lower() == "chaotic neutral":
                if roll == 1:
                    playoff.append("Arkansas State")
                    del types[5]
                elif 2 <= roll <= 7:
                    playoff.append("Virginia")
                    del types[5]
                elif 8 <= roll <= 13:
                    playoff.append("UCLA")
                    del types[5]
                elif 14 <= roll <= 19:
                    playoff.append("Utah State")
                    del types[5]
                elif roll == 20:
                    playoff.append("Oklahoma")
                    del types[5]
            elif choice == "6" or choice.lower() == "lawful evil":
                if roll == 1:
                    playoff.append("New Mexico")
                    del types[6]
                elif 2 <= roll <= 7:
                    playoff.append("Arizona State")
                    del types[6]
                elif 8 <= roll <= 13:
                    playoff.append("UCF")
                    del types[6]
                elif 14 <= roll <= 19:
                    playoff.append("Mississippi State")
                    del types[6]
                elif roll == 20:
                    playoff.append("San Diego State")
                    del types[6]
            elif choice == "7" or choice.lower() == "neutral evil":
                if roll == 1:
                    playoff.append("FIU")
                    del types[7]
                elif 2 <= roll <= 7:
                    playoff.append("Florida")
                    del types[7]
                elif 8 <= roll <= 13:
                    playoff.append("Maryland")
                    del types[7]
                elif 14 <= roll <= 19:
                    playoff.append("Tennessee")
                    del types[7]
                elif roll == 20:
                    playoff.append("Oregon")
                    del types[7]
            elif choice == "8" or choice.lower() == "chaotic evil":
                if roll == 1:
                    playoff.append("Duke")
                    del types[8]
                elif 2 <= roll <= 7:
                    playoff.append("Tulane")
                    del types[8]
                elif 8 <= roll <= 13:
                    playoff.append("Kent State")
                    del types[8]
                elif 14 <= roll <= 19:
                    playoff.append("Liberty")
                    del types[8]
                elif roll == 20:
                    playoff.append("Oregon State")
                    del types[8]
    if length == len(types):
            second_try = input("""
            Please make an available choice. Your choices are:
            {types}
            I would suggest choosing by number.
            """.format(types=types))
            time.sleep(1)
            college_team(second_try)

def true_neutral():
    roll = random.randint(1,20)
    print("You have rolled a " + str(roll) + "!")
    if roll == 1:
        print("Ouch!")
    elif roll == 20:
        print("Wow!")
    time.sleep(1)
    playoff.append(neutrals[roll])
college_team(choice)
print("Your first team is " + playoff[0] + "!")
time.sleep(1)
choice_2 = input("""
                What is your next choice? You have the following options available: 
                {types}. 
                Remember only use the number or name! 
                """.format(types=types)) 
college_team(choice_2)
print("Your second team is " + playoff[1] + "!")
time.sleep(1)
choice_3 = input("""
                What is your final choice? You have the following options available: 
                {types}. 
                Remember only use the number or name! 
                """.format(types=types)) 
college_team(choice_3)
print("Your third team is " + playoff[2] + "!")
time.sleep(1)

print(f"Congratulations, {name}! So far you have gotten {playoff[0]}, {playoff[1]}, and {playoff[2]} in your playoff! This last school will not be made by you, but shall be a truly Neutral School! Good Luck!")
true_neutral()
time.sleep(3)
print(f"The final school is {playoff[3]}. Your playoff is complete. The schools are {playoff[0]}, {playoff[1]}, {playoff[2]}, and {playoff[3]}! {name}, may your teams be blessed with good fortune! Good Luck!")

