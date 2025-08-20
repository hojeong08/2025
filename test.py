import streamlit as st


# -----------------------------
# 동물 질병 데이터베이스 (수정 없음)
# - 'icon': 동물을 대표하는 이모지 (혹은 질병 관련 이모지)
# - 'severity': 질병의 심각도 ('높음', '중간', '낮음')
# -----------------------------
disease_db = {
    # 개
    "개": {
        "개 홍역": {
            "symptoms": ["고열", "콧물", "눈곱", "기침", "구토", "설사", "발진", "경련", "마비"],
            "info": "바이러스 감염으로 여러 장기에 영향을 주는 치명적인 전염병.",
            "treatment": "완치는 어렵고 증상 완화 치료가 중요. 예방접종 필수.",
            "icon": "EMOJI_1",
            "severity": "높음"
        },
        "개 파보바이러스": {
            "symptoms": ["구토", "설사", "혈변", "식욕 부진", "기력 저하", "고열"],
            "info": "강아지에게 치명적인 전염성 바이러스성 장염.",
            "treatment": "수액, 구토 억제제 등 보조치료 필요. 예방 백신 중요.",
            "icon": "EMOJI_2",
            "severity": "높음"
        },
        "개 피부병": {
            "symptoms": ["가려움", "발적", "탈모", "딱지", "비듬"],
            "info": "다양한 원인(알레르기, 기생충, 세균 등)으로 발생하는 피부 질환.",
            "treatment": "원인에 따른 약물 치료 및 환경 관리.",
            "icon": "EMOJI_3",
            "severity": "중간"
        }
    },

    # 고양이
    "고양이": {
        "고양이 백혈병 바이러스": {
            "symptoms": ["식욕부진", "체중 감소", "빈혈", "림프절 비대", "구강 염증"],
            "info": "면역력 저하를 일으키는 전염병.",
            "treatment": "완치는 어렵고 면역력 관리가 핵심. 백신 접종 가능.",
            "icon": "EMOJI_4",
            "severity": "높음"
        },
        "고양이 범백혈구 감소증": {
            "symptoms": ["구토", "설사", "식욕 부진", "발열", "기력 상실"],
            "info": "치사율 높은 전염병 (고양이 파보).",
            "treatment": "수액 및 보조 치료. 예방 백신 필수.",
            "icon": "EMOJI_5",
            "severity": "높음"
        },
        "고양이 신장 질환": {
            "symptoms": ["다음다뇨", "체중 감소", "구토", "식욕부진", "탈수"],
            "info": "만성 신장 질환은 고양이에게 흔하며, 조기 발견 및 관리가 중요.",
            "treatment": "식이 요법, 수액 치료, 약물 치료.",
            "icon": "EMOJI_6",
            "severity": "높음"
        },
        "고양이 비대성 심근병증": {
            "symptoms": ["호흡 곤란", "기침", "무기력", "식욕 부진", "급사", "뒷다리 마비"],
            "info": "고양이에게 가장 흔한 심장 질환으로, 심장벽이 비대해져 기능 저하를 일으킴.",
            "treatment": "약물 관리, 정기 검진 필수. 완치 어려움.",
            "icon": "EMOJI_7",
            "severity": "높음"
        }
    },

    # 소동물
    "토끼": {
        "토끼 위정체": {
            "symptoms": ["식욕 부진", "대변 감소", "웅크림", "복부 딱딱"],
            "info": "토끼 장 운동이 멈추는 위험한 상태.",
            "treatment": "빠른 진료 필요. 건초 급여로 예방.",
            "icon": "EMOJI_8",
            "severity": "높음"
        },
        "토끼 부정교합": {
            "symptoms": ["식욕 부진", "침 흘림", "체중 감소", "눈물", "음식물 흘림"],
            "info": "토끼의 치아가 과도하게 자라거나 배열이 맞지 않아 발생하는 문제. 소화 장애로 이어질 수 있음.",
            "treatment": "정기적인 치아 트리밍 및 발치, 식이 개선(건초 위주).",
            "icon": "EMOJI_9",
            "severity": "중간"
        }
    },
    "햄스터": {
        "햄스터 웻테일": {
            "symptoms": ["설사", "꼬리 젖음", "악취", "무기력"],
            "info": "햄스터의 치명적인 세균성 장염.",
            "treatment": "항생제 치료와 깨끗한 환경 유지.",
            "icon": "EMOJI_10",
            "severity": "높음"
        },
        "햄스터 감기": {
            "symptoms": ["재채기", "콧물", "무기력", "식욕 부진"],
            "info": "사람에게도 옮을 수 있는 호흡기 질환.",
            "treatment": "따뜻하고 습한 환경 유지, 심할 경우 항생제 처방.",
            "icon": "EMOJI_11",
            "severity": "낮음"
        }
    },
    "기니피그": {
        "기니피그 괴혈병": {
            "symptoms": ["보행 이상", "식욕 부진", "털 거침", "피부 건조", "관절 부종"],
            "info": "비타민 C 결핍으로 발생.",
            "treatment": "비타민 C 보충 필수.",
            "icon": "EMOJI_12",
            "severity": "높음"
        }
    },

    # 새
    "새": {
        "새 호흡기 질환": {
            "symptoms": ["콧물", "재채기", "쌕쌕거림", "숨 가쁨"],
            "info": "새는 호흡기가 약해 쉽게 감염.",
            "treatment": "항생제 치료와 온습도 조절.",
            "icon": "EMOJI_13",
            "severity": "중간"
        },
        "새 깃털뽑기": {
            "symptoms": ["깃털 빠짐", "피부 손상"],
            "info": "스트레스, 영양 부족, 기생충 등 원인 다양.",
            "treatment": "환경 개선, 영양제, 스트레스 완화 필요.",
            "icon": "EMOJI_14",
            "severity": "낮음"
        }
    },

    # 물고기
    "물고기": {
        "물고기 백점병": {
            "symptoms": ["몸에 흰 점", "호흡곤란", "바닥에 몸 비빔"],
            "info": "기생충에 의해 발생하는 흔한 질환.",
            "treatment": "수온 상승+항기생충제 사용.",
            "icon": "EMOJI_15",
            "severity": "낮음"
        },
        "물고기 지느러미썩음병": {
            "symptoms": ["지느러미 붉음", "지느러미 닳음"],
            "info": "세균성 질환. 수질 악화가 원인.",
            "treatment": "수질 개선 및 항생제 치료.",
            "icon": "EMOJI_16",
            "severity": "중간"
        },
        "물고기 수종병": {
            "symptoms": ["복부 팽창", "비늘 곤두섬"],
            "info": "세균성 복강 감염.",
            "treatment": "격리, 항생제, 수질 관리.",
            "icon": "EMOJI_17",
            "severity": "높음"
        }
    },

    # 파충류
    "파충류": {
        "파충류 구강염": {
            "symptoms": ["입 분비물", "먹이 거부"],
            "info": "입안 세균 감염으로 발생.",
            "treatment": "소독 및 항생제 치료 필요.",
            "icon": "EMOJI_18",
            "severity": "중간"
        },
        "파충류 대사성 골질환": {
            "symptoms": ["뼈 휘어짐", "움직임 이상", "무기력"],
            "info": "칼슘, 비타민 D 부족으로 발생.",
            "treatment": "칼슘+비타민 D 보충, UVB 조명 제공.",
            "icon": "EMOJI_19",
            "severity": "높음"
        },
        "파충류 호흡기 감염": {
            "symptoms": ["입 벌리고 호흡", "콧물", "거품", "호흡곤란"],
            "info": "저온·습기 원인. 세균/바이러스 감염.",
            "treatment": "따뜻한 환경+항생제 치료.",
            "icon": "EMOJI_20",
            "severity": "중간"
        }
    },
}

