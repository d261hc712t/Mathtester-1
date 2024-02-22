from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
import pygame
import sys


class PygameWidget(Widget):
    def __init__(self, **kwargs):
        super(PygameWidget, self).__init__(**kwargs)

        # Khởi tạo Pygame
        pygame.init()

        # Màu sắc
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)

        # Kích thước cửa sổ
        WIDTH, HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Drag and Drop Item")

        # Tạo hình chữ nhật (item)
        self.item_rect = pygame.Rect(100, 100, 50, 50)
        self.dragging = False

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        self.screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.item_rect.collidepoint(event.pos):
                    self.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    self.item_rect.move_ip(event.rel)

        pygame.draw.rect(self.screen, (255, 0, 0), self.item_rect)
        pygame.display.flip()


class PygameApp(App):
    def build(self):
        return PygameWidget()


if __name__ == '__main__':
    PygameApp().run()
