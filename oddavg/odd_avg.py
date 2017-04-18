# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

class OddAvg():
    def odd_average(self, number_list):
        self.number_list = number_list
        counter = 0
        sum_numbers = 0
        average = 0
        for number in self.number_list:
            if number % 2 == 0:
                counter += 1
                sum_numbers += number
                average = sum_numbers/counter
        return average
