import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import os
import requests
from io import BytesIO
from PIL import Image
import time
import numpy as np
pylab.rcParams['figure.figsize'] = 20, 12
from GLIP.maskrcnn_benchmark.config import cfg
from GLIP.maskrcnn_benchmark.engine.predictor_glip import GLIPDemo


class GLIP:

    def __init__(self, size=None):
        self.GLIP = self.setup(size)

    def load(self, url):
        """
        Given an url of an image, downloads the image and
        returns a PIL image
        """
        response = requests.get(url)
        pil_image = Image.open(BytesIO(response.content)).convert("RGB")
        # convert to BGR format
        image = np.array(pil_image)[:, :, [2, 1, 0]]
        return image

    def imshow(self, img, caption):
        plt.imshow(img[:, :, [2, 1, 0]])
        plt.axis("off")
        plt.figtext(0.5, 0.09, caption, wrap=True, horizontalalignment='center', fontsize=20)
        plt.savefig(f"GLIP/testing/{time.time()}.png")

    def setup(self, size='L'):
        if size == 'S':
            # Use this command for evaluate the GLPT-T model
            config_file = "GLIP/configs/pretrain/glip_Swin_T_O365_GoldG.yaml"
            weight_file = "GLIP/MODEL/glip_tiny_model_o365_goldg_cc_sbu.pth"
        else:
            config_file = "GLIP/configs/pretrain/glip_Swin_L.yaml"
            weight_file = "GLIP/MODEL/glip_large_model.pth"

        # Tokenizers cannot parallelize with dataloaders
        os.environ["TOKENIZERS_PARALLELISM"] = "false"

        # update the config options with the config file
        # manual override some options
        cfg.local_rank = 0
        cfg.num_gpus = 1
        cfg.merge_from_file(config_file)
        cfg.merge_from_list(["MODEL.WEIGHT", weight_file])
        cfg.merge_from_list(["MODEL.DEVICE", "cuda"])

        glip_demo = GLIPDemo(
            cfg,
            min_image_size=800,
            confidence_threshold=0.7,
            show_mask_heatmaps=False
        )

        return glip_demo

    def run(self, image, caption, thresh=0.7, save=False):
        result = self.GLIP.inference(image, caption)
        if save:
            res_image, result = self.GLIP.run_on_web_image(image, caption, thresh)
            self.imshow(res_image, caption)
        return result
