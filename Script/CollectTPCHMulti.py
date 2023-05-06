import math
import os
import sys
import subprocess
repeat_times = 20

epsilons = [4]
queries = ["Q3", "Q4", "Q5", "Q6", "Q7", "Q8"]
scales = ["_4_"]


def main(argv):
    for query in queries:
        output_file = open("../Result/TPCH/PrivMultiSJA_" + query + ".txt", 'w')
        
        for scale in scales:
            cmd = "../../python ../Code/PMSJA.py -I " + "../Information/TPCH/" + query  +scale + " -e 4 -b 0.1 -d 0.0000001"

            for i in range(repeat_times):
                shell = os.popen(cmd, 'r')
                res = shell.read()

                output_file.write("The result for the "+str(i)+"th execution is"+"\n")
                output_file.write( res + "\n")

if __name__ == "__main__":
	main(sys.argv[1:])