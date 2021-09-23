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
the solve consists in 

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

# BIBLIOGRAPHY
* 
