# cholec-mt-dssd

This repository implements Multi-tasking deconvolutional single shot detector (MT-DSSD). The base package used was https://github.com/ZQPei/DSSD. 

### Train:

This package supports pascal voc and coco dataset formats. To initiate the training, please use the below command.

 > sh scripts/resnet101_mt_dssd320_voc0712_m2cai_single_gpu.sh
 
### Architecture Overview:

Utilized MT-DSSD architecture overview is given here.
<img src="/evaluation_results/Network_architecture.png?" width="70%" >

### Results:

Sample results on cholecystectomy is given below:
<img src="/evaluation_results/results.png?" width="70%" >

Confusion matrix of surgical tool detection on m2cai16-tool-location dataset is given below:
<img src="/evaluation_results/confusion_matrix.png?" width="70%" >

Tool wise mAP of surgical tool detection on m2cai16-tool-location dataset is given below:
<img src="/evaluation_results/tool_detections_map.jpg?" width="40%" >

Surgical tool detection mAP on m2cai16-tool-location dataset is compared with SOTA below:
<img src="/evaluation_results/tool_detections_comparison.jpg?" width="40%" >

Surgical tool presence vs ground truth time progression comparison is given below.
<img src="/evaluation_results/tools_vs_time.png?" width="70%" >

Surgical Phase vs time plot is given below:
<img src="/evaluation_results/phase_time.png?" width="70%" >

Surgical Phase vs tools illustration is given below:
<img src="/evaluation_results/phase_vs_tools.png?" width="70%" >





For trained network models please contact the author.
