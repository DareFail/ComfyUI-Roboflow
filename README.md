# ComfyUI-Roboflow

  This is a ComfyUI node that connects with [Roboflow workflows](https://roboflow.com/workflows/build). 
  
  Roboflow hosts hundreds of thousands of open source and custom object detection models: [https://universe.roboflow.com/](https://universe.roboflow.com/).

  Workflows has a node based drag & drop system similar to ComfyUI that can optionally be hosted. The default setting for this repository is to use the hosted version.


## Included Nodes

-  **Background Removal**: Removes the background from an image

-  **Label Emotions**: Detects human faces and labels them with the emotion they are expressing.

-  **Custom Workflow - 1 Image**: Template for sending an image to a workflow you make and exporting up to 4 images and/or 4 strings to send to other nodes.

-  **Detect Objects (Soon)**: Detect objects on an image using YOLO, vLLMs, Clip, or any trained Object Detection / Classification / Instance Segmentation model in the Roboflow Universe.

-  **Count Objects (Soon)**: Count objects in an image using YOLO, vLLMs, or any trained Object Detection / Instance Segmentation model in the Roboflow Universe.

-  **Blur Objects (Soon)**: Detect and Blur objects in an image using YOLO, vLLMs, or any trained Object Detection / Instance Segmentation model in the Roboflow Universe.

-  **Crop Objects (Soon)**: Detect and Crop objects in an image using YOLO, vLLMs, or any trained Object Detection / Instance Segmentation model in the Roboflow Universe.



### Prerequisites

  
Get your workflow ID and free API key from [Roboflow](https://roboflow.com/) to use this node.

  

### Installation

  

1. Download or clone the repo

```sh

git clone https://github.com/DareFail/ComfyUI-Roboflow

```



2. Copy the ComfyUI-Roboflow folder into your ComfyUI/customer_nodes folder



3. Restart ComfyUI and add any node under "Roboflow"



## Acknowledgements

  

- Thanks to Roboflow for sponsoring this project. Get your free API key at: [Roboflow](https://roboflow.com/)



## License
  

Distributed under the APACHE 2.0 License. See `LICENSE` for more information.

  

## Contact (feel free to ask questions!)

  

Twitter: [@darefailed](https://twitter.com/darefailed)

  

Youtube: [How to Video coming soon](https://www.youtube.com/@darefail)

  

Project Link: [https://github.com/DareFail/ComfyUI-Roboflow](https://github.com/DareFail/ComfyUI-Roboflow)
