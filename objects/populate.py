import random
from math import sqrt


def get_distance_full_path(path):
    total = 0
    for index, cord in enumerate(path):
        # Check if index is in range
        if index + 1 >= len(path):
            break
        # Calculate the distance between two points
        else:
            distance = sqrt((float(path[index + 1][1]) - float(cord[1])) ** 2 +
                            (float(path[index + 1][2]) - float(cord[2])) ** 2)

            total += distance  # Add to the total distance value

    return total


class GreedyAlgorithm:

    @staticmethod
    def get_distance_single_point(c1, c2):

        res = sqrt((float(c1[1]) - float(c2[1]))**2
                   + (float(c1[2]) - float(c2[2]))**2)
        return res

    # Extract coordinates from the file
    @staticmethod
    def parse(file_path):
        with open(file_path, 'r+') as temp_file:
            lines = temp_file.readlines()
            cords = []
            for line in lines:
                if line[0].isdigit():
                    cords.append(line.split()[0:3])
            temp_file.close()

            # Return nested list of coordinates i.e [[12,34], [34,23]...]
            # print(cords)
            return cords

    # Calculate distance using greedy algorithm

    @staticmethod
    def calculate(cords_list):

        cords_list_backup = cords_list.copy()
        full_road = []

        for i in range(0, len(cords_list)):

            if len(cords_list) == 0:
                break
            # Starting from random city
            total = 0
            start_city = cords_list[i]
            path = [start_city]
            cords_list.remove(start_city)

            # Loop trough cities added to path, continuous loop until all cities are visited
            for city in path:
                # print(f'We are now going from {city}')
                distances = {}

                # Check if there are cities left to visit
                if len(cords_list) == 0:
                    break

                # Loop trough every city in cords list to find the shortest path
                for decision in cords_list:

                    distance = GreedyAlgorithm.get_distance_single_point(decision, city)

                    # Add distance to the city with its instance index
                    distances[decision[0]] = distance

                # Get the shortest path from the dictionary
                closest_city = min(distances, key=distances.get)
                total += distances[closest_city]

                # Find the closest city in cords list, append it to path and remove from
                # cords
                for x in cords_list:
                    if x[0] == closest_city:
                        path.append(x)
                        cords_list.remove(x)
                        break

            path.append(start_city)
            final_length = get_distance_full_path(path)
            path.insert(0, final_length)

            full_road.append(path)
            cords_list = cords_list_backup.copy()
        return full_road


# PathCalc shuffles cords from the file, and calculates their
# path going through indexes of shuffled
# coordinates

class PathCalc:

    # Extract coordinates from the file
    @staticmethod
    def parse_random_cords_order(file_path):
        with open(file_path, 'r+') as temp_file:
            lines = temp_file.readlines()
            cords = []
            for line in lines:
                if line[0].isdigit():
                    cords.append(line.split()[0:3])
            temp_file.close()

            # Return nested list of coordinates i.e [[12,34], [34,23]...]
            random.shuffle(cords)
            return cords

    # Calculate distance going in index order
    @staticmethod
    def calculate_cords_increasing_order(cords_list_inp):
        cords_list = list(cords_list_inp)
        total = 0
        cords_list.append(cords_list[0])

        total = get_distance_full_path(cords_list)

        cords_list.insert(0, total)
        return cords_list

