
from flask import Flask, render_template, request, redirect, url_for, flash
import random
import webbrowser
import time

app = Flask(__name__)
app.secret_key = 'secret_key'

# قائمة من رسائل التصيد الاحتيالي
phishing_emails = [
    "Dear user, your account will be suspended unless you verify your information.",
    "Congratulations! You've won a gift card. Click here to claim your prize!",
    "Your invoice is attached. Please open it to view your payment details.",
    "Important security notice: Update your password immediately."
]

# الصفحة الرئيسية
@app.route('/')
def index():
    email = random.choice(phishing_emails)  # اختيار رسالة عشوائية من القائمة
    return render_template('index.html', email=email)  # تمرير الرسالة إلى القالب

# محاكاة رسالة البريد الإلكتروني
@app.route('/phishing-simulation', methods=['POST'])
def phishing_simulation():
    user_choice = request.form.get('choice')
    if user_choice == 'yes':
        flash('Great job! You avoided the phishing attempt.', 'success')
    else:
        flash('Oops! You fell for the phishing email.', 'danger')
    return redirect(url_for('index'))

# صفحة المحتوى التعليمي
@app.route('/education')
def education():
    content = """
    Phishing emails try to trick you into clicking malicious links.
    Always check the sender’s email and avoid clicking on suspicious links.
    """
    return render_template('education.html', content=content)

if __name__ == '__main__':
    # فتح المتصفح تلقائيًا
    time.sleep(1)  # تأخير لبدء التطبيق أولاً
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
