good = r"""      __,,__
             _,-"      "-,_
           ,"              "-,
          /                   ",
          |                     \
          ;     ,    ,,          \
           \   ( "-,/             \
            \   \ \/  /~\   (\/)\  \
             |  ) {  / ) \     } \  ;
            /  /  | | /   |   =|  | }
           |  /   / |/     ~\  |  | \
           J \    J \,       (_o ,/ L
            "'     '"             "'
"""

bad = r"""            _     _          
                     | |   (_)         
  __ _  ___ _ __ ___ | |__  _  ___ ___ 
 / _` |/ _ \ '__/ _ \| '_ \| |/ __/ __|
| (_| |  __/ | | (_) | |_) | | (__\__ \
 \__,_|\___|_|  \___/|_.__/|_|\___|___/
"""
has_key = True
if has_key:
    outcome = ("Click: We can get in!")
    print(good)
else:
    outcome = ("Doom: We can't get in!")
    print(bad)
print(outcome)