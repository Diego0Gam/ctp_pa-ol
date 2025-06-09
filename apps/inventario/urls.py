from django.urls import path
from .views import EstudianteCreateView, EstudianteListView, EstudianteDeleteView, EstudianteUpdateView
from .views import CursoCreateView, CursoDeleteView, CursoListView, CursoUpdateView
from .views import MateriaCreateView, MateriaDeleteView, MateriaListView, MateriaUpdateView
from .views import ComputadoraCreateView, ComputadoraDeleteView, ComputadoraListView, ComputadoraUpdateView
from .views import PrestamoCreateView, PrestamoListView, PrestamoDeleteView, PrestamoUpdateView

app_name = "inventario"

urlpatterns = [
#Estudiante
    path('estudiante/crear/', EstudianteCreateView.as_view(), name = 'estudiante_create'),
    path('estudiante/lista/', EstudianteListView.as_view(), name = 'estudiante_list'),
    path('estudiante/<int:pk>/editar/', EstudianteUpdateView.as_view(), name = 'estudiante_update'),
    path('estudiante/<int:pk>/eliminar/', EstudianteDeleteView.as_view(), name = 'estudiante_delete'),
#Curso
    path('curso/crear/', CursoCreateView.as_view(), name = 'curso_create'),
    path('curso/lista/', CursoListView.as_view(), name = 'curso_list'),
    path('curso/<int:pk>/editar/', CursoUpdateView.as_view(), name = 'curso_update'),
    path('curso/<int:pk>/eliminar/', CursoDeleteView.as_view(), name = 'curso_delete'),
#Materia
    path('materia/crear/', MateriaCreateView.as_view(), name = 'materia_create'),
    path('materia/lista/', MateriaListView.as_view(), name = 'materia_list'),
    path('materia/<int:pk>/editar/', MateriaUpdateView.as_view(), name = 'materia_update'),
    path('materia/<int:pk>/eliminar/', MateriaDeleteView.as_view(), name = 'materia_delete'),
#Computadora
    path('computadora/crear/', ComputadoraCreateView.as_view(), name = 'computadora_create'),
    path('computadora/lista/', ComputadoraListView.as_view(), name = 'computadora_list'),
    path('computadora/<int:pk>/editar/', ComputadoraUpdateView.as_view(), name = 'computadora_update'),
    path('computadora/<int:pk>/eliminar/', ComputadoraDeleteView.as_view(), name = 'computadora_delete'),
#Prestamo
    path('prestamo/crear/', PrestamoCreateView.as_view(), name = 'prestamo_create'),
    path('prestamo/lista/', PrestamoListView.as_view(), name = 'prestamo_list'),
    path('prestamo/<int:pk>/editar/', PrestamoUpdateView.as_view(), name = 'prestamo_update'),
    path('prestamo<int:pk>/eliminar/', PrestamoDeleteView.as_view(), name = 'prestamo_delete')
]