
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_FORM = """<!DOCTYPE html>
<html lang='ar' dir='rtl'>
<head>
  <meta charset='UTF-8'>
  <title>حاسبة تأسيس الشركات</title>
  <style>
    body { font-family: Tahoma; background: #f0f0f0; padding: 20px; }
    .container { background: white; padding: 25px; border-radius: 10px; max-width: 700px; margin: auto; box-shadow: 0 0 15px rgba(0,0,0,0.1); }
    input, select, button { padding: 10px; margin: 10px 0; width: 100%; max-width: 500px; border-radius: 5px; border: 1px solid #ccc; }
    button { background: #007bff; color: white; border: none; cursor: pointer; }
    button:hover { background: #0056b3; }
    .result { margin-top: 20px; background: #fafafa; padding: 20px; border-radius: 8px; }
  </style>
</head>
<body>
  <div class="container">
    <h2>🧾 حاسبة تكلفة تأسيس شركة</h2>
    <form method="post">
      <input name="name" placeholder="اسم الشركة" required>
      <input name="owner" placeholder="اسم المالك" required>
      <input name="location" placeholder="موقع الشركة (المحافظة)" required>
      <input name="partners" type="number" placeholder="عدد الشركاء" required>
      <select name="type" required>
        <option>منشأة فردية</option>
        <option>شركة تضامن</option>
        <option>شركة توصية بسيطة</option>
        <option>شركة ذات مسؤولية محدودة</option>
        <option>شركة مساهمة</option>
        <option>فرع شركة أجنبية</option>
      </select>
      <button type="submit">احسب التكلفة</button>
    </form>

    {% if result %}
    <div class="result">
      <h3>📋 تفاصيل التكلفة</h3>
      <p><strong>اسم الشركة:</strong> {{ result.name }}</p>
      <p><strong>المالك:</strong> {{ result.owner }}</p>
      <p><strong>الموقع:</strong> {{ result.location }}</p>
      <p><strong>نوع الشركة:</strong> {{ result.type }}</p>
      <p><strong>عدد الشركاء:</strong> {{ result.partners }}</p>
      <p><strong>💸 التكلفة الأساسية:</strong> {{ result.base_cost }} جنيه</p>
      <p><strong>💼 المبلغ الثابت الإضافي:</strong> 5000 جنيه</p>
      <p><strong>💰 الإجمالي:</strong> {{ result.total }} جنيه</p>
      <p><strong>⏱️ المدة المتوقعة للتنفيذ:</strong> {{ result.duration }}</p>
      <p><strong>📌 ملاحظات:</strong> {{ result.notes }}</p>
    </div>
    {% endif %}
  </div>
</body>
</html>"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name = request.form["name"]
        owner = request.form["owner"]
        location = request.form["location"]
        partners = request.form["partners"]
        company_type = request.form["type"]

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

        result = {
            "name": name,
            "owner": owner,
            "location": location,
            "type": company_type,
            "partners": partners,
            "base_cost": base_cost,
            "total": total,
            "duration": duration,
            "notes": notes
        }

    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    app.run(debug=True)
