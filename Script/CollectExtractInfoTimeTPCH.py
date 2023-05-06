import sys
import os
import time



def main(argv):
    queries = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"]
    scales = ["_4"]
    repeat_time = 10

    output_file = open( "../Result/TPCH/TPCH_Times.txt", 'w')
    for query in queries:
        for scale in scales:
            output_file.write(query+" times: \n")
            times = []
            for i in range(repeat_time):
                start = time.time()
                if query=="Q1" or query=="Q2":
                    cmd = "../../python ../Code/ExtractInfoMultiple.py -D sc4 -Q ../Query/"+query+".txt -P customer -K ../Query/"+query+"_key.txt -O ../Information/"+query+scale
                elif query=="Q6" or query=="Q7":
                    cmd = "../../python ../Code/ExtractInfoMultiple.py -D psc4 -Q ../Query/"+query+".txt -P ids -K ../Query/"+query+"_key.txt -O ../Information/"+query+scale
                elif query=="Q8":
                    cmd = "../../python ../Code/ExtractInfoMultiple.py -D pso4 -Q ../Query/Q8_100.txt -P ids -K ../Query/"+query+"_key.txt -O ../Information/"+query+scale
                else:
                    cmd = "../../python ../Code/ExtractInfoMultiple.py -D sc4 -Q ../Query/"+query+".txt -P ids -K ../Query/"+query+"_key.txt -O ../Information/"+query+scale
                
                shell = os.popen(cmd, 'r')
                shell.read()
                shell.close()
                end= time.time()
                time_used = end-start
                output_file.write("The time for the "+str(i)+"th execution is"+"\n")
                output_file.write(str(time_used)+"\n")
                times.append(time_used)
            average_time = sum(times)/repeat_time
            output_file.write("Average time for "+query+" is")
            output_file.write(str(average_time)+"\n")

    
if __name__ == "__main__":
	main(sys.argv[1:])

