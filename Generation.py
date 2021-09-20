import  random
from typing import  Iterator
from settings import  Settings
from Chromosome import  Chromosome

class  Generation:
    def __init__(self, settings):
        self.chromosomes = [Chromosome(settings) for chrom in range(settings.num_chr_per_gen)]
        self.max_valued_chr = max(self.chromosomes, key = (lambda chr: chr.ff_value))
        self.settings = settings

    def new_generation(self):
        new_generation = []
        iterator = 1
        probabilistic_dist = [chr.chosen_prob for chr in self.chromosomes]
        while(iterator <= len(self.chromosomes) / 2):
            chr1, chr2 = tuple(random.choices(self.chromosomes,k=2,weights=probabilistic_dist))
            random_value = random.random()
            if random_value <= self.settings.crossover_prob:
                chr1, chr2 = self.crossover(chr1, chr2)
            random_value = random.random()
            if random_value <= self.settings.mutation_prob:
                chr1, chr2 = self.mutation(chr1, chr2)
            new_generation.append(chr1)
            new_generation.append(chr2)
            iterator+=1
        self.chromosomes = new_generation
        self.max_valued_chr = max(self.chromosomes, key=(lambda chr: chr.ff_value))
        self.recalculate_chromosomes()
    
    def recalculate_chromosomes(self):
        num_ones_per_pos_gene = [sum([self.chromosomes[i].sequence[j]==1 for i in range(self.settings.num_chr_per_gen)]) for j in range(self.settings.num_genes_per_chr)]
        #print(num_ones_per_pos_gene)
        for chr in self.chromosomes:
            chr.define_ff(num_ones_per_pos_gene)
    
    def crossover(self, chr1, chr2):
        pos_inicial = int(random.random() * self.settings.num_genes_per_chr)
        aux_sequence = chr1.sequence[pos_inicial:]
        _chr1 = Chromosome(self.settings)
        _chr2 = Chromosome(self.settings)
        _chr1.sequence = chr1.sequence[:pos_inicial] + chr2.sequence[pos_inicial:]
        _chr2.sequence = chr2.sequence[:pos_inicial] + aux_sequence
        return _chr1, _chr2

    def mutation(self, chr1, chr2):
        pos_flip = int(random.random() * self.settings.num_genes_per_chr)
        chr1.sequence[pos_flip] = chr1.sequence[pos_flip]-1 if chr1.sequence[pos_flip]-1 >= 0 else chr1.sequence[pos_flip]+1
        chr2.sequence[pos_flip] = chr2.sequence[pos_flip]-1 if chr2.sequence[pos_flip]-1 >= 0 else chr2.sequence[pos_flip]+1
        return chr1, chr2

    def show(self):
        return [chr.show() for chr in self.chromosomes]