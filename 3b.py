import copy

main_list = []
col_width = 0
row_width = 0

def process_input():
    global col_width, row_width
    print("Processing input file...")

    with open("3.txt") as input_file:
        line = input_file.readline()
        inner_list = []
        
        while line:
            inner_list.clear()

            for char in line:
                inner_list.append(char)
            
            # record col_width, row_width
            col_width = len(inner_list)
            row_width = row_width + 1
            
            # add to main list
            main_list.append(copy.copy(inner_list))
            
            # read next line of input
            line = input_file.readline()

def traverse_list_count_trees(right_count, down_count):
    colidx = 0
    rowidx = 0
    char = '' # can be tree (#) or empty (.)
    tree_cnt = 0

    for idx in range(len(main_list)):
        colidx = colidx + right_count 
        rowidx = rowidx + down_count

        # maxed our rows / end of file
        if rowidx >= row_width:
            break
        
        # rotate
        if colidx >= col_width:
            colidx = abs(col_width - colidx)

        # get char to check
        char = main_list[rowidx][colidx]
        
        # if char is tree, increment count
        if char == "#":
            tree_cnt = tree_cnt + 1
        
    
    return tree_cnt

if __name__ == "__main__":
    # read input file
    process_input()

    # traverse as per 3 right 1 down and count trees (#)
    ans1 = traverse_list_count_trees(1,1)
    ans2 = traverse_list_count_trees(3,1)
    ans3 = traverse_list_count_trees(5,1)
    ans4 = traverse_list_count_trees(7,1)
    ans5 = traverse_list_count_trees(1,2)
    final_ans = ans1 * ans2 * ans3 * ans4 * ans5

    print(f"Found {final_ans} trees along all the rides")