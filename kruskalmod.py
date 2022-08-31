import networkx as nx
import matplotlib.pyplot as plt

def minimize(edge):   #If there are multiple edges between 2 vertices then select one with max bandwidth
    for n in range(len(edge)-1):
        for n1 in range(n+1,len(edge)-1):
            if n1<=(len(edge)-1) and n<=(len(edge)-1):
                if edge[n][0]==edge[n1][0] and edge[n][1]==edge[n1][1]:  
                    if edge[n][2]>edge[n1][2]:      #For edges between 2 vertices.If first edge is greater 
                        edge.pop(n1)                #pop second(smaller) edge
                    else:                           #For edges between 2 vertices.If second edge is greater 
                        edge.pop(n)                 #pop first(smaller) edge
                        n1=n
    return edge

def printgraph(x_coordinates,y_coordinates,edgee):
    damn=nx.Graph()                     #initialize a graph
    for i in range (len(x_coordinates)):
        damn.add_node(i,pos=(x_coordinates[i],y_coordinates[i]))    #add vertices
    pos=nx.get_node_attributes(damn,'pos')
    damn.add_weighted_edges_from(edgee)         #add edges between vertices
    nx.draw(damn,pos,with_labels=True)          #print vertices
    lab=nx.get_edge_attributes(damn,'weight')
    nx.draw_networkx_edge_labels(damn,pos,edge_labels=lab)  #print edges
    plt.show()              #show graph

def inputfromfile(filename):            
    f=open(filename,'r')            #open input file
    temp,Startingnode,ll,count,tempcount,flag,node,x_coordinates,y_coordinates,i,edgee=([],' ',0,0,0,1,[],[],[],0,[])
    while 1:
        lines = f.read(1)
        if lines >='A' and lines<='Z':
            continue
        if lines.isspace():
            if count>0:     #to see if number of inputs has been read from file
                lin1=''.join(temp)
                lin=int(lin1)
                count=0
                temp.clear()
                break
        else:
            temp.append(lines)
            count+=1
    lin*=3
    while 1:                #To read vertices and their (x_coordinates,y_coordinates) coordinates
        lines =f.read(1)
        temp.append(lines)
        count+=1
        if lines.isspace():
            temp.pop()
            count-=1
            if count >0:
                ll=''.join(temp)
                ll=float(ll)
                if flag==1:
                    node.append(ll)
                elif flag==2:
                    x_coordinates.append(ll)
                else:
                    y_coordinates.append(ll)
                    i+=1
                    flag=0
                flag+=1
                temp.clear()
                count=0
                if tempcount == lin-1:
                    break
                else:
                    tempcount+=1
    next(f)
    for lines  in f.readlines():
        linee=lines.split()
        if len(linee)==1:                   # To see if starting node had been read from file
           Startingnode=linee
        val=int(float(len(linee)-1)/4.0)
        for n in range(val):
            edgee.append([int(linee[0]),int(linee[1+n*(4)]),float(linee[3+n*4])/10000000])
    f.close()
    return x_coordinates,y_coordinates,edgee,Startingnode


def find_set_of_particular_node(set, curr_node):
        return set[curr_node]

def union_of_sets( sets, size_of_sets, u, v):
        first_node_set =sets[u]
        #  find_set_of_particular_node(sets, first_node)
        second_node_set = sets[v]       
         # find_set_of_particular_node(sets, second_node)
        if size_of_sets[first_node_set] < size_of_sets[second_node_set]:
            for n in range(len(sets)):
                if sets[n]==sets[u] and n!=u:
                    sets[n]=sets[v]
            sets[u]=sets[v]
            size_of_sets[second_node_set] += 1
        elif size_of_sets[first_node_set] > size_of_sets[second_node_set]:
            for n in range(len(sets)):
                if sets[n]==sets[v] and n!=v:
                    sets[n]=sets[u]
            sets[v]=sets[u]
            size_of_sets[first_node_set] += 1
        else:
            for n in range(len(sets)):
                if sets[n]==sets[v] and n!=v:
                    sets[n]=sets[u]
            sets[v]=sets[u]
            size_of_sets[first_node_set] += 1

    #  Applying Kruskal algorithm
def kruskal_algo(edges,no_of_nodes,x_coordinates,y_coordinates):
        result = []
        i, e = 0, 0
        graph = sorted(edges, key=lambda item: item[2],reverse=True)
        sets = []
        size_of_sets = []
        for node in range(no_of_nodes):
            sets.append(node)
            size_of_sets.append(0)
        while e < no_of_nodes - 1:
            u, v, w = graph[i]
            i = i + 1
            first_node = find_set_of_particular_node(sets, u)
            second_node = find_set_of_particular_node(sets, v)
            if first_node != second_node:
                e = e + 1
                result.append([u, v, w])
                union_of_sets(sets, size_of_sets, u, v)
        printgraph(x_coordinates,y_coordinates,result)
def kruskal(filename):
    x_coordinates,y_coordinates,edgee,startnode=inputfromfile(filename)
    edgee=minimize(edgee)
    kruskal_algo(edgee,len(x_coordinates),x_coordinates,y_coordinates)