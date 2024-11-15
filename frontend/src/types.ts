export type ImageDescription = {
  url: string
  alt: string
  width: number
  height: number
}

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
  image: ImageDescription | null
  image_answer: ImageDescription | null
  answers: PageAnswer[]
  points: number
  answer_description: string
  button_text: string
}

export type Page = TextPage | QuizPage

export type Chapter = {
  id: number
  title: string
  description: string
  image: ImageDescription | null
  locked_by_default: boolean
  pages: Page[] | null
}
