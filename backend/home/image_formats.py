from wagtail.images.formats import (
    Format,
    register_image_format,
    unregister_image_format,
)

# Unregister the default image formats
unregister_image_format("left")
unregister_image_format("right")

# TODO:
# unregister_image_format("fullwidth")

# Register new image formats
# register_image_format(Format('fullwidth', 'Full width', 'richtext-image full-width', 'max-1200x1200'))
