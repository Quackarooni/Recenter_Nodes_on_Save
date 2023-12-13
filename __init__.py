# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
bl_info = {
    "name": "Recenter Nodes on Save",
    "author": "Quackers",
    "description": "Centers all nodetrees on origin when blendfile is saved.",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Node Editor",
    "category": "Node",
}

from . import operators, prefs
modules = (operators, prefs)

import bpy
from bpy.app.handlers import persistent


@persistent
def execute_on_save(dummy):
    bpy.ops.recenter_nodes.main_operator('EXEC_DEFAULT')


def register():
    for module in modules:
        module.register()

    bpy.app.handlers.save_pre.append(execute_on_save)


def unregister():
    for module in modules:
        module.unregister()

    bpy.app.handlers.save_pre.remove(execute_on_save)


if __name__ == "__main__":
    register()
