```mermaid
graph LR
    A[Intranet Portal] --> B[Finance Management System]
    A[Intranet Portal] --> C[Project Management Tool]
    A[Intranet Portal] --> G[Information Management System]
    G[Information Management System] --> J[Validate Document for Project]
    B[Finance Management System] --> D[Payroll System]
    C[Project Management Tool] --> E[Time Tracking System]
    B[Finance Management System] --> F[Employee Performance System]
    A[Intranet Portal] --> H[Document Management System]
    F[Employee Performance System] --> I[Learning & Development System]
    
    classDef cloud fill:#f9f,stroke:#333,stroke-width:2px;
    class A,B,C,D,E,F,G,H,I cloud;

%% Pie chart diagram
pie
    title Distribution of Departemen
    "Dept Proyek Management" : 50 #ff5733
    "Dept Finance" : 30 #33b5ff
    "Dept DI" : 20 #00ff00
    "Dirut" : 10 #ffcc00

