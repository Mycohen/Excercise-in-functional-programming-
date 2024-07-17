
# File: snake_game.py
# Author: Moshe Yaakov Cohen
#
# This module implements a simple snake game using the pygame library. The game consists of a snake that moves around a grid,
# eating food to grow longer. The game ends if the snake runs into itself.

import pygame
import random

# Initialize pygame
pygame.init()

# Constants defining screen dimensions, grid size, and colors
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Snake:
    """Represents the snake in the game.

    Attributes:
        positions (list of tuples): The segments of the snake, where each segment's position is a tuple (x, y).
        direction (tuple): The current movement direction of the snake as a tuple (x, y).
        grow (bool): Flag to determine whether the snake should grow after eating food.
    """

    def __init__(self):
        """Initializes the snake object."""
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)  # Initially moving right
        self.grow = False

    def get_head_position(self):
        """Returns the position of the snake's head."""
        return self.positions[0]

    def turn(self, point):
        """Changes the snake's direction unless it's the opposite of the current direction.

        Args:
            point (tuple): The new direction for the snake.
        """
        if self.direction != (-point[0], -point[1]):  # Prevent reversing
            self.direction = point

    def move(self):
        """Moves the snake in the current direction and handles growing and resetting."""
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + x) % GRID_WIDTH), (cur[1] + y) % GRID_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if self.grow:
                self.grow = False
            else:
                self.positions.pop()

    def reset(self):
        """Resets the snake to its initial state."""
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def draw(self, surface):
        """Draws the snake on the screen.

        Args:
            surface (pygame.Surface): The pygame surface to draw the snake on.
        """
        for p in self.positions:
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, GREEN, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def handle_keys(self):
        """Handles keyboard input for controlling the snake."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))

    def collide_with_food(self, food_position):
        """Checks if the snake's head collides with food.

        Args:
            food_position (tuple): The position of the food.

        Returns:
            bool: True if the snake's head collides with the food, False otherwise.
        """
        if self.get_head_position() == food_position:
            self.grow = True
            return True
        return False


class Food:
    """Represents the food in the game.

    Attributes:
        position (tuple): The position of the food on the grid.
        color (tuple): The color of the food.
    """

    def __init__(self):
        """Initializes the food object."""
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        """Randomizes the position of the food on the grid."""
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        """Draws the food on the screen.

        Args:
            surface (pygame.Surface): The pygame surface to draw the food on.
        """
        r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)


def main():
    """Main function to run the game."""
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Snake Game')

    snake = Snake()
    food = Food()

    while True:
        snake.handle_keys()
        snake.move()

        if snake.collide_with_food(food.position):
            food.randomize_position()

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()

        if len(snake.positions) > GRID_WIDTH * GRID_HEIGHT:
            snake.reset()

        clock.tick(10)  # Control game speed


if __name__ == '__main__':
    main()