# -----------------------------
# 동물별 건강 관리 가이드 데이터베이스 (새로 추가)
# -----------------------------
health_tips_db = {
    "개": {
        "title": "EMOJI_21 우리 댕댕이 건강하게 키우기",
        "tips": [
            "**정기적인 예방접종과 건강검진:** 매년 필수 예방접종과 종합 건강검진으로 질병을 미리 예방하세요.",
            "**균형 잡힌 사료 급여:** 나이, 활동량, 품종에 맞는 사료를 급여하고, 비만 예방에 신경 써주세요.",
            "**매일 충분한 산책:** 에너지를 발산하고 사회성을 기를 수 있도록 매일 꾸준히 산책시켜주세요.",
            "**구강 관리:** 정기적인 양치질과 스케일링으로 치아 질환을 예방해주세요.",
            "**심장사상충 및 외부 기생충 예방:** 매월 예방약 투여로 치명적인 기생충 감염을 막아주세요."
        ]
    },
    "고양이": {
        "title": "EMOJI_22 우리 냥이 집사 필독! 건강 가이드",
        "tips": [
            "**음수량 체크:** 신장 질환 예방을 위해 항상 깨끗한 물을 제공하고, 음수량을 늘릴 수 있는 환경을 만들어주세요.",
            "**화장실 청결 유지:** 고양이는 청결에 민감해요. 화장실을 깨끗하게 관리해야 스트레스를 줄일 수 있습니다.",
            "**규칙적인 놀이 시간:** 사냥 놀이를 통해 스트레스를 해소하고 적정 활동량을 유지시켜주세요.",
            "**헤어볼 관리:** 빗질을 자주 해주고 헤어볼 영양제를 급여하여 헤어볼 문제를 예방해주세요.",
            "**정기적인 건강검진:** 고양이는 아픔을 잘 숨기기 때문에 주기적인 건강검진이 더욱 중요합니다."
        ]
    },
    "토끼": {
        "title": "EMOJI_23 토끼 집사 주목! 건강 관리 팁",
        "tips": [
            "**건초는 무제한:** 섬유질이 풍부한 건초를 주식으로 무제한 급여하여 소화기 건강과 치아 관리를 동시에 해주세요.",
            "**깨끗한 환경:** 항상 깨끗하고 건조한 환경을 제공하여 피부병이나 호흡기 질환을 예방하세요.",
            "**치아 관리:** 치아는 평생 자라므로, 건초와 딱딱한 장난감으로 자연스러운 마모를 유도하세요.",
            "**스트레스 관리:** 토끼는 예민한 동물입니다. 조용하고 안정적인 환경을 제공하고 큰 소리나 급격한 변화를 피해주세요.",
            "**건강 변화 관찰:** 토끼는 아파도 티를 잘 안 내므로, 평소보다 식욕이 없거나 활동량이 줄면 즉시 수의사를 찾아야 합니다."
        ]
    },
    "햄스터": {
        "title": "EMOJI_24 귀요미 햄스터 건강 팁",
        "tips": [
            "**온도 및 습도 관리:** 적절한 온도(20~26℃)와 습도를 유지하여 호흡기 질환을 예방하세요.",
            "**사육 환경 청결:** 케이지 청소를 자주 하여 세균 번식을 막고 위생을 철저히 하세요.",
            "**균형 잡힌 식단:** 햄스터 전용 사료와 소량의 채소, 과일 등을 급여하여 영양 균형을 맞춰주세요.",
            "**물병 위생:** 물병의 급수 꼭지가 막히지 않았는지 매일 확인하고, 물을 신선하게 갈아주세요."
        ]
    },
    "기니피그": {
        "title": "EMOJI_25 기니피그 건강 유지 가이드",
        "tips": [
            "**비타민 C 필수:** 기니피그는 체내에서 비타민 C를 합성하지 못하므로, 매일 비타민 C가 풍부한 채소나 보충제를 급여해야 합니다.",
            "**건초는 언제나:** 토끼와 마찬가지로 건초가 주식이며, 소화기와 치아 건강에 매우 중요합니다.",
            "**청결한 케이지:** 습기와 암모니아 가스는 호흡기 질환을 유발할 수 있으므로, 케이지를 항상 청결하게 관리해주세요.",
            "**활동 공간:** 충분히 움직일 수 있는 넓은 공간을 제공하여 스트레스를 줄이고 건강을 증진시켜주세요."
        ]
    },
    "새": {
        "title": "EMOJI_26 우리 새 친구 건강 지키기",
        "tips": [
            "**온도 변화에 주의:** 새는 온도 변화에 매우 민감하니, 급격한 온도 변화를 피하고 적정 온도를 유지해주세요.",
            "**신선한 물과 먹이:** 매일 신선한 물과 균형 잡힌 먹이를 제공하고, 케이지 내 위생을 철저히 해주세요.",
            "**환기 및 습도:** 주기적인 환기로 공기를 맑게 하고, 적절한 습도를 유지해주세요.",
            "**횃대 및 장난감 교체:** 다양한 굵기의 횃대와 청결한 장난감을 제공하여 발 건강과 스트레스 해소를 도와주세요."
        ]
    },
    "물고기": {
        "title": "EMOJI_27 건강한 물고기 키우는 법",
        "tips": [
            "**정기적인 물 갈이:** 어항의 수질은 물고기 건강에 가장 중요해요. 정기적으로 물을 갈아주고 여과기를 관리해주세요.",
            "**적정 수온 유지:** 물고기 종류에 맞는 적정 수온을 항상 유지시켜 주세요. 갑작스러운 변화는 스트레스를 줍니다.",
            "**과다 급여 금지:** 사료를 너무 많이 주면 수질 악화의 원인이 되니, 물고기가 다 먹을 수 있는 만큼만 급여하세요.",
            "**수초 및 은신처:** 스트레스를 줄이고 안정감을 느낄 수 있도록 수초나 은신처를 마련해주세요."
        ]
    },
    "파충류": {
        "title": "EMOJI_28 파충류 건강을 위한 완벽 가이드",
        "tips": [
            "**온도 및 습도 조절:** 각 파충류 종에 맞는 정확한 온도 및 습도 환경을 조성해주는 것이 생명 유지에 필수적입니다.",
            "**UVB 램프 설치:** 많은 파충류에게 칼슘 흡수를 돕는 UVB 램프는 필수적이므로, 주기적으로 교체하고 적절한 거리에 설치해주세요.",
            "**청결한 사육장:** 위생은 질병 예방의 기본입니다. 사육장을 항상 청결하게 관리하고 배설물을 즉시 치워주세요.",
            "**균형 잡힌 식단:** 파충류 종류에 맞는 영양 균형 잡힌 먹이를 제공하고, 비타민/칼슘 보충제를 급여해주세요."
        ]
    }
}


