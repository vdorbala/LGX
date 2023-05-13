# Can an Embodied Agent Find Your “Cat-shaped Mug”? LLM-Based Zero-Shot Object Navigation

This repo contains code for our paper - 
#### [**Can an Embodied Agent Find Your “Cat-shaped Mug”? LLM-Based Zero-Shot Object Navigation**](https://arxiv.org/pdf/2303.03480.pdf). 
*Vishnu Sashank Dorbala, James F. Mullen Jr., Dinesh Manocha*

## Overview

<img src="https://github.com/vdorbala/LGX/blob/master/images/overview.jpg">

## Abstract
*We present LGX, a novel algorithm for Object
Goal Navigation in a “language-driven, zero-shot manner”,
where an embodied agent navigates to an arbitrarily described
target object in a previously unexplored environment. <br> 
Our approach leverages the capabilities of Large Language Models
(LLMs) for making navigational decisions by mapping the
LLMs implicit knowledge about the semantic context of the
environment into sequential inputs for robot motion planning.
Simultaneously, we also conduct generalized target object detection 
using a pre-trained Vision-Language grounding model. <br>
We achieve state-of-the-art zero-shot object navigation results
on RoboTHOR with a success rate (SR) improvement of over
27% over the current baseline of the OWL-ViT CLIP on Wheels
(OWL CoW). Furthermore, we study the usage of LLMs for
robot navigation and present an analysis of the various semantic
factors affecting model output. <br> Finally, we showcase the benefits
of our approach via real-world experiments that indicate the
superior performance of LGX when navigating to and detecting
visually unique objects.*

### Prerequisites

Our experiments use Python 3.8, ROS Melodic, CUDA 11.1 and Torch 1.10.0. In addition, you will need to install the following packages/submodules.
1. Conda Setup -
    Use the `conda_reqs.txt` file provided to setup the conda environment for LGX.
