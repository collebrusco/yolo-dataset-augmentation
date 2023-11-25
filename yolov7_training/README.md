### Training yolo
Here's a short description of how the baseline was trained for replication      
I used A100s on colab which required fixing some bugs in the yolo code (simple cuda stuff)   
on colab I had to manually set the command line args in the python file to run it from an nb  
but I've mirrored those parameters in train.sh

### Train
train.sh begins training but it needs to be copied to the yolov7/ directory and run there   
I couldn't keep it there because yolov7 is a submodule
```
cp yolov7_training/train.sh ./yolov7_training/yolov7/train.sh
cd yolov7_training/yolov7
sh ./train.sh
```       

   
that should work, reach out if not. It will generate yolov7/runs/ and keep everything there.
