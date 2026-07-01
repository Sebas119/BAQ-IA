#CODIGO INICIAL
def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))
#PARTE LIA 

def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return f"{weight / height ** 2:.2f}"


print(bmi(weight = lb_to_kg(132.277), height = ft_and_inch_to_m(5, 3)))

#PARTE SEBASTIÁN

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return f"{weight / height ** 2:.2f}"


print(bmi(weight = lb_to_kg(149.914), height = ft_and_inch_to_m(5.64)))



