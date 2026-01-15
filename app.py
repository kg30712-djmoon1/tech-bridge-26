import streamlit as st

# 1. 페이지 설정 (브랜드 로고 및 제목)
st.set_page_config(page_title="Tech-Bridge 26 리스크 진단", page_icon="🛡️", layout="wide")

# 2. 사이드바 디자인
with st.sidebar:
    st.image("https://www.innopolis.or.kr/images/kor/main/logo.png", width=200) # 재단 로고 예시
    st.title("사업조정실 컨트롤타워")
    st.info("2026 전략기술 사업화 통합 조정 플랫폼 [Tech-Bridge 26] 전용 진단 도구입니다.")

# 3. 메인 화면 타이틀
st.title("🛡️ R&D 행정리스크 자가진단 네비게이션")
st.markdown("---")

# 4. 질문 섹션 (디자인을 위해 컬럼 분할)
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 연구비 집행 점검")
    q1 = st.selectbox("1. 연구비의 목적 외 사용(개인용도, 타사업 전용 등)이 있습니까?", ["아니오", "예"])
    q2 = st.selectbox("2. 인건비를 회수하여 공동 관리(풀링 등)하고 있습니까?", ["아니오", "예"])

with col2:
    st.subheader("👥 인력 및 행정 점검")
    q3 = st.selectbox("3. 팀 내 참여제한 중인 연구원이 포함되어 있습니까?", ["아니오", "예"])
    q4 = st.selectbox("4. 외부 전문기관의 행정 컨설팅을 받은 적이 있습니까?", ["예", "아니오"])

# 5. 진단 실행 버튼
if st.button("🚀 실시간 리스크 분석 시작"):
    # 리스크 로직 계산
    risk_score = 0
    if q1 == "예": risk_score += 40
    if q2 == "예": risk_score += 30
    if q3 == "예": risk_score += 30
    if q4 == "아니오": risk_score += 10 # 컨설팅 안 받으면 가점 리스크
    
    st.markdown("### 📊 진단 결과 보고서")
    
    # 신호등 시각화
    if risk_score >= 70:
        st.error(f"🔴 [위험] 현재 리스크 지수: {risk_score}%")
        st.critical("사업조정실의 집중 관리가 필요한 단계입니다. 즉시 소명 자료를 준비하십시오.")
    elif risk_score >= 30:
        st.warning(f"🟡 [주의] 현재 리스크 지수: {risk_score}%")
        st.info("일부 행정 보완이 필요합니다. 'R&D 제재처분 가이드라인'을 숙독하세요.")
    else:
        st.success(f"🟢 [안전] 현재 리스크 지수: {risk_score}%")
        st.balloons() # 축하 효과
        st.write("무결함 R&D를 수행 중입니다. 2026 AI 빅테크 사업 연계가 권장됩니다.")