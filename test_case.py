import transport_function
import unittest


class Transport_solve_test(unittest.TestCase):
    def test_for_minimum_function(self):
        matrix_C = [5, 15, 3, 6, 10,
                    23, 8, 13, 27, 12,
                    27, 14, 14, 10, 18,
                    8, 26, 7, 28, 9]
        vector_a = [9, 11, 15, 16]
        vector_b = [8, 9, 13, 8, 12]
        self.assertLessEqual(transport_function.transport_solve(matrix_C, vector_a, vector_b), 429.0)


if __name__ == '__main__':
    unittest.main()
