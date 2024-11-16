1. github에 코드 올리기
2. img2img 오류 해결하기
	C:\Projects\memoji\stablediffusion\scripts\img2img.py:56: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. 
	
	It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). 
	
	In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  pl_sd = torch.load(ckpt, map_location="cpu")

3. ldm -> stablediffusion1 -> stablediffusion2 구조 이해하기
4. Sweep & LoRA 적용하기
	[LoRA](https://www.youtube.com/watch?v=e7r_xT-sM4o)