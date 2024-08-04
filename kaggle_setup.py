import os
import sys
import random
from PIL import Image

def setup_images(kaggle_root, save_root):
    kaggle_path = os.path.join(kaggle_root, "data")
    labels = ["infected", "notinfected"]

    for split in ["test", "train"]:
        for label in labels:
            images = [f for f in os.listdir(os.path.join(kaggle_path, split, label)) if os.path.isfile(os.path.join(kaggle_path, split, label, f))]
            image_names = [label+"_"+f[:-4]+"_original" for f in images]
            
            for i,fname in enumerate(image_names):
                num = random.random()
                if num >= 0.2:
                    print(f"SKIP {split} - {fname}")
                    continue

                try:
                    im = Image.open(os.path.join(kaggle_path, split, label, images[i]))
                except:
                    print(f"FAIL {split} - {fname}")
                    continue

                save_path = os.path.join(save_root, split, fname)
                os.makedirs(save_path)

                im.save(os.path.join(save_path, fname + ".tiff"))
                print(f"SUCCESS {split} - {fname}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR: incorrect usage")
        print("USAGE: python kaggle_setup.py <kaggle_root> <save_root>")

    else:
        kaggle_root = sys.argv[1]
        save_root = sys.argv[2]
        setup_images(kaggle_root, save_root)

