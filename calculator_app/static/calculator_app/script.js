const display = document.getElementById('display');
let currentExpression = '';

function appendCharacter(char) {
    if (currentExpression === '0' && char !== '.') {
        currentExpression = char;
    } else {
        currentExpression += char;
    }
    display.innerText = currentExpression;
}

function clearDisplay() {
    currentExpression = '0';
    display.innerText = currentExpression;
}

function deleteChar() {
    currentExpression = currentExpression.slice(0, -1);
    if (currentExpression === '') {
        currentExpression = '0';
    }
    display.innerText = currentExpression;
}

async function calculate() {
    try {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const response = await fetch('/calculate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ expression: currentExpression }) // Send as JSON object
        });
        const data = await response.json();
        if (data.result.toString().startsWith('Error')) {
            display.innerText = data.result;
            currentExpression = '0'; // Reset expression on error
        }
        else {
            currentExpression = data.result.toString();
            display.innerText = currentExpression;
        }
    }
    catch (error) {
        display.innerText = 'Error';
        currentExpression = '0'; // Reset expression on error
    }
}
