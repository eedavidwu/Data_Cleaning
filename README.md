# Data_Cleaning
## Construct the data set after detection：

1. Use yolo to detect the object:

   First: 

   python create_val.py

   Second:

   ./darknet detector valid Person/yolov3.data ~/Weights/yolov3.cfg ~/Weights/yolov3_final.weights

2. Draw bbox: (pay attention to the label attribution)

   python draw_bbox.py

3. Delete the image with too small size and create labels:

   python delete_small_create_labels.py

