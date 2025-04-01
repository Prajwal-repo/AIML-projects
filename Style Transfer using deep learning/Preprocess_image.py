import torch
import torch.optim as optim
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
from loss_function import loss_func
from features import feature

class Process_Image:
    def load_image(img_path, max_size=512):
        image = Image.open(img_path).convert("RGB")
        size = max(image.size)
        if size > max_size:
            image = transforms.Resize((max_size, max_size))(image)
 
        transform = transforms.Compose([
        transforms.ToTensor(), 
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
        return transform(image).unsqueeze(0)  
    
    def gram_matrix(tensor):
        b, c, h, w = tensor.shape
        tensor = tensor.view(c, h * w)  
        return torch.mm(tensor, tensor.t())   
    
    def train_nst(content_img, style_img, model, num_steps=300, content_weight=1e4, style_weight=1e2):
        target = content_img.clone().requires_grad_(True) 
        optimizer = optim.Adam([target], lr=0.003)
    
        content_features = feature.get_features(content_img, model)
        style_features = feature.get_features(style_img, model)

        for step in range(num_steps):
            optimizer.zero_grad()

        target_features = feature.get_features(target, model)

        c_loss = loss_func.content_loss(content_features['conv_4'], target_features['conv_4'])
        s_loss = loss_func.style_loss(style_features, target_features)
        tv_loss = loss_func.total_variation_loss(target)

        total_loss = content_weight * c_loss + style_weight * s_loss + 1e-6 * tv_loss
        total_loss.backward()

        optimizer.step()

        if step % 50 == 0:
            print(f"Step {step}: Total Loss = {total_loss.item():.4f}")

        return target

    def show_image(tensor):
        image = tensor.clone().detach().squeeze(0)  
        unnormalize = transforms.Normalize(mean=[-2.118, -2.036, -1.804], std=[4.367, 4.464, 4.444])
        image = unnormalize(image).clamp(0, 1)  
        image_np = image.permute(1, 2, 0).cpu().numpy() 

        return image_np