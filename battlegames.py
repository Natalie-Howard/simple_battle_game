wizard = "Wizard" 
elf = "Elf" 
human = "Human" 
dwarf = "Dwarf" 

wizard_hp = 70
elf_hp = 100
human_hp = 150
dwarf_hp = 125

wizard_damage = 150 
elf_damage = 100
human_damage = 20
dwarf_damage = 50

dragon_hp = 300
dragon_damage = 50

while True:
    option = input("\n1) Wizard \n2) Elf \n3) Human \n4) Dwarf\n5) Exit Game\n\nChoose your character by picking a number and defeat the Dragon!: ").lower()
    print(" ") 

    if option == "1":
        print("You're a Wizard, Harry!\n")
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage

        break

    elif option == "2":
        print("You have chosen the Elf!\n")
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage

        break

    elif option == "3":
        print("You have chosen the Human!\n")
        character = human
        my_hp = human_hp    
        my_damage = human_damage

        break

    elif option == "4":
        print("You have chosen the Dwarf!\n")
        character = dwarf
        my_hp = dwarf_hp
        my_damage = dwarf_damage

        break

        
    elif option == "5":
        print ("Goodbye")
        exit()
    
    else:
        print("Unknown character, choose again!")
        continue


    print("\ncharacter:" , character, "HP:" , my_hp, "Damage:" , my_damage)
    

while True:
    dragon_hp = dragon_hp - my_damage

    print("\nthe" , character , "damaged the Dragon!","The Dragon's HP is now:", dragon_hp)
    if dragon_hp <=0: #hp less than 0 defeats the dragon
        print("\nThe Dragon has been defeated!")
        break
        #the dragon attacks
    my_hp = my_hp - dragon_damage

    print("The dragon strikes back at the" , character, "HP is now:", my_hp)
    if my_hp <=0: #hp less than 0 the dragon defeats the character
        print("\nThe", character, "has been defeated by the Dragon!")
        break

    #python battlegames.py 