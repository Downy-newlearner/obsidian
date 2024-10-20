- RuntimeError: image too small, should be larger than 256x256
    
    Traceback (most recent call last):  
    File "C:\Projects\stablediffusion\scripts\  
    [img2img.py](http://img2img.py/)", line 281, in <module>  
    main()  
    File "C:\Projects\stablediffusion\scripts\  
    [img2img.py](http://img2img.py/)", line 260, in main  
    img = put_watermark(img, wm_encoder)  
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\scripts\  
    [txt2img.py](http://txt2img.py/)", line 209, in put_watermark  
    img = wm_encoder.encode(img, 'dwtDct')  
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\stable_env\Lib\site-packages\imwatermark\  
    [watermark.py](http://watermark.py/)", line 78, in encode  
    raise RuntimeError('image too small, should be larger than 256x256')  
    RuntimeError: image too small, should be larger than 256x256  
    
  
- torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 4.88 GiB. GPU 0 has a total capacity of 12.00 GiB of which 0 bytes is free. Of the allocated memory 13.31 GiB is allocated by PyTorch, and 1.06 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management ([https://pytorch.org/docs/stable/notes/cuda.html#environment-variables](https://pytorch.org/docs/stable/notes/cuda.html#environment-variables))
    
    Traceback (most recent call last):  
    File "C:\Projects\stablediffusion\scripts\  
    [img2img.py](http://img2img.py/)", line 281, in <module>  
    main()  
    File "C:\Projects\stablediffusion\scripts\  
    [img2img.py](http://img2img.py/)", line 226, in main  
    init_latent = model.get_first_stage_encoding(model.encode_first_stage(init_image)) # move to latent space  
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\stable_env\Lib\site-packages\torch\utils\_contextlib.py", line 116, in decorate_context  
    return func(*args, **kwargs)  
    ^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\ldm\models\diffusion\  
    [ddpm.py](http://ddpm.py/)", line 830, in encode_first_stage  
    return self.first_stage_model.encode(x)  
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\ldm\models\  
    [autoencoder.py](http://autoencoder.py/)", line 83, in encode  
    h = self.encoder(x)  
    ^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\stable_env\Lib\site-packages\torch\nn\modules\  
    [module.py](http://module.py/)", line 1553, in _wrapped_call_impl  
    return self._call_impl(*args, **kwargs)  
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\stable_env\Lib\site-packages\torch\nn\modules\  
    [module.py](http://module.py/)", line 1562, in _call_impl  
    return forward_call(*args, **kwargs)  
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    [model.py](http://model.py/)", line 536, in forward  
    h = self.mid.attn_1(h)  
    ^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\stable_env\Lib\site-packages\torch\nn\modules\  
    [module.py](http://module.py/)", line 1553, in _wrapped_call_impl  
    return self._call_impl(*args, **kwargs)  
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\stable_env\Lib\site-packages\torch\nn\modules\  
    [module.py](http://module.py/)", line 1562, in _call_impl  
    return forward_call(*args, **kwargs)  
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    File "C:\Projects\stablediffusion\ldm\modules\diffusionmodules\  
    __[model.py](http://model.py/)__", line 191, in forward  
    w  
    _= torch.bmm(q,k) # b,hw,hw w[b,i,j]=sum_c q[b,i,c]k[b,c,j]  
    ^^^^^^^^^^^^^^  
    torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 4.88 GiB. GPU 0 has a total capacity of 12.00 GiB of which 0 bytes is free. Of the allocated memory 13.31 GiB is allocated by PyTorch, and 1.06 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (  
    [https://pytorch.org/docs/stable/notes/cuda.html#environment-variables](https://pytorch.org/docs/stable/notes/cuda.html#environment-variables))