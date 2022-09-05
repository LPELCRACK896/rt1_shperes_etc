import lpmath as lpm

WHITE = (1,1,1)
BLACK = (0,0,0)

class Intersect(object):
    def __init__(self, distance, point, normal, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObj = sceneObj

class Material(object):
    def __init__(self, diffuse = WHITE):
        self.diffuse = diffuse


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = lpm.suma_o_resta_vectores(self.center, orig, True)
        tca = lpm.productoPunto(L, dir)
        d = (lpm.magnitud_vector(L) ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        # P = O + t0 * D
        P = [ori+(t0*diri) for ori, diri in zip(orig, dir)]
        normal = lpm.suma_o_resta_vectores(P, self.center, True)
        normal = lpm.normalizaVector(normal)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         sceneObj = self)
