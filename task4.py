good = r"""      __,,__
             _,-"      "-,_
           ,"              "-,
          /                   \
          |                    \
          ;     ,    /          \
           \   ( "-,/            \
            \   \  /  /\   (\/)\  \
             |  ) {  /\ \      }\  }
            /  /  | |  \ [  = =| | |
           |  /   / |   \ ~\  /  | \
           ) \    ) \,  / ((_o) ,/ (
            "'    '~"   "'       "~`
"""

bad = r"""            _     _          
                     | |   (_)         
  __ _  ___ _ __ ___ | |__  _  ___ ___ 
 / _` |/ _ \ '__/ _ \| '_ \| |/ __/ __|
| (_| |  __/ | | (_) | |_) | | (__\__ \
 \__,_|\___|_|  \___/|_.__/|_|\___|___/
"""
drawbridge_raised = True
if not drawbridge_raised:
    outcome = ("Thunder: It's raised!")
    print(bad)
else:
    outcome = ("Doom: It's down!")
    print(good)
print(outcome)