2. [GLIP](https://github.com/microsoft/GLIP) - 
    Follow the installation instructions from the official documentation. Make sure to include the GLIP folder inside the root directory.
    `GLIP_utils.py` contains helper funtions for using and running GLIP.
3. [OpenAI GPT-3 API Key](https://platform.openai.com/) - 
    You need to update the `OPENAI_KEY` parameter in `helper.py` with your key.
4. A ROS Navigation Stack and RTABMAP - 
    We use RTABMAP along with the `husky navigation package` for generating a occupancy grid and path planning. The former can be installed using instructions [here](https://github.com/introlab/rtabmap/wiki/Installation), and the latter using `sudo apt install ros-melodic-husky-navigation`. Once installed, replace the `costmap_common.yaml` file in the configs folder of the package with the one provided in this repo.
5. [YOLO](https://github.com/ultralytics/yolov5) and [LAVIS](https://github.com/salesforce/LAVIS)
    Finally, we also require LAVIS and YOLO to be installed for running either LAVIS + LGX or YOLO + LGX.

### Installation
To run LGX, we use ROS melodic with python 3.8. This requires you to first need to setup a catkin workspace as follows.
 #### Catkin Workspace Setup
 1. You'll need to install ROS. Since python3 isn't supported in Melodic, some packages need to be catkin installed to handle `opencv` and `tf2_ros` errors.
 2. Catkin install - `geometry2`, `vision-opencv`, and source the workspace. Use GCC version 9 and G++ version 9.
 3. Use `catkin config --extend /opt/ros/melodic` to set your `$CMAKE_PREFIX_PATH` in the catkin workspace (More details [here](https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_config.html)).
 4. Setup catkin build, and use the config - 
 `-DPYTHON_EXECUTABLE=/python3.8-install-location/bin/python -DPYTHON_INCLUDE_DIR=/python3.8-install-location/include/python3.8 -DPYTHON_LIBRARY=/python3.8-install-location/lib/libpython3.8.so`. 
 Replace the executable paths with wherever python3.8 has been installed in  your system. It can point to your conda environment.
 5. Follow instructions from [here](https://answers.ros.org/question/326226/importerror-dynamic-module-does-not-define-module-export-function-pyinit__tf2/?answer=326302#post-id-326302) to install the `geometry2` package for python3. The instructions use `catkin_make`, but it can simply be substituted with `catkin build` which is far more convenient to use.
 6. Then download the melodic/noetic/yourversion branch of the `vision-opencv` package ([here](https://github.com/ros-perception/vision_opencv)) in the catkin src folder, and build that using `catkin build`.
 7. Finally, after building everything, ensure that your catkin workspace is sourced in the .bashrc file AFTER the ROS source. Echoing the `$CMAKE_PREFIX_PATH` should look something like - `/home/user/catkin_ws/devel:/opt/ros/melodic`.
 8. If all these steps have been followed correctly, after opening up a python3.8 terminal, running `import tf2_ros` and `from cv_bridge.boost.cv_bridge_boost import getCvType` should return no errors.
 9. Alternatively, you could use the `catkin_ws` folder provided in the repo and source it accordingly.
 
 ### Inference & Results

 1. Run `roscore`, and keep it running on a separate terminal.
 2. Activate the conda environment using `conda activate LGX`.
 3. Run  `roslaunch move.launch`, followed by `python3 lgx-run.py`. 
 4. (Optional) Open rviz, and load the `lgx.rviz` config file provided for visualization. Or run `rviz -d lgx.rviz`.
 5. Once the experiment is done, you can get statistics and results using `compute_results.py`.

 If everything runs successfully, you should see the results folder getting populated, and rviz showing the map and pointcloud similar to the image below.

 <img src="https://github.com/vdorbala/LGX/blob/master/images/example_costmap.jpg">

 ## Useful Commands, Tips & Debugging Info

 - The presence of a `results` folder (empty or not) is necessary for the code to run. Clear this folder if you need to start afresh.
 - Use `rosservice call /rtabmap/reset` to clear the costmap and pointcloud.
 - Run `rosrun map_server map_saver [--occ <threshold_occupied>] [--free <threshold_free>] [-f <mapname>] map:=/your/costmap/topic` for manually saving the map.
- If you get CUDA Runtime errors, run `nvidia-smi`, and note the PID for the `python3` process(es). Then kill it using `sudo kill -9 PID`.
 - Ensuring the gridmap size is the same in `costmap_common.yaml` and Thor's `locobot controller` is very important. Right now it is set to `0.25`. If you change this value, make sure you change it in both places.
 - Check `rosparam get /move_base/NavfnROS/allow_unknown` is `False` to ensure the path planning takes place only inside the visible costmap, when target locking starts taking place. Also ensure `rosparam get /move_base/global_costmap/track_unknown_space` returns `True`.
 - If you face cuda toolkit sourcing errors, add the CUDA toolkit install location to .bashrc as follows- 
 `export CUDA_HOME="/cuda_install_path/cuda"`
 `export PATH=/cuda_install_path/cuda/bin:$PATH`
 `export LD_LIBRARY_PATH="/cuda_install_path/cuda/lib64:$LD_LIBRARY_PATH"`
 - We use the following command for a Torch + CUDA install (CUDA 11.1, torch v1.10.0)
 pip install torch\==1.10.0+cu111 torchvision\==0.11.0+cu111 torchaudio\==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
 - If you get the Libtiff error, remove only that package from conda -`conda remove --force libtiff`
 - I've used [notify.run](https://notify.run/) for debugging at various points in the code (commented). You can try to set it up yourself incase you face issues.
 - Run `TMPDIR=<cache_dir> pip install --cache-dir=<cache_dir> pkg_name` if running low on space during pip install.


If you found our work useful, please do cite us!

```
@article{dorbala2023can,
  title={Can an Embodied Agent Find Your" Cat-shaped Mug"? LLM-Based Zero-Shot Object Navigation},
  author={Dorbala, Vishnu Sashank and Mullen Jr, James F and Manocha, Dinesh},
  journal={arXiv preprint arXiv:2303.03480},
  year={2023}
}
```
