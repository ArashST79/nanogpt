# Nano GPT Shakespeare

This project implements a small GPT model (nano GPT) trained on Shakespeare's text. The implementation is based on Andrej Karpathy's nanoGPT, but simplified and focused on the Shakespeare dataset.

## Project Structure

- `model.py`: Contains the GPT model implementation
- `config.py`: Model configurations (nano and tiny variants)
- `data.py`: Data loading and preprocessing for Shakespeare's text
- `train.py`: Training script
- `requirements.txt`: Project dependencies

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set up Weights & Biases for experiment tracking:
```bash
wandb login
```

## Training

To train the model:

```bash
python train.py
```

The script will:
1. Download Shakespeare's text if not already present
2. Initialize the nano GPT model
3. Train the model for 5000 iterations
4. Save the model checkpoint
5. Log metrics and sample generations to Weights & Biases (if configured)

## Model Architecture

The nano GPT model has the following specifications:
- 6 transformer layers
- 8 attention heads
- 384 embedding dimensions
- 128 context window
- Character-level tokenization

## Training Details

- Batch size: 64
- Learning rate: 3e-4
- Weight decay: 0.1
- AdamW optimizer with beta1=0.9, beta2=0.95
- Training iterations: 5000
- Evaluation every 100 iterations
- Sample generation every 500 iterations

## Results

The model will generate Shakespeare-like text samples during training. You can monitor the training progress through:
1. Console output showing loss values
2. Weights & Biases dashboard (if configured)
3. Generated text samples

## Next Steps

After training, you can:
1. Fine-tune the model on MMLU dataset
2. Experiment with different model configurations
3. Try different training hyperparameters
4. Generate more text samples with the trained model # nanogpt