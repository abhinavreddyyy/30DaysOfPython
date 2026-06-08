class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def mean(self):
        return sum(self.numbers) / len(self.numbers)
    
    def median(self):
        sorted_numbers = sorted(self.numbers)

        if len(sorted_numbers) % 2 == 0:
            mid1 = len(sorted_numbers) // 2 - 1
            mid2 = len(sorted_numbers) // 2
            return (sorted_numbers[mid1] + sorted_numbers[mid2]) / 2
        else:
            mid = len(sorted_numbers) // 2
            return sorted_numbers[mid]
    
    def count(self):
        return len(self.numbers)
    def sum(self):
        return sum(self.numbers)
    def min(self):
        return min(self.numbers)
    def max(self):
        return max(self.numbers)
    def range(self):
        return self.max() - self.min()
    def mode(self):
        frequency = {}
        for number in self.numbers:
            frequency[number] = frequency.get(number, 0) + 1
        
        max_freq = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_freq]
        
        return modes
    def variance(self):
        mean = sum(self.numbers) / len(self.numbers)
        return sum((x - mean) ** 2 for x in self.numbers) / len(self.numbers)
    
    def standard_deviation(self):
        variance = self.variance()
        return variance ** 0.5

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.standard_deviation()) # 4.2
print('Variance: ', data.variance()) # 17.5
