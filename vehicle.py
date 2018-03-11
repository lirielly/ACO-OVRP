# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:10:01 2018
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 28-02-2018 09:00:00 PM
"""

class Vehicle(object):
    def __init__(self, v_cost, km_cost, capacity, max_time):
        self._vehicle_cost = v_cost
        self._km_cost = km_cost
        self._path = []
        self._capacity = capacity
        self._occupancy = 0
        self._distance = 0
        self._max_travel_time = max_time
        self._travel_time = 0      
   
     
    def put_node_path(self, node, occupancies, distances, times):
        '''
        Function to update path, occupancy, distance, travel_time of a vehicle
        '''
        if self._path:
            self._path.append(node)
            self._occupancy += occupancies[node]
            self._distance += distances[self.path[-2], self.path[-1]]
            self._travel_time += times[self.path[-2], self.path[-1]]
        else:
            self._path.append(node)
            #Quando não for o zero no começo inserir aqui self.occupancy += occupancies[node]

   
    @property        
    def occupancy(self):
        '''
        Function to return occupancy
        '''
        return self._occupancy
    
    @occupancy.setter
    def occupancy(self, value):
        '''
        Function to update occupancy
        '''
        self._occupancy = value
    
    @property        
    def distance(self):
        '''
        Function to return the distance
        '''
        return self._distance
    
    @distance.setter
    def distance(self, value):
        '''
        Function to update distance
        '''
        self._distance = value
    
    @property     
    def travel_time(self):
        '''
        Function to return traveled time
        '''
        return self._travel_time
    
    @travel_time.setter
    def travel_time(self, value):
        '''
        Function to update traveled time
        '''
        self._travel_time = value
        
    @property     
    def max_travel_time(self):
        '''
        Function to return max traveled time
        '''
        return self._max_travel_time
        
    @property     
    def capacity(self):
        '''
        Function to return capacity
        '''
        return self._capacity
    
    @property     
    def path(self):
        '''
        Function to return path
        '''
        return self._path
    
    @path.setter
    def path(self, value):
        '''
        Function to update traveled time
        '''
        self._path = value
    
    @property     
    def vehicle_cost(self):
        '''
        Function to return vehicle_cost
        '''
        return self._vehicle_cost
    
    @property     
    def km_cost(self):
        '''
        Function to return km_cost
        '''
        return self._km_cost
    