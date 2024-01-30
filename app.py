from flask import Flask, render_template, request

app = Flask(__name__)

# Logique factice pour simuler les recommandations
def get_recommendations(category, city):
    # Chargez les données depuis le fichier correspondant
    filename = f'{category.lower()}.txt'
    with open(filename, 'r') as file:
        places = [line.strip().split(', ') for line in file]

    # Filtrer les lieux par ville
    recommendations = [name for name, location in places if location.lower() == city.lower()]

    return recommendations

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    show_text_input = False
    recommendations = []
    contact_creators_text = None
    report_error_text = None

    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input == "Je veux contacter tes créateurs":
            return "Contactez-nous à l'adresse e-mail : etudexplorers@gmail.com"
        elif user_input == "Je veux reporter une erreur":
            return "Envoyez un e-mail à etudexplorers@gmail.com"
        elif user_input == "Je cherche un lieu":
            show_text_input = True
        elif user_input in ["Etudier", "Fastfood", "Divertissement", "Sport"]:
            city = request.form['city']
            recommendations = get_recommendations(user_input, city)

    return render_template('index.html', show_text_input=show_text_input, recommendations=recommendations, contact_creators_text=contact_creators_text, report_error_text=report_error_text)

if __name__ == '__main__':
    app.run(debug=True)