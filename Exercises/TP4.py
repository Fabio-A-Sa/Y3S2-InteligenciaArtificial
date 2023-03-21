import numpy as np
import copy, random, math

enrollments = {
    1: [1,2,3,4,5],
    2: [6,7,8,9], 
    3: [10,11,12],
    4: [1,2,3,4],
    5: [5,6,7,8],
    6: [9,10,11,12],
    7: [1,2,3,5],
    8: [6,7,8],
    9: [4,9,10,11,12],
    10: [1,2,4,5],
    11: [3,6,7,8],
    12: [9,10,11,12]
}
slots = 4
num_students = 12
num_enrollments = len(enrollments)

# 4.1 a)
def generate_random_solution():
    return np.random.randint(1, slots + 1, num_enrollments)

# 4.1 b)
def get_num_incompatibilities(discipline_1, discipline_2):
    if (discipline_1 not in enrollments or discipline_2 not in enrollments):
        return 0
    incompatibilities = [student for student in enrollments[discipline_1] if student in enrollments[discipline_2]];
    return len(incompatibilities)
    
# 4.1 c)
def evaluate_solution(solution):
    num_incompatibilities = 0

    #Your Code Here
    
    return -num_incompatibilities

# 4.1 d)
# Change the slot of a discipline
def get_neighbor_solution1(solution):
    neighbor = copy.deepcopy(solution)
    
    #Your Code Here
    
    return neighbor

# Exchange the slots of two disciplines
def get_neighbor_solution2(solution):
    neighbor_solution = copy.deepcopy(solution)
    
    #Your Code Here
    
    return neighbor_solution

# Neighbour 1 or 2 with 50% each
def get_neighbor_solution3(solution):
    if (np.random.randint(0,2)==0):
        return get_neighbor_solution1(solution)
    else:
        return get_neighbor_solution2(solution)
    
#Test Solution Generation
s = generate_random_solution()
print(s)

#Test Incompatibility Matrix
print('   1  2  3  4  5  6  7  8  9 10 11 12')
for d1 in range(0,num_enrollments):
        print(d1+1, end='  ')
        for d2 in range (0,num_enrollments):
            print(get_num_incompatibilities(d1,d2), end='  ')
        print()

#Test Evaluation
print(evaluate_solution(s))
print(evaluate_solution([1,1,1,2,2,2,3,3,3,4,4,4]))

#Test Neighbours
s = [1,1,1,2,2,2,3,3,3,4,4,4]
print(s)
for d1 in range(0,20):
    print(get_neighbor_solution1(s))

# 4.1 e) Hill Climbing
def get_hc_solution(num_iterations, log=False):
    iteration = 0;
    best_solution = generate_random_solution() # Best solution after 'num_iterations' iterations without improvement
    best_score = evaluate_solution(best_solution)
    
    print(f"Init Solution:  {best_solution}, score: {best_score}")
    
    while iteration < num_iterations:
        iteration += 1
    
        #Your Code Here
    
        if log:
                (print(f"Solution:       {best_solution}, score: {best_score}"))
            
    print(f"Final Solution: {best_solution}, score: {best_score}")
    return best_solution

# 4.1 e) Simulated Annealing
def get_sa_solution(num_iterations, log=False):
    iteration = 0;
    temperature = 1000;
    solution = generate_random_solution() # Best solution after 'num_iterations' iterations without improvement
    score = evaluate_solution(solution)
    
    best_solution = copy.deepcopy(solution)
    best_score = score
    
    print(f"Init Solution:  {best_solution}, score: {best_score}")
    
    while iteration < num_iterations:
        temperature = temperature * 0.999  # Test with different cooling schedules
        iteration += 1
        
        #Your Code Here
        
        if log:
                    print(f"Solution:       {best_solution}, score: {best_score},  Temp: {temperature}")
                
    print(f"Final Solution: {best_solution}, score: {best_score}")
    return best_solution 

# Genetic Algorithms 

# 4.2 c)
def midpoint_crossover(solution_1, solution_2):
    
    #Your Code Here
    
    return child_1, child_2

def randompoint_crossover(solution_1, solution_2):
    
    #Your Code Here
    
    return child_1, child_2
    
#4.2 d)
def generate_population(population_size):
    solutions = []
    for i in range(population_size):
        solutions.append(generate_random_solution())
    return solutions

def print_population(population):
    solutions = []
    for i in range(len(population)):
        print(f"Solution {i}: {population[i]}, {evaluate_solution(population[i])}")
    
def tournament_select(population, tournament_size):
        
    #Your Code Here
    
    return best_solution

def get_greatest_fit(population):
    best_solution = population[0]
    best_score = evaluate_solution(population[0])
    for i in range(1, len(population)):
        score = evaluate_solution(population[i])
        if score > best_score:
            best_score = score
            best_solution = population[i]
    return best_solution, best_score

def replace_least_fittest(population, offspring):
    least_fittest_index = 0
    least_fittest_value = evaluate_solution(population[0])
    for i in range(1, len(population)):
        score = evaluate_solution(population[i])
        if score < least_fittest_value:
            least_fittest_value = score
            least_fittest_index = i
    population[least_fittest_index] = offspring

def roulette_select(population):
    #Your Code Here
    pass
        
#4.2 e)
def mutate_solution_1(solution):
    index_1 = np.random.randint(0, len(solution))
    index_2 = (index_1 + np.random.randint(0, len(solution))) % (len(solution) - 1) # Efficient way to generate a non-repeated index
    solution[index_1], solution[index_2] = solution[index_2], solution[index_1]
    return solution

def mutate_solution_2(solution):
    index = np.random.randint(0, len(solution))
    solution[index] = np.random.randint(1, slots + 1)
    return solution

def mutate_solution_3(solution):
    return (get_neighbor_solution3(solution))

#4.3 f)       

def genetic_algorithm(num_iterations, population_size, crossover_func, mutation_func, log=False):
    population = generate_population(population_size)
    
    best_solution = population[0] # Initial solution
    best_score = evaluate_solution(population[0])
    best_solution_generation = 0 # Generation on which the best solution was found
    
    generation_no = 0
    
    print(f"Initial solution: {best_solution}, score: {best_score}")
    
    while(num_iterations > 0):
        
        generation_no += 1
        
        tournment_winner_sol = tournament_select(population, 4)
        roulette_winner_sol = roulette_select(population)
        
        # Next generation Crossover and Mutation
        
        #Your Code Here
        
        # Checking the greatest fit among the current population
        greatest_fit, greatest_fit_score = get_greatest_fit(population)
        if greatest_fit_score > best_score:
            best_solution = greatest_fit
            best_score = greatest_fit_score
            best_solution_generation = generation_no
            if log:
                print(f"\nGeneration: {generation_no }")
                print(f"Solution: {best_solution}, score: {best_score}")
                print_population(population)
        else:
            num_iterations -= 1
        
    print(f"  Final solution: {best_solution}, score: {best_score}")
    print(f"  Found on generation {best_solution_generation}")
    
    return best_solution