import os
import getopt
import math
import sys
import random
import numpy as np
import time
import copy
import glob

def ReadInput():
    global items
    global result
    global num_query
    global norms
    global S
    global input_file_prefix
    
    input_file_names = glob.glob(input_file_prefix+"*")
    num_query = len(input_file_names)
    items = []
    dic = {}
    result = []
    values = [[] for i in range(num_query)]   
    connections = [[] for i in range(num_query)]

    idx = 0
    i= 0
    for input_file_name in input_file_names:
        #For each query
        input_file = open(input_file_name,'r')

        for line in input_file.readlines():
            elements = line.split()

            values[i].append(float(elements[0]))

            if elements[1] not in dic:
                dic[elements[1]] = idx
                elements[1] = dic[elements[1]]
                items.append(elements[1])
                idx +=1
            else :
                elements[1] = dic[elements[1]]

            connections[i].append(elements[1])

        result.append(sum(values[i]))
        i+=1
        input_file.close()

    N = len(items)
    S = np.zeros((N, num_query))

    for k in range(num_query):
        for j in range(len(connections[k])):
            idx = connections[k][j]
            S[idx,k]+=values[k][j]


    norms = []
    for i in range(N):
        norms.append(math.sqrt(sum(S[i, : ]**2)))
        
        
def count(threshold):
    count = 0
    for i in range(len(items)):
        if norms[i]<=threshold:
            count+=1
    
    return count


def RunAlgorithm():
    global GS
    global rho
    global beta
    
    N = len(items)
    GS = math.sqrt(num_query)*GS #u
    
    rho1 = rho/2  #for quantile
    rho2 = rho/2  #for result noise
    m1 = N - math.sqrt(2*num_query/rho2)
    m2 = N- 2*math.sqrt(math.log(GS,  2)*math.log(math.log(GS, 2)/beta)/rho1)
    m = min(m1,m2)
    m = max(m,1)
    noise_scale = math.sqrt(math.log(GS, 2)/(2*rho1)) #for rank estimation
    
    #fisrt select quantile
    right = GS
    left = 0
    while left<right:
        mid = (left+right)/2
        c = count(mid) + np.random.normal(0, noise_scale)
        if c<m:
            left = mid +1
        else:
            right = mid
            
            
    tau = (left+right)/2

    #calculate truncated Q
    Q = np.zeros(num_query)
    for i in range(N):
        if norms[i]>tau:
            Q += tau*S[i]/norms[i]
        else:
            Q +=S[i]
            

    Q_hat = Q+ np.random.normal(0, math.sqrt(2*tau**2/rho2), num_query)
    
    return Q_hat
   
    
def main(argv):
    #The input file including the relationships between aggregations and base tuples
    global input_file_prefix
    input_file_prefix = ""
    #Privacy budget
    global rho
    global epsilon
    global delta
    #Error probablity: with probablity at least 1-beta, the error can be bounded
    global beta
    beta = 0.1
    global num_query
    global GS

    try:
        opts, args = getopt.getopt(argv,"h:I:e:d:G:b:",["Input=","epsilon=","delta=","Global_sensitivity=","beta="])
    except getopt.GetoptError:
        print("OptMean.py -I <input file> -e <epsilon> -b <beta(default 0.1)> -d <desired delta> -G <Global sensitivity bound> ")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("OptMean.py -I <input file> -e <epsilon> -b <beta(default 0.1)> -d <desired delta> -G <Global sensitivity bound>")
            sys.exit()
        elif opt in ("-I", "--Input"):
            input_file_prefix = str(arg)
        elif opt in ("-e","--epsilon"):
            epsilon = float(arg)
        elif opt in ("-G","--Global_sensitivity"):
            GS = float(arg)
        elif opt in ("-b","--beta"):
            beta = float(arg)
        elif opt in ("-d","--delta"):
            delta = float(arg)

    start = time.time()
    ReadInput()
    x = math.sqrt(2*math.log(1/delta)+2*epsilon) - math.sqrt(2*math.log(1/delta))
    rho = x**2/2
    Q = RunAlgorithm()
    end= time.time()
    print("Query Result")
    print(result)
    print("Noised Result")
    print(Q)
    abs_error = []
    error_rate = []
    total_error = 0.0
    for i in range(num_query):
        total_error+=abs(Q[i]-result[i])**2
        abs_error.append(abs(Q[i]-result[i]))
        error_rate.append(abs(Q[i]-result[i])/result[i])
    total_error = np.sqrt(total_error)

    print("Time")
    print(end-start)


if __name__ == '__main__':
	main(sys.argv[1:])
