#!/usr/bin/env python
"""
CePO Framework - Main execution script

This script provides a command-line interface to run the CePO pipeline
on user-provided problems and display the results.
"""

import os
import sys
import time
import argparse
import logging
from pathlib import Path
from cepo.pipeline import CePOPipeline
from cepo.utils.logging import setup_logging


current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="CePO: Chain-of-thought Execution with Plan Optimization")
    
    # Required arguments
    parser.add_argument("query", nargs="?", help="The problem to solve")
    
    # Optional arguments
    parser.add_argument("-f", "--file", help="Path to a file containing the problem")
    parser.add_argument("-m", "--model", default="openai/llama-3.3-70b", help="Cerebras model to use (default: llama-3.3-70b)")
    parser.add_argument("-e", "--executions", type=int, default=3, help="Number of executions (default: 3)")
    parser.add_argument("-t", "--temperature", type=float, default=0.7, help="Temperature (default: 0.7)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-o", "--output", help="Save results to this file")
    
    return parser.parse_args()

def get_query(args):
    """Get the query from arguments or file."""
    if args.file:
        try:
            with open(args.file, 'r') as f:
                return f.read().strip()
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            sys.exit(1)
    elif args.query:
        return args.query
    else:
        print("Error: Please provide a query either directly or via a file (-f)")
        sys.exit(1)

def get_api_key():
    """Get OpenAI API key from environment."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Please set it using: export OPENAI_API_KEY=your_api_key")
        sys.exit(1)
    return api_key

def display_result(result, verbose=False):
    """Display the result of the CePO pipeline."""
    # Print query
    print("\n📝 QUERY:")
    print(result.query)
    
    # Print plan
    if verbose:
        print("\n🔍 PLAN:")
        for i, step in enumerate(result.plan.steps):
            print(f"{i+1}. {step}")
    
    # Print summary
    print("\n📊 SUMMARY:")
    print(f"- Generated {len(result.solutions)} solutions")
    print(f"- Found {len(result.analysis.inconsistencies)} inconsistencies")
    print(f"- Detected {len(result.analysis.errors)} potential errors")
    print(f"- Processing time: {result.processing_time:.2f} seconds")
    
    # Print selected solution
    print("\n✅ BEST SOLUTION:")
    print(f"Confidence: {result.selection.confidence}/10")
    if verbose:
        print(f"Explanation: {result.selection.explanation}")
    print("\n" + "=" * 80)
    print(result.selection.solution.content)
    print("=" * 80)
    
    # Print analysis if verbose
    if verbose:
        print("\n🔎 ANALYSIS:")
        if result.analysis.inconsistencies:
            print("\nInconsistencies:")
            for inc in result.analysis.inconsistencies:
                print(f"- {inc}")
        
        if result.analysis.errors:
            print("\nErrors:")
            for err in result.analysis.errors:
                print(f"- {err}")
        
        if result.analysis.corrections:
            print("\nCorrections:")
            for corr in result.analysis.corrections:
                print(f"- {corr}")

def save_results(result, output_file):
    """Save results to a file."""
    try:
        with open(output_file, 'w') as f:
            f.write(f"QUERY:\n{result.query}\n\n")
            
            f.write("PLAN:\n")
            for i, step in enumerate(result.plan.steps):
                f.write(f"{i+1}. {step}\n")
            
            f.write("\nANALYSIS:\n")
            f.write("Inconsistencies:\n")
            for inc in result.analysis.inconsistencies:
                f.write(f"- {inc}\n")
            
            f.write("\nErrors:\n")
            for err in result.analysis.errors:
                f.write(f"- {err}\n")
            
            f.write("\nBEST SOLUTION:\n")
            f.write(f"Confidence: {result.selection.confidence}/10\n")
            f.write(f"Explanation: {result.selection.explanation}\n\n")
            f.write(f"{result.selection.solution.content}\n")
        
        print(f"\nResults saved to {output_file}")
    except Exception as e:
        print(f"Error saving results: {str(e)}")

def main():
    """Main function to run the CePO pipeline."""
    # Parse arguments
    args = parse_arguments()
    
    # Set up logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logger = setup_logging(level=log_level)
    
    # Get API key and query
    api_key = get_api_key()
    query = get_query(args)
    
    print("\nCePO: Chain-of-thought Execution with Plan Optimization")
    print("=" * 60)
    print(f"Model: {args.model}")
    print(f"Executions: {args.executions}")
    print(f"Temperature: {args.temperature}")
    
    # Initialize the CePO pipeline
    try:
        pipeline = CePOPipeline(
            openai_api_key=api_key,
            openai_model=args.model,
            temperature=args.temperature,
            n_executions=args.executions
        )
        
        # Run the pipeline
        print("\nRunning CePO pipeline... (this may take a few minutes)")
        start_time = time.time()
        result = pipeline.run(query)
        
        # Display results
        display_result(result, args.verbose)
        
        # Save results if requested
        if args.output:
            save_results(result, args.output)
            
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=args.verbose)
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()