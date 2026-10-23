# Security policy

## Scope

Zentrix AI is a learning and portfolio project. Do not use it to process confidential data or credentials belonging to other people.

## Reporting a concern

Please do not publish API keys, tokens, passwords, session data, or sensitive screenshots in a public issue or pull request. Use GitHub's private vulnerability reporting feature if it is enabled for this repository; otherwise contact the maintainer through the [GitHub profile](https://github.com/Hariharans1971) with a concise description and safe reproduction steps.

## Credential handling

- Keep provider keys in environment variables or a local secrets file excluded from Git.
- Treat any credential committed to a public repository as exposed: revoke or rotate it with the issuer first.
- Removing a file from the latest commit does not remove it from prior Git history. History cleanup must be reviewed separately and verified with a history-aware scan.
- Do not paste secrets into logs, screenshots, issues, or support requests.
- Use synthetic data only; this project is not designed for confidential or regulated information.
