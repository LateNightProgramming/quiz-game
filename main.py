from time import sleep

def main():
    points = 3
    q1 = ("yes","yeah","yep")
    q2 = ("no","no, its a markup language")
    while True:
        ans = input("is python slow")
        if ans in q1:
            print("good job!")
            break
        elif ans == "elaborate":
            print("no")
        else:
            print("wrong answer")
            points-=1
    while True:
        ans = input("is PHP bad")
        if ans in q1 or ans == "php is horrible":
            print("good job")
            break
        elif ans == "elaborate":
            print("no")
        else:
            print("wrong answer")
            points-=1
    while True:
        ans = input("is HTML a programming language")
        if ans in q2:
            print("good job")
            break
        elif ans == "elaborate":
            print("no")
        else:
            print("wrong answer")
            points-=1
    print("now, the moment youve been waiting for")
    for x in range(4):
        print(".")
        sleep(0.9)
    print("your final score is...\n",points)
    if points == 3:
        print("amazing")
    elif points > 0 and points < 3:
        print("you did mid as shit fam")
    else:
        print("bro how the fuck are this dumb 0 points havin ass infact yo dad got doo doo crumbs in his beard your barber lined you up with a weed whacker yo mom uses a jump rope as belt you look like you brush your teeth with a veggie straw discord ceo lookin ass your hairlines just as fake as your parents love for you your uncle got caught giving a lap dance to a pickle you tried turning your grandma into a bitcoin mining rig your uncle built like an expired chug jug your mom lookin straight outa SpongeBob in fact she shat herself in the kitchen and said it's the dirty bubble! You look like you picking up girls at lunch with your sacred furry mating call cringe radiating food wasting piece of shit you ugly as hell boy get yo riggidy diggidy ass outa here boy you look like your pastor did questionable things to you in the back of a church chapel lookin like an off brand Ben 10 character bro yo grandma exploited herself to bling bling boy to pay off her houses mortgage your best friend is a cockroach who lives under yo bed in a pringles can you built like an among us character yo future kids lookin like thing 1 and thing 2 coz you object 3 with yo stanky ass you live in a goddamn wet Amazon box you sounding like ghghthghgnghghththth fuckin mac user lookin ass your brain a 2400rpm hard drive you tried to sell nfts of yo grandma twerking on a pickle yo dad tried sell expired milk on the dark web you look like an expired block of cheese you smell like a dead deer carcass with that shitty as cologn eBay listing lookin ass registered internet felon you have to alert yo neighbours when you move in near em you got 50 years for doing mr wood style things to yo grandma while she gave a Jamaican cricket a lap dance in front of toys r us you got a drop of dark elixir rolling down yo head with yo Emo lookin ass you bring the power of 50 titans with you when walk")

    while True:
        ans = input("do you wish to restart? ")
        if ans in q1:
            print("restarting...")
            main()
            break
        elif ans == "no":
            print("quiz over or smoething idfk")
            exit()
        else:
            print("please god you know how english works")
main()
