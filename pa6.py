
def make_change(total):
    coins = [1, 5, 10, 25, 100]
    result = []

    def find_combinations(remaining, combo, start):
        if remaining == 0:
            result.append(combo[:])
            return
        for i in range(start, len(coins)):
            coin = coins[i]
            if remaining >= coin:
                combo.append(coin)
                find_combinations(remaining - coin, combo, i)
                combo.pop()
    
    find_combinations(total, [], 0)
    return result

def dict_filter(func, dictionary):
    filtered_dict = {}
    for key, value in dictionary.items():
        if func(key, value):
            filtered_dict[key] = value
    return filtered_dict

def checker(name, abbrev):
    return abbrev[0] == "I" and name[1] == "l"

class KVTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def treemap(func, tree):
    tree.key, tree.value = func(tree.key, tree.value)
    for child in tree.children:
        treemap(func, child)

class DTree:
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if (variable is not None and threshold is not None and
                lessequal is not None and greater is not None and outcome is None) or \
                (variable is None and threshold is None and
                 lessequal is None and greater is None and outcome is not None):
            self.variable = variable
            self.threshold = threshold
            self.lessequal = lessequal
            self.greater = greater
            self.outcome = outcome
        else:
            raise ValueError("invalid arguments combination")

    def tuple_atleast(self):
        def helper(node):
            if node is None:
                return 0
            var_size = 0 if node.variable is None else node.variable + 1
            return max(var_size, helper(node.lessequal), helper(node.greater))

        return helper(self)

    def find_outcome(self, observations):
        current_node = self
        while current_node.outcome is None:
            if observations[current_node.variable] <= current_node.threshold:
                current_node = current_node.lessequal
            else:
                current_node = current_node.greater
        return current_node.outcome

    def no_repeats(self):
        def helper(node, seen_variables):
            if node is None:
                return True
            if node.variable in seen_variables:
                return False
            seen_variables.add(node.variable)
            return helper(node.lessequal, seen_variables.copy()) and helper(node.greater, seen_variables.copy())

        return helper(self, set())
