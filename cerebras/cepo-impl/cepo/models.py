from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Plan:
    """A structured plan with steps to solve a problem."""
    steps: List[str]
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Solution:
    """A solution produced by executing a plan."""
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Analysis:
    """Analysis of multiple solutions for consistency and errors."""
    inconsistencies: List[str]
    errors: List[str]
    corrections: List[str]
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Selection:
    """A selected solution with confidence score and explanation."""
    solution: Solution
    confidence: float  
    explanation: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CePOResult:
    """Complete result of the CePO pipeline."""
    query: str
    plan: Plan
    solutions: List[Solution]
    analysis: Analysis
    selection: Selection
    processing_time: float