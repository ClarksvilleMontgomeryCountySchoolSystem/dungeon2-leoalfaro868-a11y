good = r"""                    888     d8b                 
                               888     Y8P                 
                               888                         
 8888b.  .d88b. 888d888 .d88b. 88888b. 888 .d8888b.d8888b  
    "88bd8P  Y8b888P"  d88""88b888 "88b888d88P"   88K      
.d88888888888888888    888  888888  888888888     "Y8888b. 
888  888Y8b.    888    Y88..88P888 d88P888Y88b.        X88 
"Y888888 "Y8888 888     "Y88P" 88888P" 888 "Y8888P 88888P'
"""
bad = r"""                                   88          88             
                                             88          ""             
                                             88                         
,adPPYYba,  ,adPPYba, 8b,dPPYba,  ,adPPYba,  88,dPPYba,  88  ,adPPYba,  
""     `Y8 a8P_____88 88P'   "Y8 a8"     "8a 88P'    "8a 88 a8"     ""  
,adPPPPP88 8PP""""""" 88         8b       d8 88       d8 88 8b          
88,    ,88 "8b,   ,aa 88         "8a,   ,a8" 88b,   ,a8" 88 "8a,   ,aa  
`"8bbdP"Y8  `"Ybbd8"' 88          `"YbbdP"'  8Y"Ybbd8"'  88  `"Ybbd8"'  
                                                                        
                                                                        
           
           
           
           
,adPPYba,  
I8[    ""  
 `"Y8ba,   
aa    ]8I  
`"YbbdP"'  
"""
guard_awake = True
if not guard_awake:
    outcome = ("Shadow: He's here!")
    print(bad)
else:
    outcome = ("Doom:We're all good!")
    print(good)
print(outcome)