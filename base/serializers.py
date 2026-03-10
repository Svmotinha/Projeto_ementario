from rest_framework import serializers

from .models import (
    Curso,
    CursoEdicaoUsuario, # Novo: Importante para interceptar o PUT/PATCH
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


# --- INÍCIO DAS ALTERAÇÕES NO CURSO SERIALIZER ---
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"
        read_only_fields = ['id_curso', 'codigo_curso'] # Protege os identificadores principais

    def to_representation(self, instance):
        """
        No GET: Mascara os campos do banco com os valores consolidados
        (prioridade para edição do usuário, fallback para o Selenium).
        """
        data = super().to_representation(instance)
        
        campos_conflito = [
            'nome_curso', 'turno_curso', 'modalidade_curso', 
            'area_conhecimento_curso', 'funcionamento_curso', 
            'grau_academico', 'ato_autorizacao_curso', 
            'ato_reconhecimento_curso', 'conceito_mec_curso'
        ]

        for campo in campos_conflito:
            atributo_final = f"{campo}_final"
            if hasattr(instance, atributo_final):
                data[campo] = getattr(instance, atributo_final)
                
        return data

    def update(self, instance, validated_data):
        """
        No PUT/PATCH: Direciona as edições do usuário para a tabela 'CursoEdicaoUsuario',
        mantendo a tabela principal 'Curso' intacta.
        """
        edicao, created = CursoEdicaoUsuario.objects.get_or_create(curso=instance)
        
        for attr, value in validated_data.items():
            if hasattr(edicao, attr):
                setattr(edicao, attr, value)
        
        edicao.save()
        
        # Retorna a instância recalculada para refletir na resposta da API
        return Curso.objects.consolidados().get(pk=instance.pk)
# --- FIM DAS ALTERAÇÕES ---


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