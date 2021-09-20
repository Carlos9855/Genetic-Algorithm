from settings import Settings
from GeneticLocalSearch import GeneticLocalSearch
from Generation import Generation
import random
from pprint import pprint
import numpy as np

def main():
    max_num_of_gene = '1'
    settings = Settings(max_num_of_gene)
    initial_generation = Generation(settings)
    lsg = GeneticLocalSearch(initial_generation, settings)
    lsg.show_results()
    lsg.solve()
    lsg.show_results()

if __name__ == '__main__':
    main()