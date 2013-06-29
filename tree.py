import json
from pprint import pprint

class TreeNode(object):
    pass


class YesNo(TreeNode):
    def __init__(self, name, question, y_node, n_node):
        self.name     = name
        self.question = question
        self.y_node   = y_node
        self.n_node   = n_node

    def __repr__(self):
        return "YesNo(name={}, question='{}')".format(self.name, self.question)


class Leaf(TreeNode):
    def __init__(self, name, display):
        self.name = name
        self.display = display

    def __repr__(self):
        return "Leaf(name={}, display='{}')".format(self.name, self.display)


def parse_tree(data):
    # this exists to prevent double-loading while processing dependencies.
    nodes = {}

    # returns the node and puts in the node in nodes
    # only parses if key is not already in nodes
    def parse_key(key):
        # avoid parsing twice
        if key in nodes:
            return nodes[key]

        raw_node = data[key]
        if raw_node['type'] == 'y/n':
            # print 'WARN: skipping y/n'
            # nodes[key] = {
            #     'type': 'y/n',
            #     'name': raw_node['name'],
            #     'question': raw_node['question'],
            #     'y-to': parse_key(raw_node['y-to']),
            #     'n-to': parse_key(raw_node['y-to']),
            # }
            nodes[key] = YesNo(raw_node['name'], raw_node['question'],
                parse_key(raw_node['y-to']),
                parse_key(raw_node['n-to']))
        elif raw_node['type'] == 'leaf':
            # print 'WARN: skipping leaf'
            # nodes[key] = {
            #     'type': 'leaf',
            #     'name': raw_node['name'],
            #     'display': raw_node['display'],
            # }
            nodes[key] = Leaf(raw_node['name'], raw_node['display'])
        else:
            raise ValueError("Unrecognized node type '#{}'".format(raw_node['type']))

    map(parse_key, data.iterkeys())
    return nodes


def load_tree(data_path):
    with open(data_path, 'r') as f:
        data = json.load(f)
        return parse_tree(data)


if __name__ == "__main__":
    data_path = 'tree.json'
    nodes = load_tree(data_path)
    pprint(nodes)
    print nodes['parens'].y_node
    print nodes['parens'].y_node.display
