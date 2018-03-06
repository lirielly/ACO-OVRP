# -*- coding: utf-8 -*-
"""
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 01-07-2018 06:00:00 PM
"""

import math
import numpy as np
from random import shuffle

# Class ant represents one ant and its path
class Ant(object):
    def __init__(self, start_node, size, vehicles):
        self.path = [start_node]
        self.of_value = math.inf
        self.distance = 0.0
        self.possible_nodes = [x for x in range(size) if x != start_node]
        self.vehicles = vehicles
        shuffle(self.vehicles)
        self.vehicle_idx = 0
        
        print("Aqui")
        print(len(vehicles))
   
    
    def calculate_probabilities(self, distances, feasible_nodes, pheromone, alpha, beta):
        '''
        Function to calculate the feasible nodes probability values
        '''
        probabilities = []
        current_node = self.vehicles[self.vehicle_idx].path[-1]
        for i in feasible_nodes:
            probabilities.append((pheromone[current_node, i]**alpha)*
                                 ((1/distances[current_node, i])**beta))

        return probabilities/sum(probabilities)
   
    
    def constrains(self, times, occupancies):
        '''
        Function to test each node in the constrains and return the feasibles 
        nodes according to the constrains outcome
        '''
        feasible_nodes = []
        for node in self.possible_nodes:
            if (self.vehicles[self.vehicle_idx].travel_time + times[self.path[-1], node]) <= self.vehicles[self.vehicle_idx].max_travel_time and (self.vehicles[self.vehicle_idx].occupancy + occupancies[node]) <= self.vehicles[self.vehicle_idx].capacity:
                feasible_nodes.append(node)
                
        return feasible_nodes


    def chose_next_node(self, distances, feasible_nodes, pheromone, alpha, 
                        beta, occupancies, times):
        '''
        Function to chose the next visited node
        '''
        probabilities = self.calculate_probabilities(distances, feasible_nodes, 
                                                     pheromone, alpha, beta)
        rw = np.random.rand()
        sum_ = 0.0
        for i in range(len(probabilities)):
            sum_ += probabilities[i]
            if sum_ >= rw:
                node_chosen = self.possible_nodes.pop(i)
                self.path.append(node_chosen)
                self.vehicles[self.vehicle_idx].put_node_path(node_chosen, 
                             occupancies, distances, times)
                break
         
            
    def build_path(self, distances, times, occupancies, pheromone, alpha, 
                   beta):
        '''
        Function to build a path for an ant
        '''
        for i in range(distances.shape[0] - 1):
            feasible_nodes = []
            while(not feasible_nodes):
                feasible_nodes = self.constrains(times, occupancies)
                
                if not feasible_nodes and self.vehicles[self.vehicle_idx].occupancy != 0:
                    self.vehicle_idx += 1
                elif not feasible_nodes and self.vehicles[self.vehicle_idx].occupancy == 0:
                    print("Impossible solution. Tried to use another vehicle without use the previews one!")
                    self.vehicles = []
                    self.path = []
                    self.vehicle_idx = 0
                    return
            
            self.chose_next_node(distances, feasible_nodes, pheromone, alpha, 
                                 beta, occupancies, times)
            
            
    def calculate_distance(self, distances):
        '''
        Function to calculate the distance traveled by the ant
        '''
        current_node = self.path[0]
        for i in range(len(self.path) - 1):
            next_node = self.path[i+1]
            self.distance += distances[current_node, next_node]
            current_node = next_node
        self.distance += distances[current_node, self.path[0]]
     
        
    def objectve_function(self, distance_cost):
        '''
        Function to calculate the objection function of the problem
        '''
        vehicle_cost = 0
        distance = 0
        
        for x in range(self.vehicle_idx):
            if self.vehicles[x].occupancy != 0:
                vehicle_cost += self.vehicles[x].v_cost
                distance += (self.vehicles[x].distance * self.vehicles[x].km_cost)
        
        self.of_value = vehicle_cost + distance 
    
    
    def of(self):
        '''
        Function to return the of value
        '''
        return self.of_value            