bl_info = {
    "name": "Custom Menu",
    "author": "Anusree Nellikkunnummal",
    "version": (0, 0, 1),
    "blender": (3, 6, 1),
    "location": "Windows > Topbar > Custom Menu",
    "description": "My custom operator buttons",
    "category": "Development",
}
 

import bpy

class OBJECT_OT_property_example(bpy.types.Operator):
    """ Create custom operators for the panel layout"""
    
    bl_idname = "object.property_example" 
    bl_label = "Property Example One" # found on top of each property item
    bl_options = {'REGISTER', 'UNDO'}
    
    my_float: bpy.props.FloatProperty(name="Some Floating Point")
    my_bool: bpy.props.BoolProperty(name="Toggle Option")
    my_string: bpy.props.StringProperty(name="String Value")
    
    # define property group options
    my_enum : bpy.props.EnumProperty(           
        name = "Enumerator/Dropdown",
        description = "sample text",
        items = [('OP1', "This is Option 1", "" ),
                 ('OP2', "This is Option 2", "" ),
                 ('OP3', "This is Option 3", "" )
        
        ]
    )
        
    def execute(self, context):
        self.report(
            {'INFO'}, 'F: %.2f  B: %s  S: %r' %
            (self.my_float, self.my_bool, self.my_string)
        )
        # adding print to check if property return values 
        print('My float:', self.my_float)
        print('My bool:', self.my_bool)
        print('My string:', self.my_string)
        return {'FINISHED'}


class CustomMenu(bpy.types.Menu):
    """creating custom menu"""
    
    bl_label = "Custom Menu" # naming menu
    bl_idname = "CustomMenu"

    def draw(self, context):
        #define layout of the menu
        layout = self.layout

        layout.operator("object.property_example", text="menu item 3", icon='WORLD_DATA')
        layout.operator("object.property_example", text="menu item 3")
        layout.separator()
        layout.operator_menu_enum("object.property_example", "my_enum", text="menu item 3")
                
def draw_item(self, context):
    layout = self.layout
    layout.menu(CustomMenu.bl_idname)


def register():
    bpy.utils.register_class(CustomMenu)
    bpy.utils.register_class(OBJECT_OT_property_example)

    # lets add ourselves to the main header
    bpy.types.TOPBAR_MT_editor_menus.append(draw_item)
    

def unregister():
    bpy.utils.unregister_class(CustomMenu)
    bpy.utils.unregister_class(OBJECT_OT_property_example)
    
    # lets remove ourselves to the main header
    bpy.types.TOPBAR_MT_editor_menus.remove(draw_item)


if __name__ == "__main__":
    register()


