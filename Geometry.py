import math
def cross_line_plane(A,v,B,v1,v2):
    l0 = [-v[0],v1[0],v2[0],A[0] - B[0]]
    l1 = [-v[1],v1[1],v2[1],A[1] - B[1]]
    l2 = [-v[2],v1[2],v2[2],A[2] - B[2]]
    m,hS = gorner([l0,l1,l2])
    if len(m):
        a = m[0]
        return [A[0] + a * v[0],A[1] + a * v[1],A[2] + a * v[2]]
    else:
        return []
# A = list([int(s) for s in input().split()])
# v = list([int(s) for s in input().split()])
#
# B = list([int(s) for s in input().split()])
# v1 = list([int(s) for s in input().split()])
# v2 = list([int(s) for s in input().split()])
# print(cross_line_plane(A,v,B,v1,v2))
def gorner(p):
    a = []
    for i in range(len(p)):
        a.append(p[i])
    n = len(a)
    for i in range(n):
        if (abs(a[i][i])<0.0000001):
            k = -1
            for j in range(i,n):
                if (abs(a[j][i]) > 0.0000001):
                    k = j
                    break
            if k != -1:
                for j in range(i,n+1):
                    t = a[i][j]
                    a[i][j] = a[k][j]
                    a[k][j] = t
            else:
                endlessSolutions = 1
                for l in range(i+1,n+1):
                    if a[i][l] != 0:
                        endlessSolutions = 0
                        break
                if endlessSolutions:
                    return [],1
                return [],0
                # print("Problem")
                # exit()
        c = a[i][i]
        for k in range(i,n+1):
            a[i][k] /= c
        for k in range(i+1,n):
            c = a[k][i]
            for l in range(i,n+1):
                a[k][l] -= a[i][l]*c

    for i in reversed(range(1,n)):
        for k in range(i):
            a[k][n] -= a[i][n]*a[k][i]
            a[k][i] = 0
    b = []
    for i in range(n):
        b.append(a[i][n])
    return b,1
    # for v in a:
    #     print(v)
# n = int(input())
# a = []
# for i in range(n):
#     a.append([int(t) for t in input().split()])
# print(gorner(a))


# def cross_lines(A, v1, B, v2):
def cross_segments(A,B,C,D):
    v1,v2 = segment_to_line(A,B),segment_to_line(C,D)
    l0 = [v1[0],-v2[0],C[0] - A[0]]
    l1 = [v1[1],-v2[1],C[1] - A[1]]
    m,hasSol = gorner([l0,l1])
    if hasSol and not len(m):
        print("equal segments")
    if hasSol:
        a = m[0]
        b = m[1]
        if abs(a) <= 1 and abs(b) <= 1:
            return [A[0] + v1[0] * a,A[1] + v1[1] * a,A[2] + v1[2] * a]
    return -1
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# C = [int(i) for i in input().split()]
# D = [int(i) for i in input().split()]
# print(cross_segments(A,B,C,D))
def segment_to_line(A,B):
    v = []
    for i in range(3):
        v.append(B[i] - A[i])
    return v
def take_plane(A,B,C):
    return A,segment_to_line(A,B),segment_to_line(A,C)
def point_belong_plane(T,A,v1,v2):
    l0 = [v1[0],v2[0],T[0] - A[0]]
    l1 = [v1[1],v2[1],T[1] - A[1]]
    m,has_solutions = gorner([l0,l1])
    if has_solutions and len(m) == 0:
        return True
    return (len(m) != 0) and T[2] == A[2] + m[0] * v1[2] + m[1] * v2[2]
def unique3D(AllObjs, searchingObj):
    for obj in AllObjs:
        equal = 1
        for j in searchingObj:
            if j not in obj:
                equal = 0
                break
        if equal:
            return False
    return True
def findPlanesWithMore3Points(Points):
    n = len(Points)
    planes = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                A,v1,v2 = take_plane(Points[i], Points[j], Points[k])
                points_in_plane = [Points[i], Points[j], Points[k]]
                for l in range(k+1,n):
                    susp_P = Points[l]
                    if point_belong_plane(susp_P,A,v1,v2):
                        points_in_plane.append(susp_P)
                if len(points_in_plane) > 3 and unique3D(planes, points_in_plane):
                    planes.append(points_in_plane)
    return planes
