class Settings:
    num_genes_per_chr = 20
    num_chr_per_gen = 100
    crossover_prob = 0.7
    mutation_prob = 0.001

    def __init__(self, max_num_gene):
        if(max_num_gene == '1'):
            self.max_num_gene = int(max_num_gene)
            self.goal_ff = 20
            self.fitness_function = lambda sequence: sum(sequence)
            