# 심각도에 따른 색상/아이콘 매핑
severity_map = {
    "높음": "EMOJI_29 심각",
    "중간": "EMOJI_30 주의",
    "낮음": "EMOJI_31 경미"
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="반려동물 질병 & 건강 도우미", page_icon="EMOJI_32", layout="centered")

st.title("EMOJI_33 반려동물 질병 & 응급처치 도우미")
st.markdown("---")
st.warning("⚠️ 본 정보는 참고용이며, 정확한 진단 및 치료는 반드시 수의사에게 받아야 합니다.")

# 1차 카테고리 선택
categories = list(set(disease_db.keys()))
animal = st.selectbox("EMOJI_34 동물 종류를 선택하세요", sorted(categories))

# --- 반려동물 건강 관리 가이드 섹션 (새로 추가) ---
st.markdown("## ✨ 반려동물 건강 관리 가이드")
st.markdown(f"**{health_tips_db.get(animal, {'title': '정보 없음'})['title']}**")
for tip in health_tips_db.get(animal, {'tips': ["해당 동물의 건강 관리 팁이 아직 준비되지 않았습니다. ㅠㅠ"]})['tips']:
    st.markdown(f"- {tip}")
st.markdown("---")

# --- 질병 검색 섹션 ---
st.markdown("## EMOJI_35 질병 검색")
diseases = disease_db[animal]
symptom_input = st.text_input("EMOJI_36 증상을 쉼표(,)로 구분하여 입력하세요 (예: 구토, 설사, 콧물)")

