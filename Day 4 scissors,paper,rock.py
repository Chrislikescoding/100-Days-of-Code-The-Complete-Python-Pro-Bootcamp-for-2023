import random
#Write the rest of your code below this line 👇
hort=random.randint(0,1)
if hort==1:
    print("Heads")
else:
    print("Tails")

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    # Write your code below this line 👇
    import random

    value = [paper, scissors, rock]
    computer_index = random.randint(0, 2)
    computer_choice = value[computer_index]
    print(computer_choice)
    my_index = random.randint(0, 2)
    my_choice = value[my_index]
    print(my_choice)

    if computer_index > my_index:
        print("computer won")
    elif my_index > computer_index:
        print("you won")
    else:
        print("draw")