from django.shortcuts import render
from django.http import JsonResponse
from asteval import Interpreter
import math

# Create your views here.
def calculator_view(request):
    return render(request, 'calculator_app/index.html')

def calculate_api(request):
    if request.method == 'POST':
        try:
            data = request.FILES['data'].read().decode('utf-8')
            expression = data
        except KeyError:
            expression = request.body.decode('utf-8')

        # Initialize asteval interpreter
        aeval = Interpreter()
        # Add math functions and constants
        aeval.symtable['sin'] = math.sin
        aeval.symtable['cos'] = math.cos
        aeval.symtable['tan'] = math.tan
        aeval.symtable['sqrt'] = math.sqrt
        aeval.symtable['pi'] = math.pi
        aeval.symtable['pow'] = math.pow

        try:
            # Evaluate the expression
            result = aeval(expression)
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'result': 'Error: ' + str(e)})
    return JsonResponse({'result': 'Invalid request method.'})