if st.button("검색하기"):
    if symptom_input:
        user_symptoms_raw = [s.strip() for s in symptom_input.split(',') if s.strip()]
        user_symptoms_unique = list(set(user_symptoms_raw)) # 중복 제거

        if not user_symptoms_unique:
            st.error("❗ 유효한 증상을 입력해주세요.")
        else:
            found = []
            for disease, data in diseases.items():
                matched_count = 0
                for user_symptom in user_symptoms_unique:
                    if user_symptom in data["symptoms"]:
                        matched_count += 1
                
                if matched_count > 0:
                    accuracy = (matched_count / len(user_symptoms_unique)) * 100
                    found.append((disease, data, accuracy))
            
            found.sort(key=lambda x: x[2], reverse=True)

            if found:
                st.success(f"입력하신 증상 '{', '.join(user_symptoms_unique)}'에 대한 검색 결과입니다.")
                # 긴급 연락처/응급처치 안내 메시지 (여기서 한 번만 띄우기 위해 플래그 사용)
                displayed_emergency_prompt = False

                for disease, data, accuracy in found:
                    current_severity = data.get('severity', '정보 없음')
                    
                    # 빨간색 박스 긴급 안내 (첫 번째 '높음' 질병 발견 시)
                    if current_severity == "높음" and not displayed_emergency_prompt:
                        st.markdown(f"""
                        <div style="background-color: #ffcccc; padding: 15px; border-radius: 10px; border: 2px solid #cc0000;">
                            <h3 style="color: #cc0000; margin-top: 0;">EMOJI_37 긴급 상황 알림! EMOJI_38</h3>
                            <p style="color: #cc0000;">지금 바로 수의사에게 연락하세요! 반려동물의 생명이 위급할 수 있습니다. 지체하지 마세요.</p>
                            <p style="color: #cc0000; font-weight: bold;">가까운 동물병원을 검색해보세요 ⬇️</p>
                        </div>
                        """, unsafe_allow_html=True)
                        st.markdown("---")
                        displayed_emergency_prompt = True # 한 번 띄웠으면 다시 띄우지 않음

                    st.markdown(f"""
                    ### {data['icon']} {disease} {severity_map.get(current_severity, '정보 없음')}
                    **매칭 정확도:** {accuracy:.1f}% EMOJI_39
                    **어떤 병?** {data['info']}  
                    **주요 증상:** {", ".join(data['symptoms'])}  
                    **응급처치:** {data['treatment']}  
                    """)
                    st.markdown("---")
            else:
                st.warning(f"⚠️ 입력하신 증상 '{symptom_input}'에 맞는 질병을 찾을 수 없습니다. 꼭 수의사에게 진료를 받아보세요.")
    else:
        st.error("❗ 증상을 입력해주세요.")

# --- 동물병원 찾기 섹션 (새로 추가) ---
st.markdown("---")
st.markdown("## EMOJI_40 가까운 동물병원 찾기")
vet_location = st.text_input("EMOJI_41 현재 계신 동네나 시/군/구를 입력하세요 (예: 서울 강남구, 분당, 부산 해운대)")

if st.button("동물병원 검색"):
    if vet_location:
        search_query = f"동물병원 {vet_location}"
        # 구글맵스 검색 링크 생성
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={search_query}"
        st.markdown(f"'{vet_location}' 근처 동물병원을 Google Maps에서 찾아보세요:")
        st.markdown(f"[**EMOJI_42 {vet_location} 동물병원 검색하기**]({google_maps_url})")
        st.info("EMOJI_43 링크를 클릭하면 새 탭에서 구글맵스 검색 결과가 열립니다. 급한 상황이라면 바로 연락해서 방문하세요!")
    else:
        st.warning("⚠️ 검색할 지역을 입력해주세요.")
import streamlit as st

