import getopt
import psycopg2
import sys
import time

def ReadQuery():
    global query
    global query_path
    query = ""
    query_file = open(query_path,'r')
    # Read the query file and store in query
    for line in query_file.readlines():
        query = query + line
        if ";" in query:
            query = query.replace('\n'," ")
            query = " "+query
            break

def ReadPrimaryKey():
    global primary_key_list
    global primary_key_path
    # Read and store the primary key(s) of the private relation
    key_list_file = open(primary_key_path,'r')
    line = key_list_file.readline()
    primary_key_list = line.split()
    
def ReadGroups():
    global query
    global group_ids
    global group_concat_attr
    query_t = query
    query_t = query_t.replace(";","")
    query_t = query_t.replace(" by "," ")
    query_t = query_t.replace(" group ","\n")
    group_attributes = query_t.split("\n")
    group_attributes = group_attributes[1]
    group_attributes = group_attributes.replace(",","\n")
    group_attributes = group_attributes.split("\n")
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    # Construct a new query
    query_t = query
    query_t = query_t.replace(" from ","\n")
    query_t = query_t.split("\n")
    query_t = query_t[1]
    group_concat_attr = "concat("
    first_group = True
    for group_attribute in group_attributes:
        if first_group:
            first_group = False
            group_concat_attr = group_concat_attr + group_attribute
        else:
            group_concat_attr = group_concat_attr + ",\'||\',"+group_attribute
    group_concat_attr = group_concat_attr+")"
    new_query = "select "+group_concat_attr+", count(*) from "+query_t
    # Run the query and get the results
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    cur.execute(new_query)
    res = cur.fetchall()
    group_ids = {}
    group_id = 0
    for each_res in res:
        group_ids[each_res[0]] = group_id
        group_id +=1
    con.commit()
    con.close()

def RewriteQuery():
    global query
    global private_relation_name
    global rewrite_query
    global primary_key_list
    global renaming_private_relations
    global group_concat_attr
    
    # Split the query into select, from and where clauses
    parser_string = query
    parser_string = parser_string.replace(" select ", "")
    parser_string = parser_string.replace(" from ", "\n")
    parser_string = parser_string.replace(" where ", "\n")
    parser_string = parser_string.replace(" by ", " ")
    parser_string = parser_string.replace(" group ", "\n")
    parser_string = parser_string.replace(";", "")
    parser_strings = parser_string.split("\n")
    select_strings = parser_strings[0]
    from_strings = parser_strings[1]
    where_strings = parser_strings[2]
    
    # Split the select attributes
    select_strings = select_strings.replace(",", "\n")
    select_strings = select_strings.split("\n")

    # Split the relations
    relations_strings = from_strings.replace(",", "\n")
    relations_strings = relations_strings.split("\n")

    # Renaming_private_relations stores all the relations that are private
    renaming_private_relations = []

    # Go through the relations in the from clause
    for relations_string in relations_strings:
        relations_string = relations_string.split()
        origin_relation = relations_string[0]
        # Case 1: there is a renaming, xxx as xxx
        if len(relations_string) > 1:
            renaming_relation = relations_string[2]
        # Case 2: there is no renaming
        else:
            renaming_relation = relations_string[0]
        # Append the private relations to the list
        if origin_relation == private_relation_name:
            renaming_private_relations.append(renaming_relation)

    # Rewrite the query
    rewrite_query = "select " + group_concat_attr+", "
    aggre_function = ""
    for select_word in select_strings:
        # Case 1: aggregation query
        if "sum(" in select_word:
            aggre_function = select_word
            if " as " in select_word:
                aggre_function = select_word.replace(" as ", "\n").split("\n")[0]
            rewrite_query = rewrite_query + aggre_function[aggre_function.find('(') + 1 : aggre_function.rfind(')')] + ", "
        # Case 2: counting query
        if "count(" in select_word: 
            rewrite_query = rewrite_query + "1, "

    # Go through all the private relations
    for i in range(len(renaming_private_relations)):
        concat_attr = ""
        # Concatenate all the private key(s) as the attribbute
        for j in range(len(primary_key_list)):
            if j == 0:
                concat_attr = "concat(" + renaming_private_relations[i] + "." + primary_key_list[j] + ",\',\')"
            else:
                concat_attr = concat_attr + "||concat(" + renaming_private_relations[i] + "." + primary_key_list[j] + ",\',\')"
        concat_attr = concat_attr + " as id" + str(i)
        # Add the private relation to select clause
        if i == 0:
            rewrite_query = rewrite_query + concat_attr
        else:
            rewrite_query = rewrite_query + ", " + concat_attr
    rewrite_query = rewrite_query + " from " + from_strings + " where " + where_strings+";"

def ExtractRelationship():
    global database_name
    global rewrite_query
    global output_file_prefix
    global renaming_private_relations
    global group_ids
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    # Run the query and get the results
    cur.execute(rewrite_query)
    res = cur.fetchall()
    id_dic = {}
    results = []
    for i in range(len(group_ids)):
        results.append(open(output_file_prefix+"_"+str(i)+".txt", 'w'))
    num_id = 0
    # Go through the results
    for i in range(len(res)):
        temp_res = res[i]
        group_id = group_ids[temp_res[0]]
        # Write the count/aggregation result
        results[group_id].write(str(temp_res[1]) + " ")
        # Write the private relations in the result
        for j in range(2, len(renaming_private_relations) + 2):
            temp_id = temp_res[j]
            # Reordering the private relations
            if temp_id in id_dic:
                results[group_id].write(str(id_dic[temp_id]) + " ")
            else:
                id_dic[temp_id] = num_id
                results[group_id].write(str(num_id) + " ")
                num_id += 1
        results[group_id].write("\n")
    con.commit()
    con.close()

def main(argv):
    # Name of the database to be queried
    global database_name
    # Path of the txt file storing the query
    global query_path
    # Name of the private relation
    global private_relation_name
    # Path of the txt file storing the primary key(s) of the private relation
    global primary_key_path
    # Path of the output file of the query results
    global output_file_prefix
    global group_ids

    try:
        opts, args = getopt.getopt(argv,"h:D:Q:P:K:O:",["Database=","QueryPath=","PrivateRelationName=","PrimaryKey=","OutputPrefix="])
    except getopt.GetoptError:
        print("ExtractInfoMultiple.py -D <database name> -Q <query file path> -P <private relation name> -K <primary key of private relation> -O <output file prefix>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("ExtractInfoMultiple.py -D <database name> -Q <query file path> -P <private relation name> -K <primary key of private relation> -O <output file prefix>")
            sys.exit()
        elif opt in ("-D", "--Database"):
            database_name = arg
        elif opt in ("-Q","--QueryPath"):
            query_path = arg
        elif opt in ("-P","--PrivateRelationName"):
            private_relation_name = arg
        elif opt in ("-K","--PrimaryKey"):
            primary_key_path=arg
        elif opt in ("-O","--Output"):
            output_file_prefix=arg
    start = time.time()
    ReadQuery()
    ReadPrimaryKey()
    ReadGroups()
    RewriteQuery()
    ExtractRelationship()
    end= time.time()
    print("Group number")
    print(len(group_ids))
    print("Time")
    print(end-start)
    
if __name__ == "__main__":
   main(sys.argv[1:])
