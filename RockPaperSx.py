import random
def play():
    user=input("Please chosse: 'r'for rock,'p' for paper or 's' for scissors:\n").lower()
    computer=random.choice(['r','p','s'])

    if user==computer:
        return 'its a tie'

    if is_win(user,computer):
        return 'you won!'

    return 'you lost!'

def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') \
        or (player=='s' and opponent=='p'):

        return True



print(play())