# -----------------------------
# 동물 질병 데이터베이스 (수정 없음)
# - 'icon': 동물을 대표하는 이모지 (혹은 질병 관련 이모지)
# - 'severity': 질병의 심각도 ('높음', '중간', '낮음')
# -----------------------------
disease_db = {
    # 개
    "개": {
        "개 홍역": {
            "symptoms": ["고열", "콧물", "눈곱", "기침", "구토", "설사", "발진", "경련", "마비"],
            "info": "바이러스 감염으로 여러 장기에 영향을 주는 치명적인 전염병.",
            "treatment": "완치는 어렵고 증상 완화 치료가 중요. 예방접종 필수.",
            "icon": "EMOJI_1",
            "severity": "높음"
        },
        "개 파보바이러스": {
            "symptoms": ["구토", "설사", "혈변", "식욕 부진", "기력 저하", "고열"],
            "info": "강아지에게 치명적인 전염성 바이러스성 장염.",
            "treatment": "수액, 구토 억제제 등 보조치료 필요. 예방 백신 중요.",
            "icon": "EMOJI_2",
            "severity": "높음"
        },
        "개 피부병": {
            "symptoms": ["가려움", "발적", "탈모", "딱지", "비듬"],
            "info": "다양한 원인(알레르기, 기생충, 세균 등)으로 발생하는 피부 질환.",
            "treatment": "원인에 따른 약물 치료 및 환경 관리.",
            "icon": "EMOJI_3",
            "severity": "중간"
        }
    },

    # 고양이
    "고양이": {
        "고양이 백혈병 바이러스": {
            "symptoms": ["식욕부진", "체중 감소", "빈혈", "림프절 비대", "구강 염증"],
            "info": "면역력 저하를 일으키는 전염병.",
            "treatment": "완치는 어렵고 면역력 관리가 핵심. 백신 접종 가능.",
            "icon": "EMOJI_4",
            "severity": "높음"
        },
        "고양이 범백혈구 감소증": {
            "symptoms": ["구토", "설사", "식욕 부진", "발열", "기력 상실"],
            "info": "치사율 높은 전염병 (고양이 파보).",
            "treatment": "수액 및 보조 치료. 예방 백신 필수.",
            "icon": "EMOJI_5",
            "severity": "높음"
        },
        "고양이 신장 질환": {
            "symptoms": ["다음다뇨", "체중 감소", "구토", "식욕부진", "탈수"],
            "info": "만성 신장 질환은 고양이에게 흔하며, 조기 발견 및 관리가 중요.",
            "treatment": "식이 요법, 수액 치료, 약물 치료.",
            "icon": "EMOJI_6",
            "severity": "높음"
        },
        "고양이 비대성 심근병증": {
            "symptoms": ["호흡 곤란", "기침", "무기력", "식욕 부진", "급사", "뒷다리 마비"],
            "info": "고양이에게 가장 흔한 심장 질환으로, 심장벽이 비대해져 기능 저하를 일으킴.",
            "treatment": "약물 관리, 정기 검진 필수. 완치 어려움.",
            "icon": "EMOJI_7",
            "severity": "높음"
        }
    },

    # 소동물
    "토끼": {
        "토끼 위정체": {
            "symptoms": ["식욕 부진", "대변 감소", "웅크림", "복부 딱딱"],
            "info": "토끼 장 운동이 멈추는 위험한 상태.",
            "treatment": "빠른 진료 필요. 건초 급여로 예방.",
            "icon": "EMOJI_8",
            "severity": "높음"
        },
        "토끼 부정교합": {
            "symptoms": ["식욕 부진", "침 흘림", "체중 감소", "눈물", "음식물 흘림"],
            "info": "토끼의 치아가 과도하게 자라거나 배열이 맞지 않아 발생하는 문제. 소화 장애로 이어질 수 있음.",
            "treatment": "정기적인 치아 트리밍 및 발치, 식이 개선(건초 위주).",
            "icon": "EMOJI_9",
            "severity": "중간"
        }
    },
    "햄스터": {
        "햄스터 웻테일": {
            "symptoms": ["설사", "꼬리 젖음", "악취", "무기력"],
            "info": "햄스터의 치명적인 세균성 장염.",
            "treatment": "항생제 치료와 깨끗한 환경 유지.",
            "icon": "EMOJI_10",
            "severity": "높음"
        },
        "햄스터 감기": {
            "symptoms": ["재채기", "콧물", "무기력", "식욕 부진"],
            "info": "사람에게도 옮을 수 있는 호흡기 질환.",
            "treatment": "따뜻하고 습한 환경 유지, 심할 경우 항생제 처방.",
            "icon": "EMOJI_11",
            "severity": "낮음"
        }
    },
    "기니피그": {
        "기니피그 괴혈병": {
            "symptoms": ["보행 이상", "식욕 부진", "털 거침", "피부 건조", "관절 부종"],
            "info": "비타민 C 결핍으로 발생.",
            "treatment": "비타민 C 보충 필수.",
            "icon": "EMOJI_12",
            "severity": "높음"
        }
    },

    # 새
    "새": {
        "새 호흡기 질환": {
            "symptoms": ["콧물", "재채기", "쌕쌕거림", "숨 가쁨"],
            "info": "새는 호흡기가 약해 쉽게 감염.",
            "treatment": "항생제 치료와 온습도 조절.",
            "icon": "EMOJI_13",
            "severity": "중간"
        },
        "새 깃털뽑기": {
            "symptoms": ["깃털 빠짐", "피부 손상"],
            "info": "스트레스, 영양 부족, 기생충 등 원인 다양.",
            "treatment": "환경 개선, 영양제, 스트레스 완화 필요.",
            "icon": "EMOJI_14",
            "severity": "낮음"
        }
    },

    # 물고기
    "물고기": {
        "물고기 백점병": {
            "symptoms": ["몸에 흰 점", "호흡곤란", "바닥에 몸 비빔"],
            "info": "기생충에 의해 발생하는 흔한 질환.",
            "treatment": "수온 상승+항기생충제 사용.",
            "icon": "EMOJI_15",
            "severity": "낮음"
        },
        "물고기 지느러미썩음병": {
            "symptoms": ["지느러미 붉음", "지느러미 닳음"],
            "info": "세균성 질환. 수질 악화가 원인.",
            "treatment": "수질 개선 및 항생제 치료.",
            "icon": "EMOJI_16",
            "severity": "중간"
        },
        "물고기 수종병": {
            "symptoms": ["복부 팽창", "비늘 곤두섬"],
            "info": "세균성 복강 감염.",
            "treatment": "격리, 항생제, 수질 관리.",
            "icon": "EMOJI_17",
            "severity": "높음"
        }
    },

    # 파충류
    "파충류": {
        "파충류 구강염": {
            "symptoms": ["입 분비물", "먹이 거부"],
            "info": "입안 세균 감염으로 발생.",
            "treatment": "소독 및 항생제 치료 필요.",
            "icon": "EMOJI_18",
            "severity": "중간"
        },
        "파충류 대사성 골질환": {
            "symptoms": ["뼈 휘어짐", "움직임 이상", "무기력"],
            "info": "칼슘, 비타민 D 부족으로 발생.",
            "treatment": "칼슘+비타민 D 보충, UVB 조명 제공.",
            "icon": "EMOJI_19",
            "severity": "높음"
        },
        "파충류 호흡기 감염": {
            "symptoms": ["입 벌리고 호흡", "콧물", "거품", "호흡곤란"],
            "info": "저온·습기 원인. 세균/바이러스 감염.",
            "treatment": "따뜻한 환경+항생제 치료.",
            "icon": "EMOJI_20",
            "severity": "중간"
        }
    },
}

