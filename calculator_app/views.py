from django.shortcuts import render
from django.http import JsonResponse
from asteval import Interpreter
import math
import json # Import the json module

# Create your views here.
def calculator_view(request):
    return render(request, 'calculator_app/index.html')

def calculate_api(request):
    if request.method == 'POST':
        try:
            # Correctly parse JSON from request body
            data = json.loads(request.body)
            expression = data.get('expression', '')
        except json.JSONDecodeError:
            return JsonResponse({'result': 'Error: Invalid JSON'}, status=400)

        # Initialize asteval interpreter
        aeval = Interpreter()
        # Add math functions and constants
        aeval.symtable['sin'] = math.sin
        aeval.symtable['cos'] = math.cos
        aeval.symtable['tan'] = math.tan
        aeval.symtable['sqrt'] = math.sqrt
        aeval.symtable['pi'] = math.pi
        aeval.symtable['pow'] = math.pow
        aeval.symtable['abs'] = math.fabs # Add abs for completeness

        try:
            # Evaluate the expression
            result = aeval(expression)
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'result': 'Error: ' + str(e)})
    return JsonResponse({'result': 'Error: Invalid request method.'}, status=405) # Return JSON for error