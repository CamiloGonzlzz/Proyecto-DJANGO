from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
from .forms import VectorForm
import json

def graficar_vectorR2(request):
    if request.method == 'POST':
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))

        plt.figure()

        # Dibujar el vector
        plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='black', label=f'Vector ({x}, {y})')

        # Dibujar las líneas extrapolares
        plt.plot([0, x], [y, y], linestyle='--', color='blue', label='Línea Extrapolar Y')  # Línea horizontal
        plt.plot([x, x], [0, y], linestyle='--', color='red', label='Línea Extrapolar X')  # Línea vertical

        # Configuraciones de la gráfica
        max_range = max(abs(x), abs(y)) + 1
        plt.xlim(-max_range, max_range)
        plt.ylim(-max_range, max_range)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()

        # Guardar la imagen en memoria
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        imagen_png = buffer.getvalue()
        buffer64 = base64.b64encode(imagen_png)
        imagen = buffer64.decode('utf-8')
        plt.close()

        return render(request, 'grafico_app/grafico.html', {'imagen': imagen})

    return render(request, 'grafico_app/grafico.html')





def vector_grafico(request):
    if request.method == 'POST':
        form = VectorForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            z = form.cleaned_data['z']
            vector_data = {'x': x, 'y': y, 'z': z}  # Crear un diccionario con los datos
            return render(request, 'grafico_app/graficoR3.html', {'form': form, 'vector_data': json.dumps(vector_data)})
    else:
        form = VectorForm()
    return render(request, 'grafico_app/graficoR3.html', {'form': form})

def grafico_vector(request):
    return render(request, 'grafico_app/grafico_vector.html')
