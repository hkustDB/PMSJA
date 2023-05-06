import math
import os
import sys

repeat_times = 20

epsilons = [4]
queries = ["Q1", "Q2"]


def main(argv):
    for query in queries:
        for epsilon in epsilons:
            output_file = open( "../Result/TPCH/ClipMean_" + query  + ".txt", 'w')
            cmd = "../../python ../Code/OptMean.py -I ../Information/TPCH/"+query+"_4_ "+ " -e 4 -b 0.1 -G 1000000 -d 0.0000001"

            for i in range(repeat_times):
                shell = os.popen(cmd, 'r')
                res = shell.read()
                output_file.write("The result for the "+str(i)+"th execution is"+"\n")
                output_file.write( res + "\n")

if __name__ == "__main__":
	main(sys.argv[1:])
