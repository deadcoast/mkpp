# Contributing to milk++

> **Navigation**: [← Back to README](README.md) | [Development Guide](Docs/development.md) | [Command Reference](Docs/command_reference.md)

Thank you for your interest in contributing to milk++! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Process](#contributing-process)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Issues and Bug Reports](#issues-and-bug-reports)

## Code of Conduct

This project adheres to a code of conduct that ensures a welcoming environment for all contributors. Please be respectful and constructive in all interactions.

## Getting Started

### Prerequisites

- Python 3.7+
- Git
- Windows 7+ (for testing)
- Notepad++ (for testing)

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/mkpp.git
   cd mkpp
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install in development mode**:
   ```bash
   pip install -e .
   ```

5. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Contributing Process

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Follow the [Code Style](#code-style) guidelines
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Test the CLI
mkpp --help

# Test specific functionality
mkpp install test-theme.xml
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "Add: Brief description of your changes"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Code Style

### Python Code

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

### Example

```python
def install_theme(theme_path: str, custom_name: str = None) -> bool:
    """
    Install a theme file to Notepad++ themes directory.

    Args:
        theme_path: Path to the theme XML file
        custom_name: Optional custom name for the theme

    Returns:
        bool: True if installation successful, False otherwise
    """
    # Implementation here
    pass
```

## Testing

### Manual Testing

1. **Test theme installation**:
   ```bash
   mkpp install path/to/theme.xml
   ```

2. **Test Git repository installation**:
   ```bash
   mkpp install https://github.com/user/repo.git
   ```

3. **Test batch operations**:
   ```bash
   mkpp scan path/to/themes/folder
   ```

### Automated Testing

We're working on adding automated tests. For now, please test manually and report any issues.

## Documentation

### Updating Documentation

- Update `README.md` for user-facing changes
- Update `Docs/` folder for technical documentation
- Add examples for new features
- Keep installation instructions current

### Documentation Structure

```
Docs/
├── command_reference.md    # CLI command documentation
├── development.md          # Development setup and technical details
└── configuration_file.md   # Configuration options
```

## Issues and Bug Reports

### Reporting Issues

When reporting issues, please include:

1. **Operating System**: Windows version
2. **Python Version**: `python --version`
3. **Notepad++ Version**: Version number
4. **Steps to Reproduce**: Detailed steps
5. **Expected Behavior**: What should happen
6. **Actual Behavior**: What actually happens
7. **Error Messages**: Full error output

### Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass (when available)
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] Manual testing completed
- [ ] No breaking changes
- [ ] Backward compatibility maintained

## Checklist
- [ ] Code follows project style
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No merge conflicts
```

## Development Workflow

### Branch Naming

- `feature/description`: New features
- `bugfix/description`: Bug fixes
- `docs/description`: Documentation updates
- `refactor/description`: Code refactoring

### Commit Messages

Use clear, descriptive commit messages:

```
Add: Theme validation before installation
Fix: Handle missing Notepad++ directory gracefully
Update: Improve error messages for Git operations
```

## Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Code Review**: All PRs receive thorough code review

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to milk++! 🎉

---

## Related Documentation

- **[README](README.md)** - Project overview and quick start
- **[Development Guide](Docs/development.md)** - Technical setup and troubleshooting
- **[Command Reference](Docs/command_reference.md)** - Complete CLI documentation
- **[Configuration Guide](Docs/configuration_file.md)** - Configuration options
