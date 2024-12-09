export type ImageDescription = {
  svg?: boolean
  thumbnail_url?: string
  original_url: string
  url: string
  alt: string
  width: number
  height: number
  // preload info not from api
  original_preloaded?: boolean
  thumbnail_preloaded?: boolean
  preloaded?: boolean
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
  text_images: ImageDescription[]
  button_text: string
}

export type QuizPage = BasePage & {
  type: 'quiz'
  image: ImageDescription | null
  image_answer: ImageDescription | null
  question: string
  answers: PageAnswer[]
  points: number
  answer_description: string
  answer_description_images: ImageDescription[]
  button_text: string
}

export type Page = TextPage | QuizPage

export type Chapter = {
  id: number
  title: string
  description: string
  image: ImageDescription | null
  locked_by_default: boolean
  is_feedback: boolean
  pages: Page[] | null
}
