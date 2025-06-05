from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Estudiante, Curso, Materia, Computadora, Prestamo

#Estudiante
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiante/list.html'
    context_object_name = 'estudiantes' # Esta es la variable que se usará en el template con {% for estudiante in estudiantes %} para mostrar los estudiantes.

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = '__all__'
    template_name = 'estudiante/create.html'
    success_url = reverse_lazy('inventario:estudiante_list')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = '__all__'
    template_name = 'estudiante/update.html'
    success_url = reverse_lazy('inventario:estudiante_list')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'estudiante/delete.html'
    success_url = reverse_lazy('inventario:estudiante_list')

#Curso
class CursoListView(ListView):
    model = Curso
    template_name = 'curso/list.html'
    context_object_name = 'cursos'

class CursoCreateView(CreateView):
    model = Curso
    fields = '__all__'
    template_name = 'curso/create.html'
    success_url = reverse_lazy('inventario:curso_list')

class CursoUpdateView(UpdateView):
    model = Curso
    fields = '__all__'
    template_name = 'curso/update.html'
    success_url = reverse_lazy('inventario:curso_list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'curso/delete.html'
    success_url = reverse_lazy('inventario:curso_list')

#Materia
class MateriaListView(ListView):
    model = Materia
    template_name = 'materia/list.html'
    context_object_name = 'materias'

class MateriaCreateView(CreateView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/create.html'
    success_url = reverse_lazy('inventario:materia_list')

class MateriaUpdateView(UpdateView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/update.html'
    success_url = reverse_lazy('inventario:materia_list')

class MateriaDeleteView(DeleteView):
    model = Materia
    template_name = 'materia/delete.html'
    success_url = reverse_lazy('inventario:materia_list')

#Computadora
class ComputadoraListView(ListView):
    model = Computadora
    template_name = 'computadora/list.html'
    context_object_name = 'computadoras'

class ComputadoraCreateView(CreateView):
    model = Computadora
    fields = '__all__'
    template_name = 'computadora/create.html'
    success_url = reverse_lazy('inventario:computadora_list')

class ComputadoraUpdateView(UpdateView):
    model = Computadora
    fields = '__all__'
    template_name = 'computadora/update.html'
    success_url = reverse_lazy('inventario:computadora_list')

class ComputadoraDeleteView(DeleteView):
    model = ConnectionRefusedError
    template_name = 'computadora/delete.html'
    success_url = reverse_lazy('inventario:computadora_list')

#Prestamo
class PrestamoListView(ListView):
    model = Prestamo
    template_name = 'prestamo/list.html'
    context_object_name = 'prestamos'

class PrestamoCreateView(CreateView):
    model = Prestamo
    fields = '__all__'
    template_name = 'prestamo/create.html'
    success_url = reverse_lazy('inventario:prestamo_list')

class PrestamoUpdateView(UpdateView):
    model = Prestamo
    fields = '__all__'
    template_name = 'prestamo/update.html'
    success_url = reverse_lazy('inventario:prestamo_list')

class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = 'prestamo/delete.html'
    success_url = reverse_lazy('inventario:prestamo_list')