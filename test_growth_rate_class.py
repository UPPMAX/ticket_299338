import random
from CellModeller.Regulation.ModuleRegulator import ModuleRegulator
from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller.GUI import Renderers
import numpy as np
import math
import time



class Module():

    def __init__(self, sim, parameters=None):
        # Define parameters for the simulation here

        self.sim = sim
        self.dt = self.sim.dt
        
        self.visualize_cas = True
        self.max_cas = 1000

        if parameters is None:
            self.parameters = {'kd_plasmid_division':12, 
                               'max_plasmids':10, 
                               'max_pili': 3,
                               'pili_production_rate': 10,
                               'k2':10,
                               'target_sites':1,
                               'plasmid_mean':3,
                               'cascade_mean':100,
                               'growth_rate':1,
                               'inducer_concentration': 0.5,
                               'camp': 1 # 1 for glucose, something big for glycerol
                               }
        else:
            self.parameters = parameters
    
    
    def setup(self, sim):
        # Set biophysics module
        biophys = CLBacterium(sim, jitter_z=False, 
                                max_cells=100000,
                                max_planes=5,
                                cgs_tol=1E-5,
                                compNeighbours=True,
                                gamma=100,
                                max_jitter=0.01,
                                max_spheres=2)
        plane_coeff= 1
        biophys.addPlane((0,-32,0), (0,1,0), plane_coeff)
        biophys.addPlane((0,32,0), (0,-1,0), plane_coeff)
        biophys.addPlane((0,0,0), (1,0,0), plane_coeff)
        # biophys.addSphere((0,-32,0), 1, 1.0, 1)
        # biophys.addSphere((0,32,0), 1, 1.0, 1)
        #biophys.addPlane((0,0,10), (0,0,1), 1)



        # Set up regulation module
        regul = ModuleRegulator(sim, sim.moduleName)	
        # Only biophys and regulation
        sim.init(biophys, regul, None, None)
    
        # Specify the initial cell and its location in the simulation
        sim.addCell(cellType=random.choice([0,1]), pos=(2,0,0), dir=(1,0,0))#acceptor
        for i in range(1,32):
            sim.addCell(cellType=random.choice([0,1]), pos=(2,((-1)**i)*i,0), dir=(1,0,0))#acceptor
            sim.addCell(cellType=random.choice([0,1]), pos=(2,((-1)**(i-1))*i,0), dir=(1,0,0)) 
        


        # Add some objects to draw the models
        therenderer = Renderers.GLBacteriumRenderer(sim)
        sim.addRenderer(therenderer)
        
        # Specify how often data is saved
        #sim.pickleSteps = 10

    def init(self, cell):
        # Specify mean and distribution of initial cell size
        cell.targetLength = 3.5 + np.random.normal(0.0,0.5) # Seems like this should be normally distributed
        # Specify growth rate of cells
        cell.growthRate = self.parameters['growth_rate'] + random.uniform(-0.5,0.5) # This too

            #cell.color = (0.0,0.0,1.0)


    def update(self, cells):
        """This will run without changing the growth rate. This should in theory be run in parallel with physics
        therefore, the growth rate for the physics should be the same as at the start of this process (or an average)"""
        
        dt = self.dt
        #print(f'cell ids: {list(cells.keys())}')
        for (id, cell) in cells.items():

            #Iterate through each cell and flag cells that reach target size for division
            if cell.length > cell.targetLength:
                # SHOULD DEFINE THIS THROUGH LENGTH INSTEAD
                cell.divideFlag = True
            
            # Remove cells that reach the outer channel
            if cell.pos[0] > 32:
                cell.killFlag = True
            #If cell is a transconjugant or donor, infect neighbours
            
            # if cell.cellType == 0: # acceptor:
            #     pass
            

    def divide(self, parent, d1, d2):
        # Specify target cell size that triggers cell division
        # DEFINE TARGET LENGTH INSTEAD
        d1.targetLength = 3.5 + np.random.normal(0.0,0.5)
        d2.targetLength = 3.5 + np.random.uniform(0.0,0.5)

        
