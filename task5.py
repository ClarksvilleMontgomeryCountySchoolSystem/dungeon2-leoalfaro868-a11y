good = r"""                _,-'^\
                       _,-'   ,\ )
                   ,,-'     ,'  d'
    ,,,           J_ \    ,'
   `\ /     __ ,-'  \ \ ,'
   / /  _,-'  '      \ \
  / |,-'             /  }
 (                 ,'  /
  '-,________         /
             \       /
              |      |
             /       |
            /        |
           /  /~\   (\/)
          {  /   \     }
          | |     |   =|
          / |      ~\  |
          J \,       (_o
           '"
"""

bad = r"""                                                                         
                                             88          88             
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
escaped = True
if escaped:
    outcome = ("Legend: We did it!")
    print(good)
else:
    outcome = ("Doom: We were so close!")
    print(bad)
print(outcome)