
import torch 

class loss_func:
    def content_loss(content_features, target_features):
        return torch.mean((content_features - target_features) ** 2)

    def style_loss(style_features, target_features):
        from Preprocess_image import Process_Image
        loss = 0
        for layer in style_features:
            gram_s = Process_Image.gram_matrix(style_features[layer])
            gram_t = Process_Image.gram_matrix(target_features[layer])
            loss += torch.mean((gram_s - gram_t) ** 2)
        return loss
    
    def total_variation_loss(image):
        return torch.sum(torch.abs(image[:, :, :-1] - image[:, :, 1:])) + \
               torch.sum(torch.abs(image[:, :-1, :] - image[:, 1:, :]))