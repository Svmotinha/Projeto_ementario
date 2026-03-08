interface PlaceholderPageProps {
  title: string
  description: string
}

// Componente temporario usado para rotas ja mapeadas,
// mas que ainda nao possuem implementacao funcional completa.
export function PlaceholderPage({ title, description }: PlaceholderPageProps) {
  return (
    <section className="placeholder-page">
      <h1>{title}</h1>
      <p>{description}</p>
      <p className="placeholder-page__hint">Tela em construção para a próxima iteração do front-end.</p>
    </section>
  )
}
