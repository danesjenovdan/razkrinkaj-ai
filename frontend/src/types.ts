export interface PageAnswer {
  correct: boolean
  text: string
}

export interface Page {
  title: string
  text?: string
  type: string
  id: number
  image: string
  image_answer: string
  points: number
  answers: PageAnswer[]
  answer_description: string
}

export interface Chapter {
  title: string
  shortDescription?: string
  description: string
  id: number
  image: string
  locked_by_default: boolean
  pages: Page[]
}
