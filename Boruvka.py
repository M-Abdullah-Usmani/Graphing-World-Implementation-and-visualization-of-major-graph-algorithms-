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
    
def findmin(set, visited):
        min = 9999
        for v in range(len(set)):
            if set[v] < min and visited[v] ==False:
                min = set[v]
                min_index = v
        return min_index
def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])
def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
  
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
  
def boruvkaMST(V,graph,x,y):
        parent = []; rank = []; 
  
        cheapest =[]
  
        numTrees = V
        MSTweight = 0
  
        for node in range(V):
            parent.append(node)
            rank.append(0)
            cheapest =[-1] * V

        mst = []
  
        while numTrees > 1:
            for edge in range(len(graph)):
                u,v,w =  graph[edge][0], graph[edge][1], graph[edge][2]
                set1 = find(parent, u)
                set2 = find(parent ,v)
                if set1 != set2:     
                      
                    if cheapest[set1] == -1 or cheapest[set1][2] < w :
                        cheapest[set1] = [u,v,w] 
  
                    if cheapest[set2] == -1 or cheapest[set2][2] < w :
                        cheapest[set2] = [u,v,w]
              
            for node in range(V):
                if cheapest[node] != -1:
                    u,v,w = cheapest[node]
                    set1 = find(parent, u)
                    set2 = find(parent ,v)
  
                    if set1 != set2 :
                        MSTweight += w
                        union(parent, rank, set1, set2)
                        mst.append([u,v,w])
                        numTrees = numTrees - 1
              
            cheapest =[-1] * V
  
        printgraph(x,y,mst)


def boruvka(filename):
    node,x,y,edgee,startnode=inputfromfile(filename)
    edgee=minimize(edgee)
    boruvkaMST(int(node),edgee,x,y)