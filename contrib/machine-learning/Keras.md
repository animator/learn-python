# Keras 

## Introduction :-
Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, Theano, and other frameworks. It is designed for fast experimentation, with an intuitive and user-friendly interface that simplifies the creation and training of deep learning models. 

## Key - Features :-
Keras leverages various optimization techniques to make high level neural network API easier and more performant. It supports the following features −

- Consistent, simple and extensible API.
- Minimal structure - easy to achieve the result without any frills.
- It supports multiple platforms and backends.
- It is user friendly framework which runs on both CPU and GPU.
- Highly scalability of computation.

## Installation :-

### Prerequisites :-
You must satisfy the following requirements −

- Any kind of OS (Windows, Linux or Mac)
- Python version 3.5 or higher.



You can install Keras from PyPI via:

    pip install --upgrade keras 

You can check your local Keras version number via:

    import keras
    print(keras.__version__)

# Keras for Classifictaion dataset :-

## Downloading the Dataset
First, we need to install the Kaggle API and authenticate it to download the "Traffic Sign Detection" dataset.

**Description :-** This script installs the kaggle package, then uses the files module from google.colab to upload the kaggle.json file containing Kaggle API credentials. It creates a .kaggle directory to store this file, copies the uploaded file to this directory, and sets the file permissions to ensure only you can read and write it for security purposes.

``` python 
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download the dataset
dataset = 'ahemateja19bec1025/traffic-sign-dataset-classification'
destination = 'traffic-sign-dataset-classification.zip'
api.dataset_download_file(dataset, file_name='', path='.')

# Create the destination directory if it doesn't exist
destination_dir = 'traffic_sign_dataset'
if not os.path.exists(destination_dir):
os.makedirs(destination_dir)

# Extract the dataset
with zipfile.ZipFile(destination, 'r') as zip_ref:
zip_ref.extractall(destination_dir)

print(f'Dataset downloaded and extracted to {destination_dir}')
```

## Creating CSV files for train and test dataset :-

we are pre-processing the data and creating train_data.csv and test_data.csv file with columns image_path and label for further processing:-

``` python 
import os
import pandas as pd

# Directories for training and test data
train_dir = '/content/traffic_sign_dataset/traffic_Data/DATA'
test_dir = '/content/traffic_sign_dataset/traffic_Data/TEST'

def create_dataframe(data_dir):
    image_paths = []
    labels = []

    for label in os.listdir(data_dir):
        label_dir = os.path.join(data_dir, label)
        if os.path.isdir(label_dir):
        for image_name in os.listdir(label_dir):
            if image_name.endswith('.jpg') or image_name.endswith('.png'):
                image_path = os.path.join(label_dir, image_name)
                image_paths.append(image_path)
                labels.append(label)

data = {'Image_Path': image_paths, 'Label': labels}
df = pd.DataFrame(data)
return df

# Create DataFrame for training data
train_df = create_dataframe(train_dir)
train_csv_file_path = '/content/traffic_sign_dataset/traffic_Data/train_data.csv'
train_df.to_csv(train_csv_file_path, index=False)
print("CSV train file saved successfully!")

# Create DataFrame for test data
test_df = create_dataframe(test_dir)
test_csv_file_path = '/content/traffic_sign_dataset/traffic_Data/test_data.csv'
test_df.to_csv(test_csv_file_path, index=False)
print("CSV test file saved successfully!")
```

## Importing Libraries :-
Importing necessary libraries for pre-processing of data and using numpy for numerical computing , matplotlib to do data analysis , we're also importing **Xception** pre-trained model from keras.applications to use for classification of downloaded dataset and measuring it's accuracy by visualization of using matplotlib.

``` python 
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import Xception
from keras import layers, models, optimizers
from keras import Sequential
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.callbacks import EarlyStopping
```

## Creating Data Generators for Image Classification

This code snippet summarizes the process of creating data generators for training and validation sets . It includes setting up image data augmentation for the training set (train_datagen) and scaling for the testing set (test_datagen), defining the batch size and target image size, and loading the dataset using the flow_from_directory method with categorical class mode for image classification tasks.


``` python 
from sklearn.model_selection import train_test_split
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/content/traffic_sign_dataset/traffic_Data/train_data.csv')

# Convert the 'Label' column to a categorical data type
df['Label'] = df['Label'].astype('str')

# Perform stratified split manually to ensure all classes are present in both sets
train_list = []
val_list = []

for label in df['Label'].unique():
    class_subset = df[df['Label'] == label]
    train_class, val_class = train_test_split(class_subset, test_size=0.2, random_state=42)
    train_list.append(train_class)
    val_list.append(val_class)

# Concatenate all class splits to form the final train and validation DataFrames
train_df = pd.concat(train_list).reset_index(drop=True)
val_df = pd.concat(val_list).reset_index(drop=True)

# Check the data type of the 'Label' column in the train and validation DataFrames
print(train_df['Label'].dtype)
print(val_df['Label'].dtype)
num_classes = len(df['Label'].unique())
print(num_classes)

# Check the number of classes in each set
print("Training set classes:", len(train_df['Label'].unique()))
print("Validation set classes:", len(val_df['Label'].unique()))

train_datagen = ImageDataGenerator(
rescale=1./255,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,
rotation_range=20,
width_shift_range=0.2,
height_shift_range=0.2
)
val_datagen = ImageDataGenerator(rescale=1./255)

batch_size = 32
target_size = (224, 224)
train_generator = train_datagen.flow_from_dataframe(dataframe=train_df,
                                                x_col='Image_Path',
                                                y_col='Label',
                                                target_size=target_size,
                                                batch_size=batch_size,
                                                class_mode='categorical')

validation_generator = val_datagen.flow_from_dataframe(dataframe=val_df,
                                                        x_col='Image_Path',
                                                        y_col='Label',
                                                        target_size=target_size,
                                                        batch_size=batch_size,
                                                        class_mode='categorical')
print (num_classes)
```

