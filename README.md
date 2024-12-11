```mermaid
flowchart TD
    A[Start Migrasi] --> B[Persiapan Lingkungan]
    B --> C[Audit Kode CodeIgniter]
    C --> D[Perencanaan Migrasi]
    D --> E[Migrasi Database]
    E --> F[Migrasi Backend]
    F --> G[Migrasi Frontend]
    G --> H[Migrasi Fitur Lainnya]
    H --> I[Pengujian & Optimisasi]
    I --> J[Deployment & Go-Live]
    J --> K[End]

