import sys
import support_functions

# YOUR CODE GOES HERE

def main():
    street_list ={}
    V = {}
    E = []
    intersection_list ={}
    stree_point_list = {}
    V_list = []
    while True:
        #try:
        user_input = sys.stdin.readline().strip()
        if user_input  == '':
            break
            print 'read a line:', line
        elif user_input != "g":
            try:
                street_list = support_functions.read_input(user_input, street_list)
            except support_functions.ParseException as ex:
                sys.stderr.write("Error: {0}\n".format(ex))
        else:
            intersection_list = support_functions.find_all_intersection(street_list)
            street_point_list = support_functions.cal_street_point(street_list,intersection_list)
            street_point_list = support_functions.sort_street_point_list(street_point_list)
            V = support_functions.update_vertice_list(street_point_list,V)
            V = support_functions.int_dic(V)
            E = support_functions.edge_list(street_point_list,V)
            support_functions.print_vertix_list(V)
            support_functions.print_edge_list(E)
        #except EOFError:
            #break;
    print 'Finished reading input'
    sys.exit(0)


    ### YOUR MAIN CODE GOES HEREs

    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    #while True:
        #line = sys.stdin.readline()
        #if line == '':
            #break
        #print 'read a line:', line

    #print 'Finished reading input'
    # return exit code 0 on successful termination
    #sys.exit(0)

if __name__ == '__main__':
    main()
