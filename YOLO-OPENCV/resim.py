from pickle import TRUE
import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
from cv2 import moveWindow
import numpy as np

try:
    img=cv2.imread("modeller\kapı.jpg")
except:
    print("hata")

img=cv2.resize(img,(460,460))

img_width=img.shape[0]
img_height=img.shape[1]

img_blob=cv2.dnn.blobFromImage(img,1/255,(416,416),swapRB=True,crop=False)

labels = [  "Insan","bicycle","araba","motorcycle","airplane","bus","train","kamyonet","boat",
            "trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat",
            "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
            "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball",
            "kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket",
            "bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple",
            "sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair",
            "sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
            "remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator",
            "book","clock","vase","scissors","teddybear","hairdrier","toothbrush" ]

colors=["0,255,255","0,211,150","200,150,2","0,255,0"]
colors=[np.array(color.split(",")).astype("int") for color in colors]
colors=np.array(colors)
colors=np.tile(colors,(18,1))

###############################################################################################


model=cv2.dnn.readNetFromDarknet("modeller\yolov3.cfg","modeller\yolov3.weights")
 
layers=model.getLayerNames()
output_layer=[layers[layer-1] for layer in model.getUnconnectedOutLayers()]

model.setInput(img_blob)
detection_layers=model.forward(output_layer)


ids_list=[]
boxes_list=[]
confidence_list=[]
#########################################################################################################
 
for detection_layer in detection_layers:
    for object_detection in detection_layer:
        
        scores = object_detection[5:]
        predicted_id = np.argmax(scores)
        
        confidence = scores[predicted_id]
        
        if confidence > 0.30:
            
            label = labels[predicted_id]
            bounding_box = object_detection[0:4] * np.array([img_width,img_height,img_width,img_height])
             
             
            (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")
            
            start_x = int(box_center_x - (box_width/2))
            start_y = int(box_center_y - (box_height/2))
            


            ids_list.append(predicted_id)
            confidence_list.append(float(confidence))
            boxes_list.append([start_x,start_y,int(box_width),int(box_height)])
            
max_ids=cv2.dnn.NMSBoxes(boxes_list,confidence_list,0.5,0.5,0.4)
for max_id in max_ids:
    max_class_id=max_id
    box=boxes_list[max_class_id]

    start_x=box[0]
    start_y=box[1]
    box_width=box[2]
    box_height=box[3]

    predicted_id=ids_list[max_class_id]
    label=labels[predicted_id]
    confidence=confidence_list[max_class_id]


    end_x = start_x + box_width
    end_y = start_y + box_height
    
    box_color = colors[predicted_id]
    box_color = [int(each) for each in box_color]
    
    
    label = "{}: {:.2f}%".format(label, confidence*100)
    # print("predicted object {}".format(label))

    
    cv2.rectangle(img, (start_x,start_y),(end_x,end_y),box_color,1)

    cv2.putText(img,label,(start_x,start_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)



            
winname = "Test"
cv2.namedWindow(winname) 
cv2.moveWindow(winname, 40,30)  # Move it to (40,30)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

