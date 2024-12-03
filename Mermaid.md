```mermaid
graph LR
    A[Intranet Portal] --> B[Finance Management System]
    A[Intranet Portal] --> C[Project Management Tool]
    B[Finance Management System] --> D[Payroll System]
    C[Project Management Tool] --> E[Time Tracking System]
    B[HR Management System] --> F[Employee Performance System]
    A[Intranet Portal] --> G[Document Management System]
    F[Employee Performance System] --> H[Learning & Development System]
    
    classDef cloud fill:#f9f,stroke:#333,stroke-width:2px;
    class A,B,C,D,E,F,G,H cloud;
