# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:41:11 2024

@author: ahino
"""

def lee_vector(n):  # No se indican tipos en los parÃ¡metros
    a = []
    if n>0:
        cadenaEntrada = input()
        for i in range(0, n): 
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)
            
    return a  

def imprime_vector(a):
    n = len(a)
    if n==0:
        pass   # No hacer nada. Salir del if/funciÃ³n
    elif n==1:
        print("{:.4f}".format(a[0]))  # print(a)
    else:
        print("{:.4f}".format(a[0]),end=' ')   # imprime el primer elemento y un espacio
        imprime_vector(a[1:])  # imprime el resto de la lista (sin el primer elemento)   


def producto_matriz_vector(A,x):
    if len(A[0])!=len(x):#que las dimensiones del vector y la matriz sean compatibles
        return -1
    resultado=[0]*len(A)
    
    for i in range(len(A)):
        for j in range(len(x)):
            resultado[i]+=A[i][j] * x[j]
            
    return resultado


def traspuesta_matriz(A):
    #inicializar la matriz
    traspuesta=[[] for _ in range(len(A[0]))]
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            traspuesta[j].append(A[i][j])
    
    return traspuesta

def calcular_gradiente(A,x,b):
    #g<-2A^T Ax -2A^Tb
    g=producto_matriz_vector(traspuesta_matriz(A),producto_matriz_vector(A, x))  
    g=[2 * elemento for elemento in g] #multiplica cada elemento del vector por 2
    
    for i in range(len(g)):
        g[i]-= 2* producto_matriz_vector(traspuesta_matriz(A),b)[i]
        
    return g

def descensoGradiente(A,b,x0,alpha, epsilon):
    x=x0 #aproximacion lineal de un vector
    
    g=calcular_gradiente(A,x,b)#gradiente en x
    
    while max(abs(elemento) for elemento in g)>= epsilon:#Iterar hasta que modulo del gradiente sea muy pequeño
        x=[x[i] - alpha * g[i] for i in range (len(x))]#Actualizar aproximacion en direccion opuesta al gradiente
        
        g=calcular_gradiente(A,x,b)#actualizar gradiente
        
    return x
    
n,m = map(int,input().split())#lee el numero de ecuaciones y de incognitas (n filas con m enteros)
A=[lee_vector(m) for _ in range(n)]#lee la matriz A
b=lee_vector(n)    
x0=list(map(float,input().split()))
alpha=float(input())
epsilon=float(input())

x= descensoGradiente(A,b,x0,alpha,epsilon)
imprime_vector(x)