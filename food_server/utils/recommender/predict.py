# utils/recommender/predict.py
import torch
from utils.recommender.model import FoodRecommendationModel
from utils.recommender.train import encode_user_profile
from utils.recommender.food_data import food_list

def load_model(input_size):
    model = FoodRecommendationModel(input_size=input_size, hidden_size=16, output_size=len(food_list))
    model.load_state_dict(torch.load("utils/recommender/model.pth"))
    model.eval()
    return model

def predict_food(user_profile):
    x = torch.tensor([encode_user_profile(user_profile)], dtype=torch.float32)
    model = load_model(x.shape[1])
    with torch.no_grad():
        output = model(x)
        top_idx = output.argmax(dim=1).item()
    return food_list[top_idx]
