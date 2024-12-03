```mermaid
graph LR
    A[Intranet Portal] --> B[Finance Management System]
    A[Intranet Portal] --> C[Project Management Tool]
    A[Intranet Portal] --> G[Information Management System]
    G[Information Management System] --> J[Validate Document for Project]
    B[Finance Management System] --> D[Payroll System]
    C[Project Management Tool] --> E[Time Tracking System]
    B[Finance Management System] --> F[Invoice Tracking System]
    A[Intranet Portal] --> H[Document Management System]
    H[Document Management System] --> K[File Manager]
    F[Invoice Tracking System] --> K[File Manager]
    
    classDef cloud stroke:#333,stroke-width:2px;
    class A,B,C,D,E,F,G,H,I,J,K cloud;



