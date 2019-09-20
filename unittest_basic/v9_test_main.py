import unittest


def setUpModule():
    print('setUpModule')


def tearDownModule():
    print('setUpModule')


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\tTest1 setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('\tTest1 tearDownClass')

    def setUp(self):
        print('\t\tTest1 setUp')

    def tearDown(self):
        print('\t\tTest1 tearDown')

    def test_1(self):
        print('\t\t\tTest1 test 1')

    def test_2(self):
        print('\t\t\tTest1 test 2')


class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\tTest2 setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('\tTest2 tearDownClass')

    def setUp(self):
        print('\t\tTest2 setUp')

    def tearDown(self):
        print('\t\tTest2 tearDown')

    def test(self):
        print('\t\t\tTest2 test')
