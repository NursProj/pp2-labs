import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.init()
        pygame.mixer.init()
        self.music_folder = music_folder
        self.music_list = os.listdir(music_folder)
        self.current_track_index = 0
        self.playing = False
        self.load_track()

    def load_track(self):
        track_path = os.path.join(self.music_folder, self.music_list[self.current_track_index])
        pygame.mixer.music.load(track_path)

    def play(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True

    def pause(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next_track(self):
        self.stop()
        self.current_track_index = (self.current_track_index + 1) % len(self.music_list)
        self.load_track()
        self.play()

def format_timer(ms):
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
    return f"{minutes}:{seconds:02}"

def main():
    music_folder = "./date/musices"
    player = MusicPlayer(music_folder)

    pygame.init()
    screen = pygame.display.set_mode((600, 200))
    pygame.display.set_caption("Music Player")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # Button dimensions and positions
    button_width = 120
    button_height = 60
    play_button = pygame.Rect(50, 80, button_width, button_height)
    pause_button = pygame.Rect(200, 80, button_width, button_height)
    stop_button = pygame.Rect(350, 80, button_width, button_height)
    next_button = pygame.Rect(500, 80, button_width, button_height)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # Check if a button is clicked
                if play_button.collidepoint(mouse_pos):
                    player.play()
                elif pause_button.collidepoint(mouse_pos):
                    player.pause()
                elif stop_button.collidepoint(mouse_pos):
                    player.stop()
                elif next_button.collidepoint(mouse_pos):
                    player.next_track()

        screen.fill((255, 255, 255))
        # Render buttons with text
        pygame.draw.rect(screen, (0, 255, 0), play_button)
        pygame.draw.rect(screen, (255, 0, 0), pause_button)
        pygame.draw.rect(screen, (0, 0, 255), stop_button)
        pygame.draw.rect(screen, (255, 255, 0), next_button)

        play_text = font.render("Play", True, (0, 0, 0))
        pause_text = font.render("Pause", True, (0, 0, 0))
        stop_text = font.render("Stop", True, (0, 0, 0))
        next_text = font.render("Next", True, (0, 0, 0))

        screen.blit(play_text, (play_button.x + 10, play_button.y + 10))
        screen.blit(pause_text, (pause_button.x + 10, pause_button.y + 10))
        screen.blit(stop_text, (stop_button.x + 10, stop_button.y + 10))
        screen.blit(next_text, (next_button.x + 10, next_button.y + 10))

        # Display player name, current track name, and timer
        player_name_text = font.render("Your Name", True, (0, 0, 0))
        current_track_text = font.render(player.music_list[player.current_track_index], True, (0, 0, 0))
        timer_text = font.render(f"Time: {format_timer(pygame.mixer.music.get_pos())}", True, (0, 0, 0))

        screen.blit(player_name_text, (50, 20))
        screen.blit(current_track_text, (50, 140))
        screen.blit(timer_text, (350, 140))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
