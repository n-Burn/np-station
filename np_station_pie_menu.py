# Install this as a regular add-on, do not copy this into the NP Station
# directory. Make sure NP Station is intalled and enabled before trying to
# enable this add-on. Pie menu opened in 3D view with: CTRL + Shift + Space

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

# <pep8 compliant>

bl_info = {
    "name": "NP Station Pie Menu",
    "author": "qweqwe",
    "version": (0, 0, 2),
    "blender": (2, 75, 0),
    "description": "Pie menu for Np Station",
    "category": "User Interface"
}


import bpy

class VIEW3D_PIE_NP(bpy.types.Menu):
    """pie NP pie""" 
    bl_label = "NP"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator('object.np_020_point_move', icon='MAN_TRANS', text='point_move')
        pie.operator('object.np_020_point_copy', icon='ROTACTIVE', text='point_copy')
        pie.operator('object.np_020_point_instance', icon='ROTATECOLLECTION', text='point_instance')
        pie.operator('object.np_020_point_array', icon='MOD_ARRAY', text='point_array')
        pie.operator('object.np_020_roto_move', icon='MAN_ROT', text='roto_move')
        pie.operator('object.np_020_point_scale', icon='MAN_SCALE', text='point_scale')
        pie.operator('object.np_020_point_align', icon='ORTHO', text='point_align')
        pie.operator('object.np_020_shader_brush', icon='MOD_DYNAMICPAINT', text='shader_brush')


expected_ops = (
    'np_020_point_move',
    'np_020_point_copy',
    'np_020_point_instance',
    'np_020_point_array',
    'np_020_roto_move',
    'np_020_point_scale',
    'np_020_point_align',
    'np_020_shader_brush',
)
addon_keymaps = []


def register():
    np_station_found = True
    for op in expected_ops:
        if op not in dir(bpy.ops.Object):
            print({'WARNING'}, "Could not find expected operator: " + op)
            print("NP Station Pie Menu was not loaded.")
            print("NP Station must be enabled before enabling this add-on.")
            np_station_found = False
            break
    if np_station_found:
        bpy.utils.register_class(VIEW3D_PIE_NP)
        wm = bpy.context.window_manager
        if wm.keyconfigs.addon:
            km = wm.keyconfigs.addon.keymaps.new(name='Object Non-modal')
            kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS', ctrl=True, shift=True)
            kmi.properties.name = 'VIEW3D_PIE_NP'
            addon_keymaps.append(km)


def unregister():
    if addon_keymaps:
        bpy.utils.unregister_class(VIEW3D_PIE_NP)
        wm = bpy.context.window_manager
        if wm.keyconfigs.addon:
            for km in addon_keymaps:
                for kmi in km.keymap_items:
                    km.keymap_items.remove(kmi)
                wm.keyconfigs.addon.keymaps.remove(km)
        addon_keymaps.clear()