# n = int(input())
# points = []
# for i in range(n):
#     points.append([int(s) for s in input().split()])
# planes = findPlanesWithMore3Points(points)
# for i in planes:
#     print(i)
def perpendicularPoint(S,A,v1,v2):
    l0 = [(v1[0]**2 + v1[1]**2 + v1[2]**2),(v2[0]*v1[0] + v2[1]*v1[1] + v2[2]*v1[2]),-((A[0]-S[0])*v1[0] + (A[1]-S[1])*v1[1] + (A[2]-S[2])*v1[2])]
    l1 = [(v2[0] * v1[0] + v2[1] * v1[1] + v2[2] * v1[2]),(v2[0] ** 2 + v2[1] ** 2 + v2[2] ** 2),-((A[0] - S[0]) * v2[0] + (A[1] - S[1]) * v2[1] + (A[2] - S[2]) * v2[2])]
    m,hS = gorner([l0,l1])
    if len(m):
        H = []
        for i in range(3):
            H.append(A[i] + m[0] * v1[i] + m[1] * v2[i])
        return H
    else:
        print("WTF")
        exit()
def vecLen(v):
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5
def distPointPlane(S,A,v1,v2):
    H = perpendicularPoint(S,A,v1,v2)
    perp = segment_to_line(S,H)
    return vecLen(perp)
def areaTriangular(a,b,c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
def getPlaneSegments(Points):
    n = len(Points)
    segments = []
    for i in range(n):
        for j in range(n):
            if j == i: continue
            A,B = Points[i],Points[j]
            ABIsSegment = 1
            for k in range(n):
                if k == i or k == j: continue
                for l in range(n):
                    if l == i or l == j or l == k: continue
                    C,D = Points[k],Points[l]
                    if cross_segments(A,B,C,D) != -1:
                        ABIsSegment = 0
                        break
                if not ABIsSegment:
                    break
            if ABIsSegment and unique3D(segments, [A, B]):
                segments.append([A,B])
    return segments
# S = list([int(s) for s in input().split()])
# B = list([int(s) for s in input().split()])
# C = list([int(s) for s in input().split()])
# D = list([int(s) for s in input().split()])
# print(getPlaneSegments([S,B,C,D]))
def areaSideSurfacePyramid(S, planePoints):
    area = 0
    allSegments = getPlaneSegments(planePoints)
    for segment in allSegments:
        A,B = segment[0],segment[1]
        AB,AS,BS = vecLen(segment_to_line(A,B)),vecLen(segment_to_line(A,S)),vecLen(segment_to_line(B,S))
        area += areaTriangular(AB,AS,BS)
    return area
# n = int(input())
# points = []
# for i in range(n):
#     points.append([int(s) for s in input().split()])
# planes = findPlanesWithMore3Points(points)
# for p in points:
#     if p not in planes[0]:
#         S = p
#         break
# print(areaSideSurfacePyramid(S, planes[0]))
def scalarProduct(v1,v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
def angleLineLine(v1,v2):
    return math.acos(abs(scalarProduct(v1,v2))/(vecLen(v1)*vecLen(v2)))
def angleLinePlane(A,v,B,v1,v2):
    C = cross_line_plane(A,v,B,v1,v2)
    H = perpendicularPoint(A,B,v1,v2)
    CH = segment_to_line(C,H)
    CA = segment_to_line(C,A)
    return angleLineLine(CH,CA)
# A = list([int(s) for s in input().split()])
# v = list([int(s) for s in input().split()])
# B = list([int(s) for s in input().split()])
# v1 = list([int(s) for s in input().split()])
# v2 = list([int(s) for s in input().split()])
# print(angleLinePlane(A,v,B,v1,v2))
def anglePlanePlane(A,v1,v2,B,v3,v4):
    Points = [[0,0,0],[0,0,1],[0,1,0],[1,0,0],[-1,-2,0],[-1,-3,3],[5,5,5]]  # точки,которые не могут содержать 2 плоскости сразу
    i = 0
    while point_belong_plane(Points[i],A,v1,v2):
        i+=1
    normal1 = segment_to_line(Points[i],perpendicularPoint(Points[i],A,v1,v2))
    i = 0
    while point_belong_plane(Points[i], B, v3, v4):
        i += 1
    normal2 = segment_to_line(Points[i], perpendicularPoint(Points[i], B, v3, v4))
    return angleLineLine(normal1,normal2)

