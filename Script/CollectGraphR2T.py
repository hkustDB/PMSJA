import math
import os
import sys

repeat_times = 20

datasets = ["_stackoverflow_a2q_", "_stackoverflow_c2a_"]
queries = ["Q9", "Q10", "Q14"]


def main(argv):
    for query in queries:
        for dataset in datasets:
            output_file = open( "../Result/Graph/R2T_" + query+ "_graph"+dataset+ ".txt", 'w')
            if query=="Q9":
                cmd = "../../python ../Code/R2T.py -I ../Information/Graph/"+query+ dataset+"processed_ "+" -e 4 -b 0.1 -G 1000000 -p 24 -d 0.0000001"
            if query=="Q10":
                cmd = "../../python ../Code/R2T.py -I ../Information/Graph/"+query+ dataset+"processed_ "+" -e 4 -b 0.1 -G 1000000000000 -p 24 -d 0.0000001"
            if query=="Q14":
                cmd = "../../python ../Code/R2T.py -I ../Information/Graph/"+query+ dataset+"processed_ "+" -e 4 -b 0.1 -G 1000000000000000000 -p 24 -d 0.0000001 "

            for i in range(repeat_times):
                shell = os.popen(cmd, 'r')
                res = shell.read()
                output_file.write("The result for the "+str(i)+"th execution is"+"\n")
                output_file.write( res + "\n")

if __name__ == "__main__":
	main(sys.argv[1:])

