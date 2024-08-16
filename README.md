# Data Labeler

Data Labeler is a Python application designed to read all `.jpg` files from a specified folder and use PaddleOCR to detect text within the images. The detected text and bounding box coordinates are displayed within the interface.

## Features

- **Image Loading**: Load and display all `.jpg` files from a selected folder.
- **Image Selection**: Focus on and display the selected image in the interface.
- **Text Detection**: Use PaddleOCR to detect text in the selected image, displaying bounding boxes and recognized text in the interface.

## Interface

- **Tkinter**: The entire interface is developed using Python's Tkinter library.

## Usage

1. Launch the application and select a folder containing `.jpg` images.
2. Choose an image from the list; it will be displayed and focused in the interface.
3. Click the detection button to perform text detection using PaddleOCR. The results, including bounding boxes and recognized text, will be shown in the interface.

## Requirements

This project requires the following Python packages:

- anyio==4.4.0
- astor==0.8.1
- beautifulsoup4==4.12.3
- certifi==2024.7.4
- charset-normalizer==3.3.2
- colorama==0.4.6
- contourpy==1.1.1
- cycler==0.12.1
- Cython==3.0.11
- decorator==5.1.1
- exceptiongroup==1.2.2
- fire==0.6.0
- fonttools==4.53.1
- h11==0.14.0
- httpcore==1.0.5
- httpx==0.27.0
- idna==3.7
- imageio==2.35.0
- imgaug==0.4.0
- importlib_resources==6.4.0
- kiwisolver==1.4.5
- lazy_loader==0.4
- lmdb==1.5.1
- lxml==5.3.0
- matplotlib==3.7.5
- networkx==3.1
- numpy==1.24.4
- opencv-contrib-python==4.10.0.84
- opencv-python==4.10.0.84
- opt-einsum==3.3.0
- packaging==24.1
- paddleocr==2.8.1
- paddlepaddle==2.6.1
- pillow==10.4.0
- protobuf==3.20.2
- pyclipper==1.3.0.post5
- pyparsing==3.1.2
- python-dateutil==2.9.0.post0
- python-docx==1.1.2
- PyWavelets==1.4.1
- PyYAML==6.0.2
- rapidfuzz==3.9.6
- requests==2.32.3
- scikit-image==0.21.0
- scipy==1.10.1
- shapely==2.0.5
- six==1.16.0
- sniffio==1.3.1
- soupsieve==2.6
- termcolor==2.4.0
- tifffile==2023.7.10
- tqdm==4.66.5
- typing_extensions==4.12.2
- urllib3==2.2.2
- zipp==3.20.0

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/koiMeow/Data-Labeler.git
2. Navigate to the project directory and install the dependencies:
   ```bash
   cd Data-Labeler
   pip install -r requirements.txt
3. Run the application:
   ```bash
   python src/main.py

## Contributing

Contributions are welcome. Please submit pull requests or report any issues.

## License

This project is licensed under the MIT License.
