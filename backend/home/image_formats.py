from django.utils.html import escape
from django.utils.safestring import mark_safe
from wagtail.images.formats import (
    Format,
    register_image_format,
    unregister_image_format,
)
from wagtail.images.shortcuts import get_renditions_or_not_found

# Unregister the default image formats
unregister_image_format("left")
unregister_image_format("right")
unregister_image_format("fullwidth")

THUMBNAIL_RENDITION_NAME = "width-50|format-jpeg|jpegquality-30"
REGULAR_RENDITION_NAME = "width-800|format-jpeg|jpegquality-60"
ICON_RENDITION_NAME = "width-218|format-jpeg|jpegquality-60"


class FormatWithThumbnail(Format):
    def __init__(self, name, label, classname, filter_spec):
        super().__init__(name, label, classname, filter_spec)
        self.thumbnail_filter_spec = THUMBNAIL_RENDITION_NAME

    def image_to_html(self, image, alt_text, extra_attributes=None):
        if extra_attributes is None:
            extra_attributes = {}

        renditions = get_renditions_or_not_found(
            image, [self.thumbnail_filter_spec, self.filter_spec]
        )

        extra_attributes["alt"] = escape(alt_text)
        if self.classname:
            extra_attributes["class"] = "%s" % escape(self.classname)

        if renditions[self.filter_spec].file.url:
            extra_attributes["data-src"] = renditions[self.filter_spec].file.url

        extra_attributes["width"] = image.width
        extra_attributes["height"] = image.height
        extra_attributes["style"] = f"aspect-ratio: {image.width} / {image.height};"

        img_tag = renditions[self.thumbnail_filter_spec].img_tag(extra_attributes)
        return mark_safe(f'<div class="thumbnail-image"><div>{img_tag}</div></div>')


# Register new image formats
register_image_format(
    FormatWithThumbnail(
        "fullwidth",
        "Full width",
        "richtext-image full-width is-thumbnail",
        REGULAR_RENDITION_NAME,
    )
)
