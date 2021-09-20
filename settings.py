class Settings:
    #num_genes_per_chr = 20
    #num_chr_per_gen = 20
    #crossover_prob = 0.7
    #mutation_prob = 0.001

    def __init__(self, max_num_gene, num_genes_per_chr, num_chr_per_gen, crossover_prob, mutation_prob):
        if(max_num_gene == '1'):
            self.max_num_gene = int(max_num_gene)
            self.num_genes_per_chr = num_genes_per_chr
            self.num_chr_per_gen = num_chr_per_gen
            self.crossover_prob = crossover_prob
            self.mutation_prob = mutation_prob
            self.goal_ff = 20
            self.fitness_function = lambda sequence: sum(sequence)
            