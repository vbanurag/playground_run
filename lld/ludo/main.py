# Core Classes
from abc import ABC, abstractmethod
import random
from typing import List, Dict, Optional, Tuple
import enum

# Singleton implementation for GameBoard
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Enum for Colors
class Color(enum.Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"

# Enum for SquareType
class SquareType(enum.Enum):
    NORMAL = "normal"
    HOME = "home"
    START = "start"
    SAFE = "safe"

# Observer Pattern
class GameObserver(ABC):
    @abstractmethod
    def update(self, game_state: Dict) -> None:
        pass

class ConsoleDisplayObserver(GameObserver):
    def update(self, game_state: Dict) -> None:
        print(f"Game state: {game_state}")

class GameStateObserver(GameObserver):
    def update(self, game_state: Dict) -> None:
        # Update internal state tracking
        pass

# State Pattern for Token
class TokenState(ABC):
    @abstractmethod
    def move(self, token, steps: int) -> bool:
        pass
    
    @abstractmethod
    def can_move(self, token, steps: int) -> bool:
        pass

class HomeState(TokenState):
    def move(self, token, steps: int) -> bool:
        if steps == 6:
            token.set_state(StartState())
            token.position = token.start_position
            return True
        return False
    
    def can_move(self, token, steps: int) -> bool:
        return steps == 6

class StartState(TokenState):
    def move(self, token, steps: int) -> bool:
        token.set_state(RunningState())
        token.position = (token.position + steps) % 52
        return True
    
    def can_move(self, token, steps: int) -> bool:
        return True

class RunningState(TokenState):
    def move(self, token, steps: int) -> bool:
        new_position = token.position + steps
        if new_position > 51:
            remainder = new_position - 52
            if remainder < 6:  # Can enter home zone
                token.set_state(SafeState())
                token.position = 100 + remainder  # Home zone positions start at 100
            else:
                return False
        else:
            token.position = new_position
        return True
    
    def can_move(self, token, steps: int) -> bool:
        new_position = token.position + steps
        if new_position > 51:
            remainder = new_position - 52
            return remainder < 6  # Can only enter home zone if not overshooting
        return True

class SafeState(TokenState):
    def move(self, token, steps: int) -> bool:
        new_position = token.position + steps
        if new_position == 106:  # Final home position
            token.set_state(HomeState())
            token.position = -1  # Completed
            return True
        elif new_position < 106:
            token.position = new_position
            return True
        return False
    
    def can_move(self, token, steps: int) -> bool:
        new_position = token.position + steps
        return new_position <= 106

# Command Pattern
class Command(ABC):
    @abstractmethod
    def execute(self) -> bool:
        pass

class RollCommand(Command):
    def __init__(self, dice):
        self.dice = dice
    
    def execute(self) -> int:
        return self.dice.roll()

class MoveCommand(Command):
    def __init__(self, token, steps: int):
        self.token = token
        self.steps = steps
    
    def execute(self) -> bool:
        return self.token.move(self.steps)

class KillCommand(Command):
    def __init__(self, token, target_token):
        self.token = token
        self.target_token = target_token
    
    def execute(self) -> bool:
        self.target_token.reset()
        return True

# Strategy Pattern
class PlayerStrategy(ABC):
    @abstractmethod
    def choose_token(self, player, roll: int) -> Optional['Token']:
        pass

class HumanStrategy(PlayerStrategy):
    def choose_token(self, player, roll: int) -> Optional['Token']:
        movable_tokens = [token for token in player.tokens if token.can_move(roll)]
        if not movable_tokens:
            return None
        
        # In a real implementation, this would get input from the user
        # For this example, we'll just pick the first valid token
        return movable_tokens[0] if movable_tokens else None

class ComputerStrategy(PlayerStrategy):
    def choose_token(self, player, roll: int) -> Optional['Token']:
        movable_tokens = [token for token in player.tokens if token.can_move(roll)]
        if not movable_tokens:
            return None
        
        # Simple AI strategy: prioritize getting tokens out of home
        for token in movable_tokens:
            if isinstance(token.state, HomeState) and roll == 6:
                return token
        
        # Otherwise, move the token that's furthest along
        return max(movable_tokens, key=lambda t: t.position if t.position >= 0 else -100)

# Factory Pattern
class PlayerFactory:
    @staticmethod
    def create_player(name: str, color: Color, is_human: bool = True) -> 'Player':
        strategy = HumanStrategy() if is_human else ComputerStrategy()
        return Player(name, color, strategy)

class TokenFactory:
    @staticmethod
    def create_tokens(color: Color, start_position: int) -> List['Token']:
        return [Token(color, start_position) for _ in range(4)]

# Core Classes Implementation
class Square:
    def __init__(self, position: int, square_type: SquareType = SquareType.NORMAL):
        self.position = position
        self.type = square_type
        self.tokens = []
    
    def add_token(self, token) -> None:
        self.tokens.append(token)
    
    def remove_token(self, token) -> None:
        if token in self.tokens:
            self.tokens.remove(token)
    
    def get_tokens(self) -> List['Token']:
        return self.tokens

class Token:
    def __init__(self, color: Color, start_position: int):
        self.color = color
        self.start_position = start_position
        self.position = -1  # -1 indicates in home
        self.state = HomeState()
    
    def set_state(self, state: TokenState) -> None:
        self.state = state
    
    def can_move(self, steps: int) -> bool:
        return self.state.can_move(self, steps)
    
    def move(self, steps: int) -> bool:
        return self.state.move(self, steps)
    
    def reset(self) -> None:
        self.position = -1
        self.state = HomeState()

class Dice:
    def roll(self) -> int:
        return random.randint(1, 6)

class Player:
    def __init__(self, name: str, color: Color, strategy: PlayerStrategy):
        self.name = name
        self.color = color
        self.strategy = strategy
        self.tokens = TokenFactory.create_tokens(color, self.get_start_position())
    
    def get_start_position(self) -> int:
        # Map colors to starting positions on the board
        start_positions = {
            Color.RED: 0,
            Color.GREEN: 13,
            Color.YELLOW: 26,
            Color.BLUE: 39
        }
        return start_positions[self.color]
    
    def choose_token(self, roll: int) -> Optional[Token]:
        return self.strategy.choose_token(self, roll)
    
    def has_won(self) -> bool:
        # Check if all tokens are in the home state with position -1
        return all(token.position == -1 and isinstance(token.state, HomeState) for token in self.tokens)

class GameBoard(Singleton):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.squares = [Square(i) for i in range(52)]
            # Add special squares like start, safe, etc.
            self.setup_special_squares()
            self.initialized = True
    
    def setup_special_squares(self) -> None:
        # Setting up special squares
        for color in Color:
            start_pos = self.get_start_position(color)
            self.squares[start_pos].type = SquareType.START
            
            # Safe squares are typically 8 steps before home
            safe_pos = (start_pos + 44) % 52
            self.squares[safe_pos].type = SquareType.SAFE
    
    def get_start_position(self, color: Color) -> int:
        start_positions = {
            Color.RED: 0,
            Color.GREEN: 13,
            Color.YELLOW: 26,
            Color.BLUE: 39
        }
        return start_positions[color]
    
    def get_square(self, position: int) -> Square:
        if 0 <= position < 52:
            return self.squares[position]
        # Handle home positions (100-106)
        return None
    
    def move_token(self, token: Token, steps: int) -> Tuple[bool, Optional[Token]]:
        """
        Moves a token and returns if the move was successful and a token that was killed if any
        """
        old_position = token.position
        if token.move(steps):
            # Get the new square
            if old_position >= 0 and old_position < 52:
                old_square = self.get_square(old_position)
                old_square.remove_token(token)
            
            # If in running state and on the main board
            if isinstance(token.state, RunningState) and token.position < 52:
                new_square = self.get_square(token.position)
                # Check for kills
                killed_token = None
                for other_token in new_square.get_tokens():
                    if other_token.color != token.color:
                        killed_token = other_token
                        kill_cmd = KillCommand(token, other_token)
                        kill_cmd.execute()
                        new_square.remove_token(other_token)
                
                new_square.add_token(token)
                return True, killed_token
            
            return True, None
        
        return False, None

# Decorator Pattern for Rules
class RuleDecorator(ABC):
    def __init__(self, game):
        self.game = game
    
    @abstractmethod
    def apply_rules(self, player: Player, roll: int) -> int:
        pass

class BonusTurnDecorator(RuleDecorator):
    def apply_rules(self, player: Player, roll: int) -> int:
        # If player rolls a 6, they get a bonus turn
        if roll == 6:
            return 1
        return 0

class KillBonusDecorator(RuleDecorator):
    def apply_rules(self, player: Player, token: Token, killed: bool) -> int:
        # If player kills another token, they get a bonus turn
        if killed:
            return 1
        return 0

# Facade Pattern
class GameManager:
    def __init__(self, num_players: int = 4, human_players: int = 1):
        self.board = GameBoard()
        self.dice = Dice()
        self.players = self.create_players(num_players, human_players)
        self.current_player_index = 0
        self.observers = []
        self.rule_decorators = [
            BonusTurnDecorator(self),
            KillBonusDecorator(self)
        ]
    
    def create_players(self, num_players: int, human_players: int) -> List[Player]:
        colors = list(Color)[:num_players]
        players = []
        
        for i in range(num_players):
            is_human = i < human_players
            player = PlayerFactory.create_player(f"Player {i+1}", colors[i], is_human)
            players.append(player)
        
        return players
    
    def add_observer(self, observer: GameObserver) -> None:
        self.observers.append(observer)
    
    def notify_observers(self) -> None:
        game_state = self.get_game_state()
        for observer in self.observers:
            observer.update(game_state)
    
    def get_game_state(self) -> Dict:
        return {
            "current_player": self.players[self.current_player_index].name,
            "player_tokens": {
                player.name: [token.position for token in player.tokens]
                for player in self.players
            }
        }
    
    def next_player(self) -> None:
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    
    def play_turn(self) -> bool:
        """
        Play a single turn, returns True if the game is over
        """
        player = self.players[self.current_player_index]
        
        # Roll the dice
        roll_cmd = RollCommand(self.dice)
        roll = roll_cmd.execute()
        print(f"{player.name} rolled a {roll}")
        
        # Choose token to move
        token = player.choose_token(roll)
        if token:
            # Move token
            success, killed_token = self.board.move_token(token, roll)
            if success:
                print(f"{player.name} moved a token to position {token.position}")
                
                # Check for a win
                if player.has_won():
                    print(f"{player.name} has won the game!")
                    return True
                
                # Apply rules (bonus turns)
                bonus_turn = 0
                for decorator in self.rule_decorators:
                    if isinstance(decorator, BonusTurnDecorator):
                        bonus_turn += decorator.apply_rules(player, roll)
                    elif isinstance(decorator, KillBonusDecorator) and killed_token:
                        bonus_turn += decorator.apply_rules(player, token, True)
                
                if bonus_turn > 0:
                    print(f"{player.name} gets a bonus turn!")
                    return self.play_turn()  # Recursive call for bonus turn
            else:
                print(f"{player.name} couldn't move any token")
        else:
            print(f"{player.name} has no valid moves")
        
        self.next_player()
        self.notify_observers()
        return False

# Main Game class
class Game:
    def __init__(self, num_players: int = 4, human_players: int = 1):
        self.game_manager = GameManager(num_players, human_players)
        self.game_manager.add_observer(ConsoleDisplayObserver())
    
    def start(self) -> None:
        print("Starting Ludo Game...")
        game_over = False
        
        while not game_over:
            game_over = self.game_manager.play_turn()
            # In a real implementation, we might have a delay between turns
        
        print("Game Over!")

# Example usage
if __name__ == "__main__":
    game = Game(num_players=4, human_players=1)
    game.start()