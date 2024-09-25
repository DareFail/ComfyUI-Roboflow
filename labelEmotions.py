import requests
import json
import io
import base64
from PIL import Image
import torch
import numpy as np

class LabelEmotions:
    """
    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    DEPRECATED (`bool`):
        Indicates whether the node is deprecated. Deprecated nodes are hidden by default in the UI, but remain
        functional in existing workflows that use them.
    EXPERIMENTAL (`bool`):
        Indicates whether the node is experimental. Experimental nodes are marked as such in the UI and may be subject to
        significant changes or removal in future versions. Use with caution in production workflows.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "workspace_name": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "workflow_id": ("STRING", {
                    "multiline": False,
                    "default": "recognize-emotions"
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "input_image1": ("IMAGE",),
                "input_image1_key": ("STRING", {
                    "multiline": False,
                    "default": "image"
                }),
                "output_image1_key": ("STRING",{
                    "multiline": False,
                    "default": "annotated_image"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image1",)

    FUNCTION = "use_workflow"

    #OUTPUT_NODE = False

    CATEGORY = "Roboflow"


    def use_workflow(self, workspace_name, workflow_id, api_key, input_image1, input_image1_key, output_image1_key):

        base64_image = tensor_to_base64(input_image1)

        url = f"https://detect.roboflow.com/infer/workflows/{workspace_name}/{workflow_id}"
        headers = {"Content-Type": "application/json"}
        data = {
            "api_key": api_key,
            "inputs": {
                input_image1_key: {"type": "url", "value": base64_image}
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            # Convert response to Python dict
            data = response.json()
            
            # Access 'inputs' -> 'image' in the dictionary
            output = data['outputs'][0]
        
            return (base64_to_tensor(output[output_image1_key]),)
        

def tensor_to_base64(tensor_image):
    image_squeeze = tensor_image.squeeze()
    pil_image = Image.fromarray(image_squeeze.mul(255).byte().cpu().numpy())
    buffer = io.BytesIO()
    pil_image.save(buffer, format='JPEG')
    base64_image = base64.b64encode(buffer.getvalue()).decode()
    
    return base64_image
        

def base64_to_tensor(base64_dict):
    base64_data = base64_dict['value']
    decode = base64.b64decode(base64_data)
    image = Image.open(io.BytesIO(decode))
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

