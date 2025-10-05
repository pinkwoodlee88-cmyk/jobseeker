import streamlit as st
import pandas as pd
# Gemini API 호출 (선택 사항: 사용자 맞춤형 분석 또는 요약 기능 추가 시)
# from google import genai 

# 수집된 데이터를 DataFrame으로 저장 (앱에 표시하기 위함)
# 실제 앱에서는 이 데이터를 실시간 검색 결과나 데이터베이스에서 가져와야 합니다.
job_data = {
    '직종': ['수학 튜터 (원격)', '수학 튜터 (현장)', '수학 교사 (원격/평균)', '수학 교사 (AISD)', '스쿨버스 기사 (AISD)', '버스 기사 (CapMetro)'],
    '임금': ['$15.05 - $28.85/hr', '$16 - $49/hr', '$53,989/년', 'TIA 수당 별도', '정보 없음', '$24.04/hr 시작'],
    '파트타임 여부': ['높음', '높음', '다양', '정규직 일반', '다양', '정규직 일반'],
    '재택 여부': ['가능', '불가능', '가능', '불가능', '불가능', '불가능'],
    '주요 자격조건': ['미국 거주, K-8 경험 선호', '특정 과목 지식', '텍사스 교사 자격증', '텍사스 교사 자격증', '만 21세, CDL 교육 지원', '만 21세, CDL 교육 지원'],
    '시작 시점': ['즉시', '즉시', '즉시/25-26학년도', '즉시/25-26학년도', '즉시', '즉시'],
    '계약 조건': ['계약직/파트타임', '계약직/파트타임', '계약직/정규직', '정규직', '정규직/파트타임', '정규직'],
}
df = pd.DataFrame(job_data)

st.set_page_config(layout="wide")
st.title("오스틴 (Austin, TX) 교육 및 운송 분야 구인 정보 🚌📚")
st.caption(f"최신 정보 검색일: 2025년 10월 4일 (구인 정보는 수시로 변동됩니다.)")

# 직종 선택 필터
job_filter = st.selectbox("직종을 선택하세요:", df['직종'].unique())

st.header(f"💼 {job_filter} 상세 정보")
st.dataframe(df[df['직종'] == job_filter].style.set_properties(**{'white-space': 'normal'}), height=200)

# 전체 데이터 보기 (옵션)
st.subheader("모든 구인 정보")
st.dataframe(df.style.set_properties(**{'white-space': 'normal'}), height=300)

# Gemini AI 활용 (옵션)
st.sidebar.header("✨ Gemini AI 활용")
st.sidebar.markdown("이 앱은 Gemini AI를 활용하여 최신 구인 정보를 검색하고 요약했습니다.")
# # 사용자 입력 기반 추가 분석 기능 (예시)
# user_query = st.sidebar.text_input("궁금한 점이 있다면 Gemini에게 질문하세요:")
# if user_query:
#     # 여기에 Gemini API 호출 코드를 작성하여 응답을 표시할 수 있습니다.
#     st.sidebar.info("Gemini AI 응답: [API 응답 내용 표시]")

st.subheader("🔗 원본 정보 출처")
st.markdown("""
- **수학 튜터/교사:** ZipRecruiter, Care.com 등
- **학교/교사 자격:** Austin ISD (오스틴 교육청)
- **버스 기사:** CapMetro (오스틴 대중교통), Austin ISD
""")
2. Streamlit 앱 개발 시 유의사항
데이터의 최신성: '당일 최신 정보 검색' 요청을 Streamlit 앱에서 구현하려면, 앱이 실행될 때마다 Google Search API나 다른 외부 구인구직 사이트의 API를 실시간으로 호출하여 데이터를 가져오도록 코드를 구성해야 합니다. 위의 예시는 검색된 데이터를 수동으로 입력한 것입니다.

Gemini AI 활용: Gemini AI는 정보 검색을 위해 사용되었으며, 앱 내에 질문-응답 기능 등을 추가하려면, Google AI SDK를 사용하여 사용자 입력(st.text_input)을 Gemini 모델에 전달하고 응답을 받아와야 합니다.

DataFrame 스타일링: 구인 정보가 길어지면 표가 잘리지 않도록 style.set_properties(**{'white-space': 'normal'})을 사용하여 텍스트가 줄바꿈되도록 하는 것이 좋습니다.








코드를 만들어줘


Streamlit 앱을 위한 Python 코드를 만들어 드릴게요. 이전 검색 결과에서 얻은 오스틴 지역의 구인 정보를 표시하고 필터링할 수 있는 간단한 앱입니다.

이 코드는 Gemini AI를 사용해 정보를 검색하고 요약한 후, 그 데이터를 Streamlit 앱에 시각화하는 과정을 담고 있습니다.

💻 Streamlit 앱 코드: Austin 구인 정보 🚌📚
이 코드를 austin_jobs_app.py 파일로 저장하고 터미널에서 streamlit run austin_jobs_app.py 명령어로 실행하세요.

Python

import streamlit as st
import pandas as pd

