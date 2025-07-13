from flask import Flask, render_template, jsonify, request
import json
import random

app = Flask(__name__)

# Datos de verbos irregulares organizados por categorías
IRREGULAR_VERBS = {
    "common": [
        {"infinitive": "BE", "past": "WAS/WERE", "participle": "BEEN", "meaning": "ser/estar"},
        {"infinitive": "HAVE", "past": "HAD", "participle": "HAD", "meaning": "tener"},
        {"infinitive": "DO", "past": "DID", "participle": "DONE", "meaning": "hacer"},
        {"infinitive": "SAY", "past": "SAID", "participle": "SAID", "meaning": "decir"},
        {"infinitive": "GET", "past": "GOT", "participle": "GOT/GOTTEN", "meaning": "obtener"},
        {"infinitive": "MAKE", "past": "MADE", "participle": "MADE", "meaning": "hacer"},
        {"infinitive": "GO", "past": "WENT", "participle": "GONE", "meaning": "ir"},
        {"infinitive": "KNOW", "past": "KNEW", "participle": "KNOWN", "meaning": "conocer/saber"},
        {"infinitive": "TAKE", "past": "TOOK", "participle": "TAKEN", "meaning": "tomar"},
        {"infinitive": "SEE", "past": "SAW", "participle": "SEEN", "meaning": "ver"},
        {"infinitive": "COME", "past": "CAME", "participle": "COME", "meaning": "venir"},
        {"infinitive": "THINK", "past": "THOUGHT", "participle": "THOUGHT", "meaning": "pensar"},
        {"infinitive": "LOOK", "past": "LOOKED", "participle": "LOOKED", "meaning": "mirar"},
        {"infinitive": "WANT", "past": "WANTED", "participle": "WANTED", "meaning": "querer"},
        {"infinitive": "GIVE", "past": "GAVE", "participle": "GIVEN", "meaning": "dar"},
        {"infinitive": "USE", "past": "USED", "participle": "USED", "meaning": "usar"},
        {"infinitive": "FIND", "past": "FOUND", "participle": "FOUND", "meaning": "encontrar"},
        {"infinitive": "TELL", "past": "TOLD", "participle": "TOLD", "meaning": "contar/decir"},
        {"infinitive": "ASK", "past": "ASKED", "participle": "ASKED", "meaning": "preguntar"},
        {"infinitive": "WORK", "past": "WORKED", "participle": "WORKED", "meaning": "trabajar"},
        {"infinitive": "SEEM", "past": "SEEMED", "participle": "SEEMED", "meaning": "parecer"},
        {"infinitive": "FEEL", "past": "FELT", "participle": "FELT", "meaning": "sentir"},
        {"infinitive": "TRY", "past": "TRIED", "participle": "TRIED", "meaning": "intentar"},
        {"infinitive": "LEAVE", "past": "LEFT", "participle": "LEFT", "meaning": "dejar"},
        {"infinitive": "CALL", "past": "CALLED", "participle": "CALLED", "meaning": "llamar"},
        {"infinitive": "READ", "past": "READ", "participle": "READ", "meaning": "leer"},
        {"infinitive": "NEED", "past": "NEEDED", "participle": "NEEDED", "meaning": "necesitar"},
        {"infinitive": "BUILD", "past": "BUILT", "participle": "BUILT", "meaning": "construir"},
        {"infinitive": "LIVE", "past": "LIVED", "participle": "LIVED", "meaning": "vivir"},
        {"infinitive": "HELP", "past": "HELPED", "participle": "HELPED", "meaning": "ayudar"},
        {"infinitive": "STAND", "past": "STOOD", "participle": "STOOD", "meaning": "estar de pie"},
        {"infinitive": "MOVE", "past": "MOVED", "participle": "MOVED", "meaning": "mover"},
        {"infinitive": "PAY", "past": "PAID", "participle": "PAID", "meaning": "pagar"},
        {"infinitive": "MEET", "past": "MET", "participle": "MET", "meaning": "conocer/encontrar"},
        {"infinitive": "INCLUDE", "past": "INCLUDED", "participle": "INCLUDED", "meaning": "incluir"},
        {"infinitive": "CONTINUE", "past": "CONTINUED", "participle": "CONTINUED", "meaning": "continuar"},
        {"infinitive": "SET", "past": "SET", "participle": "SET", "meaning": "establecer"},
        {"infinitive": "LEARN", "past": "LEARNED/LEARNT", "participle": "LEARNED/LEARNT", "meaning": "aprender"},
        {"infinitive": "CHANGE", "past": "CHANGED", "participle": "CHANGED", "meaning": "cambiar"},
        {"infinitive": "LEAD", "past": "LED", "participle": "LED", "meaning": "liderar"},
        {"infinitive": "UNDERSTAND", "past": "UNDERSTOOD", "participle": "UNDERSTOOD", "meaning": "entender"},
        {"infinitive": "WATCH", "past": "WATCHED", "participle": "WATCHED", "meaning": "ver/observar"},
        {"infinitive": "FOLLOW", "past": "FOLLOWED", "participle": "FOLLOWED", "meaning": "seguir"},
        {"infinitive": "STOP", "past": "STOPPED", "participle": "STOPPED", "meaning": "parar"},
        {"infinitive": "CREATE", "past": "CREATED", "participle": "CREATED", "meaning": "crear"},
        {"infinitive": "SPEAK", "past": "SPOKE", "participle": "SPOKEN", "meaning": "hablar"},
        {"infinitive": "SPEND", "past": "SPENT", "participle": "SPENT", "meaning": "gastar"},
        {"infinitive": "GROW", "past": "GREW", "participle": "GROWN", "meaning": "crecer"},
        {"infinitive": "OPEN", "past": "OPENED", "participle": "OPENED", "meaning": "abrir"},
        {"infinitive": "WALK", "past": "WALKED", "participle": "WALKED", "meaning": "caminar"},
        {"infinitive": "WIN", "past": "WON", "participle": "WON", "meaning": "ganar"},
        {"infinitive": "OFFER", "past": "OFFERED", "participle": "OFFERED", "meaning": "ofrecer"},
        {"infinitive": "REMEMBER", "past": "REMEMBERED", "participle": "REMEMBERED", "meaning": "recordar"},
        {"infinitive": "LOVE", "past": "LOVED", "participle": "LOVED", "meaning": "amar"},
        {"infinitive": "CONSIDER", "past": "CONSIDERED", "participle": "CONSIDERED", "meaning": "considerar"},
        {"infinitive": "APPEAR", "past": "APPEARED", "participle": "APPEARED", "meaning": "aparecer"},
        {"infinitive": "BUY", "past": "BOUGHT", "participle": "BOUGHT", "meaning": "comprar"},
        {"infinitive": "WAIT", "past": "WAITED", "participle": "WAITED", "meaning": "esperar"},
        {"infinitive": "SERVE", "past": "SERVED", "participle": "SERVED", "meaning": "servir"},
        {"infinitive": "DIE", "past": "DIED", "participle": "DIED", "meaning": "morir"},
        {"infinitive": "SEND", "past": "SENT", "participle": "SENT", "meaning": "enviar"},
        {"infinitive": "EXPECT", "past": "EXPECTED", "participle": "EXPECTED", "meaning": "esperar"},
        {"infinitive": "STAY", "past": "STAYED", "participle": "STAYED", "meaning": "quedarse"},
        {"infinitive": "TALK", "past": "TALKED", "participle": "TALKED", "meaning": "hablar"},
        {"infinitive": "FALL", "past": "FELL", "participle": "FALLEN", "meaning": "caer"},
        {"infinitive": "LOSE", "past": "LOST", "participle": "LOST", "meaning": "perder"},
        {"infinitive": "PRODUCE", "past": "PRODUCED", "participle": "PRODUCED", "meaning": "producir"},
        {"infinitive": "EAT", "past": "ATE", "participle": "EATEN", "meaning": "comer"},
        {"infinitive": "RECEIVE", "past": "RECEIVED", "participle": "RECEIVED", "meaning": "recibir"},
        {"infinitive": "REMAIN", "past": "REMAINED", "participle": "REMAINED", "meaning": "permanecer"},
        {"infinitive": "SUGGEST", "past": "SUGGESTED", "participle": "SUGGESTED", "meaning": "sugerir"},
        {"infinitive": "RAISE", "past": "RAISED", "participle": "RAISED", "meaning": "levantar"},
        {"infinitive": "PASS", "past": "PASSED", "participle": "PASSED", "meaning": "pasar"},
        {"infinitive": "SELL", "past": "SOLD", "participle": "SOLD", "meaning": "vender"},
        {"infinitive": "REQUIRE", "past": "REQUIRED", "participle": "REQUIRED", "meaning": "requerir"}
    ]
}

