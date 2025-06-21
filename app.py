
import streamlit as st
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import base64

def ar(text):
    return get_display(reshape(text))

def generate_pdf(data):
    buffer = io.BytesIO()
    pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))
    c = canvas.Canvas(buffer)
    c.setFont("DejaVu", 14)
    c.drawCentredString(300, 800, ar("نتيجة مساعد تأسيس شركة - يوني زون"))
    y = 760
    for label, value in data.items():
        c.drawRightString(550, y, ar(f"{label}: {value}"))
        y -= 25
    c.save()
    buffer.seek(0)
    b64 = base64.b64encode(buffer.read()).decode()
    return f'<a href="data:application/pdf;base64,{b64}" download="تقرير_الشركة.pdf">📥 تحميل التقرير PDF</a>'

st.set_page_config(page_title="مساعد تأسيس شركة - يوني زون", layout="centered")
st.title("🤖 مساعد تأسيس شركة - يوني زون")

with st.form("advisor_form"):
    st.markdown("### 🧠 جاوب على الأسئلة التالية علشان نرشحلك نوع الشركة المناسب")
    q1 = st.radio("هل أنت وحدك في المشروع؟", ["نعم", "لا"])
    q2 = st.radio("هل ترغب في حماية أموالك الشخصية من المخاطر؟", ["نعم", "لا"])
    q3 = st.radio("هل معك شريك فقط للتمويل دون إدارة؟", ["نعم", "لا"])
    q4 = st.radio("هل تنوي دخول البورصة أو الاستثمار الكبير؟", ["نعم", "لا"])
    q5 = st.radio("هل الكيان تابع لشركة أجنبية بالخارج؟", ["نعم", "لا"])
    q6 = st.radio("هل تريد المرونة في دخول وخروج الشركاء؟", ["نعم", "لا"])
    q7 = st.radio("هل تتوقع عدد شركاء أكثر من 10 أفراد؟", ["نعم", "لا"])

    st.markdown("### 📝 بيانات الشركة")
    name = st.text_input("📛 اسم الشركة")
    owner = st.text_input("👤 اسم المالك")
    location = st.text_input("📍 المحافظة")
    partners = st.number_input("👥 عدد الشركاء", min_value=1, step=1)

    submitted = st.form_submit_button("🔍 اعرف نوع الشركة والتكلفة")

if submitted:
    company_type, notes, base_cost = "", "", 0
    duration = "من 15 يوم إلى شهر عمل"

    if q5 == "نعم":
        company_type = "فرع شركة أجنبية"
        notes = "مناسب لإنشاء فرع لشركة بالخارج داخل مصر"
        base_cost = 28000
    elif q4 == "نعم" or q7 == "نعم":
        company_type = "شركة مساهمة"
        notes = "مناسبة للمشروعات الكبيرة ودخول البورصة"
        base_cost = 30000
    elif q3 == "نعم":
        company_type = "شركة توصية بسيطة"
        notes = "تناسب شراكة فيها شريك ممول غير إداري"
        base_cost = 17000
    elif q1 == "لا" and q2 == "نعم":
        company_type = "شركة ذات مسؤولية محدودة"
        notes = "مناسبة لحماية قانونية مرنة وتقييد المسؤولية"
        base_cost = 22000
    elif q1 == "لا" and q6 == "لا":
        company_type = "شركة تضامن"
        notes = "شراكة متساوية بالمسؤولية والإدارة"
        base_cost = 15000
    elif q1 == "نعم":
        company_type = "منشأة فردية"
        notes = "تناسب مشروع فردي بسيط باسم شخص واحد"
        base_cost = 10000
    else:
        company_type = "شركة ذات مسؤولية محدودة"
        notes = "اختيار مناسب للحماية القانونية والتنظيم"
        base_cost = 22000

    data = {
        "اسم الشركة": name,
        "المالك": owner,
        "الموقع": location,
        "عدد الشركاء": partners,
        "نوع الشركة المقترحة": company_type,
        "💸 التكلفة التقديرية": f"{base_cost:,} جنيه",
        "⏱️ المدة المتوقعة للتنفيذ": duration,
        "📌 ملاحظات": notes
    }

    st.markdown("---")
    st.subheader("✅ تفاصيل شركتك المقترحة:")
    for k, v in data.items():
        st.write(f"**{k}:** {v}")
    st.markdown(generate_pdf(data), unsafe_allow_html=True)
