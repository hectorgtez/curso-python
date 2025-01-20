import unittest
import change_text


class TestChangeText(unittest.TestCase):
    def test_uppercase(self):
        word = 'good morning'
        result = change_text.all_uppercase(word)

        self.assertEqual(result, 'GOOD MORNING')


if __name__ == '__main__':
    unittest.main()
