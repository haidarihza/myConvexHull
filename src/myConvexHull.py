from cmath import sqrt
import numpy as np

simplices = np.array([[1,1]])       #for initial, later will be deleted
real_data = np.array([[0.0,0.0]])   #for initial, later will be deleted

def myConvexHull(dataset) :
   #start program
   #sort the data
   global real_data
   global simplices
   simplices = np.array([[1,1]])
   real_data = dataset
   data = dataset[np.lexsort((dataset[:,1],dataset[:,0]))]
   #set the first point and last point as line S (first point is min(x) and last_point is max(x))
   first_point = data[0]
   last_point = data[len(data)-1]

   #divide points into two part, right and left, based on their determinant
   sLeft = np.array([[0.0,0.0]])
   sRight = np.array([[0.0,0.0]])
   #check every point from indeks 2 untill n-1
   for i in range(1,len(data)) :
      determinant = det(first_point,last_point,data[i])
      if (determinant > 0) :
         sLeft = np.vstack((sLeft,data[i]))
      elif (determinant < 0) :
         sRight = np.vstack((sRight,data[i]))
   #start checking
   sLeft = np.delete(sLeft,0,0)
   sRight = np.delete(sRight,0,0)
   #call the divide function
   divideUp(sLeft,first_point,last_point)
   divideDown(sRight,first_point,last_point)
   #edit the final result
   simplices = np.delete(simplices,0,0)
   simplices = simplices.astype('int')
   return simplices


def divideUp(data,point1,point2) :
   global simplices
   #check if there any point in the data
   if(len(data) == 0)  :
      #save the point1 and point2 as convex hull, save the idx of the point
      idx_p1 = -1
      idx_p2 = -1
      for i in range (len(real_data)) :
         if (real_data[i][0] == point1[0] and real_data[i][1] == point1[1]) :
            idx_p1 = i
         if (real_data[i][0] == point2[0] and real_data[i][1] == point2[1]) :
            idx_p2 = i
      idx_pair = np.array([idx_p1,idx_p2])
      simplices = np.vstack((simplices,idx_pair))

   else :
      #data still have some points, search points that have max distance with the line
      max_dist = -1.0
      max_point = point1
      for i in range (len(data)) :
         determinant = det(point1,point2,data[i])
         dist = determinant/sqrt((point2[0]-point1[0])**2+(point2[1]-point2[1])**2)
         dist = abs(dist)
         if (dist > max_dist) :
            max_point = data[i]
            max_dist = dist
         elif (dist == max_dist) :
            if (data[i][0] < max_point[0]) :
               max_point = data[i]

      #get the max point
      #check for the possible points in the left S1 (S1 = point1->max_point)
      S1 = np.array([[0.0,0.0]])
      for i in range (len(data)) :
         determinant = det(point1,max_point,data[i])
         if (determinant > 0 and (max_point[0] != data[i][0] or max_point[1] != data[i][1])) :            
            #it's in the left of the line
            S1 = np.vstack((S1,data[i]))
      S1 = np.delete(S1,0,0)

      #check for the possible points in the right S2 (S2 = point2->max_point)
      S2 = np.array([[0.0,0.0]])
      for i in range (len(data)) :
         determinant = det(max_point,point2,data[i])
         if (determinant > 0 and (max_point[0] != data[i][0] or max_point[1] != data[i][1])) :
            #it's in the right of the line
            S2 = np.vstack((S2,data[i]))
      S2 = np.delete(S2,0,0)

      #call the divide function again for S1 and S2
      divideUp(S1,point1,max_point)
      divideUp(S2,max_point,point2)

def divideDown(data,point1,point2) :
   global simplices
   #check if there any point in the data
   if(len(data) == 0)  :
      #save the point1 and point2 as convex hull, save the index of the point
      idx_p1 = -1
      idx_p2 = -1
      for i in range (len(real_data)) :
         if (real_data[i][0] == point1[0] and real_data[i][1] == point1[1]) :
            idx_p1 = i
         if (real_data[i][0] == point2[0] and real_data[i][1] == point2[1]) :
            idx_p2 = i
      idx_pair = np.array([idx_p1,idx_p2])
      simplices = np.vstack((simplices,idx_pair))

   else :
      #data still have some points, search points that have max distance with the line
      max_dist = -1.0
      max_point = point1
      for i in range (len(data)) :
         determinant = det(point1,point2,data[i])
         dist = determinant/sqrt((point2[0]-point1[0])**2+(point2[1]-point2[1])**2)
         dist = abs(dist)
         if (dist > max_dist) :
            max_point = data[i]
            max_dist = dist
         elif (dist == max_dist) :
            if (data[i][0] < max_point[0]) :
               max_point = data[i]

      #get the max point
      #check for the possible points in the left S1 (S1 = point1->max_point)
      S1 = np.array([[0.0,0.0]])
      for i in range (len(data)) :
         determinant = det(point1,max_point,data[i])
         if (determinant < 0 and (max_point[0] != data[i][0] or max_point[1] != data[i][1])) :
            #it's in the left of the line
            S1 = np.vstack((S1,data[i]))
      S1 = np.delete(S1,0,0)

      #check for the possible points in the right S2 (S2 = point2->max_point)
      S2 = np.array([[0.0,0.0]])
      for i in range (len(data)) :
         determinant = det(max_point,point2,data[i])
         if (determinant < 0 and (max_point[0] != data[i][0] or max_point[1] != data[i][1])) :
            #it's in the right of the line
            S2 = np.vstack((S2,data[i]))
      S2 = np.delete(S2,0,0)

      #call the divide function again for S1 and S2
      divideDown(S1,point1,max_point)
      divideDown(S2,max_point,point2)

def det(point1, point2, point3) :
   result = point1[0]*point2[1]+point3[0]*point1[1]+point2[0]*point3[1]-point3[0]*point2[1]-point2[0]*point1[1]-point1[0]*point3[1]
   return result
