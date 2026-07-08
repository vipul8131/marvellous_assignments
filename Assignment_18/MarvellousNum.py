def ChkPrime(no):
    facts = []
    for i in range(2, no+1):
        if no % i == 0:
            facts.append(i)
    # print(facts)
    if len(facts) == 1:
        return True
    else:
        return False
            