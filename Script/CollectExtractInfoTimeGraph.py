import sys
import os
import time



def main(argv):
    queries = ["Q9", "Q10", "Q14"]
    datasets = ["stackoverflow_a2q_10p", "stackoverflow_c2a_10p"]
    repeat_time = 10

    output_file = open( "../Result/Graph/Graph_Times.txt", 'w')
    for query in queries:
        for dataset in datasets:
            output_file.write(query+dataset+" times: \n")
            times = []
            for i in range(repeat_time):
                start = time.time()
                cmd = "../../python ../Code/ExtractInfoMultiple.py -D "+dataset+" -Q ../Query/"+query+".txt -P node -K ../Query/"+query+"_key.txt -O ../Information/"+query+"_"+dataset
                
                shell = os.popen(cmd, 'r')
                shell.read()
                shell.close()
                end= time.time()
                time_used = end-start
                output_file.write("The time for the "+str(i)+"th execution is"+"\n")
                output_file.write(str(time_used)+"\n")
                times.append(time_used)
            average_time = sum(times)/repeat_time
            output_file.write("Average time for "+query+dataset+" is \n")
            output_file.write(str(average_time)+"\n")

    
if __name__ == "__main__":
	main(sys.argv[1:])

