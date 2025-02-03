import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4



class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Paper: [GameAction.Rock, GameAction.Spock],
    GameAction.Scissors: [GameAction.Paper, GameAction.Lizard],
    GameAction.Lizard: [GameAction.Spock, GameAction.Paper],
    GameAction.Spock: [GameAction.Scissors, GameAction.Rock]
}
class Game:
    def assess_game(self, user_action, computer_action):

        game_result = None

        if user_action == computer_action:
            print(f"User and computer picked {user_action.name}. Draw game!")
            game_result = GameResult.Tie

        elif computer_action in Victories[user_action]:
            print(f"User picked {user_action.name} and computer picked {computer_action.name}. You Win!")
            game_result = GameResult.Victory

        else:
            print(f"User picked {user_action.name} and computer picked {computer_action.name}. You Defeat!")
            game_result = GameResult.Defeat

        return game_result


    def get_computer_action(self):
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")

        return computer_action


    def get_user_action(self):
        # Scalable to more options (beyond rock, paper and scissors...)
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
        user_action = GameAction(user_selection)

        return user_action


def play_another_round():
        
        valid_options = ['y', 'n']
        another_round = input("\nAnother round? (y/n): ")
        while another_round not in valid_options:
            print(f'\n{another_round} is not a valid option. Please enter y or n.')
            another_round = input("\nAnother round? (y/n): ")
            if another_round == 'y':
                return True
            elif another_round == 'n':
                return False




def main():

    continue_playing = True
    while continue_playing:
        try:
            user_action = Game().get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = Game().get_computer_action()
        Game().assess_game(user_action, computer_action)

        continue_playing = play_another_round()


if __name__ == "__main__":    
    main()
