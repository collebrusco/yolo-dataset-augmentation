# run this from yolov7 directory (I cant keep it there b/c it's a submodule)
python train_aux.py --workers 10 --device cpu --batch-size 32 \
--data ../data.yaml --img 384 384 \
--cfg cfg/training/yolov7-e6e.yaml \
--weights './yolov7-e6e-training.pt' --name yolov7-fracture \
--hyp ../frac.yaml --epochs 300
