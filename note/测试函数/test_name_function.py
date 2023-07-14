import unittest
from note.测试函数.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试"""
    """所有以test 打头的方法都将自动运行"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main
