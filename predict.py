from tensorflow.keras.preprocessing import image
import numpy as np
import os
from tensorflow.keras.models import load_model

# Create a list of all the foods
def create_foodlist(path):
    list_ = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            list_.append(name)
    return list_

# Load the model and food list
my_model = load_model(r'C:\Users\Vasanth Rao\Documents\MINI_PROJECT\food101_model.h5', compile=False)
food_list = create_foodlist(r"C:\Users\Vasanth Rao\Documents\MINI_PROJECT\food-101\test")
recipes = r"C:\Users\Vasanth Rao\Documents\MINI_PROJECT\food-101\recipes"
recipes_names = os.listdir(recipes)

# Predict classes of new images loaded from the computer
def predict_class(model, img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.
    pred = model.predict(img)
    index = np.argmax(pred)
    index=0
    food_list.sort()
    pred_value = food_list[index]
    with open(os.path.join(recipes, recipes_names[index]), 'r') as file:
        recipe = file.read()
    return pred_value, recipe

# For testing purpose
if __name__ == '__main__':
    images = [r"C:\Users\Vasanth Rao\Documents\MINI_PROJECT\food-101\demo_Images\466304.jpg"]
    for img_path in images:
        food, recipe = predict_class(my_model, img_path)
        print(f"Predicted food: {food}")
        print(f"Recipe: {recipe}")