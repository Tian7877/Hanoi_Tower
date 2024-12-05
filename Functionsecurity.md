```mermaid
mindmap
  root((Security Functional Requirements))
    FAU[FAU - Security Audit]
      FAU_ARP[FAU_ARP - Security Audit Automatic Response]
      FAU_GEN[FAU_GEN - Security Audit Data Generation]
      FAU_SAA[FAU_SAA - Security Audit Analysis]
      FAU_SAR[FAU_SAR - Security Audit Review]
    FCO[FCO - Communication]
      FCO_NRO[FCO_NRO - Non-repudiation of Origin]
      FCO_NRR[FCO_NRR - Non-repudiation of Receipt]
    FCS[FCS - Cryptographic Support]
      FCS_CKM[FCS_CKM - Cryptographic Key Management]
      FCS_COP[FCS_COP - Cryptographic Operation]
    FDP[FDP - User Data Protection]
      FDP_ACC[FDP_ACC - Access Control Policy]
      FDP_DAU[FDP_DAU - Data Authentication]
    FIA[FIA - Identification and Authentication]
      FIA_UAU[FIA_UAU - User Authentication]
      FIA_UID[FIA_UID - User Identification]
    FMT[FMT - Security Management]
      FMT_MOF[FMT_MOF - Management of Functions in TSF]
      FMT_MSA[FMT_MSA - Management of Security Attributes]
    FPR[FPR - Privacy]
      FPR_ANO[FPR_ANO - Anonymity]
      FPR_PSE[FPR_PSE - Pseudonimity]
    FPT[FPT - Protection of TSF]
      FPT_AMT[FPT_AMT - Underlying Abstract Machine Test]
      FPT_FLS[FPT_FLS - Fail Secure]
    FRU[FRU - Resource Utilisation]
      FRU_FLT[FRU_FLT - Fault Tolerance]
      FRU_RSA[FRU_RSA - Resource Allocation]
    FTA[FTA - TOE Access]
      FTA_LSA[FTA_LSA - Limitation on Scope of Selectable Attributes]
      FTA_TAH[FTA_TAH - TOE Access History]
    FTP[FTP - Trusted Path/Channels]
      FTP_ITC[FTP_ITC - Inter-TSF Trusted Channel]
      FTP_TRP[FTP_TRP - Trusted Path]
  
  %% Apply custom styles to increase spacing
  style root fill:#f9f,stroke:#333,stroke-width:4px
  style FAU fill:#cfc,stroke:#333,stroke-width:2px
  style FCO fill:#cfc,stroke:#333,stroke-width:2px
  style FCS fill:#cfc,stroke:#333,stroke-width:2px
  style FDP fill:#cfc,stroke:#333,stroke-width:2px
  style FIA fill:#cfc,stroke:#333,stroke-width:2px
  style FMT fill:#cfc,stroke:#333,stroke-width:2px
  style FPR fill:#cfc,stroke:#333,stroke-width:2px
  style FPT fill:#cfc,stroke:#333,stroke-width:2px
  style FRU fill:#cfc,stroke:#333,stroke-width:2px
  style FTA fill:#cfc,stroke:#333,stroke-width:2px
  style FTP fill:#cfc,stroke:#333,stroke-width:2px

