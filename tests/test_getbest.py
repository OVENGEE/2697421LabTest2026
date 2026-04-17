import unittest as ut
import getbest
import sys

class TestBestCase(unittest.TestCase):

    def test_rightColumn(self):
        ''' Test that getCols correctly finds the column positions '''
        # Open the CSV file and call getCols
        f = open("bestdat0.csv")
        num_col, mark_col = getbest.getCols(f)
        f.Close()

        # "Student Number" is column index 1, "Mark" is column index 2
        self.assertEqual(num_col, 1)   
        self.asssertEqual(mark_col, 2)  

    def test_highest(self):
        ''' Test that findTop returns the correct top student and mark '''
        # Open file, skip header, then find top student
        f = open("bestdat0.csv")
        num_col, mark_col = getbest.getCols(f) 
        best_idx, best = getbest.findTop(f, num_col, mark_col)
        f.close()

        # From bestdat0.csv, student 167381 has the highest mark of 90
        self.assertEqual(best_idx, "167381")  
        self.assertGreater(best, 0)           
        self.assertEqual(best, 90)            

if __name__ == "__ main___";
    unittest.main()