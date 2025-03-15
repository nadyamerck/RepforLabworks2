import unittest
import inspect

import task


# todo: replace this with an actual test
class TestClasses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.learner_defined_classes = {name: x for name, x in inspect.getmembers(task) if inspect.isclass(x)}
        cls.learner_defined_methods = {}
        if cls.learner_defined_classes:
            for class_name, class_ in cls.learner_defined_classes.items():
                cls.learner_defined_methods[class_name] = {method_name: method for method_name, method in inspect.getmembers(
                    class_, predicate=lambda x:inspect.isfunction(x) and not x.__name__.startswith('__'))}

    def test_classes_number(self):
        self.assertGreaterEqual(len(self.__class__.learner_defined_classes), 3, msg="Определите хотя бы три класса")

    def test_classes_attrs(self):
        for class_name, class_ in self.__class__.learner_defined_classes.items():
            signature = inspect.signature(class_.__init__)
            self.assertTrue(len(signature.parameters)>= 3, f'Класс {class_name} содержит менее 2 атрибутов')

    def test_methods(self):
        for class_name, methods_dict in self.__class__.learner_defined_methods.items():
            self.assertGreaterEqual(len(methods_dict), 2, f'Класс {class_name} имеет менее 2 методов')
            for method_name, method in methods_dict.items():
                self.assertTrue(inspect.getdoc(method), f'Метод {class_name}.{method_name} не документирован')
                signature = inspect.signature(method)
                self.assertNotEqual(signature.return_annotation, inspect._empty, f'метод {class_name}.{method_name} не содержит аннотацию типа возвращаемого значения')
                for parameter in [p for p in signature.parameters if not p == 'self']:
                    self.assertNotEqual(signature.parameters[parameter].annotation, inspect._empty, f'Параметр "{parameter}" не аннотирован')

    def test_doctest(self):
        import doctest
        suite = doctest.DocTestSuite(task)
        self.assertGreater(suite.countTestCases(), 0, 'в файле task.py нет ни одного doctest')
        self.assertTrue(unittest.TextTestRunner().run(suite).wasSuccessful(), 'тесты, определённые в doctest, провалились')
