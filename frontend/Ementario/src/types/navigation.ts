// Este arquivo centraliza o contrato de navegacao da aplicacao.
// As paginas, o sidebar e o topo usam os mesmos metadados para evitar duplicacao.
export type NavigationKey = 'dashboard' | 'cursos' | 'configuracoes' | 'status-api'
export type NavigationSection = 'Navegacao' | 'Sistema'

export interface NavigationItem {
  key: NavigationKey
  label: string
  topbarLabel: string
  path: string
  description: string
  section: NavigationSection
}

export const navigationItems: NavigationItem[] = [
  {
    key: 'dashboard',
    label: 'Dashboard',
    topbarLabel: 'dashboard',
    path: '/dashboard',
    description: 'Painel principal com resumo da sincronizacao e atividade recente.',
    section: 'Navegacao',
  },
  {
    key: 'cursos',
    label: 'Cursos',
    topbarLabel: 'cursos',
    path: '/cursos',
    description: 'Area para consulta e manutencao dos cursos e disciplinas.',
    section: 'Navegacao',
  },
  {
    key: 'status-api',
    label: 'Status da API',
    topbarLabel: 'status da api',
    path: '/status-api',
    description: 'Painel de monitoramento da API e da esteira de extracao.',
    section: 'Sistema',
  },
  {
    key: 'configuracoes',
    label: 'Configuracoes',
    topbarLabel: 'configuracoes',
    path: '/configuracoes',
    description: 'Preferencias gerais da aplicacao e parametros administrativos.',
    section: 'Sistema',
  },
]
