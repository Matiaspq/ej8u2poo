class Conjunto:
    def __init__(self,conjunto):
        self.__elementos=conjunto

    def __str__(self):
        return f"{self.__elementos}"
    
    def union(self,otro):
        union=[]
        for elemento in self.__elementos:
            union.append(elemento)
        for elemento in otro.__elementos:
            if elemento not in union:
                union.append(elemento)
        return union

    def __add__(self,otro):
        return self.union(otro)
    
    def diferencia(self, otro):
        diferencia=[]
        for elemento in self.__elementos:
            if elemento not in otro.__elementos:
                diferencia.append(elemento)
        return diferencia

    def __sub__(self,otro):
        return self.diferencia(otro)
    
    def iguales(self,otro):
        igual=True
        if len(self.__elementos)==len(otro.__elementos):
            i=0
            while i<len(self.__elementos) and igual==True:
                if self.__elementos[i] not in otro.__elementos:
                    igual=False
                i+=1
        return igual
                
    def __eq__(self,otro):
        return self.iguales(otro)