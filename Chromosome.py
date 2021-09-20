import random
from typing import Sequence
class Chromosome:
    def __init__(self, settings):
        gene_num = lambda : int(random.random()*(settings.max_num_gene+1))
        self.settings = settings
        self.sequence = [gene_num() for genes in range(settings.num_genes_per_chr)]
        self.goal_ff = settings.goal_ff
        self.define_ff([0 for j in range(self.settings.num_genes_per_chr)])

    def define_ff(self, num_ones_per_pos_gene):
        if(self.settings.max_num_gene == 9):
            self.ff_value = self.settings.fitness_function(self.sequence, num_ones_per_pos_gene)
            #self.ff_value = self.settings.fitness_function(self.sequence)
        else:
            self.ff_value = self.settings.fitness_function(self.sequence)   
        self.define_chosen_p()
    
    def define_chosen_p(self):
        div = (self.settings.num_genes_per_chr * self.settings.num_chr_per_gen) /2
        self.chosen_prob = self.ff_value / div

    def show(self):
        return self.sequence

