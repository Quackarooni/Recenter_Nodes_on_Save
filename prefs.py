import bpy
from bpy.props import EnumProperty


class RecenterAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    logging_messages: EnumProperty(
        name='Debug Messages',
        items=(
            ('NONE', 'None', 'No messages will be printed in system console'),
            ('MINIMAL', 'Minimal', 'Prints out successful recentering operations'),
            ('ALL', 'All', 'Prints out both successful and cancelled recentering operations',),
        ),
        default='NONE',
        description='Specifies the info printed in the system console during recentering',
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'logging_messages')


def register():
    bpy.utils.register_class(RecenterAddonPreferences)


def unregister():
    bpy.utils.unregister_class(RecenterAddonPreferences)
