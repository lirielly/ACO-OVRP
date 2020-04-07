# -*- coding: utf-8 -*-
"""
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 03-11-2018 11:30:00 AM
"""

import subprocess
from timeit import default_timer as timer

def child(k, p, a, b, n, i):
    param = "-k %d -p %f -a %f -b %f -n %d -i %d" % (k, p, a, b, n, i)

    pipe = subprocess.Popen("python aco.py " + param, stdout=subprocess.PIPE)
    
    for line in pipe.stdout:
        line = line.strip()
        print(line.decode('ascii'))
    line = line.decode('ascii')
    of = line.split(':')[1]  
    out = "%f;%f;%d;%d;%f;%f;%f\n" % (float(of), k, n, i, p, a, b)
    
    with open("out_ACO_parameter_test.csv", 'a') as fileout:
        fileout.write(out)

def parent():
    start = timer()
    print('Starting ACO Python parameter test!')
    
    out = "OF;Number Ants;Number Best Ants;Number Iterations;Rho;Alpha;Beta\n"
    with open("out_ACO_parameter_test.csv", 'w') as fileout:
        fileout.write(out)
    
    kz = [10, 50, 100, 150, 200]
    pz = [0.99, 0.98, 0.97, 0.96, 0.95]
    az = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    bz = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nz = [5, 10, 15, 20]
    iz = [10, 100, 200, 300, 500, 1000]
    
    for k in kz:
        for p in pz:
            for a in az:
                for b in bz:
                    for n in nz:
                        for i in iz:
                            if n < k and not(a == 0 and b == 0):
                                child(k, p, a, b, n, i)
    end = timer()
    print("Done!\nExecution Time: %f" % (end - start))

if __name__ == '__main__':
    parent()