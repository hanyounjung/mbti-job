import streamlit as st

st.set_page_config(page_title="MBTI 진로 & 포켓몬 추천", page_icon="🌈", layout="centered")

st.title("🌈 MBTI 진로 & 포켓몬 추천")
st.write("MBTI를 고르면 어울리는 진로 2개와 닮은 포켓몬을 추천해줄게! 🚀")

mbti_data = {
    "ISTJ": {
        "jobs": [
            ("회계사 💼", "회계학과, 경영학과", "꼼꼼하고 책임감이 강한 사람에게 잘 맞아요."),
            ("공무원 🏛️", "행정학과, 법학과", "규칙을 잘 지키고 안정적인 일을 좋아하는 사람에게 추천!")
        ],
        "pokemon": ("꼬부기", "Squirtle", "차분하고 성실하며 맡은 일을 끝까지 해내는 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png")
    },
    "ISFJ": {
        "jobs": [
            ("간호사 🩺", "간호학과, 보건학과", "다정하고 남을 잘 챙기는 사람에게 잘 어울려요."),
            ("사회복지사 🤝", "사회복지학과, 상담심리학과", "사람을 돕는 일에서 보람을 느끼는 사람에게 추천!")
        ],
        "pokemon": ("해피너스", "Blissey", "따뜻하고 배려심이 많아 친구들을 잘 챙기는 힐링 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png")
    },
    "INFJ": {
        "jobs": [
            ("상담사 🧠", "심리학과, 상담학과", "깊이 공감하고 진심으로 조언해주는 사람에게 잘 맞아요."),
            ("작가 ✍️", "문예창작학과, 국어국문학과", "생각이 깊고 표현력이 좋은 사람에게 추천!")
        ],
        "pokemon": ("뮤", "Mew", "신비롭고 깊은 생각을 가진 조용한 이상주의자 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png")
    },
    "INTJ": {
        "jobs": [
            ("데이터 분석가 📊", "데이터사이언스학과, 통계학과", "논리적으로 문제를 해결하는 사람에게 잘 맞아요."),
            ("연구원 🔬", "공학계열, 자연과학계열", "혼자 깊이 탐구하는 걸 좋아하는 사람에게 추천!")
        ],
        "pokemon": ("뮤츠", "Mewtwo", "분석적이고 독립적이며 목표를 향해 집중하는 전략가 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png")
    },
    "ISTP": {
        "jobs": [
            ("엔지니어 🛠️", "기계공학과, 전자공학과", "손으로 만들고 고치는 걸 좋아하는 사람에게 잘 맞아요."),
            ("파일럿 ✈️", "항공운항학과, 항공정비학과", "침착하고 상황 판단이 빠른 사람에게 추천!")
        ],
        "pokemon": ("리자몽", "Charizard", "자유롭고 도전적이며 실전에서 강한 행동파 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png")
    },
    "ISFP": {
        "jobs": [
            ("디자이너 🎨", "시각디자인학과, 패션디자인학과", "감각적이고 자유로운 표현을 좋아하는 사람에게 잘 맞아요."),
            ("반려동물 전문가 🐶", "동물자원학과, 반려동물학과", "따뜻하고 생명을 소중히 여기는 사람에게 추천!")
        ],
        "pokemon": ("이브이", "Eevee", "부드럽고 감성적이며 다양한 가능성을 가진 매력 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png")
    },
    "INFP": {
        "jobs": [
            ("콘텐츠 기획자 📱", "미디어학과, 광고홍보학과", "상상력이 풍부하고 의미 있는 이야기를 좋아하는 사람에게 잘 맞아요."),
            ("심리상담사 💬", "심리학과, 상담학과", "친구의 고민을 잘 들어주는 사람에게 추천!")
        ],
        "pokemon": ("님피아", "Sylveon", "다정하고 감성적이며 친구의 마음을 잘 알아주는 공감 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/700.png")
    },
    "INTP": {
        "jobs": [
            ("소프트웨어 개발자 💻", "컴퓨터공학과, 소프트웨어학과", "호기심이 많고 원리를 파고드는 사람에게 잘 맞아요."),
            ("AI 연구원 🤖", "인공지능학과, 데이터사이언스학과", "새로운 기술을 분석하고 실험하는 걸 좋아하는 사람에게 추천!")
        ],
        "pokemon": ("메타몽", "Ditto", "호기심 많고 유연하게 생각하며 새로운 방식으로 문제를 푸는 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png")
    },
    "ESTP": {
        "jobs": [
            ("마케터 📢", "광고홍보학과, 경영학과", "활동적이고 사람들과 소통을 잘하는 사람에게 잘 맞아요."),
            ("스포츠 트레이너 🏃", "체육학과, 스포츠과학과", "에너지가 넘치고 몸으로 배우는 걸 좋아하는 사람에게 추천!")
        ],
        "pokemon": ("피카츄", "Pikachu", "밝고 빠르며 어디서든 존재감이 확실한 에너지 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png")
    },
    "ESFP": {
        "jobs": [
            ("방송인 🎤", "방송연예학과, 미디어커뮤니케이션학과", "밝고 표현력이 좋은 사람에게 잘 맞아요."),
            ("이벤트 기획자 🎉", "관광경영학과, 이벤트학과", "사람들을 즐겁게 만드는 걸 좋아하는 사람에게 추천!")
        ],
        "pokemon": ("푸린", "Jigglypuff", "귀엽고 표현력이 풍부하며 분위기를 즐겁게 만드는 스타 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png")
    },
    "ENFP": {
        "jobs": [
            ("광고 기획자 💡", "광고홍보학과, 미디어학과", "아이디어가 많고 새로운 시도를 좋아하는 사람에게 잘 맞아요."),
            ("진로 코치 🌟", "교육학과, 심리학과", "사람의 가능성을 발견하고 응원하는 사람에게 추천!")
        ],
        "pokemon": ("파이리", "Charmander", "열정적이고 호기심이 많으며 새로운 모험을 좋아하는 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png")
    },
    "ENTP": {
        "jobs": [
            ("창업가 🚀", "경영학과, 창업학과", "새로운 아이디어를 실행하는 걸 좋아하는 사람에게 잘 맞아요."),
            ("변호사 ⚖️", "법학과, 정치외교학과", "토론을 좋아하고 논리적으로 설득하는 사람에게 추천!")
        ],
        "pokemon": ("나옹", "Meowth", "재치 있고 말솜씨가 좋으며 기회를 잘 잡는 아이디어 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/52.png")
    },
    "ESTJ": {
        "jobs": [
            ("관리자 📋", "경영학과, 행정학과", "계획을 세우고 사람들을 이끄는 데 강한 사람에게 잘 맞아요."),
            ("경찰관 👮", "경찰행정학과, 법학과", "책임감 있고 질서를 중요하게 생각하는 사람에게 추천!")
        ],
        "pokemon": ("윈디", "Arcanine", "믿음직하고 리더십이 있으며 책임감 있게 움직이는 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/59.png")
    },
    "ESFJ": {
        "jobs": [
            ("교사 👩‍🏫", "교육학과, 사범대학", "친절하고 사람을 잘 챙기는 사람에게 잘 맞아요."),
            ("호텔리어 🏨", "호텔경영학과, 관광경영학과", "서비스 정신이 좋고 사람 만나는 걸 좋아하는 사람에게 추천!")
        ],
        "pokemon": ("치코리타", "Chikorita", "친절하고 부드러우며 주변 사람을 편안하게 해주는 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/152.png")
    },
    "ENFJ": {
        "jobs": [
            ("교사 🧑‍🏫", "교육학과, 사범대학", "친구들을 이끌고 도와주는 걸 좋아하는 사람에게 잘 맞아요."),
            ("홍보 전문가 📣", "광고홍보학과, 커뮤니케이션학과", "말과 글로 사람의 마음을 움직이는 사람에게 추천!")
        ],
        "pokemon": ("루카리오", "Lucario", "친구의 마음을 잘 읽고 바른 방향으로 이끄는 리더 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png")
    },
    "ENTJ": {
        "jobs": [
            ("CEO 🏢", "경영학과, 경제학과", "목표가 뚜렷하고 리더십이 강한 사람에게 잘 맞아요."),
            ("프로젝트 매니저 📌", "산업공학과, 경영정보학과", "계획을 세우고 팀을 이끄는 걸 좋아하는 사람에게 추천!")
        ],
        "pokemon": ("망나뇽", "Dragonite", "강한 추진력과 리더십으로 목표를 향해 나아가는 타입!", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png")
    }
}

selected_mbti = st.selectbox("✨ 나의 MBTI를 선택해줘!", list(mbti_data.keys()))

st.divider()

st.subheader(f"🔎 {selected_mbti}에게 어울리는 진로 추천!")

for job, major, personality in mbti_data[selected_mbti]["jobs"]:
    with st.container(border=True):
        st.markdown(f"### {job}")
        st.write(f"🎓 **추천 학과:** {major}")
        st.write(f"💬 **어울리는 성격:** {personality}")

st.divider()

pokemon_kr, pokemon_en, pokemon_personality, pokemon_img = mbti_data[selected_mbti]["pokemon"]

st.subheader("💖 나와 닮은 포켓몬은?")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(pokemon_img, width=180)

with col2:
    st.markdown(f"## {pokemon_kr} ✨")
    st.write(f"영문 이름: **{pokemon_en}**")
    st.write(f"🌟 **성격 특징:** {pokemon_personality}")

st.success("MBTI와 포켓몬 추천은 재미로 보는 참고용이야! 진짜 진로는 내가 좋아하는 것, 잘하는 것, 해보고 싶은 경험을 통해 찾아가는 거야 😊")

st.divider()
st.caption("🌱 진로는 하나로 정해지는 게 아니라, 경험하면서 점점 선명해지는 거야!")
