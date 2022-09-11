import random 
response="y"
while response == "y":

    no = random.randint(1,6)
    
    if no == 1:
        print("[-----]")
        print("[-----]")
        print("[  0  ]")
        print("[-----]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[-----]")
        print("[  0  ]")
        print("[  0  ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]") 
    if no == 5:
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")  
    if no == 6:
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")               
        print("[  0  ]") 

    response = input(" press y to roll again or n to quity ")    