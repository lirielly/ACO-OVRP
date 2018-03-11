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
        self._path = [start_node]
        self._of_value = math.inf
        self._distance = 0.0
        self._possible_nodes = [x for x in range(size) if x != start_node]
        self._vehicles = vehicles
        shuffle(self._vehicles)
        self._vehicle_idx = 0
        
    
    def calculate_probabilities(self, distances, feasible_nodes, pheromone, alpha, beta):
        '''
        Function to calculate the feasible nodes probability values
        '''
        probabilities = []
        current_node = self._vehicles[self._vehicle_idx].path[-1]
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
        for node in self._possible_nodes:
            time_constraint = ((self._vehicles[self._vehicle_idx].travel_time + 
                           times[self._vehicles[self._vehicle_idx].path[-1], node]) 
                            <= self._vehicles[self._vehicle_idx].max_travel_time)
            capacity_constraint = ((self._vehicles[self._vehicle_idx].occupancy + 
                                    occupancies[node]) <= 
                                    self._vehicles[self._vehicle_idx].capacity)
            if time_constraint and capacity_constraint:
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
                node_chosen = self._possible_nodes.pop(i)
                if node_chosen != 0:
                    self._path.append(node_chosen)
                    self._vehicles[self._vehicle_idx].put_node_path(node_chosen, 
                                 occupancies, distances, times)
                    break
                else:
                    raise Exception('Warning! Next node zero is not allowed.')
         
            
    def build_path(self, distances, times, occupancies, pheromone, alpha, 
                   beta):
        '''
        Function to build a path for an ant
        '''
        for i in range(distances.shape[0] - 1):
            feasible_nodes = []
            while(not feasible_nodes):
                feasible_nodes = self.constrains(times, occupancies)
                
                if (not feasible_nodes and 
                    self._vehicles[self._vehicle_idx].occupancy != 0 and 
                    (self._vehicle_idx + 1) < len(self._vehicles)):
                    self._vehicle_idx += 1
                elif not feasible_nodes and self._vehicles[self._vehicle_idx].occupancy == 0:
                    print("Impossible solution. Tried to use another vehicle without use the previews one!")
                    self._vehicles = []
                    self._path = []
                    self._vehicle_idx = 0
                    return
            
            self.chose_next_node(distances, feasible_nodes, pheromone, alpha, 
                                 beta, occupancies, times)
            
            
    def calculate_distance(self, distances):
        '''
        Function to calculate the distance traveled by the ant
        '''
        current_node = self._path[0]
        for i in range(len(self._path) - 1):
            next_node = self._path[i+1]
            self._distance += distances[current_node, next_node]
            current_node = next_node
        self._distance += distances[current_node, self._path[0]]
     
        
    def objectve_function(self, distance_cost):
        '''
        Function to calculate the objection function of the problem
        '''
        vehicle_cost = 0
        distance = 0
        
        for x in range(self._vehicle_idx):
            if self._vehicles[x].occupancy != 0:
                vehicle_cost += self._vehicles[x].vehicle_cost
                distance += (self._vehicles[x].distance * self._vehicles[x].km_cost)
        
        self._of_value = vehicle_cost + distance 
    
   
    @property        
    def path(self):
        '''
        Function to return path
        '''
        return self._path
    
    @path.setter
    def path(self, value):
        '''
        Function to update path
        '''
        self._path = value
        
    @property        
    def of_value(self):
        '''
        Function to return of_value
        '''
        return self._of_value
    
    @of_value.setter
    def of_value(self, value):
        '''
        Function to update of_value
        '''
        self._of_value = value
        
    @property        
    def distance(self):
        '''
        Function to return distance
        '''
        return self._distance
    
    @distance.setter
    def distance(self, value):
        '''
        Function to update distance
        '''
        self._distance = value
    
    @property        
    def possible_nodes(self):
        '''
        Function to return possible_nodes
        '''
        return self._possible_nodes
    
    @possible_nodes.setter
    def possible_nodes(self, value):
        '''
        Function to update possible_nodes
        '''
        self._possible_nodes = value
   
    @property        
    def vehicles(self):
        '''
        Function to return vehicles
        '''
        return self._vehicles
    
    @vehicles.setter
    def vehicles(self, value):
        '''
        Function to update vehicles
        '''
        self._vehicles = value
    
    @property        
    def vehicle_idx(self):
        '''
        Function to return vehicle_idx
        '''
        return self._vehicle_idx
    
    @vehicle_idx.setter
    def vehicle_idx(self, value):
        '''
        Function to update vehicle_idx
        '''
        self._vehicle_idx = value    

    def __str__(self):
        '''
        Function to print important issues of an ant
        '''
        
        out = "\nNumero de veiculos utilizados na solução: %d" % (self._vehicle_idx + 1)
        out += "\nInformação dos veiculos"
        
        #print("\nNumero de veiculos utilizados na solução: %d" % (self.vehicle_idx))
        #print("Informação dos veiculos")
        for i in range(self._vehicle_idx + 1):
            if self._vehicles[i].occupancy != 0:
                out += "\n\nVeiculo: %d" % (i + 1)
                out += "\nNúmero de passageiros: %d" % (self._vehicles[i].occupancy)
                out += "\nRota: "
                out += str(self._vehicles[i].path)
                out += "\nDistância percorrida: %f" % (self._vehicles[i].distance)
                out += "\nTempo: %f \n" % (self._vehicles[i].travel_time)
                
        return out