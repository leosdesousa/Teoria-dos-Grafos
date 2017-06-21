'''
def exibenome(x,x1):
    resultadp=0
    if x1>0:
        resultadp = x+exibenome(x,x1-1)
    return resultadp

print(exibenome(x,x1))

'''

lista=[[1,2,3],[4,5,6]]


def percore(lista,x):
    resu=[]
    if (x>=0):
        print(lista[x])
        resu=percore(lista[x],len(lista)-1)
    return resu

print(percore(lista,len(lista)-1))