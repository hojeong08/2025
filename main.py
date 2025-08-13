
import streamlit as st
from PIL import Image
import os

# MBTI에 따른 추천 애완동물과 이미지 매핑 정보를 불러오는 함수
def load_mbti_mapping():
    # 각 MBTI 유형별 추천 애완동물과 이미지 경로를 사전(dictionary)에 저장
    # 이미지 파일은 프로젝트 폴더 내의 "images" 폴더에 저장되어 있어야 합니다.
    mbti_pet_mapping = {
        "INFJ": {"pet": "Cat", "description": "내성적이면서도 온화한 고양이가 잘 어울립니다.", "image": "images/cat.jpg"},
        "INFP": {"pet": "Rabbit", "description": "상냥하고 따뜻한 토끼가 좋은 친구가 될 거예요.", "image": "images/rabbit.jpg"},
        "ENFJ": {"pet": "Dog", "description": "사교적이고 충성스러운 강아지가 잘 맞습니다.", "image": "images/dog.jpg"},
        "ENFP": {"pet": "Parrot", "description": "활발하고 다채로운 앵무새가 추천됩니다.", "image": "images/parrot.jpg"},
        "INTJ": {"pet": "Owl", "description": "지적이고 신비로운 올빼미가 최적의 선택입니다.", "image": "images/owl.jpg"},
        "INTP": {"pet": "Turtle", "description": "차분하고 느긋한 거북이가 잘 어울립니다.", "image": "images/turtle.jpg"},
        "ENTJ": {"pet": "Bull", "description": "강인하고 결단력 있는 황소가 멋진 파트너가 될 거예요.", "image": "images/bull.jpg"},
        "ENTP": {"pet": "Ferret", "description": "호기심 많고 에너지 넘치는 페릿(담비)이 좋습니다.", "image": "images/ferret.jpg"},
        "ISFJ": {"pet": "Golden Retriever", "description": "따뜻하고 친근한 골든리트리버가 추천됩니다.", "image": "images/golden_retriever.jpg"},
        "ISFP": {"pet": "Rabbit", "description": "부드럽고 예민한 토끼가 어울립니다.", "image": "images/rabbit2.jpg"},
        "ESFJ": {"pet": "Dog", "description": "사교적이고 다정한 강아지가 최선입니다.", "image": "images/dog2.jpg"},
        "ESFP": {"pet": "Parrot", "description": "활기차고 생동감 있는 앵무새가 어울립니다.", "image": "images/parrot2.jpg"},
        "ISTJ": {"pet": "Cat", "description": "체계적이고 신중한 고양이가 잘 맞습니다.", "image": "images/cat2.jpg"},
        "ISTP": {"pet": "Iguana", "description": "독립적이고 개성이 강한 이구아나가 좋습니다.", "image": "images/iguana.jpg"},
        "ESTJ": {"pet": "Dog", "description": "리더십이 있는 강아지가 어울립니다.", "image": "images/dog3.jpg"},
        "ESTP": {"pet": "Parrot", "description": "활동적이고 모험을 즐기는 앵무새가 추천됩니다.", "image": "images/parrot3.jpg"}
    }
    return mbti_pet_mapping

# 사이드바에 MBTI 선택 위젯을 추가하는 함수
def setup_sidebar(mbti_pet_mapping):
    st.sidebar.title("MBTI 선택")
    st.sidebar.markdown("당신의 MBTI 유형을 선택하세요:")
    # MBTI 유형 리스트 생성 (사전의 키값 순서대로)
    mbti_types = list(mbti_pet_mapping.keys())
    selected_mbti = st.sidebar.selectbox("MBTI 선택", mbti_types)
    return selected_mbti

# 사용자 선택에 따른 애완동물 추천을 화면에 표시하는 함수
def render_recommendation(selected_mbti, mbti_pet_mapping):
    recommendation = mbti_pet_mapping.get(selected_mbti)
    if recommendation:
        st.subheader(f"{selected_mbti} 유형에 맞는 애완동물: {recommendation['pet']}")
        st.write(recommendation["description"])
        image_path = recommendation["image"]
        # 파일이 실제로 존재하는지 확인 후 이미지를 표시
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption=recommendation['pet'], use_column_width=True)
        else:
            st.error("이미지 파일을 찾을 수 없습니다.")
    else:
        st.error("해당 MBTI 유형에 대한 추천 정보를 찾을 수 없습니다.")

# 웹 앱의 스타일과 페이지 레이아웃을 설정하는 함수
def setup_layout():
    # 페이지 제목과 헤더 설정
    st.set_page_config(page_title="MBTI 애완동물 추천기", layout="wide")
    st.title("MBTI 애완동물 추천 웹앱")
    st.header("당신의 MBTI에 어울리는 애완동물을 찾아보세요!")
    st.markdown("""
        <style>
            body {
                background-color: #f0f8ff;
            }
            .header {
                color: #4a4a4a;
            }
            .recommendation {
                font-size: 18px;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("이 웹앱은 당신의 MBTI 유형에 맞는 애완동물을 추천해드립니다. 사이드바에서 MBTI를 선택해보세요!", unsafe_allow_html=True)

# 메인 함수: 앱의 전체 흐름을 제어함
def main():
    setup_layout()  # 페이지 레이아웃 및 스타일 설정
    mbti_pet_mapping = load_mbti_mapping()  # MBTI별 애완동물 정보 로드
    selected_mbti = setup_sidebar(mbti_pet_mapping)  # 사이드바를 통한 MBTI 선택
    # 사용자 선택에 따라 추천 결과 표시
    render_recommendation(selected_mbti, mbti_pet_mapping)
    # 추가적인 'About' 섹션 표시
    st.markdown("---")
    st.markdown("### 어플리케이션 정보")
    st.markdown("이 앱은 MBTI 유형과 그에 맞는 애완동물을 추천하는 간단한 웹 앱입니다. "
                "Streamlit를 이용하여 만들어졌으며, 각 애완동물의 이미지는 로컬의 'images' 폴더에 저장되어 있습니다. "
                "관심 있는 분은 GitHub에서 소스 코드를 참고해주세요.")

if __name__ == '__main__':
    main()

