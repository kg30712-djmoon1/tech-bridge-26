import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="R&D Compliance Navigator", page_icon="🛡️", layout="wide")

st.title("🛡️ R&D 행정리스크 진단 및 사후관리 네비게이션")
st.markdown("##### 과기정통부 표준 프로세스 및 제재처분 가이드라인 기반 [v4.0]")

# 2. 진단 섹션
with st.container():
    st.info("💡 진단 결과에 따라 맞춤형 행정 솔루션이 제공됩니다. (혁신법 제32조~34조 근거)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚠️ [고위험] 형사처벌 및 참여제한 직결 항목")
        # 가이드라인 상 '고의적' 위반 항목
        q1 = st.selectbox("Q1. 연구비 허위 영수증 처리 또는 개인 용도 유용(유흥비 등)이 있습니까?", ["아니오", "예"])
        q2 = st.selectbox("Q2. 학생인건비를 회수하여 연구책임자가 공동 관리 중입니까?", ["아니오", "예"])
        q3 = st.selectbox("Q3. 연구성과물(IP)을 정당한 사유 없이 개인 명의로 소유했습니까?", ["아니오", "예"])

    with col2:
        st.subheader("📝 [중위험] 행정 미숙 및 절차 위반 항목")
        # 가이드라인 상 '관리 부주의' 항목
        q4 = st.selectbox("Q4. 타 부처 과제와 연구비 증빙을 중복하여 사용했습니까?", ["아니오", "예"])
        q5 = st.selectbox("Q5. 참여제한 중인 연구원이 과제에 참여하고 있습니까?", ["아니오", "예"])
        q6 = st.selectbox("Q6. 과제 종료 후 사용실적 보고서 제출 기한을 3개월 초과했습니까?", ["아니오", "예"])

# 3. 분석 실행
if st.button("🚀 정밀 진단 및 솔루션 확인"):
    # 가이드라인 기반 리스크 지수 산출 (가상의 가중치 반영)
    critical_risks = [q1, q2, q3].count("예")
    major_risks = [q4, q5, q6].count("예")
    
    st.divider()
    
    # 4. 결과 리포트 및 해결방안 안내
    if critical_risks > 0:
        st.error(f"🚨 [경고] 심각한 행정 위반 감지 (고위험 항목 {critical_risks}건)")
        st.markdown("### 🛑 처벌 예상 수준")
        st.write("- **국가연구개발활동 참여제한**: 최대 10년 [cite: 337, 370]")
        st.write("- **제재부가금 부과**: 유용 금액의 최대 5배 [cite: 337, 375]")
        st.write("- **형사고발**: 횡령/사기 혐의로 수사기관 이첩 가능성 농후 [cite: 164, 1101]")
        
        st.markdown("### 💡 조치 가이드 (Solution)")
        st.success("**1. 자진 신고 및 피해 회복**: 처분 전 부당 집행액을 즉시 반납하고 소명할 경우 처분이 감경될 수 있습니다. ")
        st.success("**2. 소명 기회 활용**: 제재처분평가단에 출석하여 위반 행위의 비의도성을 적극 소명하십시오. (발표 10분, 질의 20분 구성) [cite: 171, 172, 173]")
        st.success("**3. 재검토 요청**: 사전통지일로부터 20일 이내에 '연구자권익보호위원회'에 재검토를 요청할 수 있습니다. [cite: 183, 458]")

    elif major_risks > 0:
        st.warning(f"⚠️ [주의] 행정 보완 필요 (중위험 항목 {major_risks}건)")
        st.markdown("### 📊 예상 리스크")
        st.write("- **정밀 정산 실시**: 회계법인을 통한 전수 조사 및 불인정 금액 회수 [cite: 82, 111]")
        st.write("- **과제 평가 반영**: 차기 과제 선정 시 감점 요인으로 작용 가능 [cite: 387]")
        
        st.markdown("### 💡 조치 가이드 (Solution)")
        st.success("**1. 사업조정실 행정 컨설팅**: 전문 회계사와 함께 집행 내역을 재분류하고 오집행 건을 즉시 수정하십시오. ")
        st.success("**2. 연구행정 역량 강화 교육**: 재단에서 실시하는 '연구윤리 및 제재처분 설명회'를 이수하여 재발을 방지하십시오. [cite: 47, 608]")
        
    else:
        st.success("✅ [안전] 무결함 행정 상태입니다.")
        st.balloons()
        st.write("2026 AI 글로벌 빅테크 육성 사업(최대 20억 지원) 참여가 권장됩니다.")