# -----------------------------
# 동물별 건강 관리 가이드 데이터베이스 (새로 추가)
# -----------------------------
health_tips_db = {
    "개": {
        "title": "EMOJI_21 우리 댕댕이 건강하게 키우기",
        "tips": [
            "**정기적인 예방접종과 건강검진:** 매년 필수 예방접종과 종합 건강검진으로 질병을 미리 예방하세요.",
            "**균형 잡힌 사료 급여:** 나이, 활동량, 품종에 맞는 사료를 급여하고, 비만 예방에 신경 써주세요.",
            "**매일 충분한 산책:** 에너지를 발산하고 사회성을 기를 수 있도록 매일 꾸준히 산책시켜주세요.",
            "**구강 관리:** 정기적인 양치질과 스케일링으로 치아 질환을 예방해주세요.",
            "**심장사상충 및 외부 기생충 예방:** 매월 예방약 투여로 치명적인 기생충 감염을 막아주세요."
        ]
    },
    "고양이": {
        "title": "EMOJI_22 우리 냥이 집사 필독! 건강 가이드",
        "tips": [
            "**음수량 체크:** 신장 질환 예방을 위해 항상 깨끗한 물을 제공하고, 음수량을 늘릴 수 있는 환경을 만들어주세요.",
            "**화장실 청결 유지:** 고양이는 청결에 민감해요. 화장실을 깨끗하게 관리해야 스트레스를 줄일 수 있습니다.",
            "**규칙적인 놀이 시간:** 사냥 놀이를 통해 스트레스를 해소하고 적정 활동량을 유지시켜주세요.",
            "**헤어볼 관리:** 빗질을 자주 해주고 헤어볼 영양제를 급여하여 헤어볼 문제를 예방해주세요.",
            "**정기적인 건강검진:** 고양이는 아픔을 잘 숨기기 때문에 주기적인 건강검진이 더욱 중요합니다."
        ]
    },
    "토끼": {
        "title": "EMOJI_23 토끼 집사 주목! 건강 관리 팁",
        "tips": [
            "**건초는 무제한:** 섬유질이 풍부한 건초를 주식으로 무제한 급여하여 소화기 건강과 치아 관리를 동시에 해주세요.",
            "**깨끗한 환경:** 항상 깨끗하고 건조한 환경을 제공하여 피부병이나 호흡기 질환을 예방하세요.",
            "**치아 관리:** 치아는 평생 자라므로, 건초와 딱딱한 장난감으로 자연스러운 마모를 유도하세요.",
            "**스트레스 관리:** 토끼는 예민한 동물입니다. 조용하고 안정적인 환경을 제공하고 큰 소리나 급격한 변화를 피해주세요.",
            "**건강 변화 관찰:** 토끼는 아파도 티를 잘 안 내므로, 평소보다 식욕이 없거나 활동량이 줄면 즉시 수의사를 찾아야 합니다."
        ]
    },
    "햄스터": {
        "title": "EMOJI_24 귀요미 햄스터 건강 팁",
        "tips": [
            "**온도 및 습도 관리:** 적절한 온도(20~26℃)와 습도를 유지하여 호흡기 질환을 예방하세요.",
            "**사육 환경 청결:** 케이지 청소를 자주 하여 세균 번식을 막고 위생을 철저히 하세요.",
            "**균형 잡힌 식단:** 햄스터 전용 사료와 소량의 채소, 과일 등을 급여하여 영양 균형을 맞춰주세요.",
            "**물병 위생:** 물병의 급수 꼭지가 막히지 않았는지 매일 확인하고, 물을 신선하게 갈아주세요."
        ]
    },
    "기니피그": {
        "title": "EMOJI_25 기니피그 건강 유지 가이드",
        "tips": [
            "**비타민 C 필수:** 기니피그는 체내에서 비타민 C를 합성하지 못하므로, 매일 비타민 C가 풍부한 채소나 보충제를 급여해야 합니다.",
            "**건초는 언제나:** 토끼와 마찬가지로 건초가 주식이며, 소화기와 치아 건강에 매우 중요합니다.",
            "**청결한 케이지:** 습기와 암모니아 가스는 호흡기 질환을 유발할 수 있으므로, 케이지를 항상 청결하게 관리해주세요.",
            "**활동 공간:** 충분히 움직일 수 있는 넓은 공간을 제공하여 스트레스를 줄이고 건강을 증진시켜주세요."
        ]
    },
    "새": {
        "title": "EMOJI_26 우리 새 친구 건강 지키기",
        "tips": [
            "**온도 변화에 주의:** 새는 온도 변화에 매우 민감하니, 급격한 온도 변화를 피하고 적정 온도를 유지해주세요.",
            "**신선한 물과 먹이:** 매일 신선한 물과 균형 잡힌 먹이를 제공하고, 케이지 내 위생을 철저히 해주세요.",
            "**환기 및 습도:** 주기적인 환기로 공기를 맑게 하고, 적절한 습도를 유지해주세요.",
            "**횃대 및 장난감 교체:** 다양한 굵기의 횃대와 청결한 장난감을 제공하여 발 건강과 스트레스 해소를 도와주세요."
        ]
    },
    "물고기": {
        "title": "EMOJI_27 건강한 물고기 키우는 법",
        "tips": [
            "**정기적인 물 갈이:** 어항의 수질은 물고기 건강에 가장 중요해요. 정기적으로 물을 갈아주고 여과기를 관리해주세요.",
            "**적정 수온 유지:** 물고기 종류에 맞는 적정 수온을 항상 유지시켜 주세요. 갑작스러운 변화는 스트레스를 줍니다.",
            "**과다 급여 금지:** 사료를 너무 많이 주면 수질 악화의 원인이 되니, 물고기가 다 먹을 수 있는 만큼만 급여하세요.",
            "**수초 및 은신처:** 스트레스를 줄이고 안정감을 느낄 수 있도록 수초나 은신처를 마련해주세요."
        ]
    },
    "파충류": {
        "title": "EMOJI_28 파충류 건강을 위한 완벽 가이드",
        "tips": [
            "**온도 및 습도 조절:** 각 파충류 종에 맞는 정확한 온도 및 습도 환경을 조성해주는 것이 생명 유지에 필수적입니다.",
            "**UVB 램프 설치:** 많은 파충류에게 칼슘 흡수를 돕는 UVB 램프는 필수적이므로, 주기적으로 교체하고 적절한 거리에 설치해주세요.",
            "**청결한 사육장:** 위생은 질병 예방의 기본입니다. 사육장을 항상 청결하게 관리하고 배설물을 즉시 치워주세요.",
            "**균형 잡힌 식단:** 파충류 종류에 맞는 영양 균형 잡힌 먹이를 제공하고, 비타민/칼슘 보충제를 급여해주세요."
        ]
    }
}


