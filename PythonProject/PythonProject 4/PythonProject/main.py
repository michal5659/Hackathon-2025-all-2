"""
Main Application Entry Point
AI Multi-Agent Orchestration System
"""
import asyncio
import sys
from pathlib import Path

from PythonProject.agents.simple_ai_agent import get_simple_ai_agent


# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from orchestarator import get_orchestrator


async def main():
    """Main application entry point"""
    try:
        agent = get_simple_ai_agent()

        # שלח prompt ל-LLM
        response = await agent.generate_response(
            prompt="How do I create a new order?",
            context={
                "user_role": "customer",
                "channel": "teams"
            }
        )

        print(response)

        # Get orchestrator instance
        print("main Application started")
        orchestrator = get_orchestrator()

        # Start the orchestration system
        print("Starting orchestrator...")
        await orchestrator.start()

    except KeyboardInterrupt:
        print("Received keyboard interrupt")
    except Exception as e:
        print(f"Application error: {str(e)}")
        raise
    finally:
        print("Application shutdown complete")


def run():
    """Run the application"""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Application stopped by user")
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    print("Application started")
    run()

