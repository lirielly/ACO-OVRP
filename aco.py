# -*- coding: utf-8 -*-
"""
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 01-07-2018 05:00:00 PM
"""

import argparse
import pandas as pd
from antColony import AntColony
from vehicle import Vehicle

def read_square_matrix(file_name):
    matrix = pd.read_csv(file_name, header=None, sep=';')
    print(matrix.info())
    if(matrix.shape[0] != matrix.shape[1]):
        raise Exception('Matrix has to be a square matrix!')
    return matrix.values

def read_list(file_name):
    teste = pd.read_csv(file_name, header=None, sep=';')
    print(teste.info())
    return pd.read_csv(file_name, header=None, sep=';').values

def read_vehicle(file_name):
    vehicles = []
    with open(file_name, 'r') as f:
        for line in f:
            values = line.replace(',', '.').split(';')
            print(int(values[0]), float(values[1]), int(values[2]), float(values[3]))
            v = Vehicle(int(values[0]), float(values[1]), int(values[2]), float(values[3]))
            vehicles.append(v)
    
    return vehicles
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ACO')
    parser.add_argument('-k', '--ants', type=int, dest='k', default='17',
                        help='ants number')
    parser.add_argument('-p', '--ro', type=float, dest='p', default='0.99',
                        help='pheromone rate decay')
    parser.add_argument('-a', '--alpha', type=float, dest='a', default='0.5',
                        help='pheromone trail importance')
    parser.add_argument('-b', '--beta', type=float, dest='b', default='8.0',
                        help='local heuristic importance')
    parser.add_argument('-c', '--distance_cost', type=float, dest='c', 
                        default='1.0', help='one unit distance cost')
    parser.add_argument('-n', '--n_best_ants', type=int, dest='n', 
                        default='10', help='best ants number')
    parser.add_argument('-i', '--iterations', type=int, dest='i', 
                        default='1', help='iterations number')
    parser.add_argument('-d', '--distance_matrix', 
                        dest='file_name_distance', default='distances.csv', 
                        help='distance matrix values')
    parser.add_argument('-v', '--vehicle_file', 
                        dest='file_name_vehicle', default='vehicles.csv', 
                        help='vehicle information')
    parser.add_argument('-t', '--time_matrix', 
                        dest='file_name_time', default='times.csv',  
                        help='time matrix values')
    parser.add_argument('-o', '--occupancies', 
                        dest='file_name_occupancy', default='occupancy.csv', 
                        help='occupancies values')
    args = parser.parse_args()
    
    print('Starting ACO Python!')    
    
    distance_matrix = read_square_matrix(args.file_name_distance)
    
    time_matrix = read_square_matrix(args.file_name_time)
    
    occupancies = read_list(args.file_name_occupancy)
    
    vehicles = read_vehicle(args.file_name_vehicle)

    colony = AntColony(distance_matrix, args.c, args.k, args.n, args.i, args.p,
                       args.a, args.b, time_matrix, occupancies, vehicles)
    best_ant = colony.run()
    
    print("OF: ")
    print(best_ant.of())
    print("PATH: ")
    print(best_ant.path)