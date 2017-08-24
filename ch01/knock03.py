
import re


def generate_pi():
    s1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    s2 = s1.replace(',', '').replace('.', '').split()
    s3 = []
    for i in s2:
        s3.append(len(i))
    return s3
