# cholec-mt-dssd

This repository implements Multi-tasking deconvolutional single shot detector (MT-DSSD). The base package used was https://github.com/ZQPei/DSSD. 

### Train:

This package supports pascal voc and coco dataset formats. To initiate the training please use the below command.

 > sh scripts/resnet101_mt_dssd320_voc0712_m2cai_single_gpu.sh
 
### Architecture Overview:

Utilized MT-DSSD architecture overview is given here.
![Alt text](/evaluation_results/Network_architecture.png?raw=true)


### Results:

Sample results on cholecystectomy is given below:
![Alt text](/evaluation_results/results.png?raw=true)

Confusion matrix of surgical tool detection on m2cai16-tool-location dataset is given below:
![Alt text](/evaluation_results/confusion_matrix.png?raw=true)

Tool wise mAP of surgical tool detection on m2cai16-tool-location dataset is given below:
![Alt text](/evaluation_results/tool_detections_map.jpg?raw=true)

Surgical tool detection mAP on m2cai16-tool-location dataset is compared with SOTA below:
![Alt text](/evaluation_results/tool_detections_comparison.jpg?raw=true)

Surgical tool presence vs ground truth time progression comparison is given below.
![Alt text](/evaluation_results/tools_vs_time.png?raw=true)

Surgical Phase vs time plot is given below:
![Alt text](/evaluation_results/phase_time.png?raw=true)

Surgical Phase vs tools illustration is given below:
![Alt text](/evaluation_results/phase_vs_tools.png?raw=true)





For trained network models please contact saipradeep.chakka@iiitb.ac.in
