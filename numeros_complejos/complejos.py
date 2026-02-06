import math
def suma(z1, z2):
    """
    Suma de dos números complejos en forma cartesiana.
    z1 y z2 son tuplas (real, imaginario)
    """
    return (z1[0] + z2[0], z1[1] + z2[1])

def resta(z1, z2):
    """
    Resta de dos números complejos en forma cartesiana.
    """
    return (z1[0] - z2[0], z1[1] - z2[1])

def producto(z1, z2):
    """
    Producto de dos números complejos en forma cartesiana.
    """
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c)

def conjugado(z):
    """
    Conjugado de un número complejo.
    """
    return (z[0], -z[1])

def modulo(z):
    """
    Módulo (magnitud) de un número complejo.
    """
    return math.sqrt(z[0] ** 2 + z[1] ** 2)

def division(z1, z2):
    """
    División de dos números complejos en forma cartesiana.
    """
    a, b = z1
    c, d = z2
    denominador = c ** 2 + d ** 2
    return (
        (a * c + b * d) / denominador,
        (b * c - a * d) / denominador
    )

def cartesiano_a_polar(z):
    """
    Convierte un número complejo de forma cartesiana a polar.
    """
    r = modulo(z)
    theta = math.atan2(z[1], z[0])
    return (r, theta)

def polar_a_cartesiano(p):
    """
    Convierte un número complejo de forma polar a cartesiana.
    """
    r, theta = p
    return (r * math.cos(theta), r * math.sin(theta))

def fase(z):
    """
    Retorna la fase (ángulo) de un número complejo.
    """
    return math.atan2(z[1], z[0])

