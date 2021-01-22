# -*- coding: cp1252 -*-
#
# from:
# https://github.com/RodolfoFerro/ConvexHull/blob/master/JarvisMarch.py (12/2018)
#
# Anpassungen: fxs
# Berechnung konvexe Hülle mit numpy und matplotlib
#    pip install numpy
#    pip install matplotlib
# update 12.11.2020 fxs lüuft

import numpy as np
import matplotlib.pyplot as plt

# CCW # Function to know if we have a CCW turn (counter-clockwise)
def CCW(p1, p2, p3):
        if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
                return True
        return False

# Main Function:
def GiftWrapping(S):
        n = len(S)
        P = [None] * n
        l = np.where(S[:,0] == np.min(S[:,0]))
        pointOnHull = S[l[0][0]]
        i = 0
        while True:
                P[i] = pointOnHull
                endpoint = S[0]
                for j in range(1,n):
                        if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(S[j],P[i],endpoint):
                                endpoint = S[j]
                i = i + 1
                pointOnHull = endpoint
                if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
                        break

        for i in range(n):
                if P[-1] is None:
                        del P[-1]
        return np.array(P)

#Anzeige Eingabeaufforderung:
def main():
        try:
                N = int(sys.argv[1])
        except:
                N = int(input("Bitte die Anzahl Zufallspunkte eingeben:  \n N = "))
# By default we build a random set of N points with coordinates in [0,300)x[0,300):        
# Zuf�llige Punkte Werte zwischen 10 und 290
        P = np.array([(np.random.randint(10,290),np.random.randint(10,290)) for i in range(N)])
        L = GiftWrapping(P)
        
# Anzeige über matplotlib.pyplot
        fig = plt.figure()
        ax = fig.add_subplot(111)  # vgl. https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html (10.12.2018)
        # vgl. https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_ylim.html
        plt.ylim(0, 300)
        plt.xlim(0, 300)
        # vgl. https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html  
        plt.plot(L[:,0],L[:,1], 'b-')  # b = blau
        plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-')
        # Punkte in Hülle: rot
        plt.plot(P[:,0],P[:,1],"r^")
        # Punkte auf Hülle: grün + square marker
        plt.plot(L[:,0],L[:,1],"gs", markersize=7)
        # Koordinaten anzeigen
        for xy in zip(L[:,0],L[:,1]):                                                           
            ax.annotate('%s, %s' %xy, xy=xy, textcoords='data', ha='center', va='bottom', fontstyle='normal')     
        plt.axis('on')
        plt.title('Berechnung einer konvexen Hülle')
        plt.show()

if __name__ == '__main__':
    main()
