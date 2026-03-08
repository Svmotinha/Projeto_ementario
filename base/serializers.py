from rest_framework import serializers

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


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = "__all__"


class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = "__all__"


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class CurriculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculo
        fields = "__all__"


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"


class CurriculoDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculoDisciplina
        fields = "__all__"


class DocenteDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocenteDisciplina
        fields = "__all__"


class PPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PPC
        fields = "__all__"


class DocumentoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoCurso
        fields = "__all__"