# 심각도에 따른 색상/아이콘 매핑
severity_map = {
    "높음": "EMOJI_29 심각",
    "중간": "EMOJI_30 주의",
    "낮음": "EMOJI_31 경미"
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="반려동물 질병 & 건강 도우미", page_icon="EMOJI_32", layout="centered")

st.title("EMOJI_33 반려동물 질병 & 응급처치 도우미")
st.markdown("---")
st.warning("⚠️ 본 정보는 참고용이며, 정확한 진단 및 치료는 반드시 수의사에게 받아야 합니다.")

# 1차 카테고리 선택
categories = list(set(disease_db.keys()))
animal = st.selectbox("EMOJI_34 동물 종류를 선택하세요", sorted(categories))
"EMOJI_34 동물 종류를 선택하세요",
    sorted(categories),
    key='animal_type_selector_unique_id'

# --- 반려동물 건강 관리 가이드 섹션 (새로 추가) ---
st.markdown("## ✨ 반려동물 건강 관리 가이드")
st.markdown(f"**{health_tips_db.get(animal, {'title': '정보 없음'})['title']}**")
for tip in health_tips_db.get(animal, {'tips': ["해당 동물의 건강 관리 팁이 아직 준비되지 않았습니다. ㅠㅠ"]})['tips']:
    st.markdown(f"- {tip}")
