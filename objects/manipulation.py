import random

from .populate import PathCalc


class Mutations:

    @staticmethod
    def swap(pop):
        position = random.randint(0, len(pop)-1)
        subject = pop[position]

        print(f'Before mutation: {subject}')

        subject.pop()
        swap_one = random.randint(1, int(len(subject) / 2))
        swap_two = random.randint(swap_one + 1, len(subject) - 1)

        print(f'Swap one is: {swap_one}, swap two is: {swap_two}')

        subject[swap_one], subject[swap_two] = subject[swap_two], subject[swap_one]

        res = PathCalc.calculate_cords_increasing_order(subject[1:])
        print(f'After mutation: {res}')

        return res

    @staticmethod
    def inversion(pop):
        start_cut, end_cut = get_random_slice_numbers(len(pop))
        res = pop.copy()
        res[start_cut:end_cut] = res[start_cut:end_cut][::-1]

        res.remove(res[0])
        dist = PathCalc.calculate_cords_increasing_order(res)[0]
        res.insert(0, dist)

        return res


def tournament(pop, c):
    warriors = []
    pool = pop.copy()
    for _ in range(0, c):

        random_choice = random.randint(0, len(pool) - 1)
        warriors.append(pop[random_choice])
        pool.remove(pool[random_choice])

    current_warrior = warriors[0]
    for unit in warriors:
        if current_warrior[0] > unit[0]:
            current_warrior = unit.copy()

    # print(current_warrior)
    return current_warrior


def get_random_slice_numbers(length_of_path):
    random_point_one = random.randint(1, length_of_path - 2)
    random_point_two = random.randint(1, length_of_path - 1)

    if random_point_one == random_point_two:
        start_cut = random_point_one
        end_cut = random_point_two

    elif random_point_one < random_point_two:
        start_cut = random_point_one
        end_cut = random_point_two

    else:
        start_cut = random_point_two
        end_cut = random_point_one

    return start_cut, end_cut


def crossover(u1, u2):
    # print(f'first list is {u1} \n second list is {u2}')
    start_cut, end_cut = get_random_slice_numbers(len(u1))
    # print(start_cut, end_cut)
    cut = u1[start_cut:end_cut]
    x = [x for x in u2 if x not in cut]
    for element in cut:
        x.insert(start_cut, element)
        start_cut += 1
    if x[-1] != x[1]:
        x.append(x[1])

    x.remove(x[0])
    dist = PathCalc.calculate_cords_increasing_order(x)[0]
    x.insert(0, dist)
    # print(x, len(x))
    return x
