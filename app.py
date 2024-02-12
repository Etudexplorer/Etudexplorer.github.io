from flask import Flask, render_template, request
import random  

app = Flask(__name__)

def get_recommendations(category, city):
    filename = f'{category.lower()}.txt'
    with open(filename, 'r') as file:
        places = [line.strip().split(', ') for line in file]

    filtered_recommendations = [name for name, location in places if location.lower() == city.lower()]

    recommendations = random.sample(filtered_recommendations, min(5, len(filtered_recommendations)))

    return recommendations

@app.route('/application.html')
def application():
    return render_template('application.html')

@app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route('/point.html')
def point():
    return render_template('point.html')

@app.route('/index.html', methods=['GET', 'POST'])
def chatbot():
    show_text_input = False
    recommendations = []
    contact_creators_text = None
    report_error_text = None

    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input == "Je veux contacter tes créateurs":
            contact_creators_text = "Contactez-nous à l'adresse e-mail : etudexplorers@gmail.com"
        elif user_input == "Je veux reporter une erreur":
            report_error_text = "Envoyez un e-mail à etudexplorers@gmail.com"
        elif user_input == "Je cherche un lieu":
            show_text_input = True
        elif user_input in ["Etudier", "Fastfood", "Divertissement", "Sport"]:
            city = request.form['city']
            recommendations = get_recommendations(user_input, city)

    return render_template('index.html', show_text_input=show_text_input, recommendations=recommendations, contact_creators_text=contact_creators_text, report_error_text=report_error_text)

if __name__ == '__main__':
    app.run(debug=True)
