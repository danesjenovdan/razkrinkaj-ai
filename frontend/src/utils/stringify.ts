import { isRef } from "vue";

function replacer(key: unknown, value: unknown) {
  if (value instanceof Map) {
    return {
      __dataType: "Map",
      entries: Array.from(value.entries()),
    };
  } else {
    return value;
  }
}

function reviver(key: unknown, value: unknown) {
  if (typeof value === "object" && value !== null) {
    if ("__dataType" in value) {
      if (value.__dataType === "Map" && "entries" in value) {
        const mapValue = value as {
          __dataType: "Map";
          entries: [unknown, unknown][];
        };
        return new Map(mapValue.entries);
      }
    }
  }
  return value;
}

export function smartToString(data: unknown): string {
  if (isRef(data)) {
    data = data.value;
  }
  return JSON.stringify(data, replacer);
}

export function smartParse(data: string): unknown {
  return JSON.parse(data, reviver);
}

export function slugify(text: string): string {
  return text
    .toString() // Convert to string
    .toLowerCase() // Convert to lowercase
    .normalize("NFD") // Normalize unicode characters
    .trim() // Remove whitespace from both ends
    .replace(/\s+/g, "-") // Replace spaces with hyphens
    .replace(/[^\w-]+/g, "") // Remove all non-word chars
    .replace(/--+/g, "-") // Replace multiple hyphens with single hyphen
    .replace(/^-+/, "") // Remove leading hyphens
    .replace(/-+$/, ""); // Remove trailing hyphens
}

export function slugifyDot(text: string): string {
  return text
    .toString() // Convert to string
    .toLowerCase() // Convert to lowercase
    .normalize("NFD") // Normalize unicode characters
    .trim() // Remove whitespace from both ends
    .replace(/\s+/g, ".") // Replace spaces with dots
    .replace(/[^\w.]+/g, "") // Remove all non-word chars
    .replace(/\.\.+/g, ".") // Replace multiple dots with single dot
    .replace(/^\.+/, "") // Remove leading dots
    .replace(/\.+$/, ""); // Remove trailing dots
}
