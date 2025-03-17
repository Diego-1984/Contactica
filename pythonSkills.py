class CreateList():
    def __init__(self, element):
        self.element = element
    def add_element(self, element):
        self.element.append(element)
    def remove_element(self, element):
        self.element.remove(element)
    def reset(self):
        self.element.clear()
    def max_sum_sublist(self):
        data_copy = self.data[:]  
        data_copy_reversed = self.data[::-1]
        prefix_sums = [sum(self.data)]
        suffix_sums = [sum(self.data)]
        
        # Max aum value from left to right
        for _ in range(len(self.data)-1):
            data_copy.pop(-1)
            prefix_sums.append(sum(data_copy))        
        
        # Max aum value from right to left
        for _ in range(len(self.data)-1):
            data_copy_reversed.pop(-1)
            suffix_sums.append(sum(data_copy_reversed))
        
        max_prefix_sum = max(prefix_sums)
        max_suffix_sum = max(suffix_sums)
        
        if max_prefix_sum >= max_suffix_sum:
            max_index = prefix_sums.index(max_prefix_sum)
            return [max_prefix_sum, self.data[:len(self.data)-max_index]]
        else:
            max_index2 = suffix_sums.index(max_suffix_sum)
            return [max_suffix_sum, self.data[len(self.data)-max_index2-1:]][::-1]   
            
    
example = CreateList([1, 2, 3,-2, 5, -3])
print(example.element)

example.max_sum_sublist()
print(example.element)

example.add_element(4)
print(example.element)

example.remove_element(3)
print(example.element)

example.max_sum_sublist()
print(example.element)

example.reset()
print(example.element)