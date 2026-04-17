import unittest
import sys
import os

# This tells Python to look one folder UP for getbest.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import getbest

class TestBestCase(unittest.TestCase):

    def test_rightColumn(self):
        ''' Test that getCols correctly finds the column positions '''
        # Go one folder up to find bestdat0.csv
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'bestdat0.csv')
        f = open(csv_path)
        num_col, mark_col = getbest.getCols(f)
        f.close()

        self.assertEqual(num_col, 1)
        self.assertEqual(mark_col, 2)

    def test_highest(self):
        ''' Test that findTop returns the correct top student and mark '''
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'bestdat0.csv')
        f = open(csv_path)
        num_col, mark_col = getbest.getCols(f)
        best_idx, best = getbest.findTop(f, num_col, mark_col)
        f.close()

        self.assertEqual(best_idx, "167381")
        self.assertGreater(best, 0)
        self.assertEqual(best, 90)

if __name__ == "__main__":
    unittest.main()