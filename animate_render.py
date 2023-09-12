bl_info = {
    "name": "Render Selected Frames",
    "author": "Anusree Nellikkunnummal",
    "version": (0, 0, 1),
    "blender": (3, 6, 1),
    "location": "Properties > Window > Render",
    "warning": "",
    "description": "Render Selected Frames",
    "category": "Render",
}

#give python access to blender's functionality
import bpy
import time
 
def set_end_frame(frame_count):
    """set the end frame"""
    bpy.context.scene.frame_end = frame_count

def set_fps(fps):
    """set the fps"""
    bpy.context.scene.render.fps = fps
    
def create_cube():
    """create a cube of cubes along the Y-axis"""
    bpy.ops.mesh.primitive_cube_add(scale=(2,2,2))        
    cube = bpy.context.active_object
    return cube

def add_camera():
    """add camera"""   
    bpy.data.cameras.new('camera')
    cam_data = bpy.data.cameras.new('camera' )
    cam = bpy.data.objects.new('camera', cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = (4, 2,1 )
  
def animate_cube():
    """ animate the location property of the cube """
    cube.location = (0, 4, 4)
    start_frame = 1
    cube.keyframe_insert("location", frame=start_frame)
    cube.location = (1,1,1)
    mid_frame = 5
    cube.keyframe_insert("location", frame=mid_frame)
    cube.location = (-1,-1,-1)
    last_frame = 10
    cube.keyframe_insert("location", frame=last_frame)
    

def Auto_render():
    render = bpy.context.scene.render 
    scale = render.resolution_percentage / 100
    
    WIDTH = int(render.resolution_x * scale)
    HEIGHT = int(render.resolution_y * scale)
    
    list = ['1'] #set the list of frame you want
    OUTPUT = "C:/Users/anusr/render_out"   # Where to save Images
    
    for i in list:
        bpy.context.scene.frame_set(int(i)) #jump to frame
        timenow = time.strftime("%m%d %H%M%S", time.localtime()) #add timemark
        filepath = OUTPUT + "/" + str(timenow) + ".png"
        bpy.context.scene.render.filepath = filepath
        bpy.ops.render.opengl(view_context=True, animation=True, write_still=True) #render viewport
    
#create parameters

frame_count = 10
fps = 5

if "__name__" == "__main__":
    pass

set_end_frame(frame_count)
set_fps(fps)
cube = create_cube()
add_camera()
animate_cube()
Auto_render()


