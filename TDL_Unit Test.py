import unittest
from TodoList import *

unittest.defaultTestLoader.sortTestMethodsUsing = None
class TDL_test(unittest.TestCase):

    def setUp(self):
        self.a = Todo('a','20/09/2018','21/09/2018','Doing')
        self.b = Todo('b','19/09/2018','21/09/2018','Doing')
        self.c = Todo('c','18/09/2018','21/09/2018','Doing')
        self.d = Todo('d','20/09/2018','21/09/2018','Doing')
        self.e = Todo('e','20/09/2018','21/09/2018','Doing')
        self.f = Todo('f','18/09/2018','21/09/2018','Doing')

    def tearDown(self):
        Todo._Todo__TodoList = []
        Todo._Todo__IDcount = []

    def test_str_to_date(self):
        with self.assertRaises(ValueError): str_to_date('28\09\2018')
        with self.assertRaises(ValueError): str_to_date('28~09~2018')
        with self.assertRaises(ValueError): str_to_date('28-Sep-2018')
        with self.assertRaises(ValueError): str_to_date('2018 Sep 28')

    def test_sort(self):
        self.assertEqual([self.c,self.f,self.b,self.a,self.d,self.e], Todo._Todo__TodoList)
        
    def test_edit(self):
        TDL_edit('ID_6', start_date = '19/09/2018', end_date = '22/09/2018', status = 'Complete', work_name = 'EST Rouge')
        self.assertEqual(self.f.start_date, str_to_date('19/09/2018'))
        self.assertEqual(self.f.end_date, str_to_date('22/09/2018'))
        self.assertEqual(self.f.work_name, 'EST Rouge')
        self.assertEqual(self.f.status, 'Complete')

    def test_delete_1(self):
        TDL_delete('ID_6')
        obj = None
        for job in Todo._Todo__TodoList:
            if job.ID == 'ID_6':
                obj = job
        self.assertEqual(None, obj)

    def test_delete_2(self):
        obj = None
        for job in Todo._Todo__TodoList:
            if job.ID == 'ID_6':
                obj = job
        self.assertEqual(self.f, obj)
        
        
if __name__ == '__main__':
    unittest.main()
