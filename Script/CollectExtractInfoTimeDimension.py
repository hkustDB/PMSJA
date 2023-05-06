import sys
import os
import time



def main(argv):
    queries = ["Q8"]
    repeat_time = 10

    output_file = open( "../Result/TPCH/Dimension_times.txt", 'w')
    for query in queries:
        output_file.write(query+" times: \n")
        times = []
        for i in range(repeat_time):
            start = time.time()
            cmd = "../../python ../Code/ExtractInfoMultiple.py -D pso4 -Q ../Query/Q8.txt -P ids -K ../Query/"+query+"_key.txt -O ../Information/"+query
            
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

