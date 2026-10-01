from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import torch


def main() -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is unavailable in the repository's shared uv environment")
    if torch.cuda.device_count() < 1:
        raise RuntimeError("no CUDA device is visible")

    devices: list[dict[str, int | float | str]] = []
    for index in range(torch.cuda.device_count()):
        device = torch.device(f"cuda:{index}")
        values = torch.arange(8, dtype=torch.float32, device=device)
        total = values.sum()
        torch.cuda.synchronize(device)
        devices.append(
            {
                "index": index,
                "name": torch.cuda.get_device_name(index),
                "tensor_device": str(values.device),
                "sum": total.item(),
            }
        )

    result = {
        "project_root": str(Path.cwd()),
        "python": sys.executable,
        "virtual_env": os.environ.get("VIRTUAL_ENV"),
        "torch": torch.__version__,
        "torch_cuda_build": torch.version.cuda,
        "cuda_available": torch.cuda.is_available(),
        "visible_device_count": torch.cuda.device_count(),
        "devices": devices,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
