# utils/recommender/user_vector.py

def create_user_vectors(user_data_list, food_list):
    """
    user_data_list: List of dictionaries. Each dict contains:
      - original_cultures
      - recent_cultures
      - dietary_restrictions
      - allergies

    food_list: List of food item dictionaries with the same keys

    Returns: list of user vectors
    """
    vectors = []
    for user in user_data_list:
        vector = []
        for food in food_list:
            score = 0
            # 점수는 일치하는 요소의 개수
            if food["culture"] in user.get("original_cultures", []):
                score += 1
            if food["culture"] in user.get("recent_cultures", []):
                score += 2  # 최근 선호는 더 높은 가중치
            if any(restrict in food.get("tags", []) for restrict in user.get("dietary_restrictions", [])):
                score -= 1
            if any(allergy in food.get("ingredients", []) for allergy in user.get("allergies", [])):
                score -= 2  # 알레르기는 더 강한 감점
            vector.append(score)
        vectors.append(vector)
    return vectors