## Customizing it according to our usecase

This code snippet summarizes the process of creating a custom keras categorical classification model in Keras. It involves loading the pre-trained Xception freezing its layers, adding custom layers for classification, compiling the model, shuffling the training data, and training the model. Finally, the trained model is saved as an HDF5 file .

``` python 
def create_model(base_model, input_shape, num_classes):
    base_model.trainable = True  # Unfreeze the base model
    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    return model
```

## Train and Evaluate :-

Creating train and evaluate function for training the dataset using imported model , validating it using validation set and measuring it's accuracy accordingly.

```python 
def train_and_evaluate(model, train_data, val_data, model_name, epochs=10):
# Compile the model
model.compile(optimizer=optimizers.Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model with the specified number of epochs
history = model.fit(train_generator,
                validation_data=validation_generator,
                steps_per_epoch=len(train_generator),
                epochs=epochs,
                callbacks=[early_stopping])

# Evaluate the model
val_accuracy = history.history['val_accuracy'][-1]
print(f'{model_name} Validation Accuracy: {val_accuracy:.4f}')

return history

save_dir = 'saved_models'
if not os.path.exists(save_dir):
os.makedirs(save_dir) 
```

## Loading the base model and Training :-

Loading the base model and training the dataset via calling the above defined functions :- 

``` python 
# Set parameters for Xception
base_model = Xception(weights='imagenet', include_top=False, input_shape=(299, 299, 3))
input_shape = (299, 299, 3)
model_name = 'Xception'
print (num_classes)

# Create the model
model = create_model(base_model, input_shape, num_classes)

# Training the model
epochs = 13
optimizer = optimizers.Adam()

# Compile the model
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

print(f'Training {model_name}...')
history = train_and_evaluate(model, train_generator, validation_generator, model_name, epochs=epochs)

# Save the trained model
model.save(os.path.join(save_dir, f'{model_name}_saved.h5'))
print(f'Saved {model_name} model to {save_dir}/{model_name}_saved.h5')
```

## Testing and Labeling Unseen data :-

Testing and Labeling the unseen dataset using saved trained model with test dataset.

``` python 
import os
from tqdm import tqdm
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.preprocessing import image

# Load test dataset
test_df = pd.read_csv('/content/traffic_sign_dataset/traffic_Data/test_data.csv')

# Load class indices (assuming you have train_generator with class indices saved)
class_indices_inverse = {v: k for k, v in train_generator.class_indices.items()}

# Directory containing the saved models
model_dir = '/content/saved_models'

# Define batch size
batch_size = 32

# Function to process images in batches
def process_images_in_batches(image_paths, model, target_size, batch_size):
    num_images = len(image_paths)
    num_batches = (num_images + batch_size - 1) // batch_size  # Calculate number of batches

    all_predictions = []

    for batch_idx in range(num_batches):
        start_idx = batch_idx * batch_size
        end_idx = min((batch_idx + 1) * batch_size, num_images)
        batch_paths = image_paths[start_idx:end_idx]

        batch_images = []
        for img_path in batch_paths:
            img = image.load_img(img_path, target_size=target_size)
            img = image.img_to_array(img)
            img = img / 255.0
            batch_images.append(img)

        batch_images = np.array(batch_images)
        batch_predictions_probs = model.predict(batch_images)
        batch_predictions = np.argmax(batch_predictions_probs, axis=1)

        all_predictions.extend(batch_predictions)

    return all_predictions

# Iterate over each model file in the directory

for model_file in os.listdir(model_dir):
if model_file.endswith('.h5'):
    # Load the model
    model_path = os.path.join(model_dir, model_file)
    model = load_model(model_path)

    # Determine target size based on model
    if "Xception_saved" in model_file:
        target_size = (299, 299)
    else:
        target_size = (224, 224)

    # Process images in batches and make predictions
    image_paths = test_df['Image_Path'].tolist()
    prediction = process_images_in_batches(image_paths, model, target_size, batch_size)

    # Map predictions to class labels
    prediction_labels = [class_indices_inverse[label] for label in prediction]

    # Create a DataFrame with predictions
    predicted_df = pd.DataFrame({
        'Image_Path': test_df['Image_Path'],
        'Label': prediction_labels,
    })

    # Save predictions to CSV
    csv_path = f'/content/saved_models/predicted_{model_file.split(".")[0]}.csv'
    predicted_df.to_csv(csv_path, header=True, index=False)

    print(f"Predictions saved to {csv_path}")
```

## Benefits of using Keras :-
Keras is highly powerful and dynamic framework and comes up with the following advantages −

- Larger community support.

- Easy to test.

- Keras neural networks are written in Python which makes things simpler.

- Keras supports both convolution and recurrent networks.

- Deep learning models are discrete components, so that, you can combine into many ways.

## Conclusion :-
Keras is based on minimal structure that provides a clean and easy way to create deep learning models based on TensorFlow or Theano. Keras is designed to quickly define deep learning models. Well, Keras is an optimal choice for deep learning applications.
