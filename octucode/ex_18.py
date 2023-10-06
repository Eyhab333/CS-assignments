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
There are two doors in front of you, a 🆁 🅴 🅳  🅳 🅾 🅾 🆁 and a 🅱 🅻 🆄 🅴  🅳 🅾 🅾 🆁

""")     

user_choise_doors = input("Which door do you want to open? enter blue or red\n").lower()
if user_choise_doors == "red":
    print("bad")
    print('Game over')
elif user_choise_doors == "blue":
    print("nice")
    user_choise_boxes = input("Now, You have to choose between three boxes! first - second -third\n").lower()
    if user_choise_boxes == 'first':
        print("first nice")
    elif user_choise_boxes == 'second':
        print("second bad")
        print('Game over')
    elif user_choise_boxes == 'third':
        print('third very bad')
        print('Game over')
    else:
        print('invalid entry')            

else:
    print("not a valid entry, please just write 'blue' or 'red'")
    print("Game over")        

