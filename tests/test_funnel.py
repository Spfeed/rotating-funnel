"""
Модуль для тестирования класса FunnelVisualizer.

Содержит тесты для проверки корректности работы методов класса FunnelVisualizer,
отвечающих за инициализацию, отрисовку дисков и воронки.

Используемые библиотеки:
- unittest для написания тестов.
- unittest.mock для создания моков и патчей.
- io.StringIO для перехвата вывода.
- OpenGL.GL для мокирования методов OpenGL.
- pygame для создания объекта FunnelVisualizer.

Классы тестов:
- TestFunnelVisualizer: Включает тесты для методов инициализации, получения цвета диска,
  отрисовки диска и воронки.

Тесты:
1. test_init: Проверяет корректность инициализации объекта FunnelVisualizer.
2. test_get_disk_color: Проверяет корректность получения цвета диска по заданному углу.
3. test_draw_disk: Проверяет корректность вызова OpenGL-методов при отрисовке диска.
4. test_draw_funnel: Проверяет корректность вызова методов при отрисовке воронки.

Пример использования:
- Запуск тестов: python test_funnel.py
"""

import unittest
from unittest.mock import *
from io import StringIO
from OpenGL.GL import *

import pygame

from funnel_virtualizer import FunnelVisualizer


class TestFunnelVisualizer(unittest.TestCase):
    def test_init(self):
        funnel_visualizer = FunnelVisualizer()
        self.assertEqual(funnel_visualizer.display, (800, 600))
        self.assertEqual(len(funnel_visualizer.disk_radius), 5)
        self.assertEqual(funnel_visualizer.num_disks, 5)

    def test_get_disk_color(self):
        funnel_visualizer = FunnelVisualizer()
        color = funnel_visualizer.get_disk_color(0)
        self.assertIsInstance(color, tuple)
        self.assertEqual(len(color), 3)
        self.assertGreaterEqual(color[0], 0)
        self.assertGreaterEqual(color[1], 0)
        self.assertGreaterEqual(color[2], 0)

    @patch('funnel_virtualizer.glBegin')
    @patch('funnel_virtualizer.glColor3fv')
    @patch('funnel_virtualizer.glVertex2f')
    @patch('funnel_virtualizer.glEnd')
    def test_draw_disk(self, mock_glEnd, mock_glVertex2f, mock_glColor3fv, mock_glBegin):
        funnel_visualizer = FunnelVisualizer()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            funnel_visualizer.draw_disk(0.5, (1, 0, 0))
            output = mock_stdout.getvalue().strip()
            mock_glBegin.assert_called_with(GL_TRIANGLE_FAN)
            mock_glColor3fv.assert_called_with((1, 0, 0))

            mock_glVertex2f.assert_called()
            args, kwargs = mock_glVertex2f.call_args
            x, y = args
            self.assertAlmostEqual(x, 0, delta=0.5)
            self.assertAlmostEqual(y, 0, delta=0.5)

            mock_glEnd.assert_called()

    @patch('funnel_virtualizer.glPushMatrix')
    @patch('funnel_virtualizer.glTranslatef')
    @patch('funnel_virtualizer.glPopMatrix')
    def test_draw_funnel(self, mock_glPopMatrix, mock_glTranslatef, mock_glPushMatrix):
        funnel_visualizer = FunnelVisualizer()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            funnel_visualizer.draw_funnel()

            mock_glPushMatrix.assert_called()
            mock_glTranslatef.assert_called()
            mock_glPopMatrix.assert_called()


if __name__ == '__main__':
    unittest.main()
