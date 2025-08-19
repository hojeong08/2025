import streamlit as st

# 병명 및 응급처치 데이터 (예시)
disease_db = {
    "개": {
        "설사": ("장염", "수분 보충, 기름진 음식 피하기"),
        "기침": ("기관지염", "따뜻한 환경 유지, 차가운 바람 피하기"),
    },
    "고양이": {
        "설사": ("소화불량", "금식 후 물 제공, 기름진 음식 피하기"),
        "식욕부진": ("간 질환 가능성", "즉시 동물병원 내원 권장"),
    }
}

# 사이트 제목
st.title("🐾 반려동물 증상 응급 도우미")

# 사용자 입력
animal = st.selectbox("동물을 선택하세요", ["개", "고양이"])
symptom = st.text_input("증상을 입력하세요 (예: 설사, 기침, 식욕부진)")

# 결과 출력
if st.button("진단하기"):
    if animal in disease_db and symptom in disease_db[animal]:
        disease, care = disease_db[animal][symptom]
        st.success(f"예상 병명: {disease}")
        st.info(f"응급처치 방법: {care}")
    else:
        st.warning("해당 증상에 대한 데이터가 없습니다. 꼭 수의사 상담을 권장합니다.")

