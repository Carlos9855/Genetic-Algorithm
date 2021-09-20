from Generation import Generation
from pprint import pprint
import matplotlib.pyplot as plt

class GeneticLocalSearch:
    def __init__(self, current_generation, settings):
        self.current_generation = current_generation
        self.goal_ff = settings.goal_ff
        self.num_generation = 1

    def solve(self):
        y_av = []
        y_min = []
        y_max = []
        while(self.current_generation.max_valued_chr.ff_value < self.goal_ff and self.num_generation<8500):
            self.current_generation.new_generation()
            self.num_generation += 1
            y_av.append(sum([chr.ff_value for chr in self.current_generation.chromosomes])/len(self.current_generation.chromosomes))
            y_min.append(min(self.current_generation.chromosomes, key=(lambda chr: chr.ff_value)).ff_value)
            y_max.append(self.current_generation.max_valued_chr.ff_value)
        self.graph_parameters_progresion(y_min, y_max, y_av)

    def graph_parameters_progresion(self, y_min, y_max, y_av):
        x = range(1,self.num_generation)
        
        plt.plot(x,y_min)
        plt.plot(x,y_av)
        plt.plot(x,y_max)
        plt.show()

    def show_results(self):
        count = 1
        print(f"Goal result in generation {self.num_generation}th")
        for chr in self.current_generation.chromosomes:
            if chr.ff_value == self.goal_ff: print(f"{count}--{chr.show()}--{chr.ff_value} <- Chromosome with goal value")
            else: print(f"{count}--{chr.show()}--{chr.ff_value}")
            count += 1