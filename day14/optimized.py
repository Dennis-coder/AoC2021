def refactor_indata(indata):
    polymer_template, pair_insertions = indata.split("\n\n")
    pair_insertions = [x.split(" -> ") for x in pair_insertions.split("\n")]
    return (polymer_template, pair_insertions)

def calc(indata, iterations):
    polymer_template, pair_insertions = indata
    new_val = dict(pair_insertions)
    pairs = dict([[x[0], [x[0][0] + x[1], x[1] + x[0][1]]] for x in indata[1]])

    count_pairs = {}
    for i in range(len(polymer_template) - 1):
        pair = polymer_template[i] + polymer_template[i+1]
        if pair in count_pairs:
            count_pairs[pair] += 1
        else:
            count_pairs[pair] = 1

    count = {}
    for char in polymer_template:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for _ in range(iterations):
        new_count_pairs = {}
        for pair in count_pairs.keys():
            if new_val[pair] in count:
                count[new_val[pair]] += count_pairs[pair]
            else:
                count[new_val[pair]] = count_pairs[pair]
            for new_pair in pairs[pair]:
                if new_pair in new_count_pairs:
                    new_count_pairs[new_pair] += count_pairs[pair]
                else:
                    new_count_pairs[new_pair] = count_pairs[pair]
        count_pairs = new_count_pairs

    most_common = max(count, key=count.get)
    least_common = min(count, key=count.get)
    return count[most_common] - count[least_common]

def calc_a(indata):
    return calc(indata, 10)

def calc_b(indata):
    return calc(indata, 40)