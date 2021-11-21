from lab_5.tarjan import tarjan
import unittest


class TestTarjan(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(tarjan([]), [])

    def test_main_case(self):
        self.assertEqual([[4], [7, 6], [5, 2, 1, 0], [3]],
                         tarjan([[1], [0, 2, 5], [1, 4, 5, 6], [5, 7], [], [1], [4, 7], [6]]))
        self.assertEqual([[2], [7, 6, 5, 3, 1, 0], [4]],
                         tarjan([[1, 2], [0, 3, 5], [], [5], [2, 6, 7], [1, 3, 6], [2, 5, 7], [5]]))

    def test_raises(self):
        self.assertRaises(ValueError, tarjan, 44)
        self.assertRaises(ValueError, tarjan, "SDO")
        self.assertRaises(ValueError, tarjan, {1: [4], 4: [1]})


if __name__ == '__main__':
    unittest.main()
