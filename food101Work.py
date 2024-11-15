# Helper method to split dataset into train and test folders
from shutil import copy
from collections import defaultdict
import os

#function to help preparing tarining set and test set....ONLY RUN ONCE
def prepare_data(filepath, src,dest):
  classes_images = defaultdict(list)
  with open(filepath, 'r') as txt:
      paths = [read.strip() for read in txt.readlines()]
      for p in paths:
        food = p.split('/')
        classes_images[food[0]].append(food[1] + '.jpg')

  for food in classes_images.keys():
    print("\nCopying images into ",food)
    if not os.path.exists(os.path.join(dest,food)):
      os.makedirs(os.path.join(dest,food))
    for i in classes_images[food]:
      copy(os.path.join(src,food,i), os.path.join(dest,food,i))
  print("Copying Done!")
image_path = r'C:\Users\Vasanth Rao\Documents\MINI_PROJECT\archive\food-101\food-101\images'
train_path = r'C:\Users\Vasanth Rao\Documents\MINI_PROJECT\archive\food-101\food-101\meta\train.txt'
test_path = r'C:\Users\Vasanth Rao\Documents\MINI_PROJECT\archive\food-101\food-101\meta\test.txt'
prepare_data(train_path,image_path , 'food-101/train')
prepare_data(test_path, image_path, 'food-101/test')
   