import BEN2
from PIL import Image
import torch


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

file = "./image.png" # input image

model = BEN2.BEN_Base().to(device).eval() #init pipeline

model.loadcheckpoints("./BEN_Base2.pth")
image = Image.open(file)
mask, foreground = model.inference(image)

mask.save("./mask.png")
foreground.save("./foreground.png")
