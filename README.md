# Sistemas-inteligentes-Practice-4
# Genetic-Algorithm
## Members
* Jose Carlos Camacho Salazar
* Diego Delgadillo
* Sebastian Lazarte Catellon

# Problem Description
There are several generations of chromosomes from which the chromosome with the highest fitness function has to be found using a genetic algorithm which contains a crossover probability and a mutation probability.

# Solution Description
For the solution of this problem were used four classes Chromosome, generation GeneticLocalSearch, settings that help to find the solution with the different poblations, probabilities of mutation and crossover 


# Running the script
In order to run the program you first have to enter the 
directory where the ***main.py*** file is located through 
the ***CMD*** console or the one of your choice.

Then in the console you have to enter the `python3 main.py` or `py main.py`, a message
 will appear asking you to enter the option of your preference

# EXPERIMENTS




## Run the algorithm 20 times, for each run it reports in which generation the strongest chromosome was found.strongest chromosome was found. Reports the average of this value

Pc: 0.7 Pm: 0.001 

|Run Number|Strong chromosome generation|
| :---: | :---: | 
|1|24|
|2|62| 
|3|28| 
|4|25| 
|5|25|
|6|15| 
|7|31| 
|8|25|  
|9|42| 
|10|30| 
|11|31| 
|12|25|
|13|42|
|14|938|
|15|46|
|16|49|
|17|719|
|18|30|
|19|30|
|20|47|
|Average | 111.6|

## Run the same experiment, but this time without crossover (pc = 0, pm = 0.001).

The algorithm was run 20 times, without considering the probability of crossover through a loop and the average number of generation in which the strongest cormosome was found was calculated. The results were as follows:

It was not possible to obtain results, we can argue as follows:

The result is very complicated to obtain because in the absence of crossover the algorithm improves in each generation only by choosing those with a high value of fitness function, and it will reach a point that the chromosome with the highest value in the initial generation has been chosen and re-chosen more than the others and the whole generation is a repetition of this, leaving the algorithm as the only way to improve a generation the appearance of a mutation that is very unlikely (0.001%).

## Run the same experiment, but this time without mutation (pc = 0.7, pm = 0).

|Run Number|Strong chromosome generation|
| :---: | :---: | 
|1|42|
|2|30| 
|3|40| 
|4|19| 
|5|36|
|6|29| 
|7|25| 
|8|40|  
|9|47| 
|10|42| 
|11|45| 
|12|37|
|13|52|
|14|40|
|15|38|
|16|33|
|17|27|
|18|30|
|19|51|
|20|23|
|Average | 36.3|

##  Run the same experiment, but this time with these values:

* pc = 0.9, pm = 0.001

|Run Number|Strong chromosome generation|
| :---: | :---: | 
|1|142|
|2|199| 
|3|39| 
|4|241| 
|5|26|
|6|27| 
|7|33| 
|8|24|  
|9|34| 
|10|29| 
|11|37| 
|12|13|
|13|24|
|14|33|
|15|911|
|16|58|
|17|39|
|18|33|
|19|2230|
|20|23|
|Average | 209.75|

* pc = 0.3, pm = 0.001

|Run Number|Strong chromosome generation|
| :---: | :---: | 
|1|1713|
|2|1007| 
|3|37| 
|4|41| 
|5|180|
|6|2588| 
|7|2760| 
|8|813|  
|9|47| 
|10|704| 
|11|2275| 
|12|2339|
|13|6368|
|14|87|
|15|5106|
|16|185|
|17|1680|
|18|38|
|19|993|
|20|211|
|Average | 1458.6|

## Which is the best choice of parameters according to the results obtained above? Why?
The best choise would be pc = 0.7, pm = 0 because the average indicates that with this parameters the algorithm finds, in less generations the strong chromosome


## Run the algorithm 20 times, for each run it reports in which generation the strongest chromosome was found.strongest chromosome was found. It reports the average of this value. Vary the population size. Test with 50, 100, 500, 1000 chromosomes. Which is the best choice? Why?

The best choise is 1000 because the average indicates that with that number of chromosomes we can find the stronger one in less generations. We deduced that because there is more variaty and better probabilities of making crossover between the strongest chromosomes.

|| With 50 chromosomes-cross-0.7-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 1161 |
||2| 45 |
||3| 38 |
||4| 442 |
||5| 161 |
||6| 31 |
||7| 1475 |
||8| 211 |
||9| 54 |
||10| 868 |
||11| 39 |
||12| 42 |
||13| 16 |
||14| 1262 |
||15| 56 |
||16| 221 |
||17| 36 |
||18| 2378 |
||19| 33 |
||20| 1350 |
||Average| 495.95 |


