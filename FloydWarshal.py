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

def printgraphforfloyd(x,y,edgee,start):
    damn=nx.Graph()
    for i in range (len(x)):
        damn.add_node(str(i)+'/',pos=(x[i],y[i]))

    pos=nx.get_node_attributes(damn,'pos')
    for i in range (len(edgee)):
        damn.add_edge(str(edgee[i][0])+'/',str(edgee[i][1])+'/',weight=edgee[i][2])
    # damn.add_weighted_edges_from(edgee)
    colors=[]
    for i in range(len(damn.nodes())):
        if i==start:
            colors.append("blue")
        else:
            colors.append("red")
    colors1=[]
    for i in range(len(damn.edges())):
        if edgee[i][0]==start:
            colors1.append("blue")
        else:
            colors1.append("red")
    nx.draw(damn,pos,node_color= colors,edge_color=colors1,with_labels=True)
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
    matrix=[[999 for _ in range(nodes)] for _ in range(nodes)]
    for weight in weights:
        if matrix[weight[0]][weight[1]]>weight[2] or matrix[weight[1]][weight[0]]>weight[2]:
            matrix[weight[0]][weight[1]]=weight[2]
            matrix[weight[1]][weight[0]]=weight[2]    
    return matrix

def floyd(matrix,V,x,y):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if i!=j and i!=k and j!=k:
                    matrix[j][k]=max(matrix[j][k],matrix[j][i]+matrix[i][k])
    gg=[]
    for i in range(len(matrix)):                      
        for j in range(len(matrix)):
            gg.append([i,j,matrix[i][j]])
        printgraphforfloyd(x,y,gg,i)
        gg.clear()
def floydwarshal(filename):
    node,x,y,edgee,startnode=inputfromfile(filename)
    edgee=minimize(edgee)
    matrix=AdjacenyMatrix(edgee,node,1)
    floyd(matrix,node,x,y)
