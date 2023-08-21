print("""
   _______________                        |*\_/*|________

  |  ___________  |     .-.     .-.      ||_/-\_|______  |

  | |           | |    .****. .****.     | |           | |

  | |   0   0   | |    .*****.*****.     | |   0   0   | |

  | |     -     | |     .*********.      | |     -     | |

  | |   \___/   | |      .*******.       | |   \___/   | |

  | |___     ___| |       .*****.        | |___________| |

  |_____|\_/|_____|        .***.         |_______________|

    _|__|/ \|_|_.............*.............._|________|_

   / ********** \                          / ********** \

 /  ************  \                      /  ************  \

--------------------                    --------------------

      """)

print("""
Welcome to my island!
There are two doors in front of you, a 🆁 🅴 🅳  🅳 🅾 🅾 🆁 and a 🅱 🅻 🆄 🅴  🅳 🅾 🅾 🆁""")     

user_choise_doors = input("Which door do you want to open? enter blue or red\n").lower()
if user_choise_doors == "red":
    print("dddddd")
    
elif user_choise_doors == "blue":
    print("hhhhhhh")
    user_choise_boxes = input("Now, You have to choose between three boxes\n")
else:
    print("not a valid entry, please just write 'blue' or 'red'")
    print("Game over")        

