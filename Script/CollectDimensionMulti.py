import math
import os
import sys

repeat_times = 20

epsilons = [2, 4, 8]
queries = ["Q8"]
scales = ["_4"]
dimensions = [12, 25, 50, 100, 200, 400]


def main(argv):
    for dimension in dimensions:
        for epsilon in epsilons:
            output_file = open( "../Result/TPCH/PrivMultiSJA_Q8_dim_" + str(dimension) +"_eps_"+str(epsilon) +".txt", 'w')


            cmd = "../../python ../Code/PMSJA.py -I ../Information/TPCH/Q8_dim_"+str(dimension)+"_processed_ -e "+str(epsilon)+ " -b 0.1 -d 0.0000001 "

            for i in range(repeat_times):
                shell = os.popen(cmd, 'r')
                res = shell.read()
                output_file.write("The result for the "+str(i)+"th execution is"+"\n")
                output_file.write( res + "\n")

if __name__ == "__main__":
	main(sys.argv[1:])

