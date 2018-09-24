import sys
import support_functions

# YOUR CODE GOES HERE

def main():
    street_list ={}
    V = {}
    E = []
    intersection_list ={}
    stree_point_list = {}

    while True:
        user_input = raw_input()
        if user_input != "g":
            try:
                street_list = support_functions.read_input(user_input, street_list)
            except support_functions.ParseException as ex:
                sys.stdout.write("Error: {0}\n".format(ex))
        else:
            intersection_list = support_functions.find_all_intersection(street_list)
            street_point_list = support_functions.cal_street_point(street_list,intersection_list)
            street_point_list = support_functions.sort_street_point_list(street_point_list)
            V = support_functions.update_vertice_list(street_point_list,V)
            E = support_functions.edge_list(street_point_list,V)
            support_functions.print_vertix_list(V)
            support_functions.print_edge_list(E)


    ### YOUR MAIN CODE GOES HEREs

    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        print 'read a line:', line

    print 'Finished reading input'
    # return exit code 0 on successful termination
    sys.exit(0)

if __name__ == '__main__':
    main()
