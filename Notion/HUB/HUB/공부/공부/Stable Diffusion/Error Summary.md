- ModuleNotFoundError: No module named 'ldm'
    
    (stablediffusion_) PS C:\Projects\stablediffusion> python scripts/txt2img.py --prompt "a professional photograph of an astronaut riding a horse" --ckpt "C:\Projects\stablediffusion\checkpoints\v2-1_768-ema-pruned.ckpt" --config configs/stable-diffusion/v2-inference-v.yaml --H 768 --W 768 --outdir "C:\Projects"  
    Traceback (most recent call last):  
    File "C:\Projects\stablediffusion\scripts\  
    [txt2img.py](http://txt2img.py/)", line 16, in <module>  
    from ldm.util import instantiate_from_config  
    ModuleNotFoundError: No module named 'ldm'  
    
[[HUB/HUB/공부/공부/Stable Diffusion/Error Summary/해결|해결]]
  
- RuntimeError: expected scalar type BFloat16 but found Float
    
    Traceback (most recent call last):  
    File "C:\Projects\stablediffusion\scripts\  
    [txt2img.py](http://txt2img.py/)", line 394, in <module>  
    main(opt)  
    File "C:\Projects\stablediffusion\scripts\  
    [txt2img.py](http://txt2img.py/)", line 353, in main  
    samples, _ = sampler.sample(S=opt.steps,  
    File "C:\Projects\stablediffusion_\lib\site-packages\torch\autograd\grad_mode.py", line 27, in decorate_context  
    return func(*args, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\models\diffusion\  
    [ddim.py](http://ddim.py/)", line 104, in sample  
    samples, intermediates = self.ddim_sampling(conditioning, size,  
    File "C:\Projects\stablediffusion_\lib\site-packages\torch\autograd\grad_mode.py", line 27, in decorate_context  
    return func(*args, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\models\diffusion\  
    [ddim.py](http://ddim.py/)", line 164, in ddim_sampling  
    outs = self.p_sample_ddim(img, cond, ts, index=index, use_original_steps=ddim_use_original_steps,  
    File "C:\Projects\stablediffusion_\lib\site-packages\torch\autograd\grad_mode.py", line 27, in decorate_context  
    return func(*args, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\models\diffusion\  
    [ddim.py](http://ddim.py/)", line 212, in p_sample_ddim  
    model_uncond, model_t = self.model.apply_model(x_in, t_in, c_in).chunk(2)  
    File "C:\Projects\stablediffusion\ldm\models\diffusion\  
    [ddpm.py](http://ddpm.py/)", line 858, in apply_model  
    x_recon = self.model(x_noisy, t, **cond)  
    File "C:\Projects\stablediffusion_\lib\site-packages\torch\nn\modules\  
    [module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\models\diffusion\  
    __[ddpm.py](http://ddpm.py/)__", line 1335, in forward  
    out = self.diffusion_model(x, t, context=cc)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[openaimodel.py](http://openaimodel.py/)__", line 797, in forward  
    h = module(h, emb, context)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[openaimodel.py](http://openaimodel.py/)__", line 84, in forward  
    x = layer(x, context)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\  
    __[attention.py](http://attention.py/)__", line 327, in forward  
    x = self.norm(x)  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[openaimodel.py](http://openaimodel.py/)__", line 84, in forward  
    x = layer(x, context)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\  
    __[attention.py](http://attention.py/)__", line 327, in forward  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[openaimodel.py](http://openaimodel.py/)__", line 84, in forward  
    x = layer(x, context)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[openaimodel.py](http://openaimodel.py/)__", line 84, in forward  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[openaimodel.py](http://openaimodel.py/)__", line 84, in forward  
    x = layer(x, context)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[openaimodel.py](http://openaimodel.py/)__", line 84, in forward  
    x = layer(x, context)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[openaimodel.py](http://openaimodel.py/)__", line 84, in forward  
    x = layer(x, context)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion\ldm\modules\  
    __[attention.py](http://attention.py/)__", line 327, in forward  
    x = self.norm(x)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[module.py](http://module.py/)", line 1130, in _call_impl  
    return forward_call(*input, **kwargs)  
    File "C:\Projects\stablediffusion  
    _\lib\site-packages\torch\nn\modules\[normalization.py](http://normalization.py/)", line 272, in forward  
    return F.group_norm(  
    File "C:\Projects\stablediffusion_\lib\site-packages\torch\nn\  
    [functional.py](http://functional.py/)", line 2516, in group_norm  
    return torch.group_norm(input, num_groups, weight, bias, eps, torch.backends.cudnn.enabled)  
    RuntimeError: expected scalar type BFloat16 but found Float  
    
[[해결 2]]
  
DeprecationWarning: torch.get_autocast_gpu_dtype() is deprecated. Please use torch.get_autocast_dtype('cuda') instead. (Triggered internally at C:\actions-runner\_work\pytorch\pytorch\builder\windows\pytorch\torch\csrc\autograd\init.cpp:734.)