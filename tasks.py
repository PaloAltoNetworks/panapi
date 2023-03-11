"""Tasks for use with Invoke."""

from invoke import task


# Tests
@task(
    optional=[
        "bandit",
        "format",
        "lint",
        "markdown",
        "all",
    ]
)
def test(
    context,
    bandit=None,
    format=None,
    lint=None,
    markdown=None,
    all=None,
):
    """Run various tests."""
    if bandit:
        context.run(
            "python -m bandit -r .",
        )
    elif format:
        context.run(
            "python -m black .",
        )
    elif lint:
        context.run(
            "python -m flake8 --verbose",
        )
    elif markdown:
        context.run(
            "pymarkdown scan .",
        )
    elif all:
        context.run(
            "python -m bandit -r . &&\n"
            "python -m black . &&\n"
            "python -m flake8 --verbose",
        )
    else:
        context.run(
            "echo 'invoke test --bandit, --format, --lint, or --all ?'",
        )
