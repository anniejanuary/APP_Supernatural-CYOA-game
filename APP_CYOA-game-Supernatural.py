print('''
                                                                                                                         88  
                                                                                 ,d                                      88  
                                                                                 88                                      88  
,adPPYba, 88       88 8b,dPPYba,   ,adPPYba, 8b,dPPYba, 8b,dPPYba,  ,adPPYYba, MM88MMM 88       88 8b,dPPYba, ,adPPYYba, 88  
I8[    "" 88       88 88P'    "8a a8P_____88 88P'   "Y8 88P'   `"8a ""     `Y8   88    88       88 88P'   "Y8 ""     `Y8 88  
 `"Y8ba,  88       88 88       d8 8PP""""""" 88         88       88 ,adPPPPP88   88    88       88 88         ,adPPPPP88 88  
aa    ]8I "8a,   ,a88 88b,   ,a8" "8b,   ,aa 88         88       88 88,    ,88   88,   "8a,   ,a88 88         88,    ,88 88  
`"YbbdP"'  `"YbbdP'Y8 88`YbbdP"'   `"Ybbd8"' 88         88       88 `"8bbdP"Y8   "Y888  `"YbbdP'Y8 88         `"8bbdP"Y8 88  
                      88                                                                                                     
                      88                                                                                                    ''')



print('''
                                              ( ((
                                               ) ))
                      .::.                    / /(
                     'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
                    (J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
                     `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
                      `::'                    \ \(
                                               ) ))
                                              (_((

''')

print("Welcome to Supernatural, Dean! \nIt's the top simulator for killing monsters, hunting things, the family business! \nYour goal is to not go to hell or become a demon.")

sell_soul= input("\nYour brother Sam is dead. He will be resurrected by Death if you sell your soul to be reaped in a year. Do you sell your soul? Yes/No: \n").lower()
if sell_soul == "yes":
  print("You sold your soul and Sam is back. But after a year of trying to find a way out, the crossroads demon Crowley     sics a hellhound on you. You die and are dragged to hell. Game over. No more pie for you.")
else:
  purgatory= input("You don't sell your soul, but find a different way to bring Sam back (as always). You kill the Leviathans' leader (the new baddie) and get dragged into Purgatory. Purgatory vampires surround you. Do you fight or wait? \n").lower()
  if purgatory == "fight":
    door = input("You kill the vamps. To escape Purgatory you need to choose the right door: red, white or black: \n").lower()
    if door == "red":
      print("You keep living your life hunting monsters with your brother Sam happily ever after and having unlimited pie. You win. Sweet!")
    elif door == "white":
      print("You fight like Steven Segal in 'Under Siege' but you're outnumbered. You get killed by Purgatory vamps and are dragged to hell. Game over. Gosh darnit!")
    elif door == "black":
      print(f"You escape Purgatory but are killed by angel Metatron (there are angels now?!) with an angel blade (sure, there might as well be angel blades now) and die (shocker). Crowley, the prince of Hell, resurrects you as a demon (yay?). Oh wait, nay! Game over.")
    else:
      print("You chose a wrong door. Game over")
  else:
    print("You run away from the Purgatory vamps but are stuck in Purgatory for eternity. No pie in Purgatory. Game over!")
