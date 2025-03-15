import inspect
import unittest

import task


# todo: replace this with an actual test
class TestInheritanceAndSetters(unittest.TestCase):
    def test_1_subclass(self):
        try:
            class_, parent, _ = task.PaperBook.__mro__
        except AttributeError:
            raise self.failureException('PaperBook не определён или не является классом')
        except ValueError:
            raise self.failureException('PaperBook не наследует Book')
        self.assertEqual(parent, task.Book, 'PaperBook не наследует Book')

        try:
            class_, parent, _ = task.AudioBook.__mro__
        except AttributeError:
            raise self.failureException('AudioBook не определён или не является классом')
        except ValueError:
            raise self.failureException('AudioBook не наследует Book')
        class_, parent, _ = task.AudioBook.__mro__
        self.assertEqual(parent, task.Book, 'AudioBook не наследует Book')

    def test_2_no_setters(self):
        paperback = task.PaperBook('DummiesForPython', 'Kaa', 666)
        with self.assertRaises(AttributeError, msg='Не должно быть возможно сменить автора'):
            paperback.author = 'Пушкин'
        with self.assertRaises(AttributeError, msg='Не должно быть возможно сменить название'):
            paperback.name = 'Избранное'
        audio = task.AudioBook('DummiesForPython', 'Kaa', 6.66)
        with self.assertRaises(AttributeError, msg='Не должно быть возможно сменить автора'):
            audio.author = 'Пушкин'
        with self.assertRaises(AttributeError, msg='Не должно быть возможно сменить название'):
            audio.name = 'Избранное'

    def test_3_setters(self):
        paperback = task.PaperBook('DummiesForPython', 'Kaa', 666)
        audio = task.AudioBook('DummiesForPython', 'Kaa', 6.66)
        with self.assertRaises(ValueError, msg='Отрицательные числа должны вызывать ошибку'):
            paperback.pages = -1
        with self.assertRaises(ValueError, msg='Отрицательные числа должны вызывать ошибку'):
            audio.duration = -6.6
        with self.assertRaises(TypeError, msg='Нецелое количество страниц должно вызывать ошибку'):
            paperback.pages = 3.14
        with self.assertRaises(TypeError, msg='Строка в качестве длительности должна вызывать ошибку'):
            audio.duration = 'duration'
