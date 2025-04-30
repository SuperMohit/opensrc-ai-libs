import os
import time
import logging
from typing import Optional, Dict, Any
from openai import OpenAI
import dspy

logger = logging.getLogger(__name__)


class OpenAIClientLM(dspy.LM):
    """DSPy language model implementation backed by OpenAI."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "llama-3.3-70b", 
                 temperature: float = 0.7, max_tokens: int = 100000, 
                 retry_attempts: int = 3, retry_delay: float = 1.5):
        """
        Initialize the OpenAI client.
        
        Args:
            api_key (str, optional): OpenAI API key
            model (str, optional): Model identifier
            temperature (float, optional): Sampling temperature
            max_tokens (int, optional): Maximum tokens to generate
            retry_attempts (int, optional): Number of retry attempts
            retry_delay (float, optional): Delay between retries in seconds
        """
        super().__init__(
            api_key=api_key,
            model=model,
            temperature=temperature,
            api_base="https://api.cerebras.ai/v1",
            model_type="chat",
            max_tokens=max_tokens,
            num_retries=retry_attempts,
        )