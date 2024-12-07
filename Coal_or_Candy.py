import pygame
import random
import sys

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hứng vật thể")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Tốc độ FPS
clock = pygame.time.Clock()
FPS = 60

# Tạo nhân vật
player_width = 100
player_height = 20
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 10

# Vật thể
object_width = 30
object_height = 30
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = -object_height
object_speed = 5
object_color = WHITE  # Mặc định là màu trắng (tốt)

# Điểm số và thời gian
score = 0
time_left = 30  # Thời gian ban đầu

# Font
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=BLACK):
    """Vẽ text lên màn hình"""
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

running = True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Điều khiển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Cập nhật vị trí vật thể
    object_y += object_speed

    # Kiểm tra nếu vật thể ra khỏi màn hình
    if object_y > SCREEN_HEIGHT:
        object_y = -object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        object_color = WHITE if random.choice([True, False]) else BLACK

    # Kiểm tra va chạm
    if (player_x < object_x + object_width and
        player_x + player_width > object_x and
        player_y < object_y + object_height and
        player_y + player_height > object_y):
        if object_color == WHITE:
            score += 1
            time_left += 2
        else:
            score -= 1
            time_left -= 2
        object_y = -object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        object_color = WHITE if random.choice([True, False]) else BLACK

    # Giảm thời gian
    time_left -= 1 / FPS
    if time_left <= 0:
        running = False

    # Vẽ nhân vật
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Vẽ vật thể
    pygame.draw.rect(screen, object_color, (object_x, object_y, object_width, object_height))

    # Hiển thị điểm và thời gian
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Time left: {int(time_left)}", 10, 50)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
