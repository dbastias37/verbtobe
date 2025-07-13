class SpinningVerbs {
    constructor() {
        this.verbs = [];
        this.currentVerbIndex = 0;
        this.currentForm = 'infinitive';
        this.isQuizMode = false;
        this.quizScore = 0;
        this.quizTotal = 0;
        this.currentQuizQuestion = null;
        this.isSpinning = false;
        this.rotation = 0;
        
        this.init();
    }
    
    async init() {
        await this.loadVerbs();
        this.createWheel();
        this.updateDisplay();
        this.bindEvents();
    }
    
    async loadVerbs() {
        try {
            const response = await fetch('/api/verbs');
            this.verbs = await response.json();
        } catch (error) {
            console.error('Error loading verbs:', error);
            // Fallback data
            this.verbs = [
                {"infinitive": "BE", "past": "WAS/WERE", "participle": "BEEN", "meaning": "ser/estar"},
                {"infinitive": "HAVE", "past": "HAD", "participle": "HAD", "meaning": "tener"},
                {"infinitive": "DO", "past": "DID", "participle": "DONE", "meaning": "hacer"}
            ];
        }
    }
    
    createWheel() {
        const wheelOuter = document.querySelector('.wheel-outer');
        wheelOuter.innerHTML = '';
        
        const totalSlots = 72;
        const angleStep = 360 / totalSlots;
        
        for (let i = 0; i < totalSlots; i++) {
            const slot = document.createElement('div');
            slot.className = 'verb-slot';
            slot.style.transform = `rotate(${i * angleStep}deg)`;
            
            const verbIndex = i % this.verbs.length;
            const verb = this.verbs[verbIndex];
            
            let displayText = '';
            switch (this.currentForm) {
                case 'infinitive':
                    displayText = verb.infinitive;
                    break;
                case 'past':
                    displayText = verb.past;
                    break;
                case 'participle':
                    displayText = verb.participle;
                    break;
            }
            
            slot.textContent = displayText;
            slot.addEventListener('click', () => this.selectVerb(verbIndex));
            
            if (verbIndex === this.currentVerbIndex) {
                slot.classList.add('active');
            }
            
            wheelOuter.appendChild(slot);
        }

        wheelOuter.style.transform = `rotate(${this.rotation}deg)`;
    }
    
    updateDisplay() {
        const currentVerb = this.verbs[this.currentVerbIndex];
        if (!currentVerb) return;
        
        // Update form selector
        document.getElementById('verbForm').value = this.currentForm;
        
        // Update wheel center
        const formNames = {
            infinitive: 'INFINITIVE',
            past: 'SIMPLE PAST',
            participle: 'PAST PARTICIPLE'
        };
        
        document.querySelector('.current-form').textContent = formNames[this.currentForm];
        
        let currentText = '';
        switch (this.currentForm) {
            case 'infinitive':
                currentText = currentVerb.infinitive;
                break;
            case 'past':
                currentText = currentVerb.past;
                break;
            case 'participle':
                currentText = currentVerb.participle;
                break;
        }
        
        document.querySelector('.current-verb').textContent = currentText;
        
        // Update info panel
        this.updateInfoPanel(currentVerb);
        
        // Update active slot
        this.updateActiveSlot();
    }
    
    updateInfoPanel(verb) {
        const panel = document.getElementById('verbInfo');
        if (!panel) return;
        
        panel.innerHTML = `
            <h3>📚 Detalles del Verbo</h3>
            <div class="verb-details">
                <div class="verb-form">
                    <h4>INFINITIVE</h4>
                    <span>${verb.infinitive}</span>
                </div>
                <div class="verb-form">
                    <h4>SIMPLE PAST</h4>
                    <span>${verb.past}</span>
                </div>
                <div class="verb-form">
                    <h4>PAST PARTICIPLE</h4>
                    <span>${verb.participle}</span>
                </div>
            </div>
            <div class="meaning">
                <strong>Significado:</strong> ${verb.meaning}
            </div>
        `;
    }
    
    updateActiveSlot() {
        document.querySelectorAll('.verb-slot').forEach((slot, index) => {
            const verbIndex = index % this.verbs.length;
            if (verbIndex === this.currentVerbIndex) {
                slot.classList.add('active');
            } else {
                slot.classList.remove('active');
            }
        });
    }
    
    rotateWheel(direction) {
        if (this.isSpinning) return;
        
        this.isSpinning = true;
        const wheelOuter = document.querySelector('.wheel-outer');
        
        if (direction === 'left') {
            this.currentVerbIndex = (this.currentVerbIndex - 1 + this.verbs.length) % this.verbs.length;
        } else {
            this.currentVerbIndex = (this.currentVerbIndex + 1) % this.verbs.length;
        }
        
        // Calculate rotation angle
        const angleStep = 360 / 72; // 72 slots total
        this.rotation += direction === 'left' ? angleStep : -angleStep;

        wheelOuter.style.transform = `rotate(${this.rotation}deg)`;
        
        setTimeout(() => {
            this.isSpinning = false;
            this.updateDisplay();
        }, 800);
    }
    
    
    selectVerb(verbIndex) {
        if (this.isSpinning) return;
        this.currentVerbIndex = verbIndex;
        this.updateDisplay();
    }
    
    changeForm(newForm) {
        if (this.isSpinning) return;
        this.currentForm = newForm;
        this.createWheel();
        this.updateDisplay();
    }
    
    randomSpin() {
        if (this.isSpinning) return;
        
        this.isSpinning = true;
        const wheelOuter = document.querySelector('.wheel-outer');
        wheelOuter.classList.add('spinning');
        
        // Random verb and form
        this.currentVerbIndex = Math.floor(Math.random() * this.verbs.length);
        const forms = ['infinitive', 'past', 'participle'];
        this.currentForm = forms[Math.floor(Math.random() * forms.length)];
        
        setTimeout(() => {
            wheelOuter.classList.remove('spinning');
            this.isSpinning = false;
            this.createWheel();
            this.updateDisplay();
        }, 2000);
    }
    
    async toggleQuiz() {
        const wheelView = document.getElementById('wheel-view');
        const quizView = document.getElementById('quiz-view');
        
        if (this.isQuizMode) {
            // Return to wheel
            wheelView.classList.remove('hidden');
            quizView.classList.add('hidden');
            this.isQuizMode = false;
        } else {
            // Start quiz
            wheelView.classList.add('hidden');
            quizView.classList.remove('hidden');
            this.isQuizMode = true;
            this.quizScore = 0;
            this.quizTotal = 0;
            await this.nextQuizQuestion();
        }
    }
    
    async nextQuizQuestion() {
        try {
            const response = await fetch('/api/quiz');
            this.currentQuizQuestion = await response.json();
            this.displayQuizQuestion();
        } catch (error) {
            console.error('Error loading quiz question:', error);
        }
    }
    
    displayQuizQuestion() {
        if (!this.currentQuizQuestion) return;
        
        const question = this.currentQuizQuestion;
        const questionEl = document.getElementById('quiz-question');
        const optionsEl = document.getElementById('quiz-options');
        const scoreEl = document.getElementById('quiz-score');
        
        const formNames = {
            'INFINITIVE': 'infinitivo',
            'SIMPLE PAST': 'pasado simple',
            'PAST PARTICIPLE': 'participio pasado'
        };
        
        questionEl.innerHTML = `
            Complete la forma <strong>${formNames[question.question_form] || question.question_form}</strong> del verbo:<br><br>
            <strong style="color: #6c5ce7; font-size: 1.4rem;">${question.verb.meaning}</strong>
        `;
        
        optionsEl.innerHTML = question.options.map(option => 
            `<div class="quiz-option" onclick="app.selectQuizAnswer('${option}')">${option}</div>`
        ).join('');
        
        scoreEl.textContent = `Puntuación: ${this.quizScore}/${this.quizTotal}`;
    }
    
    selectQuizAnswer(selected) {
        this.quizTotal++;
        const options = document.querySelectorAll('.quiz-option');
        const correct = this.currentQuizQuestion.correct_answer;
        
        options.forEach(option => {
            option.style.pointerEvents = 'none';
            if (option.textContent === correct) {
                option.classList.add('correct');
            } else if (option.textContent === selected && selected !== correct) {
                option.classList.add('incorrect');
            }
        });
        
        if (selected === correct) {
            this.quizScore++;
        }
        
        // Update score
        document.getElementById('quiz-score').textContent = `Puntuación: ${this.quizScore}/${this.quizTotal}`;
        
        // Auto-advance after 2 seconds
        setTimeout(() => {
            this.nextQuizQuestion();
        }, 2000);
    }
    
    bindEvents() {
        // Navigation buttons
        document.getElementById('rotateLeft').addEventListener('click', () => this.rotateWheel('left'));
        document.getElementById('rotateRight').addEventListener('click', () => this.rotateWheel('right'));
        
        // Form selector
        document.getElementById('verbForm').addEventListener('change', (e) => {
            this.changeForm(e.target.value);
        });
        
        // Action buttons
        document.getElementById('randomBtn').addEventListener('click', () => this.randomSpin());
        document.getElementById('quizBtn').addEventListener('click', () => this.toggleQuiz());
        
        // Quiz return button
        document.getElementById('returnBtn').addEventListener('click', () => this.toggleQuiz());
        
        // Keyboard controls
        document.addEventListener('keydown', (e) => {
            if (this.isQuizMode) return;
            
            switch(e.key) {
                case 'ArrowLeft':
                    e.preventDefault();
                    this.rotateWheel('left');
                    break;
                case 'ArrowRight':
                    e.preventDefault();
                    this.rotateWheel('right');
                    break;
                case ' ':
                    e.preventDefault();
                    this.randomSpin();
                    break;
            }
        });
    }
}

// Initialize app when DOM is ready
let app;
document.addEventListener('DOMContentLoaded', () => {
    app = new SpinningVerbs();
});

