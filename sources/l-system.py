import math
from typing import List, Tuple
from matplotlib import markers
from numpy.core.defchararray import index
from numpy.lib.function_base import copy
import pylab
import numpy as np
import cmath
import copy


class Node:
    def __init__(self, z: complex, heading: float) -> None:
        self.z = z
        self.heading = heading


class Segment:
    def __init__(self, a: Node, b: Node) -> None:
        self.a = a
        self.b = b


class Segments(List[Segment]):
    def plot(self, pathfile: str) -> None:
        data_x = [[], []]
        data_y = [[], []]

        for item in self:
            data_x[0].append(item.a.z.real)
            data_y[0].append(item.a.z.imag)

            data_x[1].append(item.b.z.real)
            data_y[1].append(item.b.z.imag)

        pylab.figure(figsize=(5, 5))
        pylab.plot(
            data_x, data_y, c="black", marker="o", markersize=12, linestyle="dashed"
        )
        pylab.savefig("toto.png")


class Rule:
    def __init__(self, r: float, theta: float) -> None:
        self.r = r
        self.theta = theta

    def apply(self, node: Node) -> Node:
        return Node(
            node.z + cmath.exp(complex(self.r, node.heading + self.theta)),
            node.heading + self.theta,
        )


class Rules(List[Tuple[float, Rule]]):
    def __init__(self):
        self.max = 0

    def pick_one_roulette_wheel(self) -> Rule:
        p = np.random.uniform(0, self.max)
        for item in self:
            if item[0] > p:
                return item
        return self[-1]

    def pick_n_roulette_wheel(self, n: int) -> List[Rule]:
        rules = []
        for _ in range(n):
            pick = self.pick_one_roulette_wheel()
            # while pick in rules:
            #     print("x")
            #     pick = self.pick_one_roulette_wheel()
            rules.append(pick)
        return rules

    def append(self, item: Tuple[float, Rule]) -> None:
        self.max += item[0]
        return super().append(item)

    def get_max(self) -> float:
        return self.max


def build(root: Node, rules: Rules, budgets: int, segments: Segments) -> None:
    terminal = [root]
    budget = 0

    while budget < budgets:
        for item in range(0, len(terminal)):
            index_pick = item  # np.random.randint(0, len(terminal))
            pick = terminal[index_pick]

            del terminal[index_pick]

            rule = rules.pick_one_roulette_wheel()

            # list_of_rule = rules.pick_n_roulette_wheel(2)
            # for rule in list_of_rule:
            new_node = rule[1].apply(pick)
            segments.append(Segment(copy.deepcopy(new_node), copy.deepcopy(pick)))
            terminal.append(new_node)
        budget += 1


if __name__ == "__main__":
    np.random.seed(None)

    rules = Rules()
    # rules.append((0.2, Rule(1, math.pi / 4)))
    rules.append((0.7, Rule(1, math.pi / 2)))
    rules.append((0.7, Rule(1, 0)))
    # rules.append((0.2, Rule(1, -math.pi / 4)))

    segments = Segments()

    root = Node(complex(0, 0), math.pi / 2)

    # build(root, rules, 2, segments)
    uu = rules[0][1].apply(root)
    segments.append(Segment(root, uu))

    gg = rules[1][1].apply(root)
    # segments.append(Segment(root, gg))

    segments.plot("test.png")
    # segments.append(Segment(root, rules[0][1].apply(root)))
    # segments.append(Segment(root, rules[1][1].apply(root)))
