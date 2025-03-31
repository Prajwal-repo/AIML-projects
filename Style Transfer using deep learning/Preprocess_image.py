import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import matplotlib.pyplot as plt
import copy

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
    
    def get_features(image, model):
        layers = {
        '0': 'conv_1',
        '5': 'conv_2',
        '10': 'conv_3',
        '19': 'conv_4',
        '28': 'conv_5',
    }
        features = {}
        x = image
        for name, layer in model._modules.items():
            x = layer(x)
            if name in layers:
                features[layers[name]] = x
        return features
    
    content_layers = ['conv_4'] 
    style_layers = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']  

    def content_loss(content_features, target_features):
        return torch.mean((content_features - target_features) ** 2)
    
    def gram_matrix(tensor):
        b, c, h, w = tensor.shape
        tensor = tensor.view(c, h * w)  
        return torch.mm(tensor, tensor.t())  

    
    def style_loss(style_features, target_features):
        loss = 0
        for layer in style_features:
            gram_s = gram_matrix(style_features[layer])
            gram_t = gram_matrix(target_features[layer])
            loss += torch.mean((gram_s - gram_t) ** 2)
        return loss
    
    def total_variation_loss(image):
        return torch.sum(torch.abs(image[:, :, :-1] - image[:, :, 1:])) + \
               torch.sum(torch.abs(image[:, :-1, :] - image[:, 1:, :]))
    
    def train_nst(content_img, style_img, model, num_steps=300, content_weight=1e4, style_weight=1e2):
        target = content_img.clone().requires_grad_(True)  # Image to be optimized
        optimizer = optim.Adam([target], lr=0.003)
    
        content_features = get_features(content_img, model)
        style_features = get_features(style_img, model)

        for step in range(num_steps):
            optimizer.zero_grad()

        target_features = get_features(target, model)

        c_loss = content_loss(content_features['conv_4'], target_features['conv_4'])
        s_loss = style_loss(style_features, target_features)
        tv_loss = total_variation_loss(target)

        total_loss = content_weight * c_loss + style_weight * s_loss + 1e-6 * tv_loss
        total_loss.backward()

        optimizer.step()

        if step % 50 == 0:
            print(f"Step {step}: Total Loss = {total_loss.item():.4f}")

        return target



