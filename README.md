## pattern_matching

It is the Pattern Matching Project on Xray tuberculosis data which basically checks the abnormalities and normalities case using ShapeContext Descriptors. 
For this we are taking the two public dataset of xray Shenzhen and Montogomery and their respective masking. 

1. Data Preprocessing
  - Creating the bounding box from the mask of given x ray .
  - Cropping the xray image with the respective bounding box.
  - Detecting edges on the cropped Image (Canny Edge detector, ..........)
  
2. Scaled the output from edge detection and scale for equal partitioning.
3. Apply Shape Context and measure the cost.

  
  
