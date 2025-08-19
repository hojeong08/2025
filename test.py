import streamlit as st

# -----------------------------
# 동물 질병 데이터베이스
# -----------------------------
disease_db = {
    # 개
    "개": {
        "개 홍역": {
            "symptoms": ["고열", "콧물", "눈곱", "기침", "구토", "설사", "발진", "경련", "마비"],
            "info": "바이러스 감염으로 여러 장기에 영향을 주는 전염병.",
            "treatment": "완치는 어렵고 증상 완화 치료가 중요. 예방접종 필수."
        },
        "개 파보바이러스": {
            "symptoms": ["구토", "설사", "혈변", "식욕 부진", "기력 저하", "고열"],
            "info": "강아지에게 치명적인 전염성 바이러스성 장염.",
            "treatment": "수액, 구토 억제제 등 보조치료 필요. 예방 백신 중요."
        },
    },

    # 고양이
    "고양이": {
        "고양이 백혈병 바이러스": {
            "symptoms": ["식욕부진", "체중 감소", "빈혈", "림프절 비대", "구강 염증"],
            "info": "면역력 저하를 일으키는 전염병.",
            "treatment": "완치는 어렵고 면역력 관리가 핵심. 백신 접종 가능."
        },
        "고양이 범백혈구 감소증": {
            "symptoms": ["구토", "설사", "식욕 부진", "발열", "기력 상실"],
            "info": "치사율 높은 전염병 (고양이 파보).",
            "treatment": "수액 및 보조 치료. 예방 백신 필수."
        },
    },

    # 소동물
    "토끼": {
        "토끼 위정체": {
            "symptoms": ["식욕 부진", "대변 감소", "웅크림", "복부 딱딱"],
            "info": "토끼 장 운동이 멈추는 위험한 상태.",
            "treatment": "빠른 진료 필요. 건초 급여로 예방."
        },
    },
    "햄스터": {
        "햄스터 웻테일": {
            "symptoms": ["설사", "꼬리 젖음", "악취", "무기력"],
            "info": "햄스터의 치명적인 세균성 장염.",
            "treatment": "항생제 치료와 깨끗한 환경 유지."
        },
    },
    "기니피그": {
        "기니피그 괴혈병": {
            "symptoms": ["보행 이상", "식욕 부진", "털 거침", "피부 건조", "관절 부종"],
            "info": "비타민 C 결핍으로 발생.",
            "treatment": "비타민 C 보충 필수."
        },
    },

    # 새
    "새": {
        "새 호흡기 질환": {
            "symptoms": ["콧물", "재채기", "쌕쌕거림", "숨 가쁨"],
            "info": "새는 호흡기가 약해 쉽게 감염.",
            "treatment": "항생제 치료와 온습도 조절."
        },
        "새 깃털뽑기": {
            "symptoms": ["깃털 빠짐", "피부 손상"],
            "info": "스트레스, 영양 부족, 기생충 등 원인 다양.",
            "treatment": "환경 개선, 영양제, 스트레스 완화 필요."
        },
    },

    # 물고기
    "물고기": {
        "물고기 백점병": {
            "symptoms": ["몸에 흰 점", "호흡곤란", "바닥에 몸 비빔"],
            "info": "기생충에 의해 발생하는 흔한 질환.",
            "treatment": "수온 상승+항기생충제 사용."
        },
        "물고기 지느러미썩음병": {
            "symptoms": ["지느러미 붉음", "지느러미 닳음"],
            "info": "세균성 질환. 수질 악화가 원인.",
            "treatment": "수질 개선 및 항생제 치료."
        },
        "물고기 수종병": {
            "symptoms": ["복부 팽창", "비늘 곤두섬"],
            "info": "세균성 복강 감염.",
            "treatment": "격리, 항생제, 수질 관리."
        },
    },

    # 파충류
    "파충류": {
        "파충류 구강염": {
            "symptoms": ["입 분비물", "먹이 거부"],
            "info": "입안 세균 감염으로 발생.",
            "treatment": "소독 및 항생제 치료 필요."
        },
        "파충류 대사성 골질환": {
            "symptoms": ["뼈 휘어짐", "움직임 이상", "무기력"],
            "info": "칼슘, 비타민 D 부족으로 발생.",
            "treatment": "칼슘+비타민 D 보충, UVB 조명 제공."
        },
        "파충류 호흡기 감염": {
            "symptoms": ["입 벌리고 호흡", "콧물", "거품", "호흡곤란"],
            "info": "저온·습기 원인. 세균/바이러스 감염.",
            "treatment": "따뜻한 환경+항생제 치료."
        },
    },
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="반려동물 질병 도우미", page_icon="🐾", layout="centered")

st.title("🐾 반려동물 질병 & 응급처치 도우미")
st.markdown("---")

# 1차 카테고리 선택
categories = list(set(disease_db.keys()))
animal = st.selectbox("📌 동물 종류를 선택하세요", sorted(categories))

# 2차 종 선택
if animal in disease_db:
    diseases = disease_db[animal]
    symptom_input = st.text_input("🔍 증상을 입력하세요 (예: 구토, 설사, 콧물)")

    if st.button("검색하기"):
        if symptom_input:
            found = []
            for disease, data in diseases.items():
                for symptom in data["symptoms"]:
                    if symptom in symptom_input:
                        found.append((disease, data))
                        break

            if found:
                for disease, data in found:
                    st.markdown(f"""
                    ### 🦠 {disease}
                    **어떤 병?** {data['info']}  
                    **주요 증상:** {", ".join(data['symptoms'])}  
                    **응급처치:** {data['treatment']}  
                    """)
                    st.markdown("---")
            else:
                st.warning("⚠️ 해당 증상에 맞는 질병을 찾을 수 없습니다. 꼭 수의사에게 진료를 받아보세요.")
        else:
            st.error("❗ 증상을 입력해주세요.")

