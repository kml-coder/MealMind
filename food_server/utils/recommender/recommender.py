def score_food(food, user_info):
    score = 0

    if food["name"] in user_info["recent_foods"]:
        return -1

    if "weather" in food and food["weather"] == user_info["current_weather"]:
        score += 1.5

    if "weight" in food and food["weight"] == user_info["preferred_weight"]:
        score += 1.2

    if "culture" in food and food["culture"] == user_info["preferred_culture"]:
        score += 1.0

    return score

def recommend_foods(food_list, user_info, top_n=3):
    scored = [(food["name"], score_food(food, user_info)) for food in food_list]
    scored = [item for item in scored if item[1] >= 0]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]
