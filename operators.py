import bpy
import itertools
from bpy.types import Operator

from . import utils

            
class RECENTER_NODES_OT_MAIN_OPERATOR(Operator):
    bl_label = "Recenter Nodes"
    bl_idname = "recenter_nodes.main_operator"
    bl_description = "Repositions nodetree such that its midpoint is at the origin"
    bl_options = {'REGISTER','UNDO_GROUPED'}

    @classmethod
    def poll(cls, context):
        return True

    def set_to_origin(self, nodetree):
        nodetree_name, nodetree_type, nodes = nodetree
        logging_type = utils.fetch_user_preferences().logging_messages

        if not nodes:
            if logging_type == "ALL":
                print(f"CANCELLED: No nodes detected in {nodetree_type} - '{nodetree_name}'.")
            return

        with utils.TemporaryUnframe(nodes):
            midpoint_x, midpoint_y = utils.get_bounds_midpoint(nodes)

            if midpoint_x == 0 and midpoint_y == 0:
                if logging_type == "ALL":
                    print(f"CANCELLED: {nodetree_type} '{nodetree_name}' already centered.")                
                return
            
            for node in nodes:
                node.location.x -= midpoint_x
                node.location.y -= midpoint_y

        if logging_type != "NONE":
            print(f"SUCCESSFUL: Successfully recentered {nodetree_type} - '{nodetree_name}'.")

        return

    @staticmethod
    def fetch_nodetrees(context):
        data = context.blend_data

        compositor_nodetrees = ((scene.name, scene.node_tree.bl_idname, scene.node_tree.nodes) for scene 
            in data.scenes if hasattr(scene, "node_tree") and (scene.node_tree is not None))

        material_nodetrees = ((material.name, material.node_tree.bl_idname, material.node_tree.nodes) for material 
            in data.materials if hasattr(material, "node_tree") and (material.node_tree is not None))

        world_nodetrees = ((world.name, world.node_tree.bl_idname, world.node_tree.nodes) for world 
            in data.worlds if hasattr(world, "node_tree") and (world.node_tree is not None))
        
        linestyle_nodetrees = ((linestyle.name, linestyle.node_tree.bl_idname, linestyle.node_tree.nodes) for linestyle 
            in data.linestyles if hasattr(linestyle, "node_tree") and (linestyle.node_tree is not None))

        texture_nodetrees = ((texture.name, texture.node_tree.bl_idname, texture.node_tree.nodes) for texture 
            in data.textures if hasattr(texture.node_tree, "nodes") and (texture.node_tree is not None))
        
        nodegroups_and_geonodes = ((group.name, group.bl_idname, group.nodes) for group 
            in data.node_groups if hasattr(group, "nodes"))

        return itertools.chain(compositor_nodetrees, material_nodetrees, world_nodetrees,
            linestyle_nodetrees, texture_nodetrees, nodegroups_and_geonodes)

    def execute(self, context):
        context.window.cursor_set('WAIT')

        for nodetree in self.fetch_nodetrees(context):
            self.set_to_origin(nodetree)

        context.window.cursor_set('DEFAULT')
        return {'FINISHED'}


def register():
    bpy.utils.register_class(RECENTER_NODES_OT_MAIN_OPERATOR)

def unregister():
    bpy.utils.unregister_class(RECENTER_NODES_OT_MAIN_OPERATOR)