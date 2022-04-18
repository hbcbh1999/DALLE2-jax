from typing import List

import numpy as onp
from jax import random, jit, nn, lax, numpy as np
from jax.numpy import einsum

from equinox import Module, static_field
from einops import rearrange, repeat

class DALLE2(Module):
    pass
