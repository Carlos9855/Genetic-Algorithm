class Settings:
    #num_genes_per_chr = 20

    #num_chr_per_gen = 20

    #crossover_prob = 0.7

    #mutation_prob = 0.001

    def __init__(self, max_num_gene, num_genes_per_chr, num_chr_per_gen, crossover_prob, mutation_prob):
        self.num_genes_per_chr = num_genes_per_chr
        self.num_chr_per_gen = num_chr_per_gen
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        if(max_num_gene == '1'):
            self.max_num_gene = int(max_num_gene)
            self.goal_ff = 20
            self.fitness_function = lambda sequence: sum(sequence)
        elif(max_num_gene == '9'):
            self.max_num_gene = int(max_num_gene)
            self.goal_ff = 1500
            self.fitness_function = lambda sequence, num_ones_per_pos_gene: self.goal_ff if all([n==1 for n in sequence]) else sum([(200 - num_ones_per_pos_gene[i]*2 if (sequence[i]==1) else 0) for i in range(self.num_genes_per_chr)])
        elif(max_num_gene == '8'):
            num_queens = int(max_num_gene)
            self.max_num_gene = num_queens-1
            self.num_genes_per_chr = num_queens
            self.goal_ff = (num_queens-1)*(num_queens)*0.5
            not_colision = lambda q1, q2: q1[0] != q2[0] and (q1[0]-q1[1])!=(q2[0]-q2[1]) and (q1[0]+q1[1]) != (q2[0]+q2[1])
            self.fitness_function = lambda sequence: sum([sum([ not_colision((sequence[queen], queen),(sequence[other_q], other_q)) for other_q in range(queen+1, num_queens)]) for queen in range(num_queens)])