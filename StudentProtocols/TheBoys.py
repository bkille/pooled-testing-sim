from .utils import TestSample

class Protocol:
    def __init__(self, population_size: int, prevalence: float):
        self.n = population_size
        self.p = prevalence

    def brute_force(self, sample: TestSample, length) -> set:
        return {i for i in range(length) if sample.query(set([i]))}

    def pool(self, min: int, max: int, groups: int):
        total_numbers = max - min + 1
        base_group_size = total_numbers // groups
        remainder = total_numbers % groups
        result = []
        start = min

        for i in range(groups):
            current_group_size = base_group_size + (1 if i < remainder else 0)
            group = list(range(start, start + current_group_size))
            result.append(group)
            start += current_group_size

        return result
    
    ## STRATEGY:
    # Two groups of 16
    # Split into groups of 4 
    # If any of the 4 positive, brute force 
    def isolate_positives(self, sample: TestSample) -> set:
        # Implement your strategy here.
        # 
        # Your goal is to return the indices of the positive samples
        # while minimizing the number of calls to sample.query

        # First pooling stage - split into 2 groups of 16
        res = set()
        pools = self.pool(0, self.n - 1, 2)

        if sample.query(pools[0]):
            # Second pooling stage - split into 4 groups of 4
            second_layer_pools = self.pool(0, (self.n - 1) // 2, 4)
            
            for pool in second_layer_pools:
                if sample.query(pool):
                    # Brute force
                    for s in pool:
                        if sample.query([s]):
                            res.add(s)
            
        if sample.query(pools[1]):
            # Second pooling stage - split into 4 groups of 4
            second_layer_pools_1 = self.pool(self.n // 2, self.n - 1, 4)
            for pool in second_layer_pools_1:
                if sample.query(pool):
                    for person in pool:
                        if sample.query([person]):
                            res.add(person)

        return res

