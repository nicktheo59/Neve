# Getting Started with Neve AI

This guide will help you get started with using the Neve AI framework for your projects.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.11 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Installation

### Quick Installation

The easiest way to install Neve AI is via pip:

```bash
pip install Neve-ai
```

### Development Installation

If you want to contribute to Neve AI or use the latest development version:

```bash
# Clone the repository
git clone https://github.com/Neve-ai/Neve.git
cd Neve

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Configuration

After installation, you'll need to configure Neve AI with your API keys:

1. Create a configuration file:

```bash
Neve init
```

2. Edit the generated `.Neve/config.yaml` file with your API keys:

```yaml
llm:
  provider: openai
  api_key: your_openai_api_key
  model: gpt-4o

# Optional: Configure other providers
anthropic:
  api_key: your_anthropic_api_key
```

## Your First Neve AI Project

### Simple Question Answering

Create a file named `simple_question.py`:

```python
from Neve import Agent

# Create a single agent
agent = Agent()

# Ask a simple question
response = agent.run("What is the capital of France?")
print(response)
```

Run the script:

```bash
python simple_question.py
```

### Web Search Example

Create a file named `web_search.py`:

```python
from Neve import Agent
from Neve.tools import SearchTool

# Create an agent with search capabilities
agent = Agent(tools=[SearchTool()])

# Search for information
response = agent.run("Find the latest research on quantum computing")
print(response)
```

Run the script:

```bash
python web_search.py
```

### Multi-Agent Collaboration

Create a file named `multi_agent.py`:

```python
from Neve import Society, Agent

# Create specialized agents
researcher = Agent(role="researcher")
analyst = Agent(role="analyst")
writer = Agent(role="writer")

# Create a society of agents
society = Society(agents=[researcher, analyst, writer])

# Execute a complex task with collaboration
response = society.run(
    "Research the impact of artificial intelligence on healthcare, " 
    "analyze the findings, and write a comprehensive report"
)
print(response)
```

Run the script:

```bash
python multi_agent.py
```

## Using the Command-Line Interface

Neve AI comes with a powerful command-line interface:

```bash
# Run a simple task
Neve run "What is the population of Tokyo?"

# Run in interactive mode
Neve interactive

# Run with a specific configuration file
Neve run --config custom_config.yaml "Summarize this article: https://example.com/article"
```

## Next Steps

- Explore the [Documentation](https://Neve-ai.github.io/docs) for more detailed information
- Check out the [Examples](https://github.com/Neve-ai/Neve/tree/main/examples) directory for more use cases
- Join our [Community](https://discord.gg/Neve-ai) to connect with other users and developers
- Consider [Contributing](https://github.com/Neve-ai/Neve/blob/main/CONTRIBUTING.md) to the project

## Getting Help

If you encounter any issues or have questions:

- Check the [FAQ](https://Neve-ai.github.io/docs/faq)
- Search for existing [Issues](https://github.com/Neve-ai/Neve/issues)
- Ask for help in our [Discord](https://discord.gg/Neve-ai) community
- Open a new [Issue](https://github.com/Neve-ai/Neve/issues/new) if you found a bug