# Configuraciones de la rueda
VERB_FORMS = ["INFINITIVE", "SIMPLE PAST", "PAST PARTICIPLE"]
TOTAL_SLOTS = 72  # Número total de verbos en el anillo exterior

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/verbs')
def get_verbs():
    """Devuelve todos los verbos disponibles"""
    return jsonify(IRREGULAR_VERBS["common"])

@app.route('/api/random-verb')
def get_random_verb():
    """Devuelve un verbo aleatorio"""
    verb = random.choice(IRREGULAR_VERBS["common"])
    return jsonify(verb)

@app.route('/api/quiz')
def get_quiz_question():
    """Genera una pregunta de quiz"""
    verb = random.choice(IRREGULAR_VERBS["common"])
    form = random.choice(VERB_FORMS)
    
    # Crear opciones incorrectas
    all_verbs = IRREGULAR_VERBS["common"]
    wrong_answers = []
    
    if form == "INFINITIVE":
        correct = verb["infinitive"]
        wrong_answers = [v["infinitive"] for v in random.sample(all_verbs, 3) if v["infinitive"] != correct]
    elif form == "SIMPLE PAST":
        correct = verb["past"]
        wrong_answers = [v["past"] for v in random.sample(all_verbs, 3) if v["past"] != correct]
    else:  # PAST PARTICIPLE
        correct = verb["participle"]
        wrong_answers = [v["participle"] for v in random.sample(all_verbs, 3) if v["participle"] != correct]
    
    options = [correct] + wrong_answers[:3]
    random.shuffle(options)
    
    return jsonify({
        "verb": verb,
        "question_form": form,
        "correct_answer": correct,
        "options": options
    })

if __name__ == '__main__':
    app.run(debug=True)
