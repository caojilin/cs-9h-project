def tree(label,branches = []):
    for branch in branches:
        assert is_tree(branches)
    return [label] + list(branches)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def label(tree):
    return tree[0]

def print_tree(tree, indent=0):
    print('  ' * indent + str(label(tree)))
    for b in branches(tree):
        print_tree(b, indent+1)

def copy_tree(t):
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def make_tree(username):
    """

    """
    return tree(username,[tree(7,[tree(3),tree(6,[tree(5),tree(11)])]),tree(15)])
def make_pytunes(username):
    """
    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2015 pop mashup
      trance
        darude
          sandstorm
    """
    return tree(username,
                    [tree('pop',
                             [tree('justin bieber',
                                        [tree('single',
                                                [tree('what do you mean?')])])
                               ,tree('2015 pop mashup')])
                    ,tree('trance',[tree('darude',[tree('sandstorm')])])])
def num_songs(tree):
    if is_leaf(tree):
        return 1
    return sum([num_songs(b) for b in branches(tree)])

def find_path(tree, x):
    if label(tree) == x:
        return [x]
    node , trees = label(tree), branches(tree)
    for path in [find_path(b,x) for b in trees]:
        if path:
            return [node] + path

def tree_max(tree):
    if is_leaf(tree):
        return label(tree)
    else:
        return max([label(tree)]+ [tree_max(b) for b in branches(tree)])

def square_tree(t):
    if is_leaf(t):
        return tree(label(t) ** 2)
    return tree ( label(t) ** 2 , [square_tree(b) for b in branches(t)])

def replace_leaf(t,old,new):
    s = copy_tree(t)
    if is_leaf(s):
        if label(s) == old:
            return tree(new)
    return tree(label(s) ,[replace_leaf(b,old,new) for b in branches(s)])

def tree_height(t):
    if is_leaf(t):
        return 0
    return 1 + max([tree_height(b) for b in branches(t)])
