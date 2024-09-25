from .customWorkflow_1image import CustomWorkflow_1image
from .removeBackground import RemoveBackground
from .labelEmotions import LabelEmotions

NODE_CLASS_MAPPINGS = {
    "RemoveBackground": RemoveBackground,
    "LabelEmotions": LabelEmotions,
    "CustomWorkflow_1image": CustomWorkflow_1image,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RemoveBackground": "Remove Background",
    "LabelEmotions": "Label Emotions",
    "CustomWorkflow_1image": "Custom Workflow - 1 Image",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']


