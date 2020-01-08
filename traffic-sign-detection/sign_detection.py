import warnings
warnings.filterwarnings('ignore')
import numpy as np
import os
import tensorflow as tf
from matplotlib import pyplot as plt
from PIL import Image
import glob as glob

import sys
# Append your Tensorflow object detection and darkflow directories to your path
# sys.path.append('/content/models/research/object_detection/') # ~/tensorflow/models/research/object_detection
# sys.path.append('/content/models/research/')
# sys.path.append('/content/darkflow') # ~/darkflow
from utils import label_map_util
from utils import visualization_utils as vis_util


def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

# MODEL_PATH = os.path.join('models', MODEL_NAME)
PATH_TO_CKPT = os.path.join('inference_graph/frozen_inference_graph.pb')

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('gtsdb_label_map.pbtxt')

NUM_CLASSES = 43

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)
IMAGE_SIZE = (20, 20)


def sign_detection(test_image,plot_show=False):

  TEST_IMAGE_PATHS = test_image
  cat = [category_index[i]['name'] for i in range(1,44)]

  #INPUT FILE
  if str(type(test_image))!="<class 'list'>":
    TEST_IMAGE_PATHS=[test_image]  
  else:
    TEST_IMAGE_PATHS=test_image
  #Collect output
  final_images,boxes_collect,scores_collect,classes_collect = [],[],[],[]

  with detection_graph.as_default():
      with tf.Session(graph=detection_graph) as sess:
          for idx, image_path in enumerate(TEST_IMAGE_PATHS):
              image = Image.open(image_path)
              
              # the array based representation of the image will be used later in order to prepare the
              # result image with boxes and labels on it.
              image_np = load_image_into_numpy_array(image)
              # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
              image_np_expanded = np.expand_dims(image_np, axis=0)
              image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
              # Each box represents a part of the image where a particular object was detected.
              boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
              # Each score represent how level of confidence for each of the objects.
              # Score is shown on the result image, together with the class label.
              scores = detection_graph.get_tensor_by_name('detection_scores:0')
              classes = detection_graph.get_tensor_by_name('detection_classes:0')
              num_detections = detection_graph.get_tensor_by_name('num_detections:0')
              # Actual detection.
              (boxes, scores, classes, num_detections) = sess.run(
                  [boxes, scores, classes, num_detections],
                  feed_dict={image_tensor: image_np_expanded})
              #Select the boxes based on threshold

              min_score_thresh = 0.4
              sc = np.where(scores[0] > min_score_thresh)[0]
              scores_sel = scores[0][sc]
              boxes_sel = boxes[0][sc,:]
              classes_ind = classes[0][sc]
            
              classes_names = [(cat[int(i-1)]) for i in classes_ind]
              # Visualization of the results of a detection.
              vis_util.visualize_boxes_and_labels_on_image_array(
                  image_np,
                  np.squeeze(boxes),
                  np.squeeze(classes).astype(np.int32),
                  np.squeeze(scores),
                  category_index,
                  min_score_thresh=min_score_thresh,
                  use_normalized_coordinates=True,
                  line_thickness=6)
              if plot_show == True:
                plt.figure(idx, figsize=IMAGE_SIZE)
                plt.imshow(image_np)
              final_images.append(image_np)
              boxes_collect.append(boxes_sel)
              scores_collect.append(scores_sel)
              classes_collect.append(classes_names)
              # num_collect.append(num)
  return final_images,boxes_collect,scores_collect,classes_collect,test_image
