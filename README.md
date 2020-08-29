# Bird-Species-Image-Classification-Flask-API

# Table of Contents
1. Problem Statement
2. Approach Used
3. Results Achieved
4. Technology Used
5. How to Use This API

# Problem Statement
The problem statement is to classify over 225 different Species of Bird.The purpose it to develop a Deep Learning Model which can classify over 225 different species of Bird.

# Approach Used
Used Transfer Learning pretrained DenseNet201 and Data Augmentation along with GlobalAveragePooling to reduce the no.of trainable Parameters and Overfitting.

# Results Achieved
Achieved an overall accuracy of 97.85% on the Training Set, 95.89% on the validation set and 98.22 percent on the Testing Set.Also Achieved Macro F1 Score,precision and recall of 0.982,0.985 and 0.982

# Technology Used
![112719_Python_Software_Foundation_Logo large](https://user-images.githubusercontent.com/37527532/91639130-21874900-ea32-11ea-8c44-b7c20a76452c.jpg)
![flask](https://user-images.githubusercontent.com/37527532/91639099-c2293900-ea31-11ea-9b8e-6a4309abc1df.png)

# How to Use this API
Step 1:Clone this Repository By typing ```git clone https://github.com/rishabh706/Bird-Species-Image-Classification-Flask-API.git```

Step 2:Open your Terminal or Bash shell and get into the project directory by typing command ```cd```

Step 3:Then Type ```conda create -n Virtual Environment Name``` to create virtual environment if you donot have conda then you can install from https://docs.conda.io/en/latest/miniconda.html as per you PC specification.

Step 4:Activate the virtual environment by typing the following command ```conda activate Name of YOUR Enviroment```

Step 4:Install the required Packages by typing ```pip install -r requirements.txt```

Step 5:Type the following command to run the server ```python app.py```

Step 6:Open Postman If you donot have you can download from https://www.postman.com/downloads/

Step 7:Type  http://127.0.0.1:5000/ to the Post Request and Hit Send you will see a response like this

