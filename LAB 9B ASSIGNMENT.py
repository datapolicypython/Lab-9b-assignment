#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:14:50 2024

@author: jennyzhong
"""

import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_empty_patch(self, world):
        empty_patches = [(i, j) for i in range(world.size) for j in range(world.size) if world.grid[i][j] is None]
        if empty_patches:
            return random.choice(empty_patches)
        return self.x, self.y

    def move(self, new_x, new_y, world):
        world.grid[self.x][self.y] = None
        world.grid[new_x][new_y] = self
        self.x = new_x
        self.y = new_y

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = []
        for _ in range(num_agents):
            while True:
                x, y = random.randint(0, size - 1), random.randint(0, size - 1)
                if self.grid[x][y] is None:
                    agent = Agent(x, y)
                    self.agents.append(agent)
                    self.grid[x][y] = agent
                    break

def simulate(world, steps):
    for _ in range(steps):
        for agent in world.agents:
            new_x, new_y = agent.find_empty_patch(world)
            agent.move(new_x, new_y, world)
        for row in world.grid:
            print(' '.join(['A' if cell else '.' for cell in row]))
        print("\n")

world = World(size=5, num_agents=3)

simulate(world, steps=5)

#link 
#https://github.com/datapolicypython/Lab-9b-assignment.git


