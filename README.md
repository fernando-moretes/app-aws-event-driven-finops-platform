# AWS Event-Driven FinOps Platform

A realistic reference architecture for an event-driven banking platform on AWS, combining domain events, service selection, FinOps, security and observability.

## Live portfolio / Portfolio ao vivo

- **Production:** [AWS Event-Driven FinOps Platform](https://finops.moretes.com)
- **Documentation:** [Project docs](docs/architecture.md)
- **GitHub:** [fernandofatech/aws-event-driven-finops-platform](https://github.com/fernandofatech/aws-event-driven-finops-platform)
- **Author:** [Fernando Francisco Azevedo](https://fernando.moretes.com) · [LinkedIn](https://www.linkedin.com/in/fernando-francisco-azevedo/) · [GitHub](https://github.com/fernandofatech)

This public repository is part of a bilingual portfolio focused on solution architecture, AWS, AI, MCP/tooling, DevSecOps, and production-ready engineering practices.

Este repositório público faz parte de um portfólio bilíngue focado em arquitetura de soluções, AWS, IA, MCP/tools, DevSecOps e boas práticas de engenharia para produção.

## Scenario

The fictional platform models a banking event mesh with events such as:

- `AccountOpened`
- `PixPaymentRequested`
- `TransactionAuthorized`
- `FraudRiskScored`
- `StatementGenerated`

## AWS services covered

- Amazon EventBridge for domain event routing.
- Amazon SQS for buffering and decoupling.
- Amazon Kinesis Data Streams for ordered streaming.
- Amazon MSK for Kafka-compatible high-volume workloads.
- AWS Lambda and Step Functions for serverless processing.
- DynamoDB for idempotency and event state.
- CloudWatch and X-Ray for observability.

## What makes it portfolio-ready

- Shows real trade-offs between AWS event services.
- Treats cost as an architectural requirement.
- Documents event contracts and ADRs.
- Includes tests for decision logic.
- Uses CI and GitFlow-compatible contribution guidance.
- Includes a static frontend in `frontend/` ready for Vercel deployment.
- Automates CodeQL, Trivy, Gitleaks, dependency review and package audits.

## Run locally

```bash
python -m pip install -e . pytest
pytest -q
```

## Frontend

```bash
cd frontend
npm ci
npm run lint
npm run build
```

The frontend is intentionally static and dependency-light to keep the portfolio demo fast, secure and easy to deploy.

## Operations

See [OPERATIONS.md](OPERATIONS.md) for GitFlow, Vercel secrets and security pipeline details.
