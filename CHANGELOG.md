# Changelog

Все изменения проекта с момента начала его разработки.

## [0.0.1]  - 2023-12-01

### Добавлено
- Добавлен класс `FunnelVisualizer` в файле "funnel_virtualizer.py", представляющий визуализацию воронки.
  - `get_disk_color`, возвращает цвет диска в зависимости от угла.
  - `draw_disk`, отрисовывает диск с заданным радиусом и цветом.
  - `draw_funnel`, отрисовывает воронку, состоящую из дисков.
  - `run`, создает окно и вызывает метод, отрисовыващий воронку.
- Создан файл "main.py" как точка входа в приложение.
- Добавлены модульные тесты для класса `FunnelVisualizer` в директории "tests" с файлом "test_funnel.py".
  - `test_init`, проверяет инициализацию объекта.
  - `test_get_disk_color`, проверяет получение цвета диска.
  - `test_draw_disk`, проверяет отрисовку диска.
  - `test_draw_funnel`, проверяет отрисовку воронки.



