bl_info = {
    "name": "Custom Panel",
    "author": "Anusree Nellikkunnummal",
    "version": (0, 0, 1),
    "blender": (3, 6, 1),
    "location": "3D Viewport > Sidebar > Custom Panel",
    "description": "My custom operator buttons",
    "category": "Development",
}
 
# give python access to Blender's functionality
import bpy

class OBJECT_OT_property_example(bpy.types.Operator):
    """ Create custom operators for the panel layout"""
    
    bl_idname = "object.property_example" 
    bl_label = "Property Example One" # found on top of each property item
    bl_options = {'REGISTER', 'UNDO'}
    
    my_float: bpy.props.FloatProperty(name="Some Floating Point")
    my_bool: bpy.props.BoolProperty(name="Toggle Option")
    my_string: bpy.props.StringProperty(name="String Value")
    
    def execute(self, context):
        self.report(
            {'INFO'}, 'F: %.2f  B: %s  S: %r' %
            (self.my_float, self.my_bool, self.my_string)
        )
        print('My float:', self.my_float)
        print('My bool:', self.my_bool)
        print('My string:', self.my_string)
        return {'FINISHED'}

class OBJECT_PT_custom_panel(bpy.types.Panel): #class naming convention 'CATEGORY_PT-name'
  
    # where to add panel in the UI
    bl_space_type = "VIEW_3D" # 3D Viewport area (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items)
    bl_region_type = "UI" # Sidebar region (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items)
    
    # add labels
    bl_idname = "object_PT_custom_panel"
    bl_label = "Custom Property Panel" # found on top of the panel
    bl_category = "Custom Panel" # naming custom tab in the sidebar
   
    def draw(self, context):
        """ define the layout of the panel """
        props = self.layout.operator('object.property_example', text='property 1')
        props.my_string = "Here adding a new property"
        
        props = self.layout.operator('object.property_example', text='property 2')
        props.my_string = "second property adding here"
        
        props = self.layout.operator('object.property_example', text='property 3')
        props.my_string = "third property adding here"
        
        # You can set properties dynamically
        if context.object:
            pass
                
def register():
    bpy.utils.register_class(OBJECT_PT_custom_panel)
    bpy.utils.register_class(OBJECT_OT_property_example)

    
def unregister():
    bpy.utils.unregister_class(OBJECT_PT_custom_panel)
    bpy.utils.unregister_class(OBJECT_OT_property_example)
  
    
if __name__ == "__main__":
    register()
 
   
