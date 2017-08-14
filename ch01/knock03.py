
import re


def generate_pi():
    s1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    s2 = re.sub(',|\.', '', s1).split()
    s3 = []
    for i in s2:
        s3.append(len(i))
    return s3
