from dataclasses import dataclass
import random

@dataclass
class Fighter:
    name: str
    strength: int  # 1-10
    defense: int  # 1 - 5
    hp: int       # 1 - 50
    crazy_factor: float # 1 - 4
    speed: int   # 1 - 10
    description: str

def mandingo_simulator(fighter_1,fighter_2):
    rounds = 1
    print("Welcome to the fight club, introducing our contestants...")
    print("first up, we have ", fighter_1.description, "give it up for ",fighter_1.name)
    print("next up, we have ", fighter_2.description, "throw it back for ",fighter_2.name)
    body_areas = ["dick", "crotch", "vagina","face","leg","stomach","ass","nose","jaw","neck","penis","arm","testicles","nipple"]
    if fighter_1.speed < fighter_2.speed:
        starting_fighter = fighter_1
        other = fighter_2
    else:
        starting_fighter = fighter_2
        other = fighter_1
    while fighter_1.hp > 0 and fighter_2.hp > 0:
        print("starting round: ",rounds)
        starting_fighter_hit = random.randint(1,starting_fighter.strength+1) * random.randint(1,starting_fighter.crazy_factor+1)
        other_hit = random.randint(1,other.strength+1) * random.randint(1,other.crazy_factor+1)
        if starting_fighter_hit >= other.defense:
            starting_fighter_hit -= other.defense
        if other_hit >= starting_fighter.defense:
            other_hit -= starting_fighter.defense
        body_part = random.randint(1,13)
        print(starting_fighter.name, " deals ",starting_fighter_hit, " to ",other.name,"'s ",body_areas[body_part])
        other.hp  -= starting_fighter_hit

        if other.hp <=0:
            print(other.name," has been knocked the fuck out. " ,starting_fighter.name," has won the fight!")
            return
        starting_fighter.hp -= other_hit
        body_part = random.randint(1,13)
        print(other.name, " deals ",other_hit, " to ",starting_fighter.name,"'s ",body_areas[body_part])
        if starting_fighter.hp <=0:
            print(starting_fighter.name," has been knocked the fuck out. ", other.name," has won the fight!")
            return
        rounds +=1



George_description =  " A small, yet wild man whose intense anger outshines his small stature. On a given day you may find him bragging about how much he loves his job or going on about how kids lack discipline."
Yousef_description =  " A lengthy stick of a boy whose love of anime drives his strange sexual desires. On a given day you may find him attempting to assimilate into the Buffalo black community and somehow suceeding."
Tony_description = " A average sized boy of thick nature whose stomach likely blocks the view of his toes. Regardless, his ego smoothes over his insecurities, of which has has many."
Michael_description = " A boy with a kind heart to put it euphamistically. What he lacks in brains he makes up for in spirit, if that's what you want to call it."
Anthony_description = " A simple boy whose temper was outgrown with age. What he lacks in size he makes up for in a quick tongue"
Lulu_description =  " An interesting girl to say the least. Her love of Tony is likely the only thing keeping her at the Rochester church as the masses of female youth continue to distance themselves"
Louis_description = " A large and imposing FOB whose huge heart hides beneath his giant tits. He is certainly the likeliest to win these sorts of competitions as his brawn took up the mantle where brains left off"
Mena_description = " An insane man. There isnt much else to say"
Gibs_description = " I mean hes a faggot what can i say. The lack of a hand will make this a difficult endevour but his temper when being attacked is something to take very seriously."
Paul_description = " A proud boy who's ego outshines his lack of common sense. He may look strong on the outside, but he's a shell of a human deep down. he spends his days writing fictional complaints online to appease his desire for attention"
Josh_description = " A man who we really have nothing  bad to say about, "

def main():
    George = Fighter("George",6,2,40,3,6,George_description)
    Yousef = Fighter("Yousef",3,1,30,1,5,Yousef_description)
    Tony = Fighter("Tony",4,3,40,3,4,Tony_description)
    Michael = Fighter("Micheal",3,1,25,2,7,Michael_description)
    Anthony = Fighter("Anthony",5,2,30,1,8, Anthony_description)
    Lulu = Fighter("Lulu", 1, 1, 20, 2, 1, Lulu_description)
    Louis = Fighter("louis",10,4,45,3,3,Louis_description)
    Mena = Fighter("Mena",6,2,40,4,5,Mena_description)
    Paul = Fighter("Paul",8,3,37,2,7,Paul_description)
    Gibs = Fighter("Gibs",6,3,40,2,9,Gibs_description)
    Josh = Fighter("Josh",5,3,34,2,6,Josh_description)


    mandingo_simulator(Yousef,Anthony)

if __name__ == '__main__':
    main()