st.markdown("---")

# --- 질병 검색 섹션 ---
st.markdown("## EMOJI_35 질병 검색")
diseases = disease_db[animal]
symptom_input = st.text_input("EMOJI_36 증상을 쉼표(,)로 구분하여 입력하세요 (예: 구토, 설사, 콧물)")

if st.button("검색하기"):
    if symptom_input:
        user_symptoms_raw = [s.strip() for s in symptom_input.split(',') if s.strip()]
        user_symptoms_unique = list(set(user_symptoms_raw)) # 중복 제거

        if not user_symptoms_unique:
            st.error("❗ 유효한 증상을 입력해주세요.")
        else:
            found = []
            for disease, data in diseases.items():
                matched_count = 0
                for user_symptom in user_symptoms_unique:
                    if user_symptom in data["symptoms"]:
                        matched_count += 1
                
                if matched_count > 0:
                    accuracy = (matched_count / len(user_symptoms_unique)) * 100
                    found.append((disease, data, accuracy))
            
            found.sort(key=lambda x: x[2], reverse=True)

            if found:
                st.success(f"입력하신 증상 '{', '.join(user_symptoms_unique)}'에 대한 검색 결과입니다.")
                # 긴급 연락처/응급처치 안내 메시지 (여기서 한 번만 띄우기 위해 플래그 사용)
                displayed_emergency_prompt = False

                for disease, data, accuracy in found:
                    current_severity = data.get('severity', '정보 없음')
                    
                    # 빨간색 박스 긴급 안내 (첫 번째 '높음' 질병 발견 시)
                    if current_severity == "높음" and not displayed_emergency_prompt:
                        st.markdown(f"""
                        <div style="background-color: #ffcccc; padding: 15px; border-radius: 10px; border: 2px solid #cc0000;">
                            <h3 style="color: #cc0000; margin-top: 0;">EMOJI_37 긴급 상황 알림! EMOJI_38</h3>
                            <p style="color: #cc0000;">지금 바로 수의사에게 연락하세요! 반려동물의 생명이 위급할 수 있습니다. 지체하지 마세요.</p>
                            <p style="color: #cc0000; font-weight: bold;">가까운 동물병원을 검색해보세요 ⬇️</p>
                        </div>
                        """, unsafe_allow_html=True)
                        st.markdown("---")
                        displayed_emergency_prompt = True # 한 번 띄웠으면 다시 띄우지 않음

                    st.markdown(f"""
                    ### {data['icon']} {disease} {severity_map.get(current_severity, '정보 없음')}
                    **매칭 정확도:** {accuracy:.1f}% EMOJI_39
                    **어떤 병?** {data['info']}  
                    **주요 증상:** {", ".join(data['symptoms'])}  
                    **응급처치:** {data['treatment']}  
                    """)
                    st.markdown("---")
            else:
                st.warning(f"⚠️ 입력하신 증상 '{symptom_input}'에 맞는 질병을 찾을 수 없습니다. 꼭 수의사에게 진료를 받아보세요.")
    else:
        st.error("❗ 증상을 입력해주세요.")

# --- 동물병원 찾기 섹션 (새로 추가) ---
st.markdown("---")
st.markdown("## EMOJI_40 가까운 동물병원 찾기")
vet_location = st.text_input("EMOJI_41 현재 계신 동네나 시/군/구를 입력하세요 (예: 서울 강남구, 분당, 부산 해운대)")

if st.button("동물병원 검색"):
    if vet_location:
        search_query = f"동물병원 {vet_location}"
        # 구글맵스 검색 링크 생성
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={search_query}"
        st.markdown(f"'{vet_location}' 근처 동물병원을 Google Maps에서 찾아보세요:")
        st.markdown(f"[**EMOJI_42 {vet_location} 동물병원 검색하기**]({google_maps_url})")
        st.info("EMOJI_43 링크를 클릭하면 새 탭에서 구글맵스 검색 결과가 열립니다. 급한 상황이라면 바로 연락해서 방문하세요!")
    else:
        st.warning("⚠️ 검색할 지역을 입력해주세요.")
