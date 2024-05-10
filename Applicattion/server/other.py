# import numpy as np 
# import os 
# import cv2 
# import matplotlib.pyplot as plt 


# def Canny_detector(img, weak_th=None, strong_th=None):
#     """
#     Applies Canny edge detection to the input image.

#     Args:
#     - img: Input image.
#     - weak_th: Weak threshold for double thresholding step.
#     - strong_th: Strong threshold for double thresholding step.

#     Returns:
#     - mag: Magnitude of gradients of edges.
#     """
#     # Conversion of image to grayscale
#     if len(img.shape) == 3:  # Ensure input image is grayscale
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Noise reduction step
#     img = cv2.GaussianBlur(img, (5, 5), 1.4)

#     # Calculating the gradients
#     gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
#     gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)

#     # Conversion of Cartesian coordinates to polar
#     mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True)

#     # Setting default thresholds if not provided
#     mag_max = np.max(mag)
#     if weak_th is None:
#         weak_th = mag_max * 0.1
#     if strong_th is None:
#         strong_th = mag_max * 0.5

#     # Double thresholding step
#     weak_ids = mag < weak_th
#     strong_ids = mag > strong_th
#     ids = np.zeros_like(img)
#     ids[strong_ids] = 2  # Strong edges
#     ids[np.logical_and(mag <= strong_th, mag >= weak_th)] = 1  # Weak edges

#     # Non-maximum suppression step
#     for i in range(1, img.shape[0] - 1):
#         for j in range(1, img.shape[1] - 1):
#             if ids[i, j] == 1:  # Weak edge
#                 if np.any(ids[i - 1:i + 2, j - 1:j + 2] == 2):
#                     ids[i, j] = 2

#     return ids

# frame = cv2.imread('02_01.JPG') 

# # calling the designed function for 
# # finding edges 
# canny_img = Canny_detector(frame) 




# @app.route('/process-image', methods=['POST'])
# def process_image_route():
#     print("enter")
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image provided'}), 400
    
#     image_file = request.files['image']
#     print(image_file)
#     image_data = image_file.read()
    
#     print(image_data)

#     processed_image_data = process_image(image_data)

#     # return jsonify({'result_image': processed_image_data})
#     return jsonify({'result_image': image_file})

# @app.route('/process_image', methods=['POST'])
# @cross_origin()
# def process_image_route():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image provided'}), 400
    
#     image_file = request.files['image']
#     # print(image_file)
    
#     if image_file.filename == '':
#         return jsonify({'error': 'No image selected'}), 400
    
#     # You can do additional checks here to ensure the file is an image file if needed
    
#     # Read the image data
#     image_data = image_file.read()
   
    
    
#     # You can process the image data here if needed
    
#     # Return the same image data
#     # return jsonify({'result_image': image_data.decode('latin1')})
#     # Encode the image data as base64
#     encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    

#     # Return the base64 encoded image data
#     return jsonify({'result_image': encoded_image})