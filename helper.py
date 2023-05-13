## Helper functions for running LGX

## Insert your OpenAI key here.
OPENAI_KEY = ""

########

import openai
import os
from transformers import pipeline

import math
import numpy as np


TARGET_OBJECT_TYPES = [
    "AlarmClock",
    "Apple",
    "BaseballBat",
    "BasketBall",
    "Bowl",
    "GarbageCan",
    "HousePlant",
    "Laptop",
    "Mug",
    "RemoteControl",
    "SprayBottle",
    "Television",
    "Vase"
]

BACKGROUND_OBJECT_TYPES = [
    "ArmChair",
    "Bed",
    "Book",
    "Bottle",
    "Box",
    "ButterKnife",
    "Candle",
    "CD",
    "CellPhone",
    "Chair",
    "CoffeeTable",
    "Cup",
    "DeskLamp",
    "Desk",
    "DiningTable",
    "Drawer",
    "Dresser",
    "FloorLamp",
    "Fork",
    "Newspaper",
    "Painting",
    "Pencil",
    "Pen",
    "PepperShaker",
    "Pillow",
    "Plate",
    "Pot",
    "SaltShaker",
    "Shelf",
    "SideTable",
    "Sofa",
    "Statue",
    "TeddyBear",
    "TennisRacket",
    "TVStand",
    "Watch"
]

ALL_OBJECTS = TARGET_OBJECT_TYPES + BACKGROUND_OBJECT_TYPES


### LLM Processing Functions
opt_generator = pipeline('text-generation', model="facebook/opt-2.7b", max_length=200)

def opt_pass(prompt):
    output = opt_generator("{}".format(prompt))[0]['generated_text']
    output = output.replace(str(prompt), '')

    return output

def chat_pass(prompt):

    from revChatGPT.V1 import Chatbot

    response = ""
    for data in chatbot.ask(prompt):
        response = str(data["message"])

    return str(response)

def gpt_pass(prompt):
    os.environ["OPENAI_API_KEY"] = OPENAI_KEY

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="{}".format(prompt),
      temperature=0.7,
      max_tokens=50,
      top_p=1,
      frequency_penalty=0.2,
      presence_penalty=0
    )

    # Extracting choice from response
    broken_text = response["choices"][0]["text"]

    # print("Original GPT reponse is - {}".format(broken_text))
    # Making it a list
    # broken_text = broken_text.split('\n')
    # Removing empty strings
    # broken_text = list(filter(None, broken_text))
    # # Getting rid of punctuation (.'s and ,'s)
    # broken_text = [''.join(c for c in s if c not in string.punctuation) for s in broken_text]
    # # Checking for numbers and removing them
    # broken_text = [re.sub(r'[0-9]+', '', text) for text in broken_text]
    # # Double checking checking for empty strings after processing.
    # broken_text = [s for s in broken_text if s]

    return broken_text



### PointCloud Functions

def pixel_to_meter(pixel_coord):

    # Calculate pixel size
    pixel_size = 2 * math.tan(math.radians(FOV / 2)) / WIDTH

    # Convert pixel coordinate to normalized camera coordinate
    x_norm = (pixel_coord[0] - cx) / fx
    y_norm = (pixel_coord[1] - cy) / fy

    # Convert normalized camera coordinate to meters
    x_m = x_norm * pixel_size
    y_m = y_norm * pixel_size

    return x_m, y_m


def getPointCloud(im, depthimage):

    # Obtain point cloud
    color = o3d.geometry.Image(im.astype(np.uint8))
    d = depthimage
    # d /= np.max(d)

    depth = o3d.geometry.Image(d)
    rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(color, depth,
                                                              depth_scale=1.0,
                                                              depth_trunc=20,
                                                              convert_rgb_to_intensity=False)
    intrinsic = o3d.camera.PinholeCameraIntrinsic(WIDTH, HEIGHT, fx, fy, cx, cy)
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsic)
    pcd.transform([[1, 0, 0, 0],
                   [0, -1, 0, 0],
                   [0, 0, -1, 0],
                   [0, 0, 0, 1]])

    # For Testing
    # o3d.visualization.draw_geometries([pcd])
    return pcd

def get3DPoint(depthimage, x, y):
    d = depthimage[x, y]
    x, y = pixel_to_meter([x, y])
    # z = d  # Diection from camera, may need to normalize with scale of depthimage
    z = np.sqrt(x**2 + y**2 + d**2)
    # x = (x - cx) * z / fx  # Left, right of camera
    # y = (y - cy) * z / fy  # Height relative to camera
    return x, y, z

def get3DPointFromBBox(depthimage, bbox):
    x_centroid = int(bbox[0] + ((bbox[2] - bbox[0]) / 2))
    y_centroid = int(bbox[1] + ((bbox[3] - bbox[1]) / 2))
    return get3DPoint(depthimage, x_centroid, y_centroid)

def calc_rotation_degree(point1_pixel, point2_pixel):
    # Convert pixel coordinates to normalized image coordinates
    point1_norm = [(point1_pixel[0] - cx) / fx, (point1_pixel[1] - cy) / fy]
    point2_norm = [(point2_pixel[0] - cx) / fx, (point2_pixel[1] - cy) / fy]

    # Calculate the vector between the two points in the image plane
    vector = np.array(point2_norm) - np.array(point1_norm)

    # Calculate the angle between the vectors using the dot product
    dot_product = np.dot(vector, [1, 0])
    norm_product = np.linalg.norm(vector) * np.linalg.norm([1, 0])
    angle = np.arccos(dot_product / norm_product)

    # Convert angle to degrees
    degrees = np.degrees(angle)

    return degrees


### Miscellaenous Helper Functions

def string_correct(string):
    idxlist = []

    for i, char in enumerate(string):
        if char.isupper() and i>0:
            idxlist.append(i)

    if len(idxlist) > 0:
        new_str = string[:idxlist[-1]] + " " + string[idxlist[-1]:]
        return new_str

    else:
        return string