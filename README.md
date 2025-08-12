# Background Remover

A powerful web application for removing backgrounds from images using YOLO-based segmentation models. This project provides both a Streamlit web interface and Jupyter notebooks for training and experimentation.

## 🚀 Features

- **Web Interface**: User-friendly Streamlit app for easy background removal
- **YOLO Integration**: Uses trained YOLO models for accurate object segmentation
- **Multiple Formats**: Supports JPEG, JPG, and PNG image formats
- **Download Results**: Export transparent PNG images with removed backgrounds
- **Real-time Processing**: Instant background removal with CPU optimization
- **Training Notebooks**: Jupyter notebooks for custom model training

## 📋 Prerequisites

- Python 3.8+
- CUDA-compatible GPU (optional, for faster processing)
- 4GB+ RAM recommended

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd backgroundRemover
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install streamlit ultralytics pillow matplotlib opencv-python numpy
   ```

3. **Download the pre-trained model:**
   - The `model.pt` file should be in the project directory
   - If missing, you can train your own model using the provided notebooks

## 🚀 Usage

### Web Application

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload an image** using the file uploader

4. **Click "Run YOLO Detection"** to remove the background

5. **Download the result** as a transparent PNG file

### Jupyter Notebooks

- **`backgroundRemover.ipynb`**: Main notebook for background removal using SAM (Segment Anything Model)
- **`humanSegmentation.ipynb`**: Specialized notebook for human body segmentation
- **`segmentation_on_custom_data.ipynb`**: Training notebook for custom datasets

## 🏗️ Project Structure

```
backgroundRemover/
├── app.py                          # Streamlit web application
├── model.pt                        # Pre-trained YOLO model
├── backgroundRemover.ipynb         # Main segmentation notebook
├── humanSegmentation.ipynb         # Human segmentation notebook
├── segmentation_on_custom_data.ipynb # Custom training notebook
└── README.md                       # This file
```

## 🔧 Technical Details

### Model Architecture
- **Base Model**: YOLO (You Only Look Once) for object detection
- **Segmentation**: Mask-based approach for precise background removal
- **Output**: RGBA images with alpha channel transparency

### Processing Pipeline
1. Image upload and conversion to RGB format
2. YOLO model inference for object detection
3. Mask generation and combination
4. Alpha channel creation for transparency
5. RGBA image output with download capability

### Performance Optimization
- CPU-based processing for accessibility
- Efficient mask operations using NumPy
- Optimized image resizing with OpenCV

## 📚 Training Custom Models

### Using the Training Notebooks

1. **Prepare your dataset** with labeled images
2. **Open `segmentation_on_custom_data.ipynb`**
3. **Configure training parameters** (epochs, learning rate, etc.)
4. **Train your model** on the custom dataset
5. **Export the trained model** as `model.pt`

### Dataset Requirements
- Images in common formats (JPEG, PNG)
- Corresponding segmentation masks
- Balanced class distribution for better results

## 🌟 Advanced Features

### SAM Integration
The notebooks include integration with Meta's Segment Anything Model (SAM) for advanced segmentation capabilities.

### Custom Segmentation
Train models on specific object types or domains for specialized use cases.

### Batch Processing
Extend the application for processing multiple images simultaneously.

## 🐛 Troubleshooting

### Common Issues

1. **"No segmentation mask found"**
   - Ensure the image contains detectable objects
   - Check if the model is properly loaded
   - Try different image formats

2. **Memory errors**
   - Reduce image resolution
   - Close other applications
   - Use smaller model variants

3. **Slow processing**
   - Consider GPU acceleration
   - Optimize image size before upload
   - Use lighter model variants

### Performance Tips

- **Image size**: Optimal size is 512x512 to 1024x1024 pixels
- **Format**: PNG provides best quality for transparent outputs
- **Model selection**: Choose model size based on accuracy vs. speed requirements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- **Ultralytics** for YOLO implementation
- **Meta AI** for Segment Anything Model
- **Streamlit** for the web framework
- **OpenCV** for computer vision operations

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the Jupyter notebooks for examples

## 🔮 Future Enhancements

- [ ] GPU acceleration support
- [ ] Batch processing capabilities
- [ ] Additional model architectures
- [ ] Real-time video processing
- [ ] API endpoint for integration
- [ ] Mobile application
- [ ] Cloud deployment options

---

**Happy background removing! 🎨✨**
