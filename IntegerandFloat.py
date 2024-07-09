# calculator saga

# learning basic arithmetic operations and the difference between int and float in terms of memory
import tracemalloc
class BasicCalculator:
    def __init__(self, option):
        self.option = option
    
    def operation(self, n1, n2):
        if self.option == 1:
            return n1 + n2
        elif self.option == 2:
            return n1 - n2
        elif self.option == 3:
            return n1 * n2
        elif self.option == 4:
            return n1 / n2
        elif self.option == 5:
            return n1 // n2
        elif self.option == 6:
            return n1 % n2
        else:
            return "Invalid Option"  
    def int_operation(self, int_n1, int_n2):
        if isinstance(int_n1, int) & isinstance(int_n2, int):
            return self.operation(int_n1, int_n2)
        else:
            return "Invalid Number"
    def float_operation(self, float_n1, float_n2):
        if isinstance(float_n1, float) & isinstance(float_n2, float):
            return self.operation(float_n1, float_n2)
        else:
            return "Invalid Number"

# statistical calculations along with explaining usage of int for indexing and comparison instead of float, and float for precision value instead of int
import scipy
from collections import Counter
import statistics

class StatisticalCalculator:
    def __init__(self, option):
        self.option = option
    
    def operation(self, list_l):
        if self.option == 1:
            #central tendency - mean, median, mode
            mean = sum(list_l)/len(list_l)
            sorted_list = sorted(list_l)
            n = len(sorted_list)
            mid = n // 2
            if n % 2 == 0:
                median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
            else:
                median = sorted_list[mid]
            data = Counter(list_l)
            mode = dict(data.most_common())
            return f"mean: {mean}\nmedian: {median}\nmode: {mode}"
        elif self.option == 2:
            #variability inter-quartile range- (25%, 50%, 75% quartiles)
            range = max(list_l) - min(list_l)
            quantiles = statistics.quantiles(list_l, n=4)
            return f"range: {range}\nquantiles: {quantiles}\n"
        elif self.option == 3:
            #standard deviation
            std = statistics.stdev(list_l)
            return f"standard deviation: {std}"
        elif self.option == 4:
            #variance
            variance = statistics.variance(list_l)
            return f"variance: {variance}"
        elif self.option == 5:
            #skewness
            return scipy.stats.skew(list_l, axis=0)
        elif self.option == 6:
            #kurtosis
            return scipy.stats.kurtosis(list_l, axis=0)
        else:
            return "Invalid Option"

#using float for scientific calculations to ensure precision
import math
class ScientificCalculator:
    def __init__(self):
        pass
    def exponential_growth(self, initial: float, growth_rate: float, time: float):
        final = initial*math.exp(growth_rate*time)
        return f"If {growth_rate:.2f} growth rate is compounded for {time:.2f} days then the final growth after mentioned days will be {(final - initial):.2f}, with final being {final:.2f}"
    def identify_exponential_growth(self, data):
        growth_rates = [data[i]/data[i-1] for i in range(1, len(data))]
        count = Counter(growth_rates)
        mode_growth = dict(count.most_common())
        growth = []
        for key, value in mode_growth.items():
            if value  > 1:
                growth.append(key)
        growth_segment = []
        for mode in growth:
            for i, data_gr in enumerate(growth_rates):
                if data_gr == mode:
                    start = data[i+1]
                    break
            for i, data_gr in enumerate(reversed(growth_rates)):
                if data_gr == mode:
                    end = data[(len(growth_rates)- i)]
                    break
            growth_segment.append([start, end, mode])
        return growth_segment
    def logarithmic_scale_for_data_representation(self, data):
        scaled_data = []
        for i in data:
            if i > 0:
                scaled_data.append(math.log10(i))
            else:
                scaled_data.append(0)
        return f"{scaled_data} - all 0s are negative and unexpected values for logarithmic scaling"
    def half_life_decay(self, initial_amount: float, time: float, half_life:float):
        final = initial_amount*(1/2)**(time/half_life)
        return f"{final} amount is expected to not decay after {time} days, assuming half-life of it is {half_life} days"

if __name__ == "__main__":
    calc_option = int(input(
        "Choose your calculator:\n1. Basic Calculator\n2. Statistic Calculator\n3. Scientific Calculator\n\n"
    ))
    if calc_option == 1:
        operation_option = int(input("Choose your operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division(ans in float)\n5. Floor Division(ans in int)\n6. Modulus\n\n"))
        if operation_option in range(1, 7):
            calc = BasicCalculator(operation_option) 
            number_option = int(input("Choose to perform 0. Int or 1. Float operation\n\n"))
            if number_option == 0:
                n1 = int(input("Enter first number: "))
                n2 = int(input("Enter second number: "))
                tracemalloc.start()
                print(calc.int_operation(n1, n2))
                print(tracemalloc.get_traced_memory())
                tracemalloc.stop()
            elif number_option == 1:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
                tracemalloc.start()
                print(calc.float_operation(n1, n2))
                print(tracemalloc.get_traced_memory())
                tracemalloc.stop()
            else:
                print("Invalid option")
        else:
            print("Invalid Option")
    elif calc_option == 2:
        operation_option = int(input("Choose your operation:\n1. Central Tendency\n2. Variability\n3. Standard Deviation\n4. Variance\n5. Skewness\n6. Kurtosis\n\n"))
        if operation_option in range(1, 7):
            list_l = list(map(int, input("Enter the list of numbers with space: ").split()))
            calc = StatisticalCalculator(operation_option)
            tracemalloc.start()
            print(calc.operation(list_l))
            print(f"memory: {tracemalloc.get_traced_memory()[1] - tracemalloc.get_traced_memory()[0]}")
            tracemalloc.stop()
        else:
            print("Invalid Option")
    elif calc_option == 3:
        calc = ScientificCalculator()
        operation_option = int(input("Choose your operation:\n1. Exponential Growth\n2. Identify Exponential Growth\n3. Logarithmic Scaling for Data Representation\n4. Half-life Decay\n\n"))
        if operation_option == 1:
            initial = float(input("Enter initial amount: "))
            growth_rate = float(input("Enter growth rate: "))
            time = float(input("Enter time: "))
            print(calc.exponential_growth(initial, growth_rate, time))
        elif operation_option == 2:
            data = list(map(float, input("Enter the list of data: ").split()))
            print(calc.identify_exponential_growth(data))
        elif operation_option == 3:
            data = list(map(float, input("Enter the list of data: ").split()))
            print(calc.logarithmic_scale_for_data_representation(data))
        elif operation_option == 4:
            initial_amount = float(input("Enter initial amount: "))
            time = float(input("Enter time: "))
            half_life = float(input("Enter half-life: "))
            print(calc.half_life_decay(initial_amount, time, half_life))
        else:
            print("Invalid Option")
    else:
        print("Invalid Option")
#### will add GUI later (maybe)