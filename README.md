# ComfyUI-Roboflow

  This is a ComfyUI node that connects with [Roboflow workflows](https://roboflow.com/workflows/build). 
  
  Roboflow hosts hundreds of thousands of open source and custom object detection models: [https://universe.roboflow.com/](https://universe.roboflow.com/).

  <img width="778" alt="Screenshot 2024-09-24 at 10 46 29 PM" src="https://github.com/user-attachments/assets/d227ad72-c5a1-4dd1-a35c-ba1df2f2c8f9">

  Workflows has a node based drag & drop system similar to ComfyUI that can optionally be hosted. The default setting for this repository is to use the hosted version.

<img width="372" alt="Screenshot 2024-09-24 at 11 08 52 PM" src="https://github.com/user-attachments/assets/e285157d-a6cc-4cff-87af-f4ea29059a51">


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

<img width="414" alt="Screenshot 2024-09-24 at 11 09 25 PM" src="https://github.com/user-attachments/assets/15f8628c-d2d1-4b31-b587-e299ea7321c6">


2. Copy the ComfyUI-Roboflow folder into your ComfyUI/customer_nodes folder

<img width="232" alt="Screenshot 2024-09-24 at 11 10 30 PM" src="https://github.com/user-attachments/assets/28aae35e-34fd-4221-9c29-f74869b11874">


3. Restart ComfyUI and add any node under "Roboflow"



## Acknowledgements

  

- Thanks to Roboflow for sponsoring this project. Get your free API key at: [Roboflow](https://roboflow.com/)



## License
  

Distributed under the APACHE 2.0 License. See `LICENSE` for more information.

  

## Contact (feel free to ask questions!)

  

Twitter: [@darefailed](https://twitter.com/darefailed)

  

Youtube: [How to Video coming soon](https://www.youtube.com/@darefail)

  

Project Link: [https://github.com/DareFail/ComfyUI-Roboflow](https://github.com/DareFail/ComfyUI-Roboflow)
