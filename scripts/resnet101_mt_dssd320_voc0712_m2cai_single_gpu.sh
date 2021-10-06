# dataset path
export VOC_ROOT="/mnt/sda/Surgical_videos_analysis/phase2_ss/datasets/m2cai16-tool-locations"


# train
#python train.py --config-file ./configs/resnet101_mt_dssd320_m2cai.yaml --eval_step 10
python train.py --config-file ./configs/resnet101_mt_dssd320_m2cai.yaml


# evaluate
# python test.py --config-file configs/resnet101_dssd320_voc0712.yaml


# inference
# python demo.py --config-file configs/resnet101_dssd320_voc0712.yaml --images_dir demo --ckpt [ckpt_path]
