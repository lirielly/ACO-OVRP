# -*- coding: utf-8 -*-
"""
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 03-11-2018 11:30:00 AM
"""

import subprocess

def child(k, p, a, b, c, n, i):
    param = "-k %d -p %f -a %f -b %f -c %f -n %d -i %d" % (k, p, a, b, c, n, i)

    p = subprocess.Popen("python aco.py " + param, stdout=subprocess.PIPE)
    
    for line in p.stdout:
        line = line.strip()
        print(line)

def parent():
    k = 10
    p = 0.99
    a = 0.5
    b = 8
    c = 1
    n = 5
    i = 10
    
    print("Inicio")
    child(k, p, a, b, c, n, i)
    print("Fim")

if __name__ == '__main__':
    parent()