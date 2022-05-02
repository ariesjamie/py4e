
import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):               
                self.contents.append(key)
        

    def draw(self, num_balls_drawn):
        balls_drawn_list = []
        if num_balls_drawn > len(self.contents):
            return self.contents
        else:
            for _ in range(num_balls_drawn):
                draw_index = random.randrange(len(self.contents))
                balls_drawn_list.append(self.contents.pop(draw_index)) 
            return balls_drawn_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_copy = copy.deepcopy(hat.contents)
    expected_balls_count = 0
    for _ in range(num_experiments):
        hat.contents = copy.deepcopy(hat_copy)
        compare_num = len(expected_balls)
        hat_drawn = hat.draw(num_balls_drawn)
        # hat_experiment_dict = convert_to_dict(hat_drawn)
        hat_drawn_dict = Counter(hat_drawn)
        for key, value in expected_balls.items():
            if key in hat_drawn_dict and value < hat_drawn_dict[key]:
                compare_num -= 1    

        if compare_num == 0:
            expected_balls_count += 1
    return expected_balls_count / num_experiments


# def convert_to_dict(list):
#     dict = {}
#     for item in list:
#         if item in dict:
#             dict[item] += 1
#         else:
#             dict[item] = 1
#     return dict