|| With 50 chromosomes-cross-0.9-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 466 |
||2| 54 |
||3| 1388 |
||4| 1988 |
||5| 4551 |
||6| 53 |
||7| 8867 |
||8| 45 |
||9| 37 |
||10| 6582 |
||11| 762 |
||12| 3885 |
||13| 3500 |
||14| 34 |
||15| 47 |
||16| 2934 |
||17| 39 |
||18| 1296 |
||19| 76 |
||20| 39 |
||Average| 1832.15 |

|| With 50 chromosomes-cross-0.3-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 1978 |
||2| 236 |
||3| 3554 |
||4| 2466 |
||5| 932 |
||6| 1850 |
||7| 1584 |
||8| 704 |
||9| 732 |
||10| 771 |
||11| 4294 |
||12| 2437 |
||13| 945 |
||14| 241 |
||15| 2262 |
||16| 634 |
||17| 3058 |
||18| 70 |
||19| 4989 |
||20| 3047 |
||Average| 1839.2 |

|| With 100 chromosomes-cross-0.7-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 25 |
||2| 35 |
||3| 34 |
||4| 27 |
||5| 27 |
||6| 30 |
||7| 22 |
||8| 20 |
||9| 22 |
||10| 27 |
||11| 28 |
||12| 22 |
||13| 29 |
||14| 19 |
||15| 37 |
||16| 16 |
||17| 20 |
||18| 32 |
||19| 32 |
||20| 20 |
||Average| 26.2 |

|| With 100 chromosomes-cross-0.9-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 25 |
||2| 38 |
||3| 54 |
||4| 44 |
||5| 26 |
||6| 33 |
||7| 33 |
||8| 45 |
||9| 35 |
||10| 26 |
||11| 30 |
||12| 9 |
||13| 40 |
||14| 36 |
||15| 22 |
||16| 30 |
||17| 51 |
||18| 34 |
||19| 62 |
||20| 29 |
||Average| 35.1 |

|| With 100 chromosomes-cross-0.3-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 79 |
||2| 19 |
||3| 40 |
||4| 53 |
||5| 36 |
||6| 59 |
||7| 1206 |
||8| 41 |
||9| 23 |
||10| 41 |
||11| 46 |
||12| 519 |
||13| 91 |
||14| 736 |
||15| 647 |
||16| 247 |
||17| 239 |
||18| 42 |
||19| 68 |
||20| 16 |
||Average| 212.4 |

|| With 500 chromosomes-cross-0.7-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 23 |
||2| 19 |
||3| 14 |
||4| 18 |
||5| 15 |
||6| 20 |
||7| 15 |
||8| 16 |
||9| 18 |
||10| 21 |
||11| 14 |
||12| 12 |
||13| 24 |
||14| 22 |
||15| 19 |
||16| 14 |
||17| 12 |
||18| 17 |
||19| 17 |
||20| 24 |
||Average| 17.7 |

|| With 500 chromosomes-cross-0.9-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 17 |
||2| 17 |
||3| 19 |
||4| 14 |
||5| 19 |
||6| 17 |
||7| 22 |
||8| 17 |
||9| 22 |
||10| 18 |
||11| 10 |
||12| 22 |
||13| 19 |
||14| 11 |
||15| 16 |
||16| 18 |
||17| 21 |
||18| 14 |
||19| 9 |
||20| 22 |
||Average| 17.2 |

|| With 500 chromosomes-cross-0.3-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 40 |
||2| 21 |
||3| 25 |
||4| 13 |
||5| 25 |
||6| 21 |
||7| 27 |
||8| 21 |
||9| 15 |
||10| 23 |
||11| 20 |
||12| 22 |
||13| 29 |
||14| 27 |
||15| 28 |
||16| 28 |
||17| 23 |
||18| 23 |
||19| 19 |
||20| 13 |
||Average| 23.15 |

|| With 1000 chromosomes-cross-0.7-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 19 |
||2| 15 |
||3| 8 |
||4| 15 |
||5| 15 |
||6| 20 |
||7| 19 |
||8| 17 |
||9| 17 |
||10| 20 |
||11| 19 |
||12| 9 |
||13| 14 |
||14| 16 |
||15| 14 |
||16| 11 |
||17| 12 |
||18| 18 |
||19| 19 |
||20| 14 |
||Average| 15.55 |

|| With 1000 chromosomes-cross-0.9-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 18 |
||2| 18 |
||3| 16 |
||4| 14 |
||5| 16 |
||6| 18 |
||7| 16 |
||8| 12 |
||9| 18 |
||10| 14 |
||11| 19 |
||12| 17 |
||13| 21 |
||14| 19 |
||15| 16 |
||16| 21 |
||17| 22 |
||18| 24 |
||19| 16 |
||20| 15 |
||Average| 17.5 |