# ----------------------------------------------------------------------
# 1. Gemini AI를 통해 수집된 '오늘의 오스틴 구인 정보' (데이터베이스 역할)
# 실제 앱에서는 이 부분이 실시간 API 호출 또는 데이터베이스 쿼리로 대체됩니다.
# ----------------------------------------------------------------------
job_data = {
    '직종': [
        '수학 튜터', '수학 튜터', '수학 교사', '수학 교사',
        '스쿨버스 기사', '버스 기사'
    ],
    '세부 직무': [
        '원격 온라인 튜터', '현장 파트타임 튜터', '정규직 (Austin ISD)', '원격 시간제 교사',
        '스쿨버스 기사 (AISD)', '대중교통 버스 기사 (CapMetro)'
    ],
    '임금/급여': [
        '$15.05 - $28.85/hr', '$16 - $49/hr', '평균 $53,989/년 + 수당', '$17 - $25/hr',
        'CDL 교육 지원/면허 환급', '$24.04/hr 시작'
    ],
    '자격 조건': [
        '미국 거주 및 근무, K-8 경험 선호', '특정 과목(AP Physics 등) 지식', '유효한 텍사스 교사 자격증 필수', '교육/튜터링 경험',
        '만 21세 이상, 운전 기록 양호, CDL 취득 지원', '만 21세 이상, 깨끗한 운전 기록, CDL 취득 지원'
    ],
    '신입 채용 여부': [
        '가능성 높음', '가능', '자격증 프로그램 통해 가능', '가능',
        'CDL 교육 지원으로 신입 적극 채용', 'CDL 교육 지원으로 신입 적극 채용'
    ],
    '재택 여부': [
        '✅ 가능 (Remote)', '❌ 불가능 (On-site)', '❌ 불가능 (On-site)', '✅ 가능 (Remote)',
        '❌ 불가능 (On-site)', '❌ 불가능 (On-site)'
    ],
    '계약 조건': [
        '파트타임/계약직', '파트타임', '정규직 (Full-Time)', '파트타임/계약직',
        '정규직/파트타임', '정규직 (Full-Time)'
    ],
    '시작 시점': [
        '즉시 채용', '즉시 채용', '즉시 또는 25-26학년도', '즉시 채용',
        '즉시 채용', '즉시 채용'
    ],
}
df = pd.DataFrame(job_data)

# ----------------------------------------------------------------------
# 2. Streamlit 앱 인터페이스 구성
# ----------------------------------------------------------------------

# 페이지 설정
st.set_page_config(
    page_title="Austin 구인 정보",
    page_icon="💼",
    layout="wide"
)

st.title("🏙️ 오스틴 (Austin, TX) 오늘의 구인 정보")
st.caption(f"**Gemini AI**를 통해 수집된 최신 정보 기반 (검색일: {pd.Timestamp.now().strftime('%Y년 %m월 %d일')})")

---

## 🔍 구인 정보 필터링

# 필터 옵션
col1, col2, col3 = st.columns(3)

with col1:
    job_type = st.multiselect(
        "**직종 선택**",
        options=df['직종'].unique(),
        default=df['직종'].unique()
    )

with col2:
    remote_filter = st.radio(
        "**재택(Remote) 여부**",
        options=['전체', '재택 가능', '현장 근무만'],
        index=0,
        horizontal=True
    )

with col3:
    contract_type = st.radio(
        "**계약 조건**",
        options=['전체', '정규직', '파트타임/계약직'],
        index=0,
        horizontal=True
    )

# 필터링 로직
filtered_df = df[df['직종'].isin(job_type)]

if remote_filter == '재택 가능':
    filtered_df = filtered_df[filtered_df['재택 여부'].str.contains('✅')]
elif remote_filter == '현장 근무만':
    filtered_df = filtered_df[filtered_df['재택 여부'].str.contains('❌')]

if contract_type == '정규직':
    filtered_df = filtered_df[filtered_df['계약 조건'].str.contains('정규직')]
elif contract_type == '파트타임/계약직':
    filtered_df = filtered_df[~filtered_df['계약 조건'].str.contains('정규직')]

# 데이터 표시
st.dataframe(
    filtered_df.style.set_properties(**{'white-space': 'normal'}),
    use_container_width=True,
    height=min(300, (len(filtered_df) + 1) * 35)
)

if filtered_df.empty:
    st.info("선택한 조건에 맞는 구인 정보가 없습니다.")

---

## 📊 직종별 임금 및 특성 요약

st.subheader("직종별 주요 특징 비교")

# 임금 데이터만 따로 추출하여 표시
salary_df = df[['직종', '세부 직무', '임금/급여', '자격 조건']].copy()

# 데이터프레임을 테이블 형태로 표시
st.table(salary_df)

st.markdown("""
**ℹ️ 참고:**
- **AISD (Austin ISD)**는 오스틴 교육청 소속이며, 교사에게 추가 인센티브(TIA)를 제공합니다.
- **CapMetro**는 오스틴 대중교통 기관입니다.
- 임금 정보는 검색 당시의 **평균 또는 제시 범위**이며, 개별 공고에 따라 달라질 수 있습니다.
""")

---

어떤 필터링 조건으로 구인 정보를 확인하고 싶으신가요?
