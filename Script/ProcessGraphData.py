import getopt
import psycopg2
import os
import sys




def Preprocessing():
    global relations
    global primary_relations
    idx = 0
    count = 0
    nodes = {}
    relations = ["NODE", "EDGE"]
    primary_relations = ["NODE"]



    output_file_path = '../Temp/'+database_name+".csv"

    input_file = open(input_file_path, 'r')
    output_file = open(output_file_path, 'w')

    for line in input_file.readlines():
        temp_line = line.split()
        if temp_line[0] not in nodes:
            nodes[temp_line[0]] = idx
            temp_line[0] = str(nodes[temp_line[0]])
            idx+=1
            count +=1
            if temp_line[1] not in nodes:
                nodes[temp_line[1]] = idx
                temp_line[1] = str(nodes[temp_line[1]])
                idx +=1
                count+=1
            else:
                temp_line[1] = str(nodes[temp_line[1]])
        elif temp_line[1] not in nodes:
            temp_line[0] = str(nodes[temp_line[0]])
            nodes[temp_line[1]] = idx
            temp_line[1] = str(nodes[temp_line[1]])
            idx +=1
            count+=1
        elif (temp_line[0] in nodes) and (temp_line[1] in nodes):
            temp_line[0] = str(nodes[temp_line[0]])
            temp_line[1] = str(nodes[temp_line[1]])

        splited_string = ""
        for i in range(len(temp_line)):
            splited_string += temp_line[i] + "|"
        splited_string = splited_string[:-1]

        output_file.write(splited_string)
        output_file.write('\n')

    output_file.close()
    input_file.close()    

    output_file_path = '../Temp/nodes.csv'

    output_file = open(output_file_path, 'w')

    for i in range(count):
        output_file.write(str(i) + "\n")
    output_file.close()

def CreateTables():
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    code = "CREATE TABLE NODE (ID INTEGER NOT NULL);"
    cur.execute(code)
    code = "CREATE TABLE EDGE (FROM_ID INTEGER NOT NULL, TO_ID INTEGER NOT NULL, DATE DATE NOT NULL);"
    cur.execute(code)

    con.commit()
    con.close()

def CopyTables():
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()

    edge_path = '../Temp/'+database_name+".csv"
    element_file = open(edge_path, 'r')
    cur.copy_from(element_file, "edge", sep='|')


    node_path = '../Temp/nodes.csv'

    ids_file = open(node_path, 'r')
    cur.copy_from(ids_file, "node", sep='|')

    os.remove(edge_path)
    os.remove(node_path)

    con.commit()
    con.close()



def AddKeys():
    con = psycopg2.connect(database=database_name)

    cur = con.cursor()

    code = "ALTER TABLE NODE ADD PRIMARY KEY (ID);"
    cur.execute(code)
    code = "COMMIT WORK;"
    cur.execute(code)
    code = "ALTER TABLE EDGE ADD FOREIGN KEY (FROM_ID) references NODE;"
    cur.execute(code)
    code = "ALTER TABLE EDGE ADD FOREIGN KEY (TO_ID) references NODE;"
    cur.execute(code)
    code = "COMMIT WORK;"
    cur.execute(code)

    con.commit()
    con.close()




def DropTables():
    global database_name
    global relations
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    code = "DROP TABLE EDGE;"
    cur.execute(code)
    code = "DROP TABLE NODE;"
    cur.execute(code)
    con.commit()
    con.close()




def main(argv):
    #The input file including the relationships between aggregations and base tuples
    global input_file_path
    input_file_path = ""
    #Privacy budget
    global database_name
    database_name = ""
    data_file = ""
    model =0
    
    try:
        opts, args = getopt.getopt(argv,"d:D:m:h:",["data_file=", "database=", "model=", "help="])
    except getopt.GetoptError:
        print("ProcessGraphData.py -d <data file name> -D<database name> -m <model:0(import)/1(clean)>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("ProcessGraphData.py -d <data file name> -D<database name> -m <model:0(import)/1(clean)>")
            sys.exit()
        elif opt in ("-d", "--data_file"):
            data_file = str(arg)
        elif opt in ("-D", "--Database"):
            database_name = str(arg)
        elif opt in ("-m","--model"):
            model = int(arg)


    if model != 0:
        DropTables()
    else:
        input_file_path = "../Data/Graph/" + data_file +".tsv"

        Preprocessing()
        CreateTables()
        CopyTables()
        AddKeys()


if __name__ == '__main__':
	main(sys.argv[1:])


