import pytest
from src.RPS_dict import GameResult, GameAction, Game


@pytest.fixture
def game():
    '''
    Setup del objeto game
    '''
    setup_game = Game()
    return setup_game

@pytest.mark.draw
def test_draw(game):
    '''
    Partidas con empate
    '''

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Rock)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Scissors, 
        computer_action=GameAction.Scissors)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Paper)

@pytest.mark.rock
def test_rock_loses(game):
    '''
    Rock pierde con Paper 
    '''
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Rock)

@pytest.mark.rock
def test_rock_wins(game):
    '''
    Rock gana a Scissors
    '''
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Rock)

@pytest.mark.paper
def test_paper_loses(game):
    '''
    Paper pierde con Scissors
    '''
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Paper)

@pytest.mark.paper
def test_paper_wins(game):
    '''
    Paper gana a Rock
    '''
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Paper)

@pytest.mark.scissors
def test_scissors_loses(game):
    '''
    Scissors pierde con Rock 
    '''
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Scissors)

@pytest.mark.scissors
def test_scissors_wins(game):
    '''
    Scissors gana a Paper 
    '''
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Scissors)
