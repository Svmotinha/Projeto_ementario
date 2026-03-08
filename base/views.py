from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Curso,
    Curriculo,
    CurriculoDisciplina,
    Disciplina,
    Docente,
    DocenteDisciplina,
    DocumentoCurso,
    PPC,
    Unidade,
    Usuario,
)
from .serializers import (
    CursoSerializer,
    CurriculoDisciplinaSerializer,
    CurriculoSerializer,
    DisciplinaSerializer,
    DocenteDisciplinaSerializer,
    DocenteSerializer,
    DocumentoCursoSerializer,
    PPCSerializer,
    UnidadeSerializer,
    UsuarioSerializer,
)


def base(request):
    return render(request, 'base.html')


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id_usuario')
    serializer_class = UsuarioSerializer


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all().order_by('id_docente')
    serializer_class = DocenteSerializer


class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all().order_by('id_unidade')
    serializer_class = UnidadeSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('id_curso')
    serializer_class = CursoSerializer


class CurriculoViewSet(viewsets.ModelViewSet):
    queryset = Curriculo.objects.all().order_by('id_curriculo')
    serializer_class = CurriculoSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all().order_by('id_disciplina')
    serializer_class = DisciplinaSerializer


class CurriculoDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = CurriculoDisciplina.objects.all().order_by('id_curriculo_disciplina')
    serializer_class = CurriculoDisciplinaSerializer


class DocenteDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = DocenteDisciplina.objects.all().order_by('id_docente_disciplina')
    serializer_class = DocenteDisciplinaSerializer


class PPCViewSet(viewsets.ModelViewSet):
    queryset = PPC.objects.all().order_by('id_ppc')
    serializer_class = PPCSerializer


class DocumentoCursoViewSet(viewsets.ModelViewSet):
    queryset = DocumentoCurso.objects.all().order_by('id_documento')
    serializer_class = DocumentoCursoSerializer
