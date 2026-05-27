import pygame
import sys
import random

# Breakout (블럭깨기) 간단 구현

WIDTH, HEIGHT = 800, 600
FPS = 60

BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 24

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 16
BALL_RADIUS = 8

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BG = (20, 24, 30)


class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - 40
        self.speed = 7

    def move(self, dir):
        self.x += dir * self.speed
        self.x = max(0, min(WIDTH - self.width, self.x))

    def draw(self, surf):
        pygame.draw.rect(surf, GRAY, (self.x, self.y, self.width, self.height), border_radius=6)


class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        angle = random.uniform(-1.0, 1.0)
        self.speed = 5
        self.vx = self.speed * angle
        self.vy = -self.speed

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= BALL_RADIUS:
            self.x = BALL_RADIUS
            self.vx *= -1
        if self.x >= WIDTH - BALL_RADIUS:
            self.x = WIDTH - BALL_RADIUS
            self.vx *= -1
        if self.y <= BALL_RADIUS:
            self.y = BALL_RADIUS
            self.vy *= -1

    def draw(self, surf):
        pygame.draw.circle(surf, WHITE, (int(self.x), int(self.y)), BALL_RADIUS)


class Brick:
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.alive = True

    def draw(self, surf):
        if not self.alive:
            return
        pygame.draw.rect(surf, self.color, self.rect)
        pygame.draw.rect(surf, BG, self.rect, 2)


def create_bricks():
    bricks = []
    colors = [(255, 99, 71), (255, 165, 0), (255, 215, 0), (144, 238, 144), (135, 206, 235), (186, 85, 211)]
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            x = col * BRICK_WIDTH
            y = 40 + row * (BRICK_HEIGHT + 6)
            color = colors[row % len(colors)]
            bricks.append(Brick(x + 4, y, BRICK_WIDTH - 8, BRICK_HEIGHT, color))
    return bricks


def clamp(n, a, b):
    return max(a, min(b, n))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("블럭깨기 - Breakout")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()

    lives = 3
    score = 0
    playing = True
    paused = False
    show_message = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_r:
                    # reset game
                    paddle = Paddle()
                    ball = Ball()
                    bricks = create_bricks()
                    lives = 3
                    score = 0
                    playing = True
                    paused = False
                    show_message = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            paddle.move(-1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            paddle.move(1)

        if not paused and playing:
            ball.update()

            # paddle collision
            paddle_rect = pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.height)
            if pygame.Rect(int(ball.x - BALL_RADIUS), int(ball.y - BALL_RADIUS), BALL_RADIUS*2, BALL_RADIUS*2).colliderect(paddle_rect):
                # reflect based on hit position
                overlap_x = (ball.x - (paddle.x + paddle.width / 2)) / (paddle.width / 2)
                ball.vx = overlap_x * ball.speed * 1.2
                ball.vy = -abs(ball.vy)

            # brick collisions
            for brick in bricks:
                if not brick.alive:
                    continue
                if pygame.Rect(int(ball.x - BALL_RADIUS), int(ball.y - BALL_RADIUS), BALL_RADIUS*2, BALL_RADIUS*2).colliderect(brick.rect):
                    brick.alive = False
                    score += 100
                    # simple direction flip depending on side
                    if abs((brick.rect.left - ball.x)) < BRICK_WIDTH and abs((brick.rect.right - ball.x)) < BRICK_WIDTH:
                        ball.vy *= -1
                    else:
                        ball.vx *= -1
                    break

            # bottom (lose life)
            if ball.y >= HEIGHT + BALL_RADIUS:
                lives -= 1
                if lives <= 0:
                    playing = False
                    show_message = True
                else:
                    ball.reset()

            # win check
            if all(not b.alive for b in bricks):
                playing = False
                show_message = True

        # drawing
        screen.fill(BG)
        for brick in bricks:
            brick.draw(screen)
        paddle.draw(screen)
        ball.draw(screen)

        hud = font.render(f"Score: {score}   Lives: {lives}   (P)ause (R)eset", True, WHITE)
        screen.blit(hud, (8, HEIGHT - 28))

        if paused:
            msg = font.render("Paused - Press P to resume", True, WHITE)
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))

        if show_message:
            if all(not b.alive for b in bricks):
                text = "You Win! Press R to Restart"
            else:
                text = "Game Over. Press R to Restart"
            msg = font.render(text, True, WHITE)
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 20))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
