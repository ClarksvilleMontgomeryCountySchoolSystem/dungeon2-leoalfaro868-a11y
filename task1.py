good = r"""
                           _,-'^\
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

bad = r"""                    _,-"^\
                          _,-"   ,\ )
                 __,,__,-"     ,'  d'
             _,-"      "-,_  ,'
           ,"              "<,
          /                   \
          |                    \
          ;     ,     ,         \
           \   ( "--,/           \
            \   \   /  /\   (\/)\ \
             |  )  {  /  \     } \ \
            /  /   | |    |   =|  | }
           |  /    / |     ~\  |  | \
           J \     J \,      (_o ,/ L
            "'      '"             "'
"""

torch_lit = True
if torch_lit:
    outcome = ("Flicker: It's Bright!")
    print(good)
else:
    outcome = ("Doom: It's dark!")
    print(bad)
print(outcome)