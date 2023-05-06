import sys
import os
import time



def main(argv):
    queries = ["Q3", "Q7"]
    scales = ["0","1","2","3","4","5","6"]
    repeat_time = 10

    output_file = open( "../Result/TPCH/Scale_Times.txt", 'w')
    for query in queries:
        for scale in scales:
            output_file.write(query+"_Scale"+scale+" times: \n")
            times = []
            for i in range(repeat_time):
                start = time.time()
                if query=="Q3":
                    cmd = "../../python ../Code/ExtractInfoMultiple.py -D sc"+scale+" -Q ../Query/"+query+".txt -P ids -K ../Query/"+query+"_key.txt -O ../Information/"+query+"_"+scale
                else:
                    cmd = "../../python ../Code/ExtractInfoMultiple.py -D psc"+scale+" -Q ../Query/"+query+".txt -P ids -K ../Query/"+query+"_key.txt -O ../Information/"+query+"_"+scale

                
                shell = os.popen(cmd, 'r')
                shell.read()
                shell.close()
                end= time.time()
                time_used = end-start
                output_file.write("The time for the "+str(i)+"th execution is"+"\n")
                output_file.write(str(time_used)+"\n")
                times.append(time_used)
            average_time = sum(times)/repeat_time
            output_file.write("Average time for "+query+"_Scale"+scale+" is \n")
            output_file.write(str(average_time)+"\n")

    
if __name__ == "__main__":
	main(sys.argv[1:])

