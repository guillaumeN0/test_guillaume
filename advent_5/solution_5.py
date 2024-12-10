import csv,re
import numpy as np


with open("input2.txt","r",encoding="utf-8") as f:
    reader=csv.reader(f,delimiter=',')
    lines_list=[row for row in reader]
    
instructions_list=[]
updates_list=[]
is_instruction=True
for line in lines_list:
    if len(line)==0 :
        is_instruction=False
    elif is_instruction:
        instructions_list.append(line[0].split('|'))
    else:
        updates_list.append(line)
    
'''middle_true=0
for update in updates_list:
    is_fine=True
    for rule in instructions_list:
        if rule[0] in update and rule[1] in update:
            index_0=update.index(rule[0])
            index_1=update.index(rule[1])
            if index_0 > index_1 :
                is_fine=False
                break
    if is_fine:
        middle_true+=int(update[len(update)//2 ])
        
        
print(middle_true)'''

def ordenar(vertices, reglas):
    n=len(vertices)
    grafo=np.zeros((n,n),dtype=int)
    for i in range(n):
        vertice=vertices[i]
        for regla in reglas:
            if vertice == regla[0]:
                segundo_vertice=regla[1]
                if segundo_vertice in vertices:
                    grafo[i,vertices.index(segundo_vertice)]=1
                    
    #print(grafo)
    grafo_completo=grafo.copy()
    visitados=np.zeros(n,dtype=int)
    def relation_ordre (ancestros_indices, actual_indice):
        #print('current summit',actual_indice)
        for j in range(n):
            if grafo[actual_indice,j]==1 and visitados[j]==0:
                visitados[j]=1
                ancestros_indices.append(actual_indice)
                relation_ordre(ancestros_indices,j)
                for i in ancestros_indices[:-1]:
                    grafo_completo[i,j]=1
                    
    def ordernación_recursiva(indices_vertices_actuales):
        if len(indices_vertices_actuales)==0:
            print('sortie vide',len(indices_vertices_actuales))
            return []
        separacion_max=-1
        indice_separacion_max=-1
        for i in indices_vertices_actuales:
            separacion=grafo_completo[i,indices_vertices_actuales].sum()
            +grafo_completo[indices_vertices_actuales,i].sum()
            if separacion > separacion_max:
                separacion_max=separacion
                indice_separacion_max=i
        indices_vertices_inferiores=[]
        indices_vertices_superiores=[]
        indices_vertices_no_relacionados=[]
        for i in indices_vertices_actuales:
            if grafo_completo[i,indice_separacion_max]==1:
                indices_vertices_inferiores.append(i)
            elif grafo_completo[indice_separacion_max,i]==1:
                indices_vertices_superiores.append(i)
            else:
                indices_vertices_no_relacionados.append(i)
         
        print(grafo_completo)   
        print('sortie divisée',indices_vertices_actuales,indices_vertices_inferiores,len(indices_vertices_superiores),len(indices_vertices_no_relacionados))
        return ordernación_recursiva(indices_vertices_inferiores) + [indice_separacion_max] + ordernación_recursiva(indices_vertices_superiores) + ordernación_recursiva(indices_vertices_no_relacionados)
                    
    relation_ordre([],0)
    print(grafo,'\n',grafo_completo)
    #indices_ordenados = ordernación_recursiva(range(n))
    return [vertices[i] for i in indices_ordenados]
    
    
#print(updates_list[0],instructions_list)
veritices_ordenados=ordenar(updates_list[0],instructions_list) 
print(veritices_ordenados)
    
        