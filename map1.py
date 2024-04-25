# Fonction pour calculer la distance entre deux points
def calc_distance(point1, point2):
    # Extrayons les coordonnées x, y, et z de chaque point
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    # Utilisation de la formule de la distance (**2(c puissance 2)et **0.5(prendre co;pte la racine))
    calc_distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5
    
    # Retourne la distance calculée
    return calc_distance

points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

# Calcul des distances entre les points correspondants
distances = [calc_distance(p1, p2) for p1, p2 in zip(points1, points2)]

# Affichage des distances
print(distances)