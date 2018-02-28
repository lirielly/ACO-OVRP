# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:10:01 2018
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 28-02-2018 09:00:00 PM
"""

class Vehicle(object):
    def __init__(self, v_cost, km_cost, capacity, max_time):
        self.vehicle_cost = v_cost
        self.km_cost = km_cost
        self.path = []
        self.capacity = capacity
        self.occupancy = 0
        self.distance = 0
        self.max_travel_time = max_time
        self.travel_time = 0      
        
    def put_node_path(self, node, occupancies, distances, times):
        '''
        Function to update path, occupancy, distance, travel_time of a vehicle
        '''
        self.path.append(node)
        self.occupancy += occupancies[node]
        if self.path:
            self.distance += distances[self.path[-2], self.path[-1]]
            self.travel_time += times[self.path[-2], self.path[-1]]
            
            
        