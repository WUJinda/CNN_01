"""
Eg1.3 : VOCSegmentation, VOCDetection
"""
from torchvision.datasets.voc import VOCSegmentation, VOCDetection

segmentation_dataset = VOCSegmentation(root="./voc_data",
                                       image_set="train",
                                       transform=None,
                                       download=False)
detection_dataset = VOCDetection(root="./voc_data",
                                 image_set="train",
                                 transform=None,
                                 download=False)
# Semantic Segmentation and Target Detection, they have different types of dataset
index = 0
print("type(segmentation_dataset[{}]): {}".format(index, type(segmentation_dataset[index])))  # <class 'tuple'>
print("type(segmentation_dataset[{}][0]): {}".format(index,
                                                     type(segmentation_dataset[index][0])))  # <class 'PIL.Image.Image'>
print("type(segmentation_dataset[{}][1]): {}".format(index, type(
    segmentation_dataset[index][1])))  # <class 'PIL.PngImagePlugin.PngImageFile'>

print("type(detection_dataset[{}]): {}".format(index, type(detection_dataset[index])))  # <class 'tuple'>
print(
    "type(detection_dataset[{}][0]): {}".format(index, type(detection_dataset[index][0])))  # <class 'PIL.Image.Image'>
print("type(detection_dataset[{}][1]): {}".format(index, type(detection_dataset[index][1])))  # <class 'dict'>
