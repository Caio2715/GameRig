import bpy

from rigify.rigs.skin.glue import Rig as glue
from rigify.rigs.skin.glue import BridgeGlueRig
from rigify.rigs.skin.glue import SimpleGlueRig


class Rig(glue):
    """Skin rig component that injects constraints into a control generated by other rigs."""

    pass

def parameters_ui(layout, params):
    if params.skin_glue_head_mode == 'BRIDGE':
        BridgeGlueRig.parameters_ui(layout, params)
    else:
        SimpleGlueRig.parameters_ui(layout, params)

def create_sample(obj):
    from ..basic.super_copy import create_sample as inner
    obj.pose.bones[inner(obj)["Bone"]].rigify_type = 'game.skin.glue'