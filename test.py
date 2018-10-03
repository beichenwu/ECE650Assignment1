import support_functions
import intersect
import unittest

class TestStringMethods(unittest.TestCase):

    #test function test_street_input_analysis(self)
    def test_street_input_analysis(self):
        self.assertEqual(support_functions.street_input_analysis('r "C"'), ('C', []))
        self.assertEqual(support_functions.street_input_analysis('a "A" (2,3)   (2,   6) (    3,7) (4,3)'), ('A', [[2,3],[2,6],[3,7],[4,3]]))
        self.assertEqual(support_functions.street_input_analysis('c "B" (2,3)   (2,3) (3,1) (3,3)'), ('B', [[2,3],[2,3],[3,1],[3,3]]))

    def test_read_input(self):
        self.assertEqual(support_functions.read_input('a "A"  (2,3)   (2,   6) (    3,7) (4,3)',{}),{"A": [[2,3],[2,6],[3,7],[4,3]]})
        self.assertEqual(support_functions.read_input('a "B"(2,3)   (2,3) (3,1) (3,3)', {"A": [[2,3], [2,6], [3,7], [4,3]]}),{"A": [[2,3], [2,6], [3,7], [4,3]],"B": [[2,3], [2,3], [3,1], [3,3]]})
        self.assertEqual(support_functions.read_input('c "B" (2,2)   (2,2) (3,5) (7,3)', {"A": [[2,3], [2,6], [3,7], [4,3]],"B": [[2,3], [2,3], [3,1], [3,3]]}),{"A": [[2,3], [2,6], [3,7], [4,3]], "B": [[2,2], [2,2], [3,5], [7,3]]})
        #self.assertEqual(support_functions.read_input('r "C"',{"A": [[2, 3], [2, 6], [3, 7], [4, 3]],"B": [[2, 3], [2, 3], [3, 1], [3, 3]]}),{"A": [[2, 3], [2, 6], [3, 7], [4, 3]]})

    def test_find_all_intersection(self):
        self.assertEqual(support_functions.find_all_intersection({"A": [[2, 1], [2, 2]],"B": [[2, 1], [4, 8]]}),[(2.0,1.0)])
        self.assertEqual(support_functions.find_all_intersection({"A": [[1, 0], [4, 0]], "B": [[2, 0], [3, 0]]}),[(2.0, 0.0),(3.0,0.0)])
        self.assertEqual(support_functions.find_all_intersection({"A": [[2, -1], [2, 2],[5,5],[5,6],[3,8]], "B": [[4, 2], [4, 8]], "C":[[1,4],[5,8]]}),[(4.0, 4.0), (4.0, 7.0)])

    def test_point_check(self):
        self.assertEqual(support_functions.point_check(intersect.Point(1,2),intersect.Line(intersect.Point(1,2),intersect.Point(1,3))),True)
        self.assertEqual(support_functions.point_check(intersect.Point(1, 2),intersect.Line(intersect.Point(3, 2), intersect.Point(4, 3))),False)
        self.assertEqual(support_functions.point_check(intersect.Point(3, 3),intersect.Line(intersect.Point(0, 0), intersect.Point(5, 5))),True)

    def test_check_exist_point(self):
        self.assertEqual(support_functions.check_exist_point([(2,3),(4,5),(6,6)],intersect.Point(4,5)), True)
        self.assertEqual(support_functions.check_exist_point([(2, 3), (4, 5), (6, 6)], intersect.Point(5, 4)), False)

    def test_two_point_equal(self):
        self.assertEqual(support_functions.two_point_equal([4,5],[5,4]), False)
        self.assertEqual(support_functions.two_point_equal([4,5],[4,5]), True)

    def test_index_in_list(self):
        self.assertEqual(support_functions.index_in_list([2,3,4,5,6,7],2),True)
        self.assertEqual(support_functions.index_in_list([2, 3, 4, 5, 6, 7], 7), True)
        self.assertEqual(support_functions.index_in_list([2, 3, 4, 5, 6, 7], 8), False)

    def test_index_in_dic(self):
        self.assertEqual(support_functions.index_in_dic({1:(2,3),2:(4,5),3:(4,7),4:(6,6)},(2,3)),1)
        self.assertEqual(support_functions.index_in_dic({1: (2, 3), 2: (4, 5), 3: (4, 7), 4: (6, 6)}, (4,7)), 3)
        self.assertEqual(support_functions.index_in_dic({1:(2,3),2:(4,5),3:(4,7),4:(6,6)},(6,3)),None)

    def test_cal_street_point(self):
        self.assertEqual(support_functions.cal_street_point({"A": [[2, -1], [2, 2], [5, 5], [5, 6], [3, 8]], "B": [[4, 2], [4, 8]], "C": [[1, 4], [5, 8]]},[(4.0, 4.0),(4.0, 7.0)]),
                         {1: [(2.0, 2.0), (5.0, 5.0), (4.0, 4.0)],
                          2: [(5.0, 6.0), (3.0, 8.0), (4.0, 7.0)],
                          3: [(1.0, 4.0), (5.0, 8.0), (4.0, 7.0)],
                          4: [(4.0, 2.0), (4.0, 8.0), (4.0, 4.0), (4.0, 7.0)]})

    def test_sort_street_list(self):
        self.assertEqual(support_functions.sort_street_point_list(
                        {1: [(2.0, 2.0), (5.0, 5.0), (4.0, 4.0)],
                          2: [(5.0, 6.0), (3.0, 8.0), (4.0, 7.0)],
                          3: [(1.0, 4.0), (5.0, 8.0), (4.0, 7.0)],
                          4: [(4.0, 2.0), (4.0, 8.0), (4.0, 4.0), (4.0, 7.0)]}),
                         {1: [(2.0, 2.0), (4.0, 4.0), (5.0, 5.0)],
                          2: [(3.0, 8.0), (4.0, 7.0),(5.0, 6.0)],
                          3: [(1.0, 4.0),(4.0, 7.0),(5.0, 8.0)],
                          4: [(4.0, 2.0),(4.0, 4.0), (4.0, 7.0), (4.0, 8.0)]})

    def test_sort_point_list(self):
        self.assertEqual(support_functions.sort_point_list([(4.0, 2.0), (4.0, 8.0), (4.0, 4.0), (4.0, 7.0)]),[(4.0, 2.0),(4.0, 4.0), (4.0, 7.0), (4.0, 8.0)])

    def test_update_vertice_list(self):
        self.assertEqual(support_functions.update_vertice_list({1: [(2.0, 2.0), (4.0, 4.0), (5.0, 5.0)],
                          2: [(3.0, 8.0), (4.0, 7.0),(5.0, 6.0)],
                          3: [(1.0, 4.0),(4.0, 7.0),(5.0, 8.0)],
                          4: [(4.0, 2.0),(4.0, 4.0), (4.0, 7.0), (4.0, 8.0)]},{}),
                         {1: (2.0, 2.0),
                          2: (4.0, 4.0),
                          3: (5.0, 5.0),
                          4: (3.0, 8.0),
                          5: (4.0, 7.0),
                          6: (5.0, 6.0),
                          7: (1.0, 4.0),
                          8: (5.0, 8.0),
                          9: (4.0, 2.0),
                          10: (4.0, 8.0)})

        street_point_list = {1: [(2.0, 2.0), (4.0, 4.0), (5.0, 5.0)],2: [(3.0, 8.0), (4.0, 7.0), (5.0, 6.0)],3: [(1.0, 4.0), (4.0, 7.0), (5.0, 8.0)]}
        vertice_list = {1: (2.0, 2.0), 2: (4.0, 4.0), 3: (5.0, 5.0), 4: (3.0, 8.0), 5: (4.0, 7.0), 6: (5.0, 6.0), 7: (1.0, 4.0), 8: (5.0, 8.0), 9: (4.0, 2.0),10: (4.0, 8.0)}
        vertice_list_new = {1: (2.0, 2.0), 2: (4.0, 4.0), 3: (5.0, 5.0), 4: (3.0, 8.0), 5: (4.0, 7.0), 6: (5.0, 6.0), 7: (1.0, 4.0), 8:(5.0,8.0)}
        self.assertEqual(support_functions.update_vertice_list(street_point_list,vertice_list),vertice_list_new)

        street_point_list = {1: [(2.0, 2.0), (4.0, 4.0), (5.0, 5.0)], 2: [(3.0, 8.0), (4.0, 7.0), (5.0, 6.0)],3: [(1.0, 4.0), (4.0, 7.0), (5.0, 8.0)], 4:[(2.0, 1.0), (2.0,2.0)]}
        vertice_list = {1: (2.0, 2.0), 2: (4.0, 4.0), 3: (5.0, 5.0), 4: (3.0, 8.0), 5: (4.0, 7.0), 6: (5.0, 6.0),7: (1.0, 4.0), 8: (5.0, 8.0), 9: (4.0, 2.0), 10: (4.0, 8.0)}
        vertice_list_new = {1: (2.0, 2.0), 2: (4.0, 4.0), 3: (5.0, 5.0), 4: (3.0, 8.0), 5: (4.0, 7.0), 6: (5.0, 6.0),7: (1.0, 4.0), 8: (5.0, 8.0), 9:(2.0, 1.0)}
        self.assertEqual(support_functions.update_vertice_list(street_point_list, vertice_list), vertice_list_new)

    def test_edge_list(self):
        street_point_list = {1: [(2.0, 2.0), (4.0, 4.0), (5.0, 5.0)], 2: [(3.0, 8.0), (4.0, 7.0), (5.0, 6.0)], 3: [(1.0, 4.0), (4.0, 7.0), (5.0, 8.0)], 4: [(2.0, 1.0), (2.0, 2.0)]}
        vertice_list = {1: (2.0, 2.0), 2: (4.0, 4.0), 3: (5.0, 5.0), 4: (3.0, 8.0), 5: (4.0, 7.0), 6: (5.0, 6.0), 7: (1.0, 4.0), 8: (5.0, 8.0), 9: (2.0, 1.0)}
        edge_list = [(1,2),(2,3),(4,5),(5,6),(7,5),(5,8),(9,1)]
        self.assertEqual(support_functions.edge_list(street_point_list,vertice_list),edge_list)

    def test_dic_to_list(self):
        vertice_list = {1: (2.0, 2.0), 2: (4.0, 4.0), 3: (5.0, 5.0), 4: (3.0, 8.0), 5: (4.0, 7.0), 6: (5.0, 6.0),7: (1.0, 4.0), 8: (5.0, 8.0), 9: (2.0, 1.0)}
        list = [(2.0, 2.0), (4.0, 4.0),(5.0, 5.0),(3.0, 8.0),(4.0, 7.0),(5.0, 6.0),(1.0, 4.0),(5.0, 8.0), (2.0, 1.0)]
        self.assertEqual(support_functions.dic_to_list(vertice_list),list)

    def test_check_exist_edge(self):
        edge_list = [(1, 2), (2, 3), (4, 5), (5, 6), (7, 5), (5, 8), (9, 1)]
        self.assertEqual(support_functions.check_exist_edge(edge_list,(5,8)),True)
        self.assertEqual(support_functions.check_exist_edge(edge_list, (5, 7)), True)
        self.assertEqual(support_functions.check_exist_edge(edge_list, (5, 9)), False)

    def test_check_int(self):
        self.assertEqual(support_functions.check_int(10),10)
        self.assertEqual(support_functions.check_int(4.0), 4)
        self.assertEqual(support_functions.check_int(5.5), 5.5)
        self.assertEqual(support_functions.check_int(0.0), 0)

    def test_int_dic(self):
        vertice_list = {1: (2.0, 2.0), 2: (4.0, 4.0), 3: (5.0, 5.0), 4: (3.0, 8.0), 5: (4.0, 7.0), 6: (5.0, 6.0),7: (1.0, 4.0), 8: (5.0, 8.0), 9: (2.0, 1.0)}
        vertice_list_new = {1: (2, 2), 2: (4, 4), 3: (5, 5), 4: (3, 8), 5: (4, 7), 6: (5, 6),7: (1, 4), 8: (5, 8), 9: (2, 1)}
        self.assertEqual(support_functions.int_dic(vertice_list),vertice_list_new)

    def test_intersect(self):
        l1 = intersect.Line(intersect.Point(3,3),intersect.Point(5,5))
        l2 = intersect.Line(intersect.Point(3,5), intersect.Point(5, 3))
        self.assertEqual(type(intersect.intersect(l1,l2)),type(intersect.Point(4,4)))
        self.assertEqual(intersect.intersect(l1, l2).x, intersect.Point(4, 4).x)
        self.assertEqual(intersect.intersect(l1, l2).y, intersect.Point(4, 4).y)

        #no intersection
        l1 = intersect.Line(intersect.Point(3,3),intersect.Point(5,5))
        l2 = intersect.Line(intersect.Point(6,6), intersect.Point(8,8))
        self.assertEqual(intersect.intersect(l1,l2),None)

        #no intersection
        l1 = intersect.Line(intersect.Point(3,3),intersect.Point(5,5))
        l2 = intersect.Line(intersect.Point(0,3), intersect.Point(3,6))
        self.assertEqual(intersect.intersect(l1,l2),None)

        #inline
        l1 = intersect.Line(intersect.Point(0,0),intersect.Point(5,0))
        l2 = intersect.Line(intersect.Point(1,0), intersect.Point(4,0))
        self.assertEqual((intersect.intersect(l1,l2)),[(1.0,0.0), (4.0,0.0)])

        #inline
        l1 = intersect.Line(intersect.Point(0,0),intersect.Point(5,0))
        l2 = intersect.Line(intersect.Point(1,0), intersect.Point(6,0))
        self.assertEqual((intersect.intersect(l1,l2)),[(1.0,0.0)])














if __name__ == '__main__':
    unittest.main()