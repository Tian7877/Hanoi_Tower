```mermaid
graph TB
  A[CRM Application] -->|Integrates with| B[ERP Application]
  A -->|Integrates with| C[Marketing Automation]
  B -->|Integrates with| D[Finance System]
  C -->|Integrates with| E[Email Marketing Service]
  D -->|Critical| F[Inventory Management]
  B -->|Integrates with| G[HRM System]
  G -->|Used by| H[Employee Portal]
  F -->|Critical| I[Supply Chain Management]

  A[CRM Application]:::app
  B[ERP Application]:::app
  C[Marketing Automation]:::app
  D[Finance System]:::app
  E[Email Marketing Service]:::app
  F[Inventory Management]:::app
  G[HRM System]:::app
  H[Employee Portal]:::app
  I[Supply Chain Management]:::app

  classDef app fill:#f9f,stroke:#333,stroke-width:2px;
  class A,B,C,D,E,F,G,H,I app;
