import type { ImageDescription, Page } from '@/types'
import { apiUrl } from '@/utils/api'

export function fixLocalUrl(url: string) {
  if (!url.startsWith('http')) {
    return `${apiUrl}${url}`
  }
  return url
}

export async function preloadImageUrl(url: string): Promise<HTMLImageElement> {
  console.info('[preload] start:', url)

  return new Promise((resolve, reject) => {
    const img = new Image()
    img.onload = () => {
      console.info('[preload] image:', url)
      resolve(img)
    }
    img.onerror = reject
    img.src = fixLocalUrl(url)
  })
}

export async function preloadImage(
  image: ImageDescription,
  preloadOriginal = false,
) {
  if (!image.thumbnail_preloaded && image.thumbnail_url) {
    preloadImageUrl(image.thumbnail_url).then(() => {
      image.thumbnail_preloaded = true
    })
  }

  if (!image.preloaded && image.url) {
    preloadImageUrl(image.url).then(() => {
      image.preloaded = true
    })
  }

  if (preloadOriginal && !image.original_preloaded && image.original_url) {
    preloadImageUrl(image.original_url).then(() => {
      image.original_preloaded = true
    })
  }
}

export async function preloadImages(
  images: ImageDescription[],
  preloadOriginal = false,
) {
  for (const image of images) {
    preloadImage(image, preloadOriginal)
  }
}

export async function preloadPageImages(page: Page, preloadOriginal = false) {
  if (page.type === 'text') {
    preloadImages(page.text_images, preloadOriginal)
  } else if (page.type === 'quiz') {
    if (page.image) {
      preloadImage(page.image, preloadOriginal)
    }
    if (page.image_answer) {
      preloadImage(page.image_answer, preloadOriginal)
    }
    preloadImages(page.answer_description_images, preloadOriginal)
  }
}
