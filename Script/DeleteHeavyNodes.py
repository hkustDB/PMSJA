import getopt
import psycopg2
import os
import math
import sys
import random
import numpy as np
import time
import gc
from ctypes import c_double


def main(argv):

    try:
        opts, args = getopt.getopt(argv,"d:n:h:",["database=","num_user=","help="])
    except getopt.GetoptError:
        print("DeleteHeavyNodes.py -d <database name> -n <num_user to delete)>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("DeleteHeavyNodes.py -d <database name> -n <num_user to delete)>")
            sys.exit()
        elif opt in ("-d", "--database"):
            database_name = str(arg)
        elif opt in ("-n","--num_user"):
            num_user = int(arg)


    input_path = "../Data/Graph/"+database_name+".tsv"
    input_file = open(input_path,'r')
    dic = {}
    for line in input_file.readlines():
        elements = line.split()
        if elements[0] not in dic:
            dic[elements[0]] = 1
        if elements[1] not in dic:
            dic[elements[1]] = 1
        if elements[0] in dic:
            dic[elements[0]] += 1
        if elements[1] in dic:
            dic[elements[1]] += 1

    input_file.close()
    sort_dic = sorted(dic.items(), key = lambda item:item[1], reverse = True)
    active_list = []
    for i in range(num_user):
        active_list.append(int(sort_dic[i][0]))

    output_path = "../Data/Graph/"+database_name+"_"+str(num_user)+".tsv"
    output_file = open(output_path, 'w')
    input_file = open(input_path,'r')
    for line in input_file.readlines():
        elements = line.split()
        if ((int(elements[0]) not in active_list) and (int(elements[1]) not in active_list)):
            output_file.write(line)

    output_file.close()
    input_file.close()

if __name__ == '__main__':
	main(sys.argv[1:])








