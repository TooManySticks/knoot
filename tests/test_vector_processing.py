import asyncio
import numpy as np
from src.vector_processing import EnhancedVectorProcessor

import pytest

@pytest.mark.asyncio
async def test_process():
    processor = EnhancedVectorProcessor()
    vectors, quality = await processor.process("Test input", domain="general")
    # Check that quality is a float and vectors have expected shape (e.g., 384 components)
    assert isinstance(quality, float)
    assert isinstance(vectors, np.ndarray)
    assert vectors.shape[0] == 384
