python train.py --workers 8 --device 0 --batch-size 32 \
--data base.yaml --img 512 512 --cfg cfg/training/yolov7-custom.yaml \
--weights 'yolov7_training.pt' --name yolov7-custom --hyp data/hyp.scratch.custom.yaml
