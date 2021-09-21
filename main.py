from settings import Settings
from GeneticLocalSearch import GeneticLocalSearch
from Generation import Generation
import random
from pprint import pprint
import numpy as np

def main():
    num_genes_per_chr = 20
    num_chr_per_gen = 100
    crossover_prob = 0.1
    mutation_prob = 0.005
    max_num_of_gene = '1'
    settings = Settings(max_num_of_gene, num_genes_per_chr, num_chr_per_gen, crossover_prob, mutation_prob)
    initial_generation = Generation(settings)
    lsg = GeneticLocalSearch(initial_generation, settings)
    lsg.show_results()
    lsg.solve()
    lsg.show_results()

if __name__ == '__main__':
    main()