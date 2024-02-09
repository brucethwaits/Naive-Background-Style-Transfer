from naive_background_style_transfer import NaiveBackgroundStyleTransfer
from naive_background_style_transfer.semantic_segmentation import SemanticSegmentation
# content = "Input_Images/Content/portrait.jpg"
content = "Input_Images/Content/2d1b589f-64d5-4713-9c60-e55a18a05e70.jpg"
# style = "Input_Images/Style/scream.jpg"
style = "Input_Images/Style/Starry_Night.jpg"
nbst = NaiveBackgroundStyleTransfer(number_of_epochs=100, verbose = True)
nbst.perform(content, style)
nbst.generate_gif(speed=1.5)
