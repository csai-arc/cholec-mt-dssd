from torch import nn
import torch.nn.functional as F

from dssd.modeling.backbone import build_backbone
from dssd.modeling.decoder import build_decoder
from dssd.modeling.box_head import build_box_head


class DSSDDetector(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.backbone = build_backbone(cfg)
        self.decoder = build_decoder(cfg)
        self.box_head = build_box_head(cfg)
        #self.phase_tool_layers = nn.ModuleList()
        self.phase_classifier = nn.Sequential(
            #nn.MaxPool2d(kernel_size=1),
            nn.Flatten(),
            nn.Linear(1024, 256),
            nn.Linear(256, 7),
        )
        self.tool_classifier = nn.Sequential(
            #nn.MaxPool2d(kernel_size=1),
            nn.Flatten(),
            nn.Linear(9216, 256),
            nn.Linear(256, 7),
        )
        self.tool_criterion = nn.MultiLabelSoftMarginLoss()
        #self.phase_tool_layers.append(self.phase_classifier)
        #self.phase_tool_layers.append(self.tool_classifier)

    def forward(self, images, targets=None):

        features_backbone = self.backbone(images)
        features = self.decoder(features_backbone)
        features_backbone=list(features_backbone)
        #print('----',len(features_backbone))
        #print('----', targets['labels'])
        phase_features =self.phase_classifier(features_backbone[-1])
        tool_features = self.tool_classifier(features_backbone[-2])
        if self.training:
            phase_loss=F.cross_entropy(phase_features,targets['phase_labels'])
            #print("---------",targets['phase_labels'])
            #print(phase_loss)
            tool_loss=self.tool_criterion(tool_features,targets['tool_labels'])
            phase_tool_losses = dict(
               phase_loss=phase_loss,
                tool_loss=tool_loss,
            )
        #print("--------------------going into box_head")
        detections, detector_losses = self.box_head(features, targets)
        #print("detections:",detections.size())
        #print(phase_tool_losses)

        #print(detector_losses)
        if self.training:
            detector_losses.update(phase_tool_losses)
            return detector_losses#.update(phase_tool_losses)
        return detections
        #return phase_features
