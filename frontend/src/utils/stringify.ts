import { isRef } from 'vue'

function replacer(key: unknown, value: unknown) {
  if (value instanceof Map) {
    return {
      __dataType: 'Map',
      entries: Array.from(value.entries()),
    }
  } else {
    return value
  }
}

function reviver(key: unknown, value: unknown) {
  if (typeof value === 'object' && value !== null) {
    if ('__dataType' in value) {
      if (value.__dataType === 'Map' && 'entries' in value) {
        const mapValue = value as {
          __dataType: 'Map'
          entries: [unknown, unknown][]
        }
        return new Map(mapValue.entries)
      }
    }
  }
  return value
}

export function smartToString(data: unknown): string {
  if (isRef(data)) {
    data = data.value
  }
  return JSON.stringify(data, replacer)
}

export function smartParse(data: string): unknown {
  return JSON.parse(data, reviver)
}
