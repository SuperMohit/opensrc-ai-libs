"""
Configuration settings for CePO.
"""


DEFAULT_CONFIG = {
    "openai_model": "openai/llama-3.3-70b",
    "temperature": 0.7,
    "max_tokens": 1024,
    "n_executions": 3,
    "confidence_threshold": 7.0,  # Minimum confidence score (0-10) to accept a solution
}


class Config:
    """Configuration manager for CePO."""
   
    def __init__(self, **kwargs):
        self.settings = DEFAULT_CONFIG.copy()
        self.settings.update(kwargs)
    
    def __getitem__(self, key):
        return self.settings.get(key)
    
    def __setitem__(self, key, value):
        self.settings[key] = value
    
    def update(self, **kwargs):
        self.settings.update(kwargs)