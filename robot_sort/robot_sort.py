import time

RETURN_LIST_TO_SORT_ = """
brainstorm:
Go through each place and find the largest/smallest of the rest to put there:
Go as right as possible
Pick up
While can move left is true, move left checking for a larger number
    if a larger number is found, swap and keep going left
Once the end is reached, bring the holding number to the empty spot
    Use iteration to count however many places gone left and go back right that many


go to right most num and pick up, go to left most and start comparing
    if holding_num > checking_num: move right
    else swap item
    repeat


def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        current_num = list_to_sort[i]
        j = i
        while j > 0 and current_num < list_to_sort[j-1]:
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        list_to_sort[j] = current_num
    return list_to_sort
"""


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)
    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1
    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0
    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            # print(f'moved right to pos {self._position}')
            return True
        else:
            # print(f'cant move right')
            return False
    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            # print(f'moved left to pos {self._position}')
            return True
        else:
            # print(f'cant move left')
            return False
    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        # print(f'swapping {self._item} and {self._list[self._position]}')
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item
    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        # print(f'comparing {self._item} to {self._list[self._position]}')
        if self._item is None or self._list[self._position] is None:
            # print(f'one of them is none')
            return None
        elif self._item > self._list[self._position]:
            # print(f'self item is larger than item in list')
            return 1
        elif self._item < self._list[self._position]:
            # print(f'self item is smaller than item in list')
            return -1
        else:
            # print(f'theyre equal')
            return 0
    def set_light_on(self):
        """
        Turn on the robot's light
        """
        # print(f'light was {self._light} and is now ON')
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        # print(f'light was {self._light} and is now OFF')
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def recursive_checking(self):
        # to move left all the way to find a bigger item, then move back right and put item there
        # print(f'\npos: {self._position}. holding: {self._item}. item at pos: {self._list[self._position]}. time: {self._time}')
        # print(f'list: {self._list}')
        # move left
        if self.can_move_left():
            # print(f'can move left')
            self.move_left()
        else:
            # print(f"can't move left, returning")
            return
        # if item in front is larger than held item, swap
        temp_var = self.compare_item()
        if temp_var == -1:
            self.swap_item()
        # elif temp_var == -1 or temp_var == 0:
        # call self again
        self.recursive_checking()
        # move right
        self.move_right()

    def sort(self):
        # print(f'sorting {self._list}')

        # start by going all the way to the right
        while self.can_move_right():
            self.move_right()
        # self._position = 99

        while not self.light_is_on():
            # swap so robot is holding the last unsorted item
            self.swap_item()
            # print(f'\nrunning recursive checking on list {self._list}:')
            # run recursive_checking
            self.recursive_checking()
            # print(f'finished recursive checking\n')
            self.swap_item()
            if self.can_move_left() is not True:
                self.set_light_on()
            else:
                self.move_left()

        # print(f'done??? {self._list}')


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    start_time = time.time()

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    # l = [5, 2, 3, 1, 4]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
    end_time = time.time()
    print(f"runtime: {end_time - start_time} seconds")
