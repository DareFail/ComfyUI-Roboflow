import requests
import json
import io
import base64
from PIL import Image
import torch
import numpy as np

class CustomWorkflow_1image:
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
                    "default": ""
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
            },
            "optional": {
                "input_image1": ("IMAGE",),
                "input_image1_key": ("STRING",),

                "output_image1_key": ("STRING",),
                "output_string1_key": ("STRING",),
                "output_image2_key": ("STRING",),
                "output_string2_key": ("STRING",),
                "output_image3_key": ("STRING",),
                "output_string3_key": ("STRING",),
                "output_image4_key": ("STRING",),
                "output_string4_key": ("STRING",),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING", "IMAGE", "STRING", "IMAGE", "STRING", "IMAGE", "STRING",)
    RETURN_NAMES = ("output_image1", "output_string1", "output_image2", "output_string2", "output_image3", "output_string3", "output_image4", "output_string4",)

    FUNCTION = "use_workflow"

    #OUTPUT_NODE = False

    CATEGORY = "Roboflow"


    def use_workflow(self, workspace_name, workflow_id, api_key, input_image1=None, input_image1_key=None, output_image1_key=None, output_string1_key=None, output_image2_key=None, output_string2_key=None, output_image3_key=None, output_string3_key=None, output_image4_key=None, output_string4_key=None):

        url = f"https://detect.roboflow.com/infer/workflows/{workspace_name}/{workflow_id}"
        headers = {"Content-Type": "application/json"}
        data = {
            "api_key": api_key,
            "inputs": {}
        }


        if input_image1 and input_image1_key:
            base64_image = tensor_to_base64(input_image1)
            data["inputs"][input_image1_key] = {"type": "url", "value": base64_image}

        output_image1 = None
        output_string1 = None
        output_image2 = None
        output_string2 = None
        output_image3 = None
        output_string3 = None
        output_image4 = None
        output_string4 = None

        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:

            data = response.json()
            output = data['outputs'][0]
            
            if output_image1_key:
                output_image1 = base64_to_tensor(output[output_image1_key])
            if output_string1_key:
                output_string1 = output[output_string1_key]
            if output_image2_key:
                output_image2 = base64_to_tensor(output[output_image2_key])
            if output_string2_key:
                output_string2 = output[output_string2_key]
            if output_image3_key:
                output_image3 = base64_to_tensor(output[output_image3_key])
            if output_string3_key:
                output_string3 = output[output_string3_key]
            if output_image4_key:
                output_image4 = base64_to_tensor(output[output_image4_key])
            if output_string4_key:
                output_string4 = output[output_string4_key]

        
        return (output_image1, output_string1, output_image2, output_string2, output_image3, output_string3, output_image4, output_string4,)

        

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

