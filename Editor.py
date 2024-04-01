import streamlit as st
from PIL import Image
import numpy as np
import cv2

# Function to apply grayscale transformation
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Function to apply Gaussian blur
def blur(img):
    return cv2.GaussianBlur(img, (15, 15), 0)

# Function to apply rotation
def rotate(img, angle):
    rows, cols = img.shape[:2]
    matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(img, matrix, (cols, rows))

# Function to apply resizing
def resize(img, width, height):
    return cv2.resize(img, (width, height))

# Function to display image
def display_img(img):
    st.image(img, caption="Processed Image", use_column_width=True)

# Main function
def main():
    st.title("Image Processing App")
    upload_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])

    if upload_file is not None:
        image = Image.open(upload_file)
        img_array = np.array(image)

        st.subheader("Original Image")
        st.image(image, use_column_width=True)

        operation = ["Grayscale", "Blur", "Rotation", "Resize", "Save"]
        selected_operation = st.selectbox("Select an operation:", operation)

        if st.button("Apply"):
            processed_img = img_array.copy()
            if selected_operation == "Grayscale":
                processed_img = grayscale(processed_img)
            elif selected_operation == "Blur":
                processed_img = blur(processed_img)
            elif selected_operation == "Rotation":
                angle = st.slider("Select rotation angle:", -180, 180, 0)
                processed_img = rotate(processed_img, angle)
            elif selected_operation == "Resize":
                new_width = st.number_input("Enter new width:", min_value=1)
                new_height = st.number_input("Enter new height:", min_value=1)
                processed_img = resize(processed_img, new_width, new_height)
            elif selected_operation == "Save":
                im = Image.fromarray(img_array)
                im.save("original_image.png")
                st.success("Original Image saved successfully.")
                im_processed = Image.fromarray(processed_img)
                im_processed.save("processed_image.png")
                st.success("Processed Image saved successfully.")

            st.subheader("Processed Image")
            display_img(processed_img)

if __name__ == "__main__":
    main()
