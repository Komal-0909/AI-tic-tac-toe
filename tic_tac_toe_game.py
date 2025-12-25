import sys
import pygame
import numpy as np

pygame.init()


background_color = (18, 18, 35)
line_color = (130, 130, 220)
person_color = (255, 180, 80)
AI_COLOR = (255, 90, 90)
text_color = (240, 240, 255)
popup_color = (245, 245, 245)
popup_border = (180, 180, 180)

button_bg = (90, 160, 255)
button_hover = (120, 190, 255)
exit_bg = (255, 120, 120)
exit_hover = (255, 160, 160)


width = 360
height = 460
topSpace = 120
rows = COLS = 3
square = width // COLS
lineWidth = 4

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AI-Based Tic Tac Toe")


board = np.zeros((rows, COLS))
human_wins = 0
ai_wins = 0
draws = 0


title_font = pygame.font.SysFont("arial", 40, bold=True)
score_font = pygame.font.SysFont("arial", 20)
result_font = pygame.font.SysFont("arial", 34, bold=True)
button_font = pygame.font.SysFont("arial", 18, bold=True)

restart_btn = pygame.Rect(width//2 - 90, 80, 80, 30)
exit_btn = pygame.Rect(width//2 + 10, 80, 80, 30)


def draw_header():
    screen.fill(background_color)
    title = title_font.render("TIC TAC TOE", True, text_color)
    screen.blit(title, (width//2 - title.get_width()//2, 10))

    score = score_font.render(
        f"You: {human_wins}   AI: {ai_wins}   Draws: {draws}",
        True, text_color
    )
    screen.blit(score, (width//2 - score.get_width()//2, 55))

def draw_board():
    for i in range(1, rows):
        pygame.draw.line(
            screen, line_color,
            (0, topSpace + i*square),
            (width, topSpace + i*square), lineWidth
        )
        pygame.draw.line(
            screen, line_color,
            (i*square, topSpace),
            (i*square, height), lineWidth
        )

def draw_figures():
    for r in range(rows):
        for c in range(COLS):
            x = c * square
            y = topSpace + r * square
            if board[r][c] == 1:
                pygame.draw.circle(
                    screen, person_color,
                    (x+square//2, y+square//2),
                    square//3, 6
                )
            elif board[r][c] == 2:
                pygame.draw.line(
                    screen, AI_COLOR,
                    (x+20, y+20),
                    (x+square-20, y+square-20), 6
                )
                pygame.draw.line(
                    screen, AI_COLOR,
                    (x+20, y+square-20),
                    (x+square-20, y+20), 6
                )

def draw_buttons():
    mouse = pygame.mouse.get_pos()

    # Restart button
    r_color = button_hover if restart_btn.collidepoint(mouse) else button_bg
    pygame.draw.rect(screen, r_color, restart_btn, border_radius=6)
    r_text = button_font.render("Restart ", True, (0, 0, 0))
    screen.blit(r_text, (restart_btn.centerx - r_text.get_width()//2,
                          restart_btn.centery - r_text.get_height()//2))

    # Exit button
    e_color = exit_hover if exit_btn.collidepoint(mouse) else exit_bg
    pygame.draw.rect(screen, e_color, exit_btn, border_radius=6)
    e_text = button_font.render("Exit ", True, (0, 0, 0))
    screen.blit(e_text, (exit_btn.centerx - e_text.get_width()//2,
                          exit_btn.centery - e_text.get_height()//2))

def show_popup(text, color):
    rect = pygame.Rect(width//2 - 130, topSpace + square*1.3, 260, 70)
    pygame.draw.rect(screen, popup_color, rect, border_radius=14)
    pygame.draw.rect(screen, popup_border, rect, 2, border_radius=14)
    msg = result_font.render(text, True, color)
    screen.blit(msg, (rect.centerx - msg.get_width()//2,
                      rect.centery - msg.get_height()//2))

# ================= GAME LOGIC =================
def available(r, c):
    return board[r][c] == 0

def full():
    return not np.any(board == 0)

def check_win(p):
    for i in range(3):
        if all(board[i, :] == p) or all(board[:, i] == p):
            return True
    if all(board[i][i] == p for i in range(3)):
        return True
    if all(board[i][2-i] == p for i in range(3)):
        return True
    return False

def minimax(temp, is_max):
    if check_win(2): return 1
    if check_win(1): return -1
    if full(): return 0

    best = -1000 if is_max else 1000
    for r in range(3):
        for c in range(3):
            if temp[r][c] == 0:
                temp[r][c] = 2 if is_max else 1
                score = minimax(temp, not is_max)
                temp[r][c] = 0
                best = max(best, score) if is_max else min(best, score)
    return best

def ai_move():
    best, move = -1000, None
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                board[r][c] = 2
                score = minimax(board, False)
                board[r][c] = 0
                if score > best:
                    best, move = score, (r, c)
    if move:
        board[move] = 2

def restart_game():
    board.fill(0)


game_over = False
score_updated = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                if restart_btn.collidepoint(event.pos):
                    restart_game()
                    game_over = False
                    score_updated = False
                elif exit_btn.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                continue

            mx = event.pos[0] // square
            my = (event.pos[1] - topSpace) // square
            if 0 <= my < 3 and available(my, mx):
                board[my][mx] = 1
                if check_win(1):
                    game_over = True
                else:
                    ai_move()
                    if check_win(2):
                        game_over = True
                if full():
                    game_over = True

    draw_header()
    draw_board()
    draw_figures()

    if game_over and not score_updated:
        if check_win(1): human_wins += 1
        elif check_win(2): ai_wins += 1
        else: draws += 1
        score_updated = True

    if game_over:
        if check_win(1):
            show_popup(" YOU WIN! ", (40, 140, 40))
        elif check_win(2):
            show_popup("AI WINS!", (180, 50, 50))
        else:
            show_popup(" DRAW!", (60, 60, 60))
        draw_buttons()

    pygame.display.update()