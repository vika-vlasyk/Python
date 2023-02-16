import random


ACTIONS = {0: "Rock", 1: "Paper", 2: "Scissors"}
VICTORIES = {
    "Rock": "Scissors",  # Rock beats scissors
    "Paper": "Rock",  # Paper beats rock
    "Scissors": "Paper",  # Scissors beats paper
}


def get_user_selection(actions):
    """Функція вибору користувача"""
    choices = [f"{actions[action]}[{action}]" for action in actions]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = actions[selection]
    return action


def get_computer_selection(actions):
    """Функція рандомного вибору комп'ютера"""
    selection = random.randint(0, len(actions) - 1)
    action = actions[selection]
    return action


def get_determine_winner(victories, user_action, computer_action):
    """Функція перевіряє комбінації та поакртає перемогуабо програш або нічию"""
    defeats = victories[user_action]
    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a tie!"  #Якщо вибір користувача співпадає з вибором комп'ютера повертається результат нічия
    elif computer_action in defeats:
        result = f"{user_action} beats {computer_action}! You win!"  #Якщо комбінація є парою ключь значення VICTORIES словника перемога користувача
    else:
        result = f"{computer_action} beats {user_action}! You lose."  #Інакше програш
    return result


if __name__ == "__main__":
    while True:  #Цикл для ого щоб гра продовжувалась
        try:
            user_selection = get_user_selection(ACTIONS)  #Вибір користувача з словника
            print(user_selection)    #Вивід вибору користувача
            computer_selection = get_computer_selection(ACTIONS)  #Вибір комп'ютера із словника
            print(computer_selection)  #Вивід вибору комп'ютера
            determine_winner = get_determine_winner(
                VICTORIES, user_selection, computer_selection  #Перевірка комбінацій визначення результату
            )
            print(determine_winner)
        except:
            range_str = f"[0, {len(ACTIONS) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        play_again = input("Play again? (y/n): ")  #запит чи потрібно продовжуівати гру
        if play_again.lower() != "y":  #якщо відповідь не "y" то гра завершується
            break
