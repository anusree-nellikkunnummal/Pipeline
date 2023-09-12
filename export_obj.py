# If you want to export as OBJ.
import bpy  
import os

def Export_Obj():
    """Export Scene as obj"""
    directory = os.path.dirname(bpy.data.filepath)
    print(directory)
    target_file = os.path.join(directory, 'myfiles.obj')
    bpy.ops.export_scene.obj(filepath=target_file) #filepath is where you want to export the model

    #further export obj options:
    bpy.ops.export_scene.obj(
     filepath=bpy.data.filepath,
     check_existing=True,
     axis_forward='-Z',
     axis_up='Y',
     filter_glob="*.obj;*.mtl",
     use_selection=False, #use_selection is if you want to export the whole scene or just the selected part
     use_animation=False,
     use_mesh_modifiers=True,
     use_edges=True,
     use_smooth_groups=False,
     use_smooth_groups_bitflags=False,
     use_normals=True,
     use_uvs=True,
     use_materials=True,
     use_triangles=False,
     use_nurbs=False,
     use_vertex_groups=False,
     use_blen_objects=True,
     group_by_object=False,
     group_by_material=False,
     keep_vertex_order=False,
     global_scale=1,
     path_mode='AUTO'
    )
    
if "__name__" == "__main__":
    pass

Export_Obj()