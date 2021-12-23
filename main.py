import random

from objects.manipulation import Mutations, tournament, crossover
from objects.populate import GreedyAlgorithm, PathCalc


def main():

    """POPULATING FROM SPECIFIED FILE"""
    population = []

    population = \
        GreedyAlgorithm.calculate(
            GreedyAlgorithm.parse(
                './coordinates_files/berlin11_modified.tsp'
            )
        )

    # How many randomly ordered coordinates should be used to populate
    for x in range(0, 150):
        data = PathCalc.parse_random_cords_order(
            './coordinates_files/berlin11_modified.tsp'
        )

        res = PathCalc.calculate_cords_increasing_order(data)
        population.append(res)

    """START OF GENETIC ALGORITHM"""
    pop_one = population.copy()
    pop_two = []
    population = sorted(population)
    # print(population)
    best_result = population[0]
    generation = 0

    while generation < 100:
        while len(pop_two) != len(pop_one):
            parent1 = tournament(pop_one, 20)
            parent2 = tournament(pop_one, 20)
            if random.randint(0, 1) == 1:
                subject = crossover(parent1, parent2)
            else:
                subject = parent1.copy()
            if random.randint(0, 20) == 5:
                subject = Mutations.inversion(subject).copy()

            if best_result[0] > subject[0]:
                best_result = subject.copy()

            pop_two.append(subject)

        generation += 1
        pop_one = pop_two.copy()
        pop_two = []

    # For pretty output
    output = []
    for point in best_result[1:]:
        output.append(point[0])

    print(f'The best path is: {output} \n'
          f' Where total distance is equal to: {best_result[0]}')


if __name__ == '__main__':

    main()
