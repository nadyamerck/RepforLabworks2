import inspect
import unittest

import task


class TestBook(unittest.TestCase):
    def test_existance(self):
        try:
            self.assertTrue(inspect.isclass(task.Book), 'Book не является классом')
        except AttributeError:
            raise self.failureException('Book не определён')

    def test_init(self):
        signature = inspect.signature(task.Book.__init__)
        self.assertGreaterEqual(len(signature.parameters), 4, 'Недостаточно параметров у инициализатора')
        self.assertTrue('id_' in signature.parameters, 'нет требуемого параметра id_')
        self.assertTrue('name' in signature.parameters, 'нет требуемого параметра name')
        self.assertTrue('pages' in signature.parameters, 'нет требуемого параметра pages')

    def test_str(self):
        book = task.Book(1, 'Python for dummies', 1024)
        self.assertEqual(f'Книга "Python for dummies"', str(book))
        self.assertEqual(f"Book(id_=1, name='Python for dummies', pages=1024)", repr(book))
