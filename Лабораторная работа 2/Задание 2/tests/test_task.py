import inspect
import unittest

import task

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class TestLibrary(unittest.TestCase):
    def test_existance(self):
        try:
            self.assertTrue(inspect.isclass(task.Library), 'Library не является классом')
        except AttributeError:
            raise self.failureException('Library не определён')

    def test_init(self):
        signature = inspect.signature(task.Library.__init__)
        try:
            self.assertNotEqual(inspect._empty, signature.parameters['books'].default,
                                'Атрибут books должен иметь значение по умолчанию')
        except KeyError:
            raise self.failureException('В инициализаторе отсутствует параметр books')
        library = task.Library()
        self.assertEqual([], library.books)

    def test_next(self):
        self.assertTrue('get_next_book_id' in [name for name, _ in inspect.getmembers(task.Library)],
                        'Не определён метод get_next_book_id')
        library = task.Library()
        self.assertEqual(1, library.get_next_book_id(), 'get_next_book_id пустой библиотеки не возвращает 1')
        library = task.Library(
            [task.Book(id_=book['id'], name=book['name'], pages=book['pages']) for book in BOOKS_DATABASE])
        self.assertEqual(3, library.get_next_book_id(), 'get_next_book_id пустой библиотеки не возвращает 1')

    def test_x_by_id(self):
        self.assertTrue('get_index_by_book_id' in [name for name, _ in inspect.getmembers(task.Library)],
                        'Не определён метод get_index_by_book_id')
        library = task.Library(
            [task.Book(id_=book['id'], name=book['name'], pages=book['pages']) for book in BOOKS_DATABASE])
        self.assertEqual(0, library.get_index_by_book_id(1))
        self.assertEqual(1, library.get_index_by_book_id(2))
        with self.assertRaises(ValueError, msg='Отсутствие запрошенной книги  библиотеке должно вызывать ошибку') as cm:
            library.get_index_by_book_id(3)
        self.assertTrue('Книги с запрашиваемым id не существует' in cm.exception.args,
                        'Сообщение об ошибке не соответствует заданному')
