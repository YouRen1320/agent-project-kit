# Example: Multi-Application Platform

This fully fictional example demonstrates cross-component ownership without exposing a real system.

Product: Atlas Market, a sample catalog platform used only in this documentation.

## Components

| Component | Repository or path | Consumers |
| --- | --- | --- |
| Core API | `atlas-core-api` | Customer web, operator console, mobile app |
| Customer web | `atlas-customer-web` | End users |
| Operator console | `atlas-operator-console` | Internal operators |
| Mobile app | `atlas-mobile` | End users |

## Contract Rule

An API change is not complete until every affected consumer is identified, updated or explicitly deferred, and independently verified.

## Example Module Registry

| Module | Producer | Consumers | Data | Owner |
| --- | --- | --- | --- | --- |
| MOD-01 Accounts | Core API | All clients | Account records | Identity Team |
| MOD-02 Catalog | Core API | Customer web, mobile | Catalog records | Catalog Team |
| MOD-03 Operations | Core API | Operator console | Audit records | Operations Team |

## Example Coordinated Change

Renaming `customerName` to `buyerName` affects the Core API, customer web, operator console, and mobile app. The preferred plan is a time-bounded phased migration: add `buyerName`, measure remaining `customerName` consumers, migrate every client, then remove the old field in a separately approved breaking release. The compatibility field has a named removal owner and deadline; it is not permanent.

Use `.agents/templates/module-registry.md` to build a real registry for the adopting project.
