import getopt
import psycopg2
import os
import sys
import random
import glob


def main(argv):
    #The input file including the relationships between aggregations and base tuples
    global input_file_prefix
    input_file_prefix = ""
    global output_file_prefix
    output_file_prefix = ""
    num_query = 10
    num_iteration = 0
    random.seed(1)
    try:
        opts, args = getopt.getopt(argv,"h:I:O:i:",["Input=","Output=", "num_iteration="])
    except getopt.GetoptError:
        print("SelectGroups.py -I <input file prefix> -O <output file prefix> -i <number of dates in on group>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("SelectGroups.py -I <input file prefix> -O <output file prefix> -i <number of dates in on group>")
            sys.exit()
        elif opt in ("-I", "--Input"):
            input_file_prefix = str(arg)
        elif opt in ("-O", "--Output"):
            output_file_prefix = str(arg)
        elif opt in ("-i","--num_iteration"):
            num_iteration = int(arg)

    input_file_names = glob.glob(input_file_prefix+"*") 
    total_file = len(input_file_names)
    file_list = random.sample(range(total_file), num_query*num_iteration) 
    for i in range(num_query):
        output_file = open(output_file_prefix+str(i), 'w')
        for j in range(num_iteration):
            input_file_name = input_file_names[file_list[i*num_iteration+j]]
            #For each query
            input_file = open(input_file_name,'r')
            for line in input_file.readlines():
                output_file.write(line) 
            input_file.close()
        output_file.close()




if __name__ == '__main__':
	main(sys.argv[1:])


# ../../python SelectGroups.py -I ../Information/Graph/Q9_stackoverflow_a2q_10p_ -O ../Information/Q9_stackoverflow_a2q_processed_ -i 40
