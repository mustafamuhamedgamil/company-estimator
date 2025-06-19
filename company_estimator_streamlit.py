
import streamlit as st

st.set_page_config(page_title="حاسبة تأسيس الشركات", layout="centered")

st.title("🧾 حاسبة تكلفة تأسيس شركة - يوني زون")

with st.form("company_form"):
    name = st.text_input("📛 اسم الشركة")
    owner = st.text_input("👤 اسم المالك")
    location = st.text_input("📍 موقع الشركة (المحافظة)")
    partners = st.number_input("👥 عدد الشركاء", min_value=1, step=1)
    company_type = st.selectbox("🏢 نوع الشركة", [
        "منشأة فردية",
        "شركة تضامن",
        "شركة توصية بسيطة",
        "شركة ذات مسؤولية محدودة",
        "شركة مساهمة",
        "فرع شركة أجنبية"
    ])
    submitted = st.form_submit_button("احسب التكلفة")

if submitted:
    base_cost = 0
    duration = ""
    notes = ""

    if company_type == "منشأة فردية":
        base_cost = 2500
        duration = "من 3 إلى 5 أيام عمل"
        notes = "مناسبة للمشروعات الفردية الصغيرة"
    elif company_type in ["شركة تضامن", "شركة توصية بسيطة"]:
        base_cost = 4000
        duration = "5 إلى 7 أيام عمل"
        notes = "مناسبة للشركاء المتضامنين أو التمويليين"
    elif company_type == "شركة ذات مسؤولية محدودة":
        base_cost = 9000
        duration = "من 7 إلى 10 أيام عمل"
        notes = "أفضل اختيار لحماية قانونية ومسؤولية محدودة"
    elif company_type == "شركة مساهمة":
        base_cost = 20000
        duration = "من 10 إلى 14 يوم عمل"
        notes = "مناسبة للمشاريع الكبيرة ورأس المال المرتفع"
    elif company_type == "فرع شركة أجنبية":
        base_cost = 15000
        duration = "من 10 إلى 15 يوم عمل"
        notes = "لفتح فرع لشركة خارجية داخل مصر"

    total = base_cost + 5000

    st.markdown("---")
    st.subheader("📋 تفاصيل التكلفة")
    st.write(f"**اسم الشركة:** {name}")
    st.write(f"**المالك:** {owner}")
    st.write(f"**الموقع:** {location}")
    st.write(f"**نوع الشركة:** {company_type}")
    st.write(f"**عدد الشركاء:** {partners}")
    st.write(f"💸 **التكلفة الأساسية:** {base_cost:,} جنيه")
    st.write("💼 **المبلغ الثابت الإضافي:** 5,000 جنيه")
    st.write(f"💰 **الإجمالي:** {total:,} جنيه")
    st.write(f"⏱️ **المدة المتوقعة للتنفيذ:** {duration}")
    st.write(f"📌 **ملاحظات:** {notes}")
