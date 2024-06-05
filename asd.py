import os

model_path = 'best_93_yoloDual.pt'
if os.path.exists(model_path):
    print(f"File found: {model_path}")
else:
    print(f"File not found: {model_path}")
