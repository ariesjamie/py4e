import copy
import random

class Hat:
    def __init__(self, **kwargs):                           # hat1 = Hat(yellow=3, blue=2, green=6)
        self.contents = []
        for key, value in kwargs.items():                   # for key, value in {"yellow":3, "blue":2, "green":6}
            for _ in range(value):
                self.contents.append(key)
        print(self.contents)

    def draw(self, num_balls_drawn):
        draw_balls_list = []
        if num_balls_drawn > len(self.contents):
            return self.contents
        else:
            for _ in range(num_balls_drawn):
                balls_index = random.randrange(len(self.contents))         ## pick one to remove it from the self.contents
                ##print("index:",balls_index)
                # balls_pick = self.contents[balls_index]
                # print("pick:",balls_pick)
                # self.contents.pop(balls_index)
                # print(self.contents)
                draw_balls_list.append(self.contents.pop(balls_index))                         ## add one to add it to the draw balls list
                # print(self.contents)
            return draw_balls_list
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    initial_contents = copy.deepcopy(hat.contents)  
    expected_balls_count_M = 0

    for _ in range(num_experiments):

        # pick balls
        hat.contents = copy.deepcopy(initial_contents)
        # hat.contents = initial_contents
        drawn_result = hat.draw(num_balls_drawn)

        # convert list to dict
        drawn_result_dict = convert_to_dict(drawn_result)
        print(drawn_result_dict)

        # compare two dicts
        numbers_compare = len(expected_balls)
        for key, value in expected_balls.items():
            # print(key, value)
            if key in drawn_result_dict and value <= drawn_result_dict[key]:
                numbers_compare -= 1

        if numbers_compare == 0:
            expected_balls_count_M += 1

    print(expected_balls_count_M)
    return expected_balls_count_M/num_experiments



    # return num_valid_experiments / num_experiments

def convert_to_dict(list):
    dict = {}
    for item in list:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    return dict 


hat = Hat(yellow=3, blue=2, green=6, red = 5)
# hat_draw = hat.draw(3)
# print(hat_draw)

experiment(hat, {"red":2,"green":2}, 5, 2000)
