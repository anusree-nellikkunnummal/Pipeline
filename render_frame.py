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


import bpy
import time

def Auto_render():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.overlay.show_overlays=False #turn off viewport layout
                    break

    list = ['55', '90', '125'] #set the list of frame you want
    OUTPUT = "C:/Users/anusr"   # Where to save Images

    for i in list:
        bpy.context.scene.frame_set(int(i)) #jump to frame
        timenow = time.strftime("%m%d %H%M%S", time.localtime()) #add timemark
        filepath = OUTPUT + "/" + str(timenow) + ".png"
        bpy.context.scene.render.filepath = filepath
        bpy.ops.render.opengl(write_still=True, view_context=True) #render viewport
        
        
if __name__ == "__main__":
    Auto_render()