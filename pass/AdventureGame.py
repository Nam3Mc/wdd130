# i tried to add thw while code but I figured it out later 
# idid ot have enogh time to finished the hole game i think i complicted all, maybe i jus needed to do it simple!

# class
sword = 'SWORDMAN'
bow = 'ARCHER'
staff = 'WIZARD'

# map
map1= 'RAGMA'
map2 = 'DAGOR'
map3 = 'BROD'

# actions 
fight = 'RECLUTE'
piece = 'TALK'

# gifs 
gift1 = 'GOLD'
gift2 = 'SILVER'
gift3 = 'COPPER'

# main
name = str.capitalize ( input ( 'Hello my friedn, What is your name ? \n ' ) )
print ( f'Hi {name }. ' )
class_ = input ( f'Select your class:\n > SWORDMAN\n > {bow}\n > {staff}\n\n > ' )
while not class_  == sword or staff or bow: 
    print ( 'This is not a right choose! ' )
    class_ = input ( f'Select your class:\n > {sword}\n > {bow}\n > {staff}\n\n > ' )
print ( 'Awesome, please select a map: ' )
if class_ == 'swordman': 
    map_ = str.lower ( input ( f'> {map1}\n > {map2}\n > {map3}\n\n > ') )
    if map_ == 'ragma':
        print ( 'You`ve received a mission! ' )
        print ( 'This town is under attack, the Ogre`s King wants to take control over the tonw ' )
        action = input ( f'How could you help this people to find piece:\n > {fight}\n > {piece}\n\n > ' )
        if action == 'reclute':
            print ('Ogre[s army is really powerfull, nevertheless, there are mani valints soldier in this town ' )
            print ( f'there are many cytizens, willing to fight in behalf of they freedon! ' )
            print ( )
            clss1 = int ( input ( f'How mani {sword}S would you like to Reclute: \n ' ) )
            print ( )
            clss2 = int ( input ( f'How mani {bow}S would you like to Reclute: \n ' ) )
            print ( )
            clss3 = int ( input ( f'How mani {staff}S would you like to Reclute: \n ' ) )
            if clss1 >= 100 and clss2 >= 70 or clss3 >= 70:
                print ( ( 'after an amazin battler, your army defeated the Ogre`s army. ' ) )
                print ( f' {( clss1 + clss2 + clss3 ) / 1.5 } wreaminen of your army. ')
                print ( 'You were declared as a new king in this amazing kingdown! ' )
                print ( 'Congratulation the victory is yours !')
            elif clss1 >= 50 and ( clss2 >= 100 or clss3 >= 70 ):
                print ( ( 'after an amazin battler, your army defeated the Ogre`s army. ' ) )
                print ( f' {( clss1 + clss2 + clss3 ) / 1.5 } wreaminen of your army. ')
                print ( 'You were declared as a new king in this amazing kingdown! ' )
                print ( 'Congratulation the victory is yours !')                
            else:
                print ( f'After  a big battler just, { ( clss2 + clss1 + clss3 ) / 10 } of your army remain. ' )
                print ( 'The Ogre`s King took possesion of the town and all the cityzens were living under his domine. ' )
                print ( f'All { map_ } is waiting for a hero since that grat battler. ' )
        elif action.lower() == 'talk':
            print ( 'Well, if you want to talk with the Ogre`s King, w can no just visit him with empty hands! ' )
            print ( )
            print ( 'In this land there are mani ore, we can convince the Ogre`s King to leave the town if we offer him enough ore! ' )
            print ( )
            ore = int ( input ( f'We have { gift1 }.\nHow mani kilos could we offer him?\n :' ) )
            print ( )
            ore2 = int ( input ( f'We have { gift2 }.\nHow mani kilos could we offer him?\n :' ) )
            print ( )
            ore3 = int ( input ( f'We have { gift3 }.\nHow mani kilos could we offer him?\n :' ) )
            if ore >= 500 and ( ore2 >= 800 or ore3 >= 1200 ):
                print ( 'We visited the Ogre`s King, wasn`t easy get to his trone! but we did it! ' )
                print ( f'The King was incredible suprised when he saw { ore } kilos of { gift1 }!')
                print ( )
                print ( ( f'He also loved all the {gift2} and {gift3}! ' ) )
                print ( f'the Ogre`s King and al his army left the town after our visit.\nNow {map_} enjoy piece. ' )
                print ( f'Thank you so much { name }, you`re our savior! \nEND'  )
            elif ore3 >= 1500 and ( ore >= 300 or ore2 >= 700 ):
                print ( 'We visited the Ogre`s King, wasn`t easy get to his trone! but we did it! ' )
                print ( f'The King was incredible suprised when he saw { ore } kilos of { gift1 }!')
                print ( )
                print ( ( f'He also loved all the {gift2} and {gift3}! ' ) )
                print ( f'the Ogre`s King and al his army left the town after our visit.\nNow {map_} enjoy piece. ' )
                print ( f'Thank you so much { name }, you`re our savior! \nEND'  )
            else:
                print ( '  ' )
    else:
        print ( 'no')
elif class_ == 'archer':
    print ( 'bow')
elif class_ == 'wizard':
    print ( 'staf')
else:
    print ( ' si ')
