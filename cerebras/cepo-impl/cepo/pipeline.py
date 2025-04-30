import time
import dspy
from typing import Optional, Dict, Any, List
import logging

from cepo.config import Config
from cepo.models import CePOResult, Plan, Solution, Analysis, Selection
from cepo.plan_gen.modules import PlanGenerator
from cepo.executor.modules import PlanExecutor
from cepo.analysis.modules import ConsistencyAnalyzer
from cepo.selection.modules import ResponseSelector
from cepo.utils.openai_client import OpenAIClientLM


logger = logging.getLogger(__name__)


class CePOPipeline:
    """
    CePO: Chain-of-thought Execution with Plan Optimization pipeline.
    
    This pipeline implements:
    1. LLM-based step-by-step planning
    2. Multiple executions of the plan
    3. Inconsistency analysis across executions
    4. Best-of-N selection with confidence scoring
    """
    
    def __init__(self, openai_api_key: Optional[str] = None, **config_kwargs):
        """
        Initialize the CePO pipeline.
        
        Args:
            openai_api_key (str, optional): OpenAI API key
            **config_kwargs: Additional configuration options
        """
        self.config = Config(**config_kwargs)

        lm = OpenAIClientLM(
            api_key=openai_api_key,
            model=self.config["openai_model"],
            temperature=self.config["temperature"],
        )
        
        dspy.configure(lm=lm)
        
        self.plan_generator = PlanGenerator()
        self.plan_executor = PlanExecutor()
        self.analyzer = ConsistencyAnalyzer()
        self.selector = ResponseSelector()
        
        logger.info(f"CePO pipeline initialized with model {self.config['openai_model']}")
    
    def run(self, query: str, n_executions: Optional[int] = None) -> CePOResult:
        """
        Run the complete CePO pipeline on a query.
        
        Args:
            query (str): The problem to solve
            n_executions (int, optional): Number of plan executions (defaults to config value)
            
        Returns:
            CePOResult: Complete pipeline result
        """
        start_time = time.time()
        
        if n_executions is None:
            n_executions = self.config["n_executions"]
        
        logger.info(f"Running CePO pipeline on query: '{query[:50]}...' with {n_executions} executions")
        
        try:
            logger.info("Step 1: Generating plan")
            plan = self.plan_generator(query)
            
            logger.info(f"Step 2: Executing plan {n_executions} times")
            solutions = self.plan_executor(query, plan, n_executions)
            
            logger.info("Step 3: Analyzing solutions for inconsistencies")
            analysis = self.analyzer(query, solutions)
            
            logger.info("Step 4: Selecting best solution")
            selection = self.selector(query, solutions, analysis)
            
            processing_time = time.time() - start_time
            logger.info(f"CePO pipeline completed in {processing_time:.2f} seconds")
            
            return CePOResult(
                query=query,
                plan=plan,
                solutions=solutions,
                analysis=analysis,
                selection=selection,
                processing_time=processing_time
            )
        
        except Exception as e:
            logger.error(f"Error in CePO pipeline: {str(e)}", exc_info=True)
            raise
    
    def generate_plan(self, query: str) -> Plan:
        """
        Generate a plan for solving a problem.
        
        Args:
            query (str): The problem to solve
            
        Returns:
            Plan: The generated plan
        """
        return self.plan_generator(query)
    
    def execute_plan(self, query: str, plan: Plan, n_executions: Optional[int] = None) -> List[Solution]:
        """
        Execute a plan multiple times.
        
        Args:
            query (str): The original problem
            plan (Plan): The plan to execute
            n_executions (int, optional): Number of executions
            
        Returns:
            List[Solution]: The generated solutions
        """
        if n_executions is None:
            n_executions = self.config["n_executions"]
        
        return self.plan_executor(query, plan, n_executions)
    
    def analyze_solutions(self, query: str, solutions: List[Solution]) -> Analysis:
        """
        Analyze solutions for inconsistencies and errors.
        
        Args:
            query (str): The original problem
            solutions (List[Solution]): The solutions to analyze
            
        Returns:
            Analysis: Analysis of the solutions
        """
        return self.analyzer(query, solutions)
    
    def select_solution(self, query: str, solutions: List[Solution], analysis: Analysis) -> Selection:
        """
        Select the best solution.
        
        Args:
            query (str): The original problem
            solutions (List[Solution]): The solutions to choose from
            analysis (Analysis): Analysis of the solutions
            
        Returns:
            Selection: The selected solution with confidence
        """
        return self.selector(query, solutions, analysis)