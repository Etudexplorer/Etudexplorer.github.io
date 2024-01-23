from flask import Flask, request, render_template

app = Flask(__name__)

# Fonction pour obtenir des recommandations de fast-foods abordables
def get_fastfood_recommendations(city):
    # Charger les données des fast-foods depuis le fichier
    with open('fastfoods.txt', 'r') as file:
        fastfoods = [line.strip().split(', ') for line in file]

    # Filtrer les fast-foods par ville
    recommendations = [name for name, location in fastfoods if location.lower() == city.lower()]

    return recommendations

# Route principale pour le chatbot
@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form['user_input']
        city = request.form['city']

        if 'où sont les fastfoods pas chers' in user_input.lower():
            # Appel à la fonction pour obtenir des recommandations
            recommendations = get_fastfood_recommendations(city)
            response = f"Voici quelques fast-foods abordables à {city} :\n{', '.join(recommendations)}"
        else:
            response = "Désolé, je ne comprends pas. Pouvez-vous reformuler votre demande?"

        return render_template('index.html', user_input=user_input, response=response, city=city)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
