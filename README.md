# pwsa-jobs-api

An API for scraping and serving job listings from the Pittsburgh Water & Sewer Authority website.

## Getting Started

### Prerequisites

- Python 3.6+
- Virtualenv

### Installation

**Disclaimer** This project is currently a non-production version!

1. **Clone the repository**:

   ```sh
   git clone https://github.com/jtroussard/pwsa-jobs-api.git
   cd pwsa-jobs-api
   ```

2. **Set up environment and install dependencies**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Start the server**:
   ```sh
   python app.py
   ```

## Usage

Currently this is a non-production application. Eventually it will be design to be setup as a plug in service for a larger application.

## Running Tests

__Requires project dependencies be installed__

1. **Run test command**
```sh
pytest tests/
```


## Contribution Guidelines

Please feel free to fork, contribute, redesign, build off from.

### How to Contribute

1. **Fork the Repository**:
   - Navigate to the repository on GitHub and click the "Fork" button to create a copy of the repository under your GitHub account.

2. **Clone the Repository**:
   - Clone the forked repository to your local machine using the command:
     ```sh
     git clone https://github.com/your-username/pwsa-jobs-api.git
     cd pwsa-jobs-api
     ```

3. **Create a Branch**:
   - Create a new branch for your feature or bug fix:
     ```sh
     git checkout -b feature/your-feature-name
     ```

4. **Make Changes**:
   - Make your changes to the codebase. Ensure that your code follows the existing coding style and conventions.

5. **Commit Changes**:
   - Commit your changes with a descriptive commit message:
     ```sh
     git add .
     git commit -m "Add feature: your feature description"
     ```

6. **Push Changes**:
   - Push your changes to your forked repository:
     ```sh
     git push origin feature/your-feature-name
     ```

7. **Create a Pull Request**:
   - Navigate to the original repository on GitHub and click the "New Pull Request" button.
   - Select the branch you just pushed from your forked repository and submit the pull request.
   - Provide a detailed description of your changes in the pull request.

### Code of Conduct

- **Be Respectful**: Treat everyone with respect. Harassment, discrimination, and offensive language will not be tolerated.
- **Provide Constructive Feedback**: Offer constructive feedback and be open to receiving it.
- **Follow the Coding Standards**: Adhere to the coding standards and best practices defined in the repository.

### Reporting Issues

- **Check Existing Issues**: Before creating a new issue, check if the issue already exists.
- **Create a New Issue**: If the issue does not exist, create a new issue with a clear title and detailed description.
- **Provide Context**: Provide as much context as possible, including steps to reproduce the issue, expected behavior, and any relevant screenshots or logs.

