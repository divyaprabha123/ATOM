# ATOM
## Automatic Assessment of Pavement Condition based on road photographs

### Problem given

  Works constructed under the PMGSY scheme are to be maintained by the contractor as per the PMGSY guidelines. Pavement Condition Index is required to be performed to identify the road condition and further to take the maintenance or upgradation of the work. Through EMARG and PMGSY-III, NRIDA has collected a vast collection of pictures of roads. These pictures are collected while doing inspection of roads or collection of PCI through visual inspections. An AI assisted module would be able to automatically assess the picture and identify common issues such as shoulder clearance, potholes, road furniture etc. Requirement is of a solution where there should be a provision to capture the chainage wise pavement condition index. Use of open source software and existing neural network is encouraged. Train a machine learning model, computer vision etc. which is able to identify common issues with pavement based on photograph(s) per road alone. Data Required: Yes (Annotated images to be released by NRIDA) Data Required: Yes (Annotated images to be released by NRIDA)
  
### Abstract

The Pradhan Mantri Gram Sadak Yojana (PMGSY), was launched by the Govt. of India to provide connectivity to unconnected Habitations as part of a poverty reduction strategy. Govt. of India is endeavouring to set high and uniform technical and management standards and facilitating policy development and planning at State level in order to ensure sustainable management of the rural roads network. 
The guidelines for the scheme suggest the following as the objective of Quality Control. [1]   
The objective of Quality Monitoring under PMGSY, i.e. inspection of road works by national level independent monitors is to identify shortcomings in respect of quality of road works and to guide the PIUs about the specifications, good practices and effective execution of works with desired quality. The role of these monitors is to critically examine the road works and give feedback about quality of road works and quality management related shortcomings to the State level quality management team and NRRDA to enable systemic improvements.   
The proposed solution aims to the provide a system to automatically assess the picture taken during inspection and identify common issues such as shoulder clearance, potholes, road furniture etc. The solution will also provide a user interface to locate the issues along each route. This thereby helps automate the monitoring process.  
The features of the proposed system  
  1. Detecting & Classifying potholes from photos 
  2. Identifying road furniture from photos 
  3. Grading road quality 
  4. Mapping them to user interface 

### TECH STACK 
  1. Python 
  2. Tensorflow 
  3. OpenCV 
  4. NumPy 
  5. MatplotLib 
  6. Python-Flask 
  7. MongoDB 
  8. Pillow

### Modules involved
1. Road Damage Type Detection
![alt text](https://drive.google.com/uc?id=1MiaRqHoFel01ZpCmvY3T8VZHpHe6oyO2)

![SIH_Road_Damage_Detection_.ipynb](https://github.com/divyaprabha123/ATOM/blob/master/SIH_Road_Damage_Detection_.ipynb)

2. Sign Detection

      ![Traffic_Sign_detection.ipynb](https://github.com/divyaprabha123/ATOM/blob/master/Traffic_Sign_detection.ipynb)

### To Test
```
!git clone https://github.com/divyaprabha123/ATOM
import detection as d
image_path = "test_images/test_image (1).jpg"
image,*_=d.detection(image_path,plot_show=True)
```
### Output

![alt text](https://drive.google.com/uc?id=1U_i2M7ewJnWzLpz0acAHvY9KBvKy0t0d)
