# =============================================================================
#         PLACEHOLDER METHODS TO TRANSFORM AN IMAGE
#           This version simply changes the image to grayscale
# =============================================================================

from PIL import Image

def run_style_transfer(img):
    image = Image.open(img.document)
    generatedImage = image.convert(mode='L')
    generatedImage.save('L.png')
    
    return generatedImage
    