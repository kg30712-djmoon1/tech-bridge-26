import streamlit as st

# 1. 페이지 설정 (매뉴얼 기반의 전문성 강조)
st.set_page_config(page_title="Innopolis R&D Compliance", page_icon="⚖️", layout="wide")

st.title("⚖️ 국가연구개발사업 제재처분 예방 자가진단 시스템")
st.caption("과학기술정보통신부 및 주요 전문기관 표준 프로세스 반영 [v3.0]")

# 2. 섹션별 진단 (자료의 '예방-점검-적발' 단계 반영)
with st.container():
    st.info("💡 본 시스템은 혁신법 및 제재처분 가이드라인에 따른 '권고적 기준'을 바탕으로 설계되었습니다.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 [STEP 1] 연구비 집행 및 점검")
        q1 = st.selectbox("1. 연구비 사용 후 세금계산서 취소 내역이 방치되어 있습니까? (이상패턴 점검)", ["아니오", "예"])
        q2 = st.selectbox("2. 특정 업체와 반복적·독점적 거래가 집중되어 있습니까? (현장조사 대상)", ["아니오", "예"])
        q3 = st.selectbox("3. 학생인건비 지급 후 일부를 회수하여 공동 관리 중입니까? (인건비 유용)", ["아니오", "예"])

    with col2:
        st.subheader("📋 [STEP 2] 제재 사유 및 행정 준수")
        q4 = st.selectbox("4. 타 부처 과제와 연구비 증빙을 중복 사용한 적이 있습니까? (중복수혜 금지)", ["아니오", "예"])
        q5 = st.selectbox("5. 연구개발 성과(IP)를 기관이 아닌 개인 명의로 소유했습니까? (성과 일탈)", ["아니오", "예"])
        q6 = st.selectbox("6. 현재 기업의 재무상태가 자본잠식 또는 부채 1000% 이상입니까? (부실기업 점검)", ["아니오", "예"])

# 3. 추가 옵션 (징수 및 감면 가능성 진단)
st.markdown("---")
st.subheader("💰 [STEP 3] 징수 및 감면 리스크 분석")
q7 = st.checkbox("현재 경영악화, 부도, 폐업 등 불가피한 사유가 있습니까? (납부유예/분납 대상 검토)")

# 4. 분석 알고리즘 (자료의 제재 수준 가이드라인 반영)
if st.button("🚀 종합 리스크 레포트 출력"):
    risk_points = 0
    if q1 == "예": risk_points += 20
    if q2 == "예": risk_points += 15
    if q3 == "예": risk_points += 30
    if q4 == "예": risk_points += 20
    if q5 == "예": risk_points += 15
    if q6 == "예": risk_points += 10
    
    st.divider()
    st.header("📊 분석 결과")
    
    # 신호등 시각화
    if risk_points >= 60:
        st.error(f"🔴 [심각] 행정리스크 지수: {risk_points}%")
        st.warning("🚨 제재처분평가단 상정 가능성이 매우 높습니다. 참여제한 및 제재부가금(최대 5배) 부과 대상입니다.")
    elif risk_points >= 25:
        st.warning(f"🟡 [주의] 행정리스크 지수: {risk_points}%")
        st.info("⚠️ 현장 정밀 점검 및 회계법인 상시 모니터링 대상입니다. 사전 소명 자료를 준비하십시오.")
    else:
        st.success(f"🟢 [안전] 행정리스크 지수: {risk_points}%")
        st.balloons()

    # 징수/감면 조언 (자료 p.16, p.20 내용 반영)
    if q7:
        st.markdown("---")
        st.subheader("📑 징수 및 감면 가이드 (자료 p.16 참조)")
        st.write("* 경영악화 시 **최대 5년 범위 내 분할납부 및 납부유예** 신청 가능")
        st.write("* 폐업/부도 시 **재산조사** 결과에 따라 징수절차 중지 및 면제 검토 가능")
