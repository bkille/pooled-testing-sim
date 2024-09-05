# DO NOT EDIT THIS FILE
# Copy this file and implement your own Protocol.isolate_positives method
#
# Create a new branch w/ your team name as the branch name
# git checkout -b your_team_name
#
# Add the file to the git repo
# git add your_file
#
# Commit it
# git commit your_file -m "A nice message"
#
# Push to your branch
# git push origin your_team_name
#
# Create a Pull Request whenever you're ready to test your method against others

from .utils import TestSample

class Protocol:
    def __init__(self, population_size: int, prevalence: float):
        self.n = population_size
        self.p = prevalence

 
    
    def isolate_positives(self, sample: TestSample) -> set:

        def recursive(low, high):
        
            is_pooled_positive = sample.query(set(range(low, high)))
            #Base case no positive 
            if not is_pooled_positive:
                return set()
            #Base case len=1 
            elif high-low == 1:
                return set(low)
            #Recursive step 
            else:
                midpoint = (low + high) // 2
                # Split into two subsets
                return recursive(low, midpoint).union(recursive(midpoint, high))
        
        if self.p > 0.5:
            return {i for i in range(self.n) if sample.query(set([i]))}
        else:
            return recursive(0, self.n)
                                      

        # Implement your strategy here.
        # Score : (1-p)^n , the higher the score, the more likely to consolidate
        # 
        # Your goal is to return the indices of the positive samples
        # while minimizing the number of calls to sample.query
        #
        # Not correctly identifying the set of positive samples results in disqualification!
        #
        # The input will be a TestSample object, which allows you to query
        # a subset of 0 ... n-1
        #
       
