# Custom Workflow - 1 Image in ComfyUI-Roboflow

You can create whatever workflow you want. This node takes in one image and will output up to 4 images and 4 strings depending on what you are doing.

<img width="1091" alt="Screenshot 2024-09-25 at 10 04 25 AM" src="https://github.com/user-attachments/assets/c507a617-5c75-475f-9618-0d1ec32212a7">


## 1. Install ComfyUI-Roboflow

Follow the instructions in [README.md](https://github.com/DareFail/ComfyUI-Roboflow?tab=readme-ov-file#installation)

## 2. Add the Roboflow Custom Workflow - 1 Image Node

Right-click

Add Node -> Roboflow -> Custom Workflow - 1 Image

<img width="513" alt="Screenshot 2024-09-25 at 9 38 30 AM" src="https://github.com/user-attachments/assets/c116b47b-fac5-48d1-91ce-45524d7a9d75">


## 3. Make your custom workflow

Add blocks or edit from a template here.


## 4. Click the Response node in your workflow


## 5. Copy the output names you care about

## 6. Paste the output names as keys in your ComfyUI Node

Output images are go under output_image1_key, output_image2_key, etc

Your input_image1_key is always "image" unless you changed it in Roboflow.


## 7. Go back to Roboflow and click "Deploy Workflow" in the top right

<img width="459" alt="Screenshot 2024-09-25 at 9 54 13 AM" src="https://github.com/user-attachments/assets/6c8998a9-574e-411b-a157-98281fb84b51">


## 8. Copy your API Key, workspace name, and workflow id

You can copy each part under the python section

Your API Key will look like this ***** but if you copy and paste it will be the actual API Key.

<img width="743" alt="Screenshot 2024-09-25 at 9 54 04 AM" src="https://github.com/user-attachments/assets/7e917c40-4fae-4cde-b94d-47b61474acd6">


## 9. Paste the information above into your node

<img width="425" alt="Screenshot 2024-09-25 at 10 04 13 AM" src="https://github.com/user-attachments/assets/79518535-2739-47f8-b6a6-c7c44fa20f28">


## 10. Use your node

I linked up a Load Image Node and sent the out to a Preview Image Node.

You can find both under Right Click 
Add Node -> image -> Load Image
Add Node -> image -> Preview Image

<img width="1091" alt="Screenshot 2024-09-25 at 10 04 25 AM" src="https://github.com/user-attachments/assets/c507a617-5c75-475f-9618-0d1ec32212a7">


# Repo Info

## License
  

Distributed under the APACHE 2.0 License. See `LICENSE` for more information.

  

## Contact (feel free to ask questions!)

  

Twitter: [@darefailed](https://twitter.com/darefailed)

  

Youtube: [How to Video coming soon](https://www.youtube.com/@darefail)

  

Project Link: [https://github.com/DareFail/ComfyUI-Roboflow](https://github.com/DareFail/ComfyUI-Roboflow)
