
import streamlit as st

# MBTI와 애완동물 추천 매핑 딕셔너리 구성
pets = {
    "INTJ": {
        "pet": "Cat",
        "description": "독립적이고 사색적인 당신에게 어울리는 고양이!",
        "image": "https://via.placeholder.com/300x200.png?text=Cat"
    },
    "ENFP": {
        "pet": "Dog",
        "description": "활발하고 친근한 당신에게 어울리는 강아지!",
        "image": "https://via.placeholder.com/300x200.png?text=Dog"
    },
    "INFJ": {
        "pet": "Rabbit",
        "description": "섬세하고 따뜻한 당신에게 어울리는 토끼!",
        "image": "https://via.placeholder.com/300x200.png?text=Rabbit"
    },
    "ESTP": {
        "pet": "Fish",
        "description": "모험심 넘치고 자유로운 당신에게 어울리는 물고기!",
        "image": "https://via.placeholder.com/300x200.png?text=Fish"
    }
}

# Streamlit 앱 타이틀 및 설명 출력
st.title("MBTI 애완동물 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 애완동물을 추천해드립니다.")

# MBTI 유형 선택하는 셀렉트 박스 생성
mbti_types = list(pets.keys())
user_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

# 선택된 MBTI 타입에 따른 추천 결과 표시
if user_mbti in pets:
    pet_info = pets[user_mbti]
    
    # 추천 결과 헤더 및 설명 출력
    st.subheader(f"추천 애완동물: {pet_info['pet']}")
    st.write(pet_info["description"])
    
    # 추천 애완동물 이미지 출력
    st.image(pet_info["image"], caption=pet_info["pet"], use_column_width=True)
else:
    # 지원하지 않는 MBTI 타입인 경우 에러 메시지 표시
    st.error("지원하지 않는 MBTI 유형입니다. 다른 유형을 선택해주세요.")

