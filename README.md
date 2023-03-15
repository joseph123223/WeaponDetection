# WeaponDetection

## Google share folder
#### This repo didn't include the custom dataset due to the size of the files. Please go to the google share folder to view the custom dataset if needed.
[https://drive.google.com/file/d/1I6KtGfSDYAYjf91UtLWL8gIS_stajgcd/view?usp=sharing](https://drive.google.com/file/d/1I6KtGfSDYAYjf91UtLWL8gIS_stajgcd/view?usp=sharing)

## Introduction

**Python version**: 3.9

**GPU using**: NVIDIA GeForce RTX 3050

## Installation

pip install for **simple_image_download** (Version 0.5 was released)
```bash
pip install simple_image_download==0.4
```
Download using **download_images.py**
```bash
python download_images.py
```

### Notice:
**Images after downloading still need to process before training**
<br /><br /><br />
pip install for **labelImg**
```bash
pip install labelImg
```

## Custom dataset
Store images data in train file and val file, and create the labels for them.

Make sure the file name are all the same in the code.


## For settings
Check the details requirements in **requirements.txt**
```bash
pip install -r requirements.txt
```

## For GPU (optional)
Check the details requirements in **requirements_gpu.txt**
```bash
pip install -r requirements_gpu.txt
```

## Files need to modify or create for the custom dataset:
- custom_data.yaml
- yolov7-custom.yaml
- hyp.scratch.custom.yaml

## Download for yolov7
[https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7/releases)

You can select which model you want to use.

## Model training
```bash
python train.py --workers 1 --device 0 --batch-size * --epochs *** --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weights yolov7.pt
```
(* and default values can be changed by using different models and settings)

## Test Result
```bash
python detect.py --weights yolov7_custom.pt --source target.filetype
```
### Other optional command

![option](https://user-images.githubusercontent.com/98665601/206914257-448e529d-477d-4e2a-bc58-74ed9d632806.png)

## References
[https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)

[https://pypi.org/project/simple-image-download/](https://pypi.org/project/simple-image-download/)

[https://pytorch.org/get-started/previous-versions/](https://pytorch.org/get-started/previous-versions/)
