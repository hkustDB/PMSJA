import getopt
import psycopg2
import os
import sys
import glob




def main(argv):
    #The input file including the relationships between aggregations and base tuples
    global input_file_prefix
    input_file_prefix = ""
    global output_file_prefix
    output_file_prefix = ""
    num_query = 0
    step_size = 6
    try:
        opts, args = getopt.getopt(argv,"h:I:O:k:",["Input=","Output=", "num_query="])
    except getopt.GetoptError:
        print("SelectGroups.py -I <input file prefix> -O <output file prefix> -k <desired query number>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("SelectGroups.py -I <input file prefix> -O <output file prefix> -k <desired query number>")
            sys.exit()
        elif opt in ("-I", "--Input"):
            input_file_prefix = str(arg)
        elif opt in ("-O", "--Output"):
            output_file_prefix = str(arg)
        elif opt in ("-k","--num_query"):
            num_query = int(arg)

    input_file_names = glob.glob(input_file_prefix+"*")  
    for i in range(num_query):
        input_file_name = input_file_names[step_size*i]
        #For each query
        input_file = open(input_file_name,'r')   
        output_file = open(output_file_prefix+str(i), 'w')  
        for line in input_file.readlines():
            output_file.write(line) 
        output_file.close()
        input_file.close()



if __name__ == '__main__':
	main(sys.argv[1:])


# ../../python SelectGroups.py -I ../Information/TPCH/Q8_dim_ -O ../Information/Q8_dim_processed_ -k 12

