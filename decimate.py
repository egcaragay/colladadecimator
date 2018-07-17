import bpy
import os
import sys
from decimal import Decimal

argv = sys.argv
argv = argv[argv.index("--") + 1:]

bpy.ops.object.select_all(action='SELECT')

bpy.ops.object.delete() 

bpy.ops.wm.collada_import(filepath=argv[0])

#Cleans all decimate modifiers

def cleanAllDecimateModifiers(obj):
    for m in obj.modifiers:
        if(m.type=="DECIMATE"):
            obj.modifiers.remove(modifier=m)


decimateRatio=Decimal(argv[2].strip(' "'));
modifierName='DecimateMod'
objectList=bpy.data.objects
for obj in objectList:
    if(obj.type=="MESH"):


        cleanAllDecimateModifiers(obj)

        modifier=obj.modifiers.new(modifierName,'DECIMATE')
        modifier.ratio=decimateRatio
        modifier.use_collapse_triangulate=True
        bpy.context.scene.objects.active = obj
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifierName)

print("saving file")
bpy.ops.wm.collada_export(filepath=argv[1])

print("Done")