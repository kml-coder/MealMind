# utils/recommender/train.py
import torch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from utils.recommender.model import FoodRecommendationModel
from utils.recommender.user_vector import create_user_vectors
from torch.utils.data import DataLoader, TensorDataset
import json
import numpy as np

def load_user_data():
    input_data = []
    label_data = []
    for file in os.listdir("user_data"):
        if file.endswith("_preferences.json"):
            with open(os.path.join("user_data", file), "r", encoding="utf-8") as f:
                user = json.load(f)
                # 임의 feature vector 생성
                input_vec = encode_user_profile(user)
                input_data.append(input_vec)
                # 예: 추천할 음식 인덱스 (food_data에서)
                label_data.append(0)
    return np.array(input_data), np.array(label_data)

def encode_user_profile(user):
    vec = []
    vec += [1 if c in user["original_cultures"] else 0 for c in ["Korean","Japanese","Chinese","American","Mexican"]]
    vec += [1 if r in user["dietary_restrictions"] else 0 for r in ["Vegan","Halal","Vegetarian"]]
    vec += [1 if a in user["allergies"] else 0 for a in ["Peanut","Egg","Seafood"]]
    return vec

def train_model():
    X, y = load_user_data()
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.long)

    dataset = TensorDataset(X_tensor, y_tensor)
    loader = DataLoader(dataset, batch_size=4, shuffle=True)

    model = FoodRecommendationModel(input_size=X.shape[1], hidden_size=16, output_size=10)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = torch.nn.CrossEntropyLoss()

    for epoch in range(20):
        for xb, yb in loader:
            pred = model(xb)
            loss = loss_fn(pred, yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"📉 Epoch {epoch+1}, Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), "utils/recommender/model.pth")

if __name__ == "__main__":
    train_model()
