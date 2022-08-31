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

def printgraph(x_coordinates,y_coordinates,edgee,mst):
    damn=nx.DiGraph()
    for i in range (len(x_coordinates)):
        damn.add_node(str(i)+'/'+str(mst[i]),pos=(x_coordinates[i],y_coordinates[i]))

    pos=nx.get_node_attributes(damn,'pos')
    for i in range (len(edgee)):
        damn.add_edge(str(edgee[i][0])+'/'+str(mst[edgee[i][0]]),str(edgee[i][1])+'/'+str(mst[edgee[i][1]]),weight=edgee[i][2])
    # damn.add_weighted_edges_from(edgee)
    nx.draw(damn,pos,with_labels=True)
    lab=nx.get_edge_attributes(damn,'weight')
    nx.draw_networkx_edge_labels(damn,pos,edge_labels=lab)
    plt.show()

def inputfromfile(filename):
    f=open(filename,'r')
    temp,dat,ll,count,tempcount,flag,node,x_coordinates,y_coordinates,i,edgee=([],0,0,0,0,1,[],[],[],0,[])
    while 1:
        lines = f.read(1)
        if lines >='A' and lines<='Z':
            continue
        if lines.isspace():
            if count>0:
                lin1=''.join(temp)
                lin=int(lin1)
                count=0
                temp.clear()
                break
        else:
            temp.append(lines)
            count+=1
    no_of_nodes=int(lin)
    lin*=3
    while 1:
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
        if len(linee)==1:
           dat=int(linee[0])
        val=int(float(len(linee)-1)/4.0)
        for n in range(val):
            edgee.append([int(linee[0]),int(linee[1+n*(4)]),float(linee[3+n*4])/10000000])
    f.close()
    return no_of_nodes,x_coordinates,y_coordinates,edgee,dat

def AdjacenyMatrix(weights,nodes,start,keep_multiple=False):
    matrix=[[0 for _ in range(nodes)] for _ in range(nodes)]
    for weight in weights:
        if matrix[weight[0]][weight[1]]<weight[2] or matrix[weight[1]][weight[0]]<weight[2]:
            matrix[weight[0]][weight[1]]=weight[2]
            matrix[weight[1]][weight[0]]=weight[2]   
    return matrix

def findmin(set, visited):
        min = 9999
        for v in range(len(set)):
            if set[v] < min and visited[v] ==False:
                min = set[v]
                min_index = v
        return min_index
def DajistraAlgorithm(matrix,V,start,x_coordinates,y_coordinates):
    graph=[]
    key = [0 for _ in range(V)]
    visited = [0 for _ in range(V)]
    for play in range(len(key)):
        key[play]=99999
        visited[play]=False
    parent=[]
    for i in range(V):
        parent.append(0)
    key[start]=0
    for ll in range(V):
            i=findmin(key,visited)
            visited[i]=True;
            for j in range(V):
                if (matrix[i][j]):        # idf there is an edge
                    if key[j] > (matrix[i][j]+key[i]):
                        key[j] = matrix[i][j]+key[i]
                        parent[j]=i
    for i in range(len(parent)): 
        if i !=start:
            graph.append([parent[i],i,matrix[parent[i]][i]])  
    printgraph(x_coordinates,y_coordinates,graph,key)
def dijkstra(filename):
    node,x_coordinates,y_coordinates,edgee,startnode=inputfromfile(filename)
    edgee=minimize(edgee)
    matrix=AdjacenyMatrix(edgee,node,1)
    DajistraAlgorithm(matrix,node,startnode,x_coordinates,y_coordinates)