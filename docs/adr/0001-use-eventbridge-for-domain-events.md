# ADR 0001: Use EventBridge for Domain Events

## Status

Accepted

## Context

Domain events require fanout, routing rules and loose coupling between bounded contexts.

## Decision

Use Amazon EventBridge as the default domain event bus. Use SQS, Kinesis or MSK only when their specific characteristics are required.

## Consequences

- Positive: easy routing, lower coupling and improved governance.
- Negative: not ideal for strict ordering or very high-throughput streaming.
