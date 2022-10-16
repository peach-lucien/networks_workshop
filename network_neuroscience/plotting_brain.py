import meshio # '4.0.16'
import pandas as pd
import numpy as np

import plotly.graph_objs as go # version 4.6.0 
from plotly.offline import iplot

def openatlas(path_pos):   
    positions = pd.read_csv(path_pos,header=None, delim_whitespace=True)    
    data = [list(row.values) for _, row in positions.iterrows()]  
    return data

def shell_brain(brain_mesh):
    vertices = brain_mesh.points
    triangles = brain_mesh.cells[0][1]
    x, y, z = vertices.T
    I, J, K = triangles.T
    
    #showlegend=True gives the option to uncover the shell
    mesh = go.Mesh3d(x=x, y=y, z=z, color='grey', i=I, j=J, k=K, opacity=0.1,
                     hoverinfo=None,showlegend = True, name ='Brain Shell'  #colorscale=pl_mygrey, #intensity=z,
                     #flatshading=True, #showscale=False
                     )
    return mesh 


def plot_brain_network(G, path_pos, path_brainobj, node_size=None, node_color=None):

    # extracting brain mesh for better visualisation
    brain_mesh =  meshio.read(path_brainobj) 
    brain_trace = shell_brain(brain_mesh)
    
    scale = 0.2 # for normalising node size

    # if node size isn't provided, then use the weighted node degree
    if not node_size:
        node_size = [scale *i[1] for i in G.degree(weight='weight')]
        node_size  = np.array(node_size ) + 1

    if not node_color:
        node_color = np.copy(node_size)

    # creates a dictionary with the positions in 3D of the nodes 
    data = openatlas(path_pos)

    # getting 3d coordinates of nodes
    x = []
    y = []
    z = []
    pos3d = {}
    for i in range(0, len(data)):
        pos3d[i] = (data[i][0], data[i][1], data[i][2])
        x.append(data[i][0])
        y.append(data[i][1])
        z.append(data[i][2])

    # defining trace for nodes
    trace_nodes = go.Scatter3d(x=x, y=y, z=z, mode='markers',
               marker=dict(sizemode='diameter', symbol='circle', showscale=True, 
                           colorbar=dict(thickness=30, x=0.95,
                                         len=0.8, tickmode='linear', 
                                         tick0=0, dtick=1), opacity=0.85, 
                                         size=10*node_size, color=node_color, 
                                         cauto=True), hoverinfo='skip', 
               showlegend=False)  

    # defining 3d coordinates for each edges
    Xed = []
    Yed = []
    Zed = []
    for edge in G.edges():
        Xed += [pos3d[edge[0]][0],pos3d[edge[1]][0], None]
        Yed += [pos3d[edge[0]][1],pos3d[edge[1]][1], None] 
        Zed += [pos3d[edge[0]][2],pos3d[edge[1]][2], None] 

    # defining trace for edges
    trace_edges = go.Scatter3d(x=Xed, y=Yed, z=Zed, mode='lines', 
                          line=dict(color='black', width=2), 
                          hoverinfo='none', showlegend=False, opacity=0.3)

    data= [brain_trace,trace_nodes,trace_edges,]
    fig = go.Figure(data=data)
    fig.update_layout(
        autosize=False,
        width=800,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, 
                   )
       )


    return iplot(fig), node_size 