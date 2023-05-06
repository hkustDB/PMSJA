import getopt
import psycopg2
import sys
import time
import os
import math

def main(argv):

    query_path = ""
    database_name = ""
    result_place = 0


    try:
        opts, args = getopt.getopt(argv,"h:D:Q:P:",["Database=","QueryPath=","Result_place="])
    except getopt.GetoptError:
        print("CollectQueryTime.py -D <database name> -Q <query file path> -P <Result_place> ")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("CollectQueryTime.py -D <database name> -Q <query file path> -P <Result_place>")
            sys.exit()
        elif opt in ("-D", "--Database"):
            database_name = arg
        elif opt in ("-Q","--QueryPath"):
            query_path = arg
        elif opt in ("-P","--Result_place"):
            result_place = int(arg)



    repeat_time = 10
    query = ""
    query_file = open(query_path,'r')
    # Read the query file and store in query
    for line in query_file.readlines():
        query = query + line


    times = []

    for i in range(repeat_time):
        start = time.time()
        con = psycopg2.connect(database=database_name)
        cur = con.cursor()
        # Run the query and get the results
        cur.execute(query)
        end = time.time()
        times.append(end-start)
        if i==9:
            res = cur.fetchall()

            total_L2 = 0
            for j in range(len(res)):
                total_L2+=(int(res[j][result_place]))**2
            total_L2 = math.sqrt(total_L2)
            print("Total L2 norm is "+ str(total_L2))
            print("nume_group is "+str(len(res)))
            

        
        
        
    average_time = sum(times)/repeat_time
    print("Average time is \n")
    print(average_time)

    
if __name__ == "__main__":
	main(sys.argv[1:])


