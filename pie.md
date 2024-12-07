```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'ganttBarHeight': 20, 'ganttBarMargin': 8, 'ganttBarFill': '#FFFFFF'}}}%%
gantt
    title Bar Chart - Data Kategori
    dateFormat  YYYY-MM-DD
    axisFormat  %d

    section Rekanan
    Data Rekanan :a1, 2024-01-01, 20d
    " " :empty1, 2024-01-01, 2d  %% Bar kosong untuk jarak

    section Verifikasi
    Data Verifikasi :a2, 2024-01-01, 30d
    " " :empty2, 2024-01-01, 2d  %% Bar kosong untuk jarak

    section Pengadaan
    Data Pengadaan :a3, 2024-01-01, 20d
    " " :empty3, 2024-01-01, 2d  %% Bar kosong untuk jarak

    section Negosiasi
    Data Negosiasi :a4, 2024-01-01, 15d
    " " :empty4, 2024-01-01, 2d  %% Bar kosong untuk jarak

    section Kontrak
    Data Kontrak :a5, 2024-01-01, 20d
    " " :empty5, 2024-01-01, 2d  %% Bar kosong untuk jarak

    section Blanket
    Data Blanket :a6, 2024-01-01, 10d
