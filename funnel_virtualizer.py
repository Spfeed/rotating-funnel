import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin, pi

"""
FunnelVisualizer - класс для визуализации воронки из окружностей с изменяющимся цветом.

Используемые библиотеки:
- Pygame для инициализации окна и обработки событий.
- OpenGL.GL и OpenGL.GLU для работы с графикой и трехмерной графикой.
- math для использования функций cos и sin.

Параметры:
- display_size: Размеры окна Pygame.

Атрибуты:
- display: Размеры окна Pygame.
- disk_radius: Список радиусов дисков, образующих воронку.
- num_disks: Количество дисков в воронке.

Методы:
- get_disk_color(theta): Возвращает цвет диска в зависимости от угла theta.
- draw_disk(radius, color): Отрисовывает диск с указанным радиусом и цветом.
- draw_funnel(): Отрисовывает воронку из дисков с изменяющимся цветом.
- run(): Основной метод, в котором обрабатываются события Pygame и отрисовывается воронка.
"""


class FunnelVisualizer:
    def __init__(self, display_size=(800, 600), testing=False):
        self.testing = testing
        pygame.init()
        self.display = display_size

        if not self.testing:
            pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
            gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
            glTranslatef(0.0, 0.0, -5)

        # Параметры дисков (радиус, количество дисков)
        self.disk_radius = [0.5, 0.4, 0.3, 0.2, 0.1]
        self.num_disks = len(self.disk_radius)

    def get_disk_color(self, theta):
        """
           Возвращает цвет диска в зависимости от угла theta.

           Параметры:
           - theta: Угол в радианах.

           Возвращаемое значение:
           - Кортеж (red, green, blue) представляющий цвет диска в формате RGB.
           """
        red = 0.5 + 0.5 * cos(theta)
        green = 0.5 + 0.5 * sin(theta)
        blue = 0.5 - 0.5 * cos(theta)
        return red, green, blue

    def draw_disk(self, radius, color):
        """
            Отрисовывает диск с указанным радиусом и цветом.

            Параметры:
            - radius: Радиус диска.
            - color: Цвет диска в формате RGB.
            """
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(color)
        glVertex2f(0, 0)
        num_segments = 100
        for i in range(num_segments + 1):
            theta = (i / num_segments) * (2 * pi)
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex2f(x, y)
        glEnd()

    def draw_funnel(self):
        """
           Отрисовывает воронку из дисков с изменяющимся цветом.
           """
        time = pygame.time.get_ticks() / 1000.0  # Получаем время в секундах
        for i in range(self.num_disks):
            glPushMatrix()
            glTranslatef(0, 0, -i)
            color = self.get_disk_color(time + i)  # Изменение цвета в зависимости от времени
            self.draw_disk(self.disk_radius[i], color)
            glPopMatrix()

    def run(self):
        """
           Основной метод, в котором обрабатываются события Pygame и отрисовывается воронка.
           """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw_funnel()
            pygame.display.flip()
            pygame.time.wait(10)
