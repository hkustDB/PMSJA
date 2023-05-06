import math
import os
import sys

repeat_times = 20

epsilons = [2, 4, 8]
queries = ["Q3", "Q7"]
scales = ["_0_","_1_","_2_","_3_","_4_","_5_","_6_"]


def main(argv):
    for query in queries:
        for scale in scales:
            for epsilon in epsilons:
                output_file = open( "../Result/TPCH/R2T_" + query+"_scale"+scale +"eps_"+str(epsilon)  + ".txt", 'w')

                cmd = "../../python ../Code/R2T.py -I ../Information/TPCH/"+query+scale+ " -e "+str(epsilon)+ " -b 0.1 -G 1000000 -p 24 -d 0.0000001"

                for i in range(repeat_times):
                    shell = os.popen(cmd, 'r')
                    res = shell.read()
                    output_file.write("The result for the "+str(i)+"th execution is"+"\n")
                    output_file.write( res + "\n")

if __name__ == "__main__":
	main(sys.argv[1:])