|| With 1000 chromosomes-cross-0.3-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 24 |
||2| 13 |
||3| 22 |
||4| 15 |
||5| 26 |
||6| 30 |
||7| 28 |
||8| 9 |
||9| 18 |
||10| 20 |
||11| 18 |
||12| 22 |
||13| 16 |
||14| 18 |
||15| 10 |
||16| 20 |
||17| 28 |
||18| 16 |
||19| 29 |
||20| 20 |
||Average| 20.1 |

## Run the algorithm for 100 generations and plot the best, worst and average fitness function found in each generation vs. the number of generations. 

![image](https://user-images.githubusercontent.com/72448046/134285908-c73a486d-c078-45d0-b9b0-ed0009cb8db2.png)

# Conclusions
We conclude that with more number of chromosomes we can find better results. This can be observed on the experiments since we have changed not oly the number of chromosomes but also the probabilities of crossover and mutation and every time we got the better result based on the number of chromosomes. 
Also another conclussion is that the changes in probabilities not always leads to a completly different result. In certain cases it does, but the number of chromosomes is a more precisely and concrete variable.

# Recommendations
It is recommended to focus on the generations where the stronger chromosome has been found because we think that it certainly represents which combination of chromosomes and probabilities are the best to solve our problem.

# Porotos
Analysis of possible fitness function

For the resolution of this function it is necessary to take into account:

The value of fitness function for a value that does not contain ones must be very low. For example one can come up with something like this:

![image](https://user-images.githubusercontent.com/72448046/134451597-c0112194-43fa-43a6-bae9-ea2901efd9c8.png)

However, this type of assessment was not determinant, the generations were considering values closer to 1, but as they were not exactly values of 1 the target chromosome was not found. The process discards chromosomes and interacambia among the selected ones and we need an exact value of 1 to be positioned in the place of each gene in the chromosome and not one close to 1, the process should be getting closer to that value 1 but at some point in a gene position there are no ones in the whole generation for that position, they have been discarded at some point and the algorithm stagnates.

We tried to improve this by giving more value to the 1s, up to several times the value of the nearest 1, but it always stagnates. (We left the implementation of this idea commented in the settings class, exactly in the constructor where the fitness function to be used for the case of 0-9 is assigned).

Explanation of the fitness function used

The fitness function used considers another argument, the number of ones in each position of a gene, i.e. it counts how many ones there are in the whole generation in each gene position, that is to say:

![image](https://user-images.githubusercontent.com/72448046/134451624-5b5a9de9-dff6-4cda-9502-65e305cd37cc.png)

Then to determine the fitness function value of a chromosome we count the amount of 1s of this one, besides trying to give a higher value to a gene with value 1 if in that position of the gene there are not many values of 1 in the rest of the generation and if in that position there are several other genes with value 1 in other chromosomes it will have less value. In short we try not to lose the value 1 at a gene position as the generations progress and cause stagnation.

This results in less stagnation and in fewer generations, which allows a miutation to break the stagnation earlier.

Experimentation

Considering that genes take values between 0-9, an initial population of 100 chromosomes, Pc = 0.7 and Pm = 0.001 we ran the algorithm 10 times and found in each iteration the generation in which the strongest chromosome was found. The results are shown in the following table:

|| With 1000 chromosomes-cross-0.3-mut-0.001
||Run Number | Strong chromosome generation
|:---: | :---: | :---: |
||1| 157 |
||2| 5195 |
||3| 1284 |
||4| 1795 |
||5| 4556 |
||6| 3389 |
||7| 58 |
||8| 49 |
||9| 728 |
||10| 3596 |
||Average| 2080.7 |

# Garbanzos

Using the genetic algorithm, taking the number of genes as the number of queens, the gene value as the queen position in the rows and the gene position as the position in the columns. In addition to the initial parameters 100 chromosomes, Pc 0.7 AND Pm = 0.01. The number of non-collisions between queens for random positions of the eight queens was found as the fitness function value. When the problem is solved, i.e. there are no collisions, the value of the **fitness function** is equal to 28.

The problem was solved as shown below. 
![image](https://user-images.githubusercontent.com/72448046/134451688-a3a6cc3f-1c6e-448c-9446-6a00d2fddd2f.png)

However, there are random starting positions that do not result in a generation with the solution chromosome.

# BIBLIOGRAPHY
* Class slides
* https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.monografias.com%2Ftrabajos27%2Falgoritmos-geneticos%2Falgoritmos-geneticos.shtml&psig=AOvVaw0-PLjMpBdxIHtsVnuCSyJy&ust=1632454086387000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCJjmrcKTlPMCFQAAAAAdAAAAABAi
