export type PageAnswer = {
  text: string
  correct: boolean
}

export type BasePage = {
  id: number
  title: string
}

export type TextPage = BasePage & {
  type: 'text'
  text: string
  button_text: string
}

export type QuizPage = BasePage & {
  type: 'quiz'
  image: string
  image_answer: string
  answers: PageAnswer[]
  points: number
  answer_description: string
}

export type Page = TextPage | QuizPage

export type Chapter = {
  id: number
  title: string
  description: string
  image: string
  locked_by_default: boolean
  pages: Page[] | null
}
