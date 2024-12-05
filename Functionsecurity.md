```mermaid
flowchart LR
    A[Security Functional Requirements] --> A1[FAU - Security Audit]
    A --> A2[FCO - Communication]
    A --> A3[FCS - Cryptographic Support]
    A --> A4[FDP - User Data Protection]
    A --> A5[FIA - Identification and Authentication]

    A --> A7[FPR - Privacy]
    A --> A8[FPT - Protection of TSF]
    A --> A9[FRU - Resource Utilisation]
    A --> A10[FTA - TOE Access]
    A --> A11[FTP - Trusted Path/Channels]

    A1 --> FAU_ARP[FAU_ARP - Security Audit Automatic Response]
    A1 --> FAU_GEN[FAU_GEN - Security Audit Data Generation]
    A1 --> FAU_SAA[FAU_SAA - Security Audit Analysis]
    A1 --> FAU_SAR[FAU_SAR - Security Audit Review]

    A3 --> FCS_CKM[FCS_CKM - Cryptographic Key Management]
    A3 --> FCS_COP[FCS_COP - Cryptographic Operation]

    A4 --> FDP_ACC[FDP_ACC - Access Control Policy]
    A4 --> FDP_DAU[FDP_DAU - Data Authentication]

    A5 --> FIA_UAU[FIA_UAU - User Authentication]
    A5 --> FIA_UID[FIA_UID - User Identification]


    A7 --> FPR_ANO[FPR_ANO - Anonymity]
    A7 --> FPR_PSE[FPR_PSE - Pseudonimity]

    A8 --> FPT_AMT[FPT_AMT - Underlying Abstract Machine Test]
    A8 --> FPT_FLS[FPT_FLS - Fail Secure]

    A9 --> FRU_FLT[FRU_FLT - Fault Tolerance]
    A9 --> FRU_RSA[FRU_RSA - Resource Allocation]

    A10 --> FTA_LSA[FTA_LSA - Limitation on Scope of Selectable Attributes]
    A10 --> FTA_TAH[FTA_TAH - TOE Access History]

    A11 --> FTP_ITC[FTP_ITC - Inter-TSF Trusted Channel]
    A11 --> FTP_TRP[FTP_TRP - Trusted Path]

    %% Communication (FCO) details
    A2 --> FCO_NRO[FCO_NRO - Non-repudiation of Origin]
    A2 --> FCO_NRR[FCO_NRR - Non-repudiation of Receipt]
