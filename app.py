import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 페이지 설정
st.set_page_config(page_title="딥테크 사전검토 시스템", layout="wide")

st.title("🛡️ 딥테크 스케일업밸리 육성사업 사전검토 시스템")
st.info("첨부파일 [별표 2] 사전지원제외 및 사후관리 검토 세부기준을 적용합니다.")

# 1. 사이드바: 데이터 입력 창
with st.sidebar:
    st.header("📝 기업 데이터 입력")
    company_name = st.text_input("기관명", value="에이아이씨엔티(주)")
    
    st.subheader("📊 재무 현황")
    capital = st.number_input("자본총계 (원)", value=100000000)
    debt = st.number_input("부채총계 (원)", value=150000000)
    current_asset = st.number_input("유동자산 (원)", value=200000000)
    current_debt = st.number_input("유동부채 (원)", value=100000000)
    
    st.subheader("👥 인력 및 기타")
    pi_projects = st.number_input("연구책임자 수행 과제 수", value=1)
    is_restriction = st.radio("국가연구개발사업 참여제한 여부", ["해당없음", "해당함"])

# 2. 검토 로직 계산 [cite: 64, 74]
debt_ratio = (debt / capital * 100) if capital > 0 else 9999
current_ratio = (current_asset / current_debt * 100) if current_debt > 0 else 0

# 상태 판정 함수 (2: PASS, 1: CAUTION, 0: FAIL)
def judge():
    checks = []
    
    # 자본잠식 
    if capital <= 0: checks.append({"cat": "재무", "item": "자본잠식", "stat": 0, "memo": "자본전액잠식 상태"})
    else: checks.append({"cat": "재무", "item": "자본잠식", "stat": 2, "memo": "정상"})
    
    # 부채비율 
    if debt_ratio >= 500: checks.append({"cat": "재무", "item": "부채비율", "stat": 0, "memo": f"부채비율 {debt_ratio:.1f}% (500% 이상)"})
    elif debt_ratio >= 300: checks.append({"cat": "재무", "item": "부채비율", "stat": 1, "memo": f"부채비율 {debt_ratio:.1f}% (사후관리 대상)"})
    else: checks.append({"cat": "재무", "item": "부채비율", "stat": 2, "memo": f"정상 ({debt_ratio:.1f}%)"})
    
    # 유동비율 
    if current_ratio <= 50: checks.append({"cat": "재무", "item": "유동비율", "stat": 0, "memo": f"유동비율 {current_ratio:.1f}% (50% 이하)"})
    elif current_ratio <= 100: checks.append({"cat": "재무", "item": "유동비율", "stat": 1, "memo": f"유동비율 {current_ratio:.1f}% (사후관리 대상)"})
    else: checks.append({"cat": "재무", "item": "유동비율", "stat": 2, "memo": f"정상 ({current_ratio:.1f}%)"})
    
    # 참여제한 및 3책5공 [cite: 47, 74]
    if is_restriction == "해당함": checks.append({"cat": "자격", "item": "참여제한", "stat": 0, "memo": "참여제한 대상자 포함"})
    else: checks.append({"cat": "자격", "item": "참여제한", "stat": 2, "memo": "이상 없음"})
    
    if pi_projects > 3: checks.append({"cat": "인력", "item": "3책5공", "stat": 0, "memo": f"책임자 과제수 {pi_projects}개 (3개 초과)"})
    else: checks.append({"cat": "인력", "item": "3책5공", "stat": 2, "memo": "준수함"})
    
    return pd.DataFrame(checks)

# 3. 시각화 대시보드 생성 함수
def draw_dashboard(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(-0.5, len(df))
    colors = {2: '#27ae60', 1: '#f1c40f', 0: '#e74c3c'}
    labels = {2: 'PASS', 1: 'CAUTION', 0: 'FAIL'}
    
    for i, row in df.iterrows():
        y = len(df) - i - 1
        ax.text(0.5, y, f"[{row['cat']}] {row['item']}", va='center', fontsize=11)
        ax.text(3, y, row['memo'], va='center', fontsize=10, color='gray')
        rect = patches.Rectangle((8, y-0.25), 1.2, 0.5, color=colors[row['stat']])
        ax.add_patch(rect)
        ax.text(8.6, y, labels[row['stat']], color='white', weight='bold', ha='center', va='center')
    
    ax.axis('off')
    st.pyplot(fig)

# 실행 및 화면 출력
results_df = judge()
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"🔍 {company_name} 검토 리포트")
    draw_dashboard(results_df)

with col2:
    st.subheader("📋 요약 및 조치사항")
    fail_items = results_df[results_df['stat'] == 0]
    if not fail_items.empty:
        st.error(f"부적격 항목 {len(fail_items)}건 발견")
        for _, row in fail_items.iterrows():
            st.write(f"- **{row['item']}**: {row['memo']}")
    else:
        st.success("모든 핵심 지표가 적격 범위 내에 있습니다.")
