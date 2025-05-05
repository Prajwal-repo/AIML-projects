
# CycleGAN Image-to-Image Translation

This project implements image-to-image translation using the CycleGAN architecture. It allows translation between two domains without requiring paired images. The architecture and scripts are inspired by the official CycleGAN and Pix2Pix implementation from Jun-Yan Zhu et al.

## Project Structure

- `CycleGAN.ipynb` - Jupyter Notebook for interactive experimentation and demonstration.
- `train.py` - Script to train the CycleGAN model on unpaired datasets.
- `test.py` - Script to test a trained CycleGAN model and generate translated results.
- `front.py` - Likely a front-end or integration script (e.g., Streamlit interface).

## Setup

### 1. Clone the repository and navigate into the directory:
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create a virtual environment and activate it (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

You may need the following key packages (manually install if not included):
```bash
pip install torch torchvision matplotlib wandb
```

## Training

To train a CycleGAN model:

```bash
python train.py --dataroot ./datasets/horse2zebra --name horse2zebra_cyclegan --model cycle_gan
```

Arguments:
- `--dataroot`: Path to the dataset.
- `--name`: Name for the experiment (used to save checkpoints and results).
- `--model`: Choose `cycle_gan` for unpaired image-to-image translation.

## Testing

To test the trained model and generate results:

```bash
python test.py --dataroot ./datasets/horse2zebra --name horse2zebra_cyclegan --model test --no_dropout
```

Results will be saved in `./results/horse2zebra_cyclegan`.

## Notebook Demo

You can explore the CycleGAN architecture interactively using `CycleGAN.ipynb` to visualize datasets, transformations, training loops, and test results.

## Frontend

If `front.py` is a Streamlit-based app, you can launch it using:
```bash
streamlit run front.py
```

## Additional Notes

- Modify `options/*.py` if you need custom training/testing settings.
- For using pretrained models or datasets, refer to: [https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
