import streamlit as st

st.title("App cho vay online _ Nguyễn Hoài Huỳnh Như đề tài 06")

# Nhập dữ liệu
STV = st.number_input(
    "Nhập số tiền muốn vay (triệu đồng):",
    min_value=0.0,
    step=1.0
)

TGV = st.number_input(
    "Nhập thời gian vay (năm):",
    min_value=0.0,
    step=1.0
)

LSV = st.number_input(
    "Nhập lãi suất cho vay (số thập phân):",
    min_value=0.0,
    step=0.01
)

TN = st.number_input(
    "Nhập thu nhập hàng tháng (triệu đồng/tháng):",
    min_value=0.0,
    step=1.0
)

SNTGD = st.number_input(
    "Nhập số người trong gia đình:",
    min_value=0,
    step=1
)

PTMC = st.number_input(
    "Nhập số tiền phải trả cho khoản vay cũ (triệu đồng):",
    min_value=0.0,
    step=1.0
)

GTTSDB = st.number_input(
    "Nhập giá trị tài sản đảm bảo (triệu đồng):",
    min_value=0.0,
    step=1.0
)

CPSH = 5  # Chi phí sinh hoạt cố định

# Nút tính toán
if st.button("Đánh giá khoản vay"):
    if TGV > 0 and TN - SNTGD * CPSH > 0 and GTTSDB > 0:
        PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))
        DTI = (PTMC + PTMM) / (TN - SNTGD * CPSH)
        LTV = STV / GTTSDB

        st.write(f"**Chỉ số DTI:** {DTI * 100:.2f}%")
        st.write(f"**Chỉ số LTV:** {LTV * 100:.2f}%")

        if DTI <= 0.7:
            st.success("ĐƯỢC CHO VAY")
        else:
            st.error("KHÔNG ĐƯỢC CHO VAY")
    else:
        st.warning("Vui lòng nhập dữ liệu hợp lệ.")
