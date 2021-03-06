from settings import Settings
from GeneticLocalSearch import GeneticLocalSearch
from Generation import Generation
import random
from pprint import pprint
import numpy as np

def main(max_num_of_gene, num_genes_per_chr, num_chr_per_gen, crossover_prob, mutation_prob):
    settings = Settings(max_num_of_gene, num_genes_per_chr, num_chr_per_gen, crossover_prob, mutation_prob)
    initial_generation = Generation(settings)
    lsg = GeneticLocalSearch(initial_generation, settings)
    lsg.show_results()
    lsg.solve()
    lsg.show_results()

if __name__ == '__main__':
    option = 0
    while(option != 5):
        print("1.- Normal run")
        print("2.- Non-crossover algorithm")
        print("3.- Algorithm without mutation")
        print("4.- Enter your own values")
        print("5.- Poroto")
        print("6.- Garbanzos")
        print("Enter an option: ") 
        option = input()
        if option == '1':
            main('1', 20, 100, 0.7, 0.001)
        if option == '2':
            main('1', 20, 100, 0, 0.001)
        if option == '3':
            main('1', 20, 100, 0.7, 0)
        if option == "4":
            print("Number of genes per chromosome: ")
            num_genes_per_chr = int(input())
            print("Number of Poblation in genes: ")
            num_chr_per_gen = int(input())
            print("Crossover probability: ")
            crossover_prob = float(input())
            print("Mutation probability: ")
            mutation_prob = float(input())
            main('1', num_genes_per_chr, num_chr_per_gen, crossover_prob, mutation_prob)
        if option == "5":
            main('9', 10, 100, 0.7, 0.001)
        if option == "6":
            main('8', 20, 100, 0.7, 0.001)