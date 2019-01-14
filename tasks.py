import random
from answer import alphabet

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    chromosome = ""
    i = 1
    while (i <= size):
        chromosome += get_letter()
        i += 1
    return chromosome


from answer import get_answer

def get_score(chrom):
    key = get_answer()
    score = 0
    # TODO: implement the scoring function
    #  * compare the chromosome with the solution (how many character are in the correct position?)
    #we're gonna fucking assume they're the same length whatever i hate all of you
    for i, c in enumerate(chrom):
        if c == key[i]:
            score +=1
            i += 1
        else:
            i += 1
            score += 0
    score_normalized = score / len(chrom)
    return score_normalized




#https://tech.io/playgrounds/334/genetic-algorithms/tools?utm_source=code-org&utm_campaign=HOC2017&utm_term=genetic-algorithms
#2:30 AM 01/12/2019 this finally passed itoghashjihs'okrmaj'eohgi

from answer import get_score
    
def score(chrom):
    # floating number between 0 and 1. The better the chromosome, the closer to 1
    # We coded the get_score(chrom) in the previous exercise
    return get_score(chrom)
    
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    scores = []
    retained_chromosomes = []
    fuckyou = {}
    population = len(chromosomes_list)
    # TODO: implement the selection function
    #  * Sort individuals by their fitting score
    for i, c in enumerate(chromosomes_list):
        fuckyou[get_score(c)] = chromosomes_list[i]
        scores.append(get_score(c))
    scores.sort()
    #  * Select the best individuals
    best = int(GRADED_RETAIN_PERCENT * population)
    for i in range(-1-best, -1):
        retained_chromosomes.append(fuckyou[scores[i]])
        fuckyou.pop(scores[i])
    #  * Randomly select other individuals
    remnant = []
    for x in fuckyou.values():
        remnant.append(x)
    while len(retained_chromosomes) != int(population * (GRADED_RETAIN_PERCENT + NONGRADED_RETAIN_PERCENT)):
        length = int(len(remnant))
        keep = random.randint(1, length)
        retained_chromosomes.append(remnant[keep-1])
        remnant.pop(keep-1)
    return retained_chromosomes

def crossover(parent1, parent2):
    # TODO: implement the crossover function
    #  * Select half of the parent genetic material
    half_parent1 = ""
    half_parent2 = ""
    half = int(0.5*len(parent1))
    half_parent1 = parent1[0:half]
    half_parent2 = parent2[half:]
    
    child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
    return child	

import random
from answer import alphabet

def get_letter():
    return random.choice(alphabet)
    
def mutation(chrom):
    mutdex = random.randint(0, len(chrom)-1)
    ugh = chrom.partition(chrom[mutdex])
    return ugh[0] + get_letter() + ugh[2]
