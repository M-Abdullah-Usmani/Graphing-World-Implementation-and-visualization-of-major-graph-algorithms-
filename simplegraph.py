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

def AdjacenyMatrix(weights,nodes,keep_multiple=False):
    matrix=[[0 for _ in range(nodes)] for _ in range(nodes)]
    for weight in weights:
        if matrix[weight[0]][weight[1]]<weight[2] or matrix[weight[1]][weight[0]]<weight[2]:
            matrix[weight[0]][weight[1]]=weight[2]
            matrix[weight[1]][weight[0]]=weight[2]
    
    return matrix



def simpleg(filename):
    x_coordinates,y_coordinates,edgee,startnode=inputfromfile(filename)
    edgee=minimize(edgee)
    printgraph(x_coordinates,y_coordinates,edgee)