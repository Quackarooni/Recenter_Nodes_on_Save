import bpy

weird_offset = 10
reroute_width = 10


class TemporaryUnframe:
    def __init__(self, nodes):
        self.parent_dict = {}
        for node in nodes:
            if node.parent is not None:
                self.parent_dict[node] = node.parent
            node.parent = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        for node, parent in self.parent_dict.items():
            node.parent = parent


def fetch_user_preferences(attr_id=None):
    prefs = bpy.context.preferences.addons[__package__].preferences

    if attr_id is None:
        return prefs
    else:
        return getattr(prefs, attr_id)


def get_width(node):
    if node.bl_idname == 'NodeReroute':
        return reroute_width
    else:
        return node.width


def get_height(node):
    if node.bl_idname == 'NodeReroute':
        return reroute_width
    else:
        return node.height


def get_left(node):
    if node.bl_static_type == 'REROUTE':
        return node.location.x
    else:
        return node.location.x


def get_center(node):
    if node.bl_static_type == 'REROUTE':
        return node.location.x
    else:
        return node.location.x + (0.5 * node.width)


def get_right(node):
    if node.bl_static_type == 'REROUTE':
        return node.location.x
    else:
        return node.location.x + node.width


def get_top(node):
    if node.bl_static_type == 'REROUTE':
        return node.location.y
    elif node.hide:
        return node.location.y + (0.5 * get_height(node)) - weird_offset
    else:
        return node.location.y


def get_middle(node):
    if node.bl_static_type == 'REROUTE':
        return node.location.y
    elif node.hide:
        return node.location.y - weird_offset
    else:
        return node.location.y - (0.5 * get_height(node))


def get_bottom(node):
    if node.bl_static_type == 'REROUTE':
        return node.location.y
    elif node.hide:
        return node.location.y - (0.5 * get_height(node)) - weird_offset
    else:
        return node.location.y - get_height(node)


def get_bounds(nodes):
    if len(nodes) <= 0:
        return 0, 0, 0, 0

    min_x = min(get_left(node) for node in nodes)
    max_x = max(get_right(node) for node in nodes)
    min_y = min(get_bottom(node) for node in nodes)
    max_y = max(get_top(node) for node in nodes)

    return min_x, max_x, min_y, max_y


def get_bounds_midpoint(nodes):
    nodes = tuple(n for n in nodes if n.bl_idname != 'NodeFrame')

    min_x, max_x, min_y, max_y = get_bounds(nodes)
    midpoint_x = 0.5 * (min_x + max_x)
    midpoint_y = 0.5 * (min_y + max_y)

    return midpoint_x, midpoint_y
