import csv
from sys import argv
from contract import *


def parse(path):
    candidates = []

    with open(path) as File:
        register = csv.reader(File)
        for row in register:
            c = Contract(row[0], int(row[1]), int(row[2]))
            if 0 <= c.start() <= 167 and 0 <= c.end() <= 167 and c.start() != c.end():
                candidates.append(c)
    return candidates


def get_contracts(contracts):
    contracts.sort(key=lambda x: x.end())
    smax = []
    for i in range(len(contracts)):
        contracts_copy = rotate(contracts.copy(), -i)
        contracts_copy = remove_incompatible_contracts(contracts_copy, contracts_copy[0])

        s = max_subset(contracts_copy)

        if len(s) > len(smax):
            smax = s

    return smax


def max_subset(contracts):
    s = [contracts[0]]
    for i in range(1, len(contracts)):

        if not are_incompatible(contracts[i], s[-1]):
            s.append(contracts[i])

    return s


def write_output(list):
    with open('salida.txt', 'w') as File:
        for candidate in list:
            File.write(candidate.name() + '\n')


def are_incompatible(a_contract, another_contract):
    if a_contract.name() == another_contract.name():
        return False
    return a_contract.is_incompatible_with(another_contract) or another_contract.is_incompatible_with(a_contract)


def remove_incompatible_contracts(a_list_of_contracts, a_contract):
    return [x for x in a_list_of_contracts if not are_incompatible(a_contract, x)]


def rotate(l, n):
    return l[-n:] + l[:-n]


def main():
    assert len(argv) == 2

    candidates = parse(argv[1])
    accepted = get_contracts(candidates)
    write_output(accepted)


main()
