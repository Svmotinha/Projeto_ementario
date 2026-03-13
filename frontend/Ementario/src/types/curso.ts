export type Curso = {
  id_curso: number;
  codigo_curso: string;
  nome_curso: string;
  nivel_curso: 'Graduação' | 'Pós-Graduação';
  turno_curso: 'Integral' | 'Matutino' | 'Vespertino' | 'Noturno' | 'Diurno' | null;
  modalidade_curso: string | null;
  area_conhecimento_curso: string | null;
  funcionamento_curso: 'Em atividade' | 'Inativo' | 'Suspenso';
  grau_academico: string | null;
  ato_autorizacao_curso: string | null;
  ato_reconhecimento_curso: string | null;
  conceito_mec_curso: string | null;
  inserido_manualmente: boolean;
  coordenador: number | null;
  created_at: string;
  updated_at: string;
}
