from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin # Import CORS from flask_cors module
import base64
import cv2
import numpy as np


from model import *
import cv2
import numpy as np



app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello'

def process_image(image_data):
    # Convert base64 image data to numpy array
    nparr = np.fromstring(base64.b64decode(image_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Process the image (example: convert to grayscale)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert the processed image back to base64
    retval, buffer = cv2.imencode('.png', gray_img)
    gray_img_base64 = base64.b64encode(buffer).decode('utf-8')

    return gray_img_base64


@app.route('/whole_area', methods=['POST'])
@cross_origin()
def whole_area_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    # Read the image data
    image_data = image_file.read()
    
    # Convert image data to numpy array
    nparr = np.frombuffer(image_data, np.uint8)
    
    # Decode the image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    
    
    # # Convert image to grayscale
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # # Apply Canny edge detection
    # edges = cv2.Canny(gray_image, 100, 200)
    
    # # Convert edges back to image format
    # edge_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    
    #  EDGE DETECTION
    edge_image=Canny_detector(image)
    
    
    # AREA
    # contours, _ = cv2.findContours(edge_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # RATIO_PIXEL_TO_M=65 #65 pixels is in  1m
    # RATIO_PIXEL_TO_SQUARE_M=65*65
    # # Calculate the area of the largest contour
    # area = calculate_area(contours)
    # area_m=round(area/RATIO_PIXEL_TO_SQUARE_M,2)
    # print(area_m)
    
    edge_area = find_edge_area(edge_image)
    non_detected_edge_area = find_non_detected_edge_area(edge_image)
    image_area = calculate_image_area(image)

    print("Area of the input image:", image_area)
    print("Area of detected edges:", edge_area)
    print("Area of non-detected edges (background):", non_detected_edge_area)
    
    constant = 2175
    actual_area=non_detected_edge_area/constant
    print(actual_area)
    area_m=actual_area
    
    
    
    # Encode the edge-detected image as base64
    _, encoded_image = cv2.imencode('.jpg', edge_image)
    encoded_image_str = base64.b64encode(encoded_image).decode('utf-8')

    # Return the base64 encoded edge-detected image
    return jsonify({'result_image': encoded_image_str, 'area_m': area_m})


@app.route('/defect_area', methods=['POST'])
@cross_origin()
def defect_area_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    # Read the image data
    image_data = image_file.read()
    
    # Convert image data to numpy array
    nparr = np.frombuffer(image_data, np.uint8)
    
    # Decode the image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    
    
    # # Convert image to grayscale
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # # Apply Canny edge detection
    # edges = cv2.Canny(gray_image, 100, 200)
    
    # # Convert edges back to image format
    # edge_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    
    #  EDGE DETECTION
    edge_image=Canny_detector1(image)
    
    
    # AREA
    # contours, _ = cv2.findContours(edge_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # RATIO_PIXEL_TO_M=65 #65 pixels is in  1m
    # RATIO_PIXEL_TO_SQUARE_M=65*65
    # # Calculate the area of the largest contour
    # area = calculate_area(contours)
    # area_m=round(area/RATIO_PIXEL_TO_SQUARE_M,2)
    # print(area_m)
    
    # edge_area = find_edge_area(edge_image)
    # non_detected_edge_area = find_non_detected_edge_area(edge_image)
    # image_area = calculate_image_area(image)

    # print("Area of the input image:", image_area)
    # print("Area of detected edges:", edge_area)
    # print("Area of non-detected edges (background):", non_detected_edge_area)
    
    # constant = 2175
    # actual_area=non_detected_edge_area/constant
    # print(actual_area)
    # area_m=actual_area
    percentage_non_detected_edge = calculate_percentage_non_detected_edge(edge_image)
    area_m=percentage_non_detected_edge
    
    
    
    # Encode the edge-detected image as base64
    _, encoded_image = cv2.imencode('.jpg', edge_image)
    encoded_image_str = base64.b64encode(encoded_image).decode('utf-8')

    # Return the base64 encoded edge-detected image
    return jsonify({'result_image': encoded_image_str, 'area_m': area_m})



if __name__ == '__main__':
    app.run(debug=True)  # You can remove debug=